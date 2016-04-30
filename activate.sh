#!/bin/bash

source $WORKON_HOME/jsonschema2code/bin/activate
export PYTHONPATH=/Users/rajivpatel/Development/jsonschema2code:$PYTHONPATH
${@:1}