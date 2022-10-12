#!/bin/bash

source=/config/scripts/src/boilerplate.yaml
dest=/config/packages/YERP

cp $source $dest/$1.yaml
sed -i -e "s/boilerplate/$1/g" $dest/$1.yaml
ls -la $dest
cat $dest/$1.yaml
