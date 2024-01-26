#!/bin/bash -u
#File: file-list-2.bash. Prints out a list of file names in a directory.
# Illustrates: looping

DIR: `/c/Users/monau/PycharmProjects/Joy_of_Coding/Practice_files`

if [! -d ${DIR} ]; then
  echo "No such directory: ${DIR}"
else
  FILES=`ls -l ${DIR} | head -2`
  for X in "${FILES}" ; do
      echo "FILES: ${X}"
  done

fi
