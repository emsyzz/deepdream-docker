#!/bin/bash

INC=0

if [[ -n $2 ]]; then
  INC="${2}"
fi

while [ ! -z $1 ]; do
  export INPUT="$1"
  if [[ $INC -gt 0 ]]; then
    export INPUT="output/sample-${INC}_${1}"
    if [[ ! -z $3 ]]; then
      python image-zoom.py "${INPUT}" "$3"
    fi
  fi
  let "INC++"
  export OUTPUT="sample-${INC}_${1}"
  if [[ -f "/data/${INPUT}" ]]; then
    python deepdream.py
  else
    ./dd.sh "$@"
  fi
done

