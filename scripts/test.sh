#!/usr/bin/sh

#cd ~/romain_project/src/romain_package/.git
#WORKTREE=~/romain_project/

#CHANGED=$(git --work-tree=${WORKTREE} status --porcelain)

#if [ -n "${CHANGED}" ]; then
#  echo 'changed';

#else
#  echo 'not changed';
#fi

[ -z "`git status --porcelain`" ] && echo "NULL-NO DIFFS" || echo "DIFFS EXIST"