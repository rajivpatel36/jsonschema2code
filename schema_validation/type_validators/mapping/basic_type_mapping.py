from __future__ import unicode_literals

from schema_validation.type_validators.custom_type import CustomTypeSchemaValidator
from schema_validation.type_validators.date_type import DateTypeSchemaValidator
from schema_validation.type_validators.integer_type import IntegerTypeSchemaValidator
from schema_validation.type_validators.string_type import StringTypeSchemaValidator

BASIC_TYPE_SCHEMA_VALIDATOR_MAPPING = {
    cls.type: cls for cls in [
        DateTypeSchemaValidator,
        IntegerTypeSchemaValidator,
        CustomTypeSchemaValidator,
        StringTypeSchemaValidator,
    ]
}
