# this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
# Do not edit manually. Instead, edit the script and run it again.

from ._core import Device
from ._array import Image
from ._decorators import plugin_function


@plugin_function
def mean_squared_error(
    input_image0: Image, input_image1: Image, device: Device = None
) -> float:
    from ._pyclesperanto import _mean_squared_error as op

    return op(device=device, src0=input_image0, src1=input_image1)


@plugin_function
def spots_to_pointlist(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _spots_to_pointlist as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def relabel_sequential(
    input_image: Image,
    output_image: Image = None,
    blocksize: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _relabel_sequential as op

    return op(
        device=device, src=input_image, dst=output_image, blocksize=int(blocksize)
    )


@plugin_function
def threshold_otsu(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _threshold_otsu as op

    return op(device=device, src=input_image, dst=output_image)
