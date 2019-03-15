from distutils.core import setup
from Cython.Build import cythonize

setup(name="ResourceMerger",
    version="0.0.1",
    description="resource merger",
    ext_modules = cythonize("ResourceMerger.py"))