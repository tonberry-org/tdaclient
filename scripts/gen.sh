#!/bin/bash -eu

datamodel-codegen --input tdaclient/schema/json\
  --input-file-type jsonschema\
   --output tdaclient/schema\
    --enum-field-as-literal one\
    --use-subclass-enum\
    --target-python-version 3.11\
    --reuse-model
