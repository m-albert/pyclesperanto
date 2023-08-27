
# this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
# Do not edit manually. Instead, edit the script and run it again.

from ._core import Device
from ._array import Image
from ._decorators import plugin_function


@plugin_function
def exclude_labels_on_edges(
    input_image: Image,
	output_image: Image = None,
	exclude_x: bool = True,
	exclude_y: bool = True,
	exclude_z: bool = True,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _exclude_labels_on_edges as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		exclude_x=bool(exclude_x),
		exclude_y=bool(exclude_y),
		exclude_z=bool(exclude_z)
    )


@plugin_function
def flag_existing_labels(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _flag_existing_labels as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def gamma_correction(
    input_image: Image,
	output_image: Image = None,
	gamma: float = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _gamma_correction as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		gamma=float(gamma)
    )


@plugin_function
def histogram(
    input_image: Image,
	output_image: Image = None,
	nbins: int = 0,
	min: float = 0,
	max: float = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _histogram as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		nbins=int(nbins),
		min=float(min),
		max=float(max)
    )


@plugin_function
def mean_of_all_pixels(
    input_image: Image,
	device: Device = None
) -> float:
    from ._pyclesperanto import _mean_of_all_pixels as op

    return op(
        device=device,
		src=input_image
    )

