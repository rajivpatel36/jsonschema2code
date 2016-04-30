from __future__ import unicode_literals

import six

from exceptions import SchemaValidationError
from schema_validation.type_validators.mapping.all_type_mapping import ALL_TYPE_SCHEMA_VALIDATOR_MAPPING


class ClassValidator(object):
    def __init__(self, class_name):
        self.class_name = class_name

    def validate(self, definitions, **kwargs):
        description = kwargs.pop("_description", None)
        if description is not None and not isinstance(description, *six.text_type):
            raise SchemaValidationError(
                "Class description must be a string.",
                self.class_name
            )
        while len(kwargs) > 0:
            property_name, property_schema = kwargs.popitem()
            property_type = property_schema.pop("type", None)
            property_type_validator_cls = ALL_TYPE_SCHEMA_VALIDATOR_MAPPING.get(property_type, None)
            if property_type_validator_cls is None:
                raise SchemaValidationError(
                    "Invalid type specified for property: {type}".format(type=property_type),
                    self.class_name,
                    property_name,
            )
            property_type_validator = property_type_validator_cls(self.class_name, property_name)
            property_type_validator.validate(definitions, **property_schema)
