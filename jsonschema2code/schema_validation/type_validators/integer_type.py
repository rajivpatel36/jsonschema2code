from __future__ import unicode_literals

import re

import six

from jsonschema2code.exceptions import SchemaValidationError
from jsonschema2code.schema_validation.type_validators.base import BaseTypeSchemaValidator
from jsonschema2code.types.type_names import INTEGER


class IntegerTypeSchemaValidator(BaseTypeSchemaValidator):

    type = INTEGER

    def validate(self, definitions, **kwargs):
        constraint = kwargs.pop("constraint", None)
        if constraint is None:
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
