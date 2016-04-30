from __future__ import unicode_literals

from jsonschema2code.exceptions import SchemaValidationError
from jsonschema2code.schema_validation.type_validators.base import BaseTypeSchemaValidator
from jsonschema2code.types.type_names import DATE


class DateTypeSchemaValidator(BaseTypeSchemaValidator):

    type = DATE

    def validate(self, definitions, **kwargs):
        format = kwargs.pop("format", None)
        if format is None:
            raise SchemaValidationError("No date format specified for date type", self.class_name, self.property_name)
