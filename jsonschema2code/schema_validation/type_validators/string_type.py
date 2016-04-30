from __future__ import unicode_literals

from jsonschema2code.schema_validation.type_validators.base import BaseTypeSchemaValidator
from jsonschema2code.types.type_names import STRING


class StringTypeSchemaValidator(BaseTypeSchemaValidator):

    type = STRING
