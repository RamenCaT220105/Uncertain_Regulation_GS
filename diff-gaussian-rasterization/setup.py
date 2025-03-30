from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension, _get_cuda_arch_flags
import os

os.path.dirname(os.path.abspath(__file__))

# Obtener las flags correctas para la arquitectura de la GPU
# cuda_arch_flags = _get_cuda_arch_flags(["7.5", "8.0", "8.6", "8.9"])
cuda_arch_flags = ["-gencode=arch=compute_75,code=sm_75",
                   "-gencode=arch=compute_80,code=sm_80",
                   "-gencode=arch=compute_86,code=sm_86",
                   "-gencode=arch=compute_89,code=sm_89",
                   "-gencode=arch=compute_90,code=sm_90"]


setup(
    name="diff_gaussian_rasterization",
    packages=['diff_gaussian_rasterization'],
    ext_modules=[
        CUDAExtension(
            name="diff_gaussian_rasterization._C",
            sources=[
                "cuda_rasterizer/rasterizer_impl.cu",
                "cuda_rasterizer/forward.cu",
                "cuda_rasterizer/backward.cu",
                "rasterize_points.cu",
                "ext.cpp"
            ],
            # extra_compile_args={
            #     "nvcc": cuda_arch_flags + ["-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")]
            # }
            extra_compile_args={"nvcc": cuda_arch_flags + ["-I/usr/include"]}
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)