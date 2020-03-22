#!/bin/bash
read -r -p 'Commit message: ' ${desc} # prompt user for commit message
git add .                             # track all files 
git add -u                            # track all deleted files
git commit -m "$desc"                 # commit with message
git push origin master                # push to origin
git push production master            # push to development server