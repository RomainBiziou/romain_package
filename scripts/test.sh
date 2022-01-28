#!/usr/bin/sh

cd ~/romain_project/src/romain_package/.git
WORKTREE=~/romain_project/src/romain_package/scripts

CHANGED=$(git --work-tree=${WORKTREE} status --porcelain)

if [ -n "${CHANGED}" ]; then
  echo 'changed';

else
  echo 'not changed';
fi
