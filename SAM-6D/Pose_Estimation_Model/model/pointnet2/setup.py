# Copyright (c) Facebook, Inc. and its affiliates.
# 
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import os
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import glob

_ext_src_root = "_ext_src"
_ext_sources = glob.glob(os.path.join(_ext_src_root, "src", "*.cpp")) + \
               glob.glob(os.path.join(_ext_src_root, "src", "*.cu"))
_ext_include_dirs = [os.path.abspath(os.path.join(_ext_src_root, "include"))]

# Specify GCC 9 as the host compiler
os.environ["CC"] = "/usr/bin/gcc-9"
os.environ["CXX"] = "/usr/bin/g++-9"

setup(
    name='pointnet2',
    packages=find_packages(),
    ext_modules=[
        CUDAExtension(
            name='pointnet2._ext',
            sources=_ext_sources,
            include_dirs=_ext_include_dirs,
            extra_compile_args={
                'cxx': ['-O2'],
                'nvcc': [
                    '-O3',
                    '--compiler-options',
                    '-fPIC',
                    '-ccbin', '/usr/bin/gcc-9',
                ],
            }
        )
    ],
    cmdclass={
        'build_ext': BuildExtension.with_options(use_ninja=True)
    }
)
