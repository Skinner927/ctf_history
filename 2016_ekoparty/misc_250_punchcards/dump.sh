#!/usr/bin/env bash
for img in *.png; do 
  echo -n "$img "
  python readcard.py "$img" "$@"
done
