#!/bin/bash

for file in *; do mv "${file}" "${file/13labels/}"; done
