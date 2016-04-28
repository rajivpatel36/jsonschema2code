from __future__ import unicode_literals

from exceptions import SchemaValidationError
from schema_validation.type_validators.base import BaseTypeSchemaValidator
from types.type_names import DATE


class DateTypeSchemaValidator(BaseTypeSchemaValidator):

    type = DATE

    def validate(self, definitions, **kwargs):
        format = kwargs.pop("format", None)
        if not format:
            raise SchemaValidationError("No date format specified for date type", self.class_name, self.property_name)
