#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use 
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import os

# Asegurar que CUDA_HOME está bien configurado
os.environ["CUDA_HOME"] = "/usr/local/cuda"

# Flags de compilación para nvcc
nvcc_flags = [
    "-std=c++17",
    "--expt-relaxed-constexpr",
    "--compiler-options", "'-fPIC'",
    "-gencode=arch=compute_75,code=sm_75",
    "-gencode=arch=compute_80,code=sm_80",
    "-gencode=arch=compute_86,code=sm_86",
    "-gencode=arch=compute_89,code=sm_89",
    "-gencode=arch=compute_90,code=sm_90"
]


# Flags de compilación para C++
cxx_compiler_flags = ["-std=c++17"]

if os.name == 'nt':  # Compatibilidad con Windows
    cxx_compiler_flags.append("/wd4624")
else:  # En Linux
    cxx_compiler_flags.append("-D_GLIBCXX_USE_CXX11_ABI=0")

setup(
    name="simple_knn",
    ext_modules=[
        CUDAExtension(
            name="simple_knn._C",
            sources=[
                "spatial.cu", 
                "simple_knn.cu",
                "ext.cpp"
            ],
            extra_compile_args={"nvcc": nvcc_flags, "cxx": cxx_compiler_flags}
        )
    ],
    cmdclass={'build_ext': BuildExtension}
)


