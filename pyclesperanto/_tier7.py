# this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
# Do not edit manually. Instead, edit the script and run it again.

from ._core import Device
from ._array import Image
from ._decorators import plugin_function


@plugin_function
def voronoi_otsu_labeling(
    input_image: Image,
    output_image: Image = None,
    spot_sigma: float = 0,
    outline_sigma: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _voronoi_otsu_labeling as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        spot_sigma=float(spot_sigma),
        outline_sigma=float(outline_sigma),
    )
