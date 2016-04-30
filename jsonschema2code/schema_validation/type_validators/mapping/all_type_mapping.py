from __future__ import unicode_literals

from jsonschema2code.schema_validation.type_validators.list_type import ListTypeSchemaValidator
from jsonschema2code.schema_validation.type_validators.mapping.basic_type_mapping import _BASIC_TYPE_SCHEMA_VALIDATORS

_ALL_TYPE_SCHEMA_VALIDATORS = _BASIC_TYPE_SCHEMA_VALIDATORS + [
    ListTypeSchemaValidator
]

ALL_TYPE_SCHEMA_VALIDATOR_MAPPING = {cls.type: cls for cls in _ALL_TYPE_SCHEMA_VALIDATORS}
