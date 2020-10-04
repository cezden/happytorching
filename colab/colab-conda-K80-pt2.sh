#!/usr/bin/env bash

#target python version
T_PY="3.8.3"

#target miniconda prefix
T_CDIX="/root/miniconda3"

#target environment name
T_EN="mast_env"

#target CUDA version - with- and witout a dot - lame, I know
C_CU_1="10.1"
C_CU_2="101"

COCO_PREFIX="${T_CDIX}/bin/"
COCO_PREFIX=""

#probable output of conda init:
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/root/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "${T_CDIX}/etc/profile.d/conda.sh" ]; then
        . "${T_CDIX}/etc/profile.d/conda.sh"
    else
        export PATH="${T_CDIX}/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<



EVAL="${COCO_PREFIX}conda create -v -y -n ${T_EN} -c numba -c nvidia -c pytorch \
 python=${T_PY} numba cudatoolkit=${C_CU_1} \
 mkl mkl-devel cffi numpy scipy mkl_fft tbb scikit-learn seaborn pandas icc_rt llvmlite cython intel-openmp \
 tbb-devel sphinx fftw pymc3 \
 cudnn nvcc_linux-64 libcumlprims \
 pytorch torchvision torchaudio \
 xgboost \
 magma-cuda${C_CU_2}"

echo "${EVAL}"
eval "${EVAL}"

#rm colab_tools.py

