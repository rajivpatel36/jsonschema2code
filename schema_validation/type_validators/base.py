from __future__ import unicode_literals


class BaseTypeSchemaValidator(object):

    type = None

    def __init__(self, class_name, property_name):
        self.class_name = class_name
        self.property_name = property_name

    def validate(self, definitions, **kwargs):
        pass
