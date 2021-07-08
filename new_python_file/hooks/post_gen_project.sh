#!/bin/bash

file_type='{{cookiecutter.type}}'

if [ "$file_type" == "runable" ]; then
	find . -maxdepth 1 -type f -name "*.py" | xargs chmod u+x 
fi
cp -rf . ..
rm -rf -- "$(pwd -P)"