from __future__ import unicode_literals

from copy import deepcopy

from jsonschema2code.exceptions import SchemaValidationError
from jsonschema2code.schema_validation.class_validator import ClassSchemaValidator


def validate_schema(schema):
    definitions = schema.pop("definitions", None)
    # The root should be the only other thing left in the schema
    root_name, root_schema = schema.popitem()
    if len(schema) > 0:
        raise SchemaValidationError("The schema can only contain one root node.")

    # validate root node
    root_node_validator = ClassSchemaValidator(root_name)
    root_node_validator.validate(definitions, **root_schema)

    # validate definitions
    if definitions is None:
        return

    definitions_copy = deepcopy(definitions)
    while len(definitions) > 0:
        definition_name, definition_schema = definitions.popitem()
        definition_validator = ClassSchemaValidator(definition_name)
        definition_validator.validate(definitions_copy, **definition_schema)
