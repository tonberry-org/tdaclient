#!/bin/bash -eu

if [ $# -ne 2 ] ; then
    echo "Usage: $0 <source-folder> <target-folder>"
fi
SOURCE_FOLDER=$1
TARGET_FOLDER=$2

for file in "${SOURCE_FOLDER}"/*.json; do
    echo "found ${file}"
    file_name=$(basename "${file}")
    target_file_name=${file_name/.json/.py}
    datamodel-codegen --input "$file" --input-file-type jsonschema --output "${TARGET_FOLDER}/${target_file_name}" --enum-field-as-literal one
done
