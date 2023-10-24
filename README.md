# py-clesperanto
[![PyPI](https://img.shields.io/pypi/v/pyclesperanto.svg?color=green)](https://pypi.org/project/pyclesperanto)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pyclesperanto.svg)](https://anaconda.org/conda-forge/pyclesperanto)
[![License](https://img.shields.io/pypi/l/pyclesperanto.svg?color=green)](https://github.com/clEsperanto/pyclesperanto/raw/main/LICENSE)
[![Development Status](https://img.shields.io/pypi/status/pyclesperanto.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![Build](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build.yml/badge.svg)](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/clesperanto/pyclesperanto/branch/main/graph/badge.svg)](https://codecov.io/gh/clesperanto/pyclesperanto)
[![Python Version](https://img.shields.io/pypi/pyversions/pyclesperanto.svg?color=green)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub stars](https://img.shields.io/github/stars/clEsperanto/pyclesperanto?style=social)](https://github.com/clEsperanto/pyclesperanto)
[![GitHub forks](https://img.shields.io/github/forks/clEsperanto/pyclesperanto?style=social)](https://github.com/clEsperanto/pyclesperanto)

pyclesperanto is the python package of [clEsperanto] - a multi-language framework for GPU-accelerated image processing.
clEsperanto uses [OpenCL kernels] from [CLIJ].
This package relies on the [CLIc] back-end for processing.

## __Installation__

* Get a conda/python environment, e.g. via [__mamba-forge__](https://github.com/conda-forge/miniforge#mambaforge).
* If you never used python/conda environments before, please follow [these instructions](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html) first.

```
conda create --name cle python=3.9
conda activate cle
```

* Install pyclesperanto-prototype using [__mamba / conda__](https://focalplane.biologists.com/2022/12/08/managing-scientific-python-environments-using-conda-mamba-and-friends/):

```
mamba install -c conda-forge pyclesperanto
```

OR using pip:

```
pip install pyclesperanto
```

## __Code Example__

**Note**: This project is under heavy development. General API, functions, and parameters are subject to change.

```python
import pyclesperanto as cle
from skimage.io import imread, imsave

# initialize GPU
device = cle.select_device()
print("Used GPU: ", device)

image = imread("https://samples.fiji.sc/blobs.png")

# push image to device memory
input_image = cle.push(image)

# process the image
inverted = cle.subtract_image_from_scalar(input_image, scalar=255)
blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
binary = cle.threshold_otsu(blurred)
labeled = cle.connected_components_labeling_box(binary)

# The maxmium intensity in a label image corresponds to the number of objects
num_labels = cle.maximum_of_all_pixels(labeled)

# print out result
print("Num objects in the image: " + str(num_labels))

# read image from device memory
output_image = cle.pull(labeled)
imsave("result.tif", output_image)
```

## __Example gallery__

<table border="0">

<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/raw/main/demos/images/labeled_blobs.png" width="300"/>
</td><td>

[Segment + analyze blobs](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/process_blobs.ipynb)

</td></tr>

<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/raw/main/demos/images/cell_segmentation.png" width="300"/>
</td><td>

[Cell segmentation + Voronoi labeling](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/cell_segmentation.ipynb)

</td></tr>

<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/raw/main/demos/images/image_filtering.png" width="300"/>
</td><td>

[3D image filtering](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/image_filtering.ipynb)

</td></tr>


<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/raw/main/demos/images/find_local_maxima.png" width="300"/>
</td><td>

[Find local maxima](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/find_local_maxima.ipynb)

</td></tr>

<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/raw/main/demos/images/tribolium3d_segmentation.png" width="300"/>
</td><td>

[3D Tribolium nuclei segmentation](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/process_tribolium.ipynb)

</td></tr>

<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/raw/main/demos/images/explore_API.png" width="300"/>
</td><td>

[Explore application programming interface (API)](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/explore_API.ipynb)

</td></tr>

<!--
<tr><td>

<img src="https://raw.githubusercontent.com/clEsperanto/pyclesperanto/main/demos/images/multi-gpu.png" width="300"/>

</td><td>

[Multi-GPU developer_docs](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/multi_gpu_demo.ipynb)

</td></tr>
-->
</table>

More usage and example can be found as notebooks in the [demos](./user_docs) folder

# __Contributing and Feedback__

clEsperanto is developed in the open because we believe in the [open source community].
Feel free to drop feedback as [github issue] or via [image.sc forum].
Contribution are also very welcome. Please read our [community guidelines] before you start and get in touch with us so that we can help you get started.
If you liked our work, star the repository, share it with your friends, and use it to make cool stuff!

## Acknowledgements

We acknowledge support by the Deutsche Forschungsgemeinschaft under Germany’s Excellence Strategy (EXC2068) Cluster of Excellence Physics of Life of TU Dresden.
This project has been made possible in part by grant number 2021-237734 ([GPU-accelerating Fiji and friends using distributed CLIJ, NEUBIAS-style, EOSS4](https://chanzuckerberg.com/eoss/proposals/gpu-accelerating-fiji-and-friends-using-distributed-clij-neubias-style/)) from the Chan Zuckerberg Initiative DAF, an advised fund of the Silicon Valley Community Foundation.

[clEsperanto]: http://clesperanto.net/
[OpenCL kernels]: https://github.com/clEsperanto/clij-opencl-kernels/tree/clesperanto_kernels
[CLIJ]: http://clij.github.io/
[CLIc]: https://github.com/clEsperanto/CLIc_prototype
[community guidelines]: https://clij.github.io/clij2-docs/community_guidelines
[github issue]: https://github.com/clEsperanto/pyclesperanto/issues
[image.sc forum]: https://forum.image.sc/
