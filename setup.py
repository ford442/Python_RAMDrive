import setuptools
from setuptools import Extension,setup; 
from Cython.Build import cythonize;
from Cython.Compiler import Options
Options.infer_types = True
Options.language_level = 3
extensions = [Extension('ramdr',['ramdr/ramdr.py'])];
setuptools.setup(
     name='ramdr',  
     version='1.0',
     description="Python ramdrive creator",
     packages=['ramdr'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD License",
         "Operating System :: OS Independent",
     ],
    ext_modules=cythonize(extensions),
 )
