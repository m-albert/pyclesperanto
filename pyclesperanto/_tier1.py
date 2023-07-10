
# this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
# Do not edit manually. Instead, edit the script and run it again.

from ._core import Device
from ._array import Image, Array
from ._decorators import plugin_function


@plugin_function
def absolute(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _absolute as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def add_images_weighted(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	factor0: float = 1,
	factor1: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _add_images_weighted as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image,
		factor0=float(factor0),
		factor1=float(factor1)
    )


@plugin_function
def add_image_and_scalar(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _add_image_and_scalar as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def binary_and(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _binary_and as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def binary_edge_detection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _binary_edge_detection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def binary_not(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _binary_not as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def binary_or(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _binary_or as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def binary_subtract(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _binary_subtract as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def binary_xor(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _binary_xor as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def convolve(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _convolve as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def copy(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _copy as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def dilate_box(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _dilate_box as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def dilate_sphere(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _dilate_sphere as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def divide_images(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _divide_images as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def equal(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _equal as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def equal_constant(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _equal_constant as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def erode_box(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _erode_box as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def erode_sphere(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _erode_sphere as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def exponential(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _exponential as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def gaussian_blur(
    input_image: Image,
	output_image: Image = None,
	sigma_x: float = 1,
	sigma_y: float = 1,
	sigma_z: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _gaussian_blur as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		sigma_x=float(sigma_x),
		sigma_y=float(sigma_y),
		sigma_z=float(sigma_z)
    )


@plugin_function
def gradient_x(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _gradient_x as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def gradient_y(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _gradient_y as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def gradient_z(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _gradient_z as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def greater(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _greater as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def greater_constant(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _greater_constant as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def greater_or_equal(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _greater_or_equal as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def greater_or_equal_constant(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _greater_or_equal_constant as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def laplace_box(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _laplace_box as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def laplace_diamond(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _laplace_diamond as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def logarithm(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _logarithm as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def mask(
    input_image: Image,
	output_image: Image = None,
	mask: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _mask as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		mask=mask
    )


@plugin_function
def mask_label(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	label: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _mask_label as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image,
		label=float(label)
    )


@plugin_function
def maximum_image_and_scalar(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_image_and_scalar as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def maximum_images(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_images as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def maximum_box(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 1,
	radius_y: int = 1,
	radius_z: int = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_box as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def maximum_x_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_x_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def maximum_y_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_y_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def maximum_z_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_z_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def mean_box(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 1,
	radius_y: int = 1,
	radius_z: int = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _mean_box as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def mean_sphere(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 1,
	radius_y: int = 1,
	radius_z: int = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _mean_sphere as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def mean_x_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _mean_x_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def mean_y_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _mean_y_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def mean_z_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _mean_z_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def minimum_box(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 1,
	radius_y: int = 1,
	radius_z: int = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_box as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def minimum_image_and_scalar(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_image_and_scalar as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def minimum_images(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_images as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def minimum_x_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_x_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def minimum_y_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_y_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def minimum_z_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_z_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def multiply_image_and_scalar(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _multiply_image_and_scalar as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def multiply_images(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _multiply_images as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def nonzero_maximum_box(
    input_image: Image,
	output_image0: Image = None,
	output_image1: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _nonzero_maximum_box as op

    return op(
        device=device,
		src=input_image,
		dst0=output_image0,
		dst1=output_image1
    )


@plugin_function
def nonzero_maximum_diamond(
    input_image: Image,
	output_image0: Image = None,
	output_image1: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _nonzero_maximum_diamond as op

    return op(
        device=device,
		src=input_image,
		dst0=output_image0,
		dst1=output_image1
    )


@plugin_function
def nonzero_minimum_box(
    input_image: Image,
	output_image0: Image = None,
	output_image1: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _nonzero_minimum_box as op

    return op(
        device=device,
		src=input_image,
		dst0=output_image0,
		dst1=output_image1
    )


@plugin_function
def nonzero_minimum_diamond(
    input_image: Image,
	output_image0: Image = None,
	output_image1: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _nonzero_minimum_diamond as op

    return op(
        device=device,
		src=input_image,
		dst0=output_image0,
		dst1=output_image1
    )


@plugin_function
def not_equal(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _not_equal as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def not_equal_constant(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _not_equal_constant as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def onlyzero_overwrite_maximum_box(
    input_image: Image,
	output_image0: Image = None,
	output_image1: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _onlyzero_overwrite_maximum_box as op

    return op(
        device=device,
		src=input_image,
		dst0=output_image0,
		dst1=output_image1
    )


@plugin_function
def onlyzero_overwrite_maximum_diamond(
    input_image: Image,
	output_image0: Image = None,
	output_image1: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _onlyzero_overwrite_maximum_diamond as op

    return op(
        device=device,
		src=input_image,
		dst0=output_image0,
		dst1=output_image1
    )


@plugin_function
def power(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _power as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def power_images(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _power_images as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def replace_intensities(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _replace_intensities as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def replace_intensity(
    input_image: Image,
	output_image: Image = None,
	scalar0: float = 1,
	scalar1: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _replace_intensity as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar0=float(scalar0),
		scalar1=float(scalar1)
    )


@plugin_function
def maximum_sphere(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 1,
	radius_y: int = 1,
	radius_z: int = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_sphere as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def minimum_sphere(
    input_image: Image,
	output_image: Image = None,
	radius_x: int = 1,
	radius_y: int = 1,
	radius_z: int = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_sphere as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		radius_x=int(radius_x),
		radius_y=int(radius_y),
		radius_z=int(radius_z)
    )


@plugin_function
def set(
    output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _set as op

    return op(
        device=device,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def set_column(
    output_image: Image = None,
	column: int = 1,
	value: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _set_column as op

    return op(
        device=device,
		dst=output_image,
		column=int(column),
		value=float(value)
    )


@plugin_function
def set_row(
    output_image: Image = None,
	row: int = 1,
	value: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _set_row as op

    return op(
        device=device,
		dst=output_image,
		row=int(row),
		value=float(value)
    )


@plugin_function
def set_nonzero_pixels_to_pixelindex(
    input_image: Image,
	output_image: Image = None,
	offset: int = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _set_nonzero_pixels_to_pixelindex as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		offset=int(offset)
    )


@plugin_function
def smaller(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _smaller as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def smaller_constant(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _smaller_constant as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def smaller_or_equal(
    input_image0: Image,
	input_image1: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _smaller_or_equal as op

    return op(
        device=device,
		src0=input_image0,
		src1=input_image1,
		dst=output_image
    )


@plugin_function
def smaller_or_equal_constant(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _smaller_or_equal_constant as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def sobel(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _sobel as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def subtract_image_from_scalar(
    input_image: Image,
	output_image: Image = None,
	scalar: float = 1,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _subtract_image_from_scalar as op

    return op(
        device=device,
		src=input_image,
		dst=output_image,
		scalar=float(scalar)
    )


@plugin_function
def sum_x_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _sum_x_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def sum_y_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _sum_y_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )


@plugin_function
def sum_z_projection(
    input_image: Image,
	output_image: Image = None,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _sum_z_projection as op

    return op(
        device=device,
		src=input_image,
		dst=output_image
    )

