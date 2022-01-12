#!/bin/bash
message=`date +'%F%T'`
git add *
git commit -m $message
git push
