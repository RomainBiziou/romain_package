#!/usr/bin/sh

[ -z "`git status --porcelain`" ] && echo "Pas de differences" || echo "Differences"
