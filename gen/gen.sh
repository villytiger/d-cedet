#!/bin/bash

DOCS="module.dd declaration.dd attribute.dd pragma.dd expression.dd traits.dd statement.dd struct.dd class.dd interface.dd enum.dd function.dd version.dd template.dd template-mixin.dd unittest.dd iasm.dd"

dir=`pwd`
cd $1

dmd -o- -c -D $DOCS "$dir/grammar.ddoc" -Dd"$dir/grammar"

cd "$dir/grammar"
cat ${DOCS//.dd/.html} >../grammar.txt
cd ..
