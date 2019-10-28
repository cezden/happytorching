#!/usr/bin/env bash

LINEM="--------------------------------"

echo "${LINEM} nvidia-smi "
nvidia-smi
echo "${LINEM} which nvidia-smi? "
which nvidia-smi
echo "${LINEM}"

echo "${LINEM} nvcc "
nvcc -V
echo "${LINEM} which nvcc?"
which nvcc
echo "${LINEM}"

echo "${LINEM} numba "
numba -s
echo "${LINEM} which numba?"
which numba
echo "${LINEM}"

echo "${LINEM} env_variables"
printenv  | sort
echo "${LINEM}"
echo "${LINEM}"

echo "${LINEM} Python "
python --version
echo "${LINEM} which Python?"
which python
echo "${LINEM}"

