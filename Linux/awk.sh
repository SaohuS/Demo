#!/bin/bash
info=git.info
#printf $info "^{^$}\n"
cat $info | awk -F 'id' '{print $2}'
#cat $info | sed -n '/id ./id /p' 
cat $info | awk -F '^id/,/id$/' '{print $1}'

sed -n '/^id/,/id$/p' git.info | grep -Ev '(^id|id$)' | cut -f 1,2 