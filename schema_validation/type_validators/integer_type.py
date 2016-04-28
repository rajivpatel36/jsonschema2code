from __future__ import unicode_literals

import re
import six

from exceptions import SchemaValidationError
from schema_validation.type_validators.base import BaseTypeSchemaValidator
from types.type_names import INTEGER


class IntegerTypeSchemaValidator(BaseTypeSchemaValidator):

    type = INTEGER

    def validate(self, definitions, **kwargs):
        constraint = kwargs.pop("constraint", None)
        if constraint:
            is_valid_constraint = all([
                isinstance(constraint, *six.string_types),
                re.match("(^[<>]=?[-]?\d+(?:\.\d+|))", constraint),
            ])
            if not is_valid_constraint:
                raise SchemaValidationError(
                    "Invalid constraint specification for integer type: {constraint}".format(constraint=constraint),
                    self.class_name,
                    self.property_name
                )
