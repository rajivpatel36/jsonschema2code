from __future__ import unicode_literals


class SchemaValidationError(Exception):
    def __init__(self, message, class_name=None, property_name=None):
        class_info = "Class: {class_name}.".format(class_name=class_name) if class_name else ""
        property_info = "Property: {property_name}.".format(property_name=property_name) if property_name else ""
        self.message = " ".join([message, class_info, property_info])
