from __future__ import unicode_literals

from schema_validation.type_validators.base import BaseTypeSchemaValidator
from types.type_names import STRING


class StringTypeSchemaValidator(BaseTypeSchemaValidator):

    type = STRING
