from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import torch.utils.cpp_extension as cpp_ext


def _skip_cuda_version_check(*args, **kwargs):
    # Newer systems may have a newer toolkit (e.g., CUDA 13) than torch wheel CUDA.
    # We allow the build to proceed and rely on compile/link errors for hard failures.
    return


cpp_ext._check_cuda_version = _skip_cuda_version_check

setup(
    name='PeriodicPrimitives',
    ext_modules=[
        CUDAExtension('PeriodicPrimitives', [
            'periodic_primitives2DRGB_cuda.cpp',
            'periodic_primitives2DRGB_cuda_kernel.cu',
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })