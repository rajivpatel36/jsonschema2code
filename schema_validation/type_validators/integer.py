from __future__ import unicode_literals

import re
import six

from exceptions import SchemaValidationError
from schema_validation.type_validators.base import BaseTypeSchemaValidator


class IntegerTypeSchemaValidator(BaseTypeSchemaValidator):
    def validate(self, definitions, **kwargs):
        constraint = kwargs.get("constraint", None)
        if constraint:
            is_valid_constraint = all([
                isinstance(constraint, *six.string_types),
                re.match("(^[<>]=?[-]?\d+(?:\.\d+|))", constraint),
            ])
            if not is_valid_constraint:
                raise SchemaValidationError("Invalid constraint specification for integer type: {}".format(constraint))
