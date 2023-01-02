#!/bin/bash -eu

datamodel-codegen --input tdaclient/schema/json --input-file-type jsonschema --output tdaclient/schema --enum-field-as-literal one 
