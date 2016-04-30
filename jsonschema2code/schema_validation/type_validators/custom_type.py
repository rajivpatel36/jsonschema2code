from __future__ import unicode_literals

import six

from jsonschema2code.exceptions import SchemaValidationError
from jsonschema2code.schema_validation.type_validators.base import BaseTypeSchemaValidator
from jsonschema2code.types.type_names import CUSTOM


class CustomTypeSchemaValidator(BaseTypeSchemaValidator):

    type = CUSTOM

    def validate(self, definitions, **kwargs):
        ref_type = kwargs.pop("ref", None)
        if ref_type is None:
            raise SchemaValidationError(
                "Ref object not specified for custom type.",
                self.class_name,
                self.property_name
            )
        if not isinstance(ref_type, *six.text_type):
            raise SchemaValidationError(
                "Ref object type must be a string.",
                self.class_name,
                self.property_name
            )
        if ref_type not in definitions:
            raise SchemaValidationError(
                "Ref object type not specified in 'definitions' in schema.",
                self.class_name,
                self.property_name
            )
