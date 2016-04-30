from __future__ import unicode_literals

from jsonschema2code.exceptions import SchemaValidationError


class BaseTypeSchemaValidator(object):

    type = None

    def __init__(self, class_name, property_name):
        self.class_name = class_name
        self.property_name = property_name

    def validate(self, definitions, **kwargs):
        pass

    def do_validation(self, definitions, **kwargs):
        self.validate(definitions, **kwargs)
        if len(kwargs) > 0:
            raise SchemaValidationError(
                message="Unsupported parameter ({parameter}) specified for {type} type.".format(
                    parameter=kwargs.popitem()[0],
                    type=self.type
                ),
                class_name=self.class_name,
                property_name=self.property_name
            )
