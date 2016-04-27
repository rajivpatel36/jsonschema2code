from __future__ import unicode_literals

from exceptions import SchemaValidationError
from schema_validation.type_validators.base import BaseTypeSchemaValidator


class DateTypeSchemaValidator(BaseTypeSchemaValidator):
    def validate(self, definitions, **kwargs):
        if not kwargs.get("format", None):
            raise SchemaValidationError("No date format specified for date type")
