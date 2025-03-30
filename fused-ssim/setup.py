from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension

cuda_arch_flags = [
    "-gencode=arch=compute_75,code=sm_75",
    "-gencode=arch=compute_80,code=sm_80",
    "-gencode=arch=compute_86,code=sm_86",
    "-gencode=arch=compute_89,code=sm_89",
    "-gencode=arch=compute_90,code=sm_90"
]

setup(
    name="fused_ssim",
    packages=['fused_ssim'],
    ext_modules=[
        CUDAExtension(
            name="fused_ssim_cuda",
            sources=[
                "ssim.cu",
                "ext.cpp"
            ],
            extra_compile_args={"nvcc": cuda_arch_flags}
        )
    ],
    cmdclass={'build_ext': BuildExtension}
)