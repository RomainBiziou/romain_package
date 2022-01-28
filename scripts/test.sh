#!/usr/bin/sh

[ -z "`git status --porcelain`" ] && echo "NULL-NO DIFFS" || echo "DIFFS EXIST"