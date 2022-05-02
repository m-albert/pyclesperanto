from skbuild import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pyclesperanto",
    version="0.4.0",
    author="Stephane Rigaud",
    author_email="stephane.rigaud@pasteur.fr",
    license="BSD-3-Clause",
    description="GPU-accelerated image processing in python using OpenCL",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['pyclesperanto'],
    cmake_install_dir='pyclesperanto',
    python_requires=">=3.7",
    install_requires =[
        'numpy',
        'toolz',
        'matplotlib',
        ],
    extras_require={"test": ["pytest"]},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    project_urls={
    'Documentation': 'https://github.com/clEsperanto/pyclesperanto#README.md',
    'Source': 'https://github.com/clEsperanto/pyclesperanto/',
    'Tracker': 'https://github.com/clEsperanto/pyclesperanto/issues',
    },
    )

# When building extension modules `cmake_install_dir` should always be set to the
# location of the package you are building extension modules for.
# Specifying the installation directory in the CMakeLists subtley breaks the relative
# paths in the helloTargets.cmake file to all of the library components.