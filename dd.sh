#!/bin/bash

INC=0
ZOOM="$3"

if [[ -n $2 ]]; then
  INC="${2}"
fi

while [ ! -z $1 ]; do
  export INPUT="$1"
  if [[ $INC -gt 0 ]]; then
    export INPUT="output/sample-${INC}_${1}"
  fi
  let "INC++"
  export OUTPUT="sample-${INC}_${1}"
  if [[ -f "/data/${INPUT}" ]]; then
    python deepdream.py
    if [[ -f "/data/output/${OUTPUT}" ]]; then
      if [[ ! -z $3 ]]; then
        python image-zoom.py "output/${OUTPUT}" "$ZOOM"
        ZOOM=$(python -c "print $ZOOM+0.005")
      fi
    else
      exit 1
    fi
  fi
done

