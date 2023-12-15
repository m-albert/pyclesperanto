# this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
# Do not edit manually. Instead, edit the script and run it again.

from ._core import Device
from ._array import Image
from ._decorators import plugin_function


@plugin_function
def array_equal(
    input_image0: Image, input_image1: Image, device: Device = None
) -> bool:
    from ._pyclesperanto import _array_equal as op

    return op(device=device, src0=input_image0, src1=input_image1)


@plugin_function
def combine_labels(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _combine_labels as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def connected_components_labeling(
    input_image: Image,
    output_image: Image = None,
    connectivity: str = "",
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _connected_components_labeling as op

    return op(
        device=device, src=input_image, dst=output_image, connectivity=connectivity
    )
