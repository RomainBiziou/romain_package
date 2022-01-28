#!/usr/bin/sh

if ! git --git-dir="~/.git" diff --quiet
then
    echo "change"
fi

#[ -z "`git status --porcelain`" ] && echo "Pas de differences" || echo "Differences"