from __future__ import unicode_literals

from jsonschema2code.schema_validation.type_validators.custom_type import CustomTypeSchemaValidator
from jsonschema2code.schema_validation.type_validators.date_type import DateTypeSchemaValidator
from jsonschema2code.schema_validation.type_validators.integer_type import IntegerTypeSchemaValidator
from jsonschema2code.schema_validation.type_validators.string_type import StringTypeSchemaValidator


_BASIC_TYPE_SCHEMA_VALIDATORS = [
    DateTypeSchemaValidator,
    IntegerTypeSchemaValidator,
    CustomTypeSchemaValidator,
    StringTypeSchemaValidator,
]

BASIC_TYPE_SCHEMA_VALIDATOR_MAPPING = {cls.type: cls for cls in _BASIC_TYPE_SCHEMA_VALIDATORS}
