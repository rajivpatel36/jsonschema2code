from __future__ import unicode_literals

from jsonschema2code.exceptions import SchemaValidationError
from jsonschema2code.schema_validation.type_validators.mapping.basic_type_mapping import BASIC_TYPE_SCHEMA_VALIDATOR_MAPPING
from jsonschema2code.schema_validation.type_validators.base import BaseTypeSchemaValidator
from jsonschema2code.types.type_names import LIST


class ListTypeSchemaValidator(BaseTypeSchemaValidator):

    type = LIST

    def validate(self, definitions, **kwargs):
        list_members = kwargs.pop("list_members", None)
        if list_members is None:
            raise SchemaValidationError(
                "List members not specified for list type.",
                self.class_name,
                self.property_name
            )
        if not isinstance(list_members, dict):
            raise SchemaValidationError(
                "List members specification is not valid for list type.",
                self.class_name,
                self.property_name,
            )
        list_members_type = list_members.pop("type", None)
        if list_members_type is None:
            raise SchemaValidationError(
                "List members type is not specified for list type.",
                self.class_name,
                self.property_name,
            )
        if list_members_type not in BASIC_TYPE_SCHEMA_VALIDATOR_MAPPING:
            raise SchemaValidationError(
                "List members type is not valid basic type: {type}".format(type=list_members_type),
                self.class_name,
                self.property_name
            )
        list_members_validator = BASIC_TYPE_SCHEMA_VALIDATOR_MAPPING[list_members_type](
            self.class_name,
            self.property_name
        )
        list_members_validator.validate(definitions, **list_members)
