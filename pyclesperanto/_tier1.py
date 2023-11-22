# this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
# Do not edit manually. Instead, edit the script and run it again.

from ._core import Device
from ._array import Image
from ._decorators import plugin_function


@plugin_function
def absolute(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _absolute as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def add_images_weighted(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    factor0: float = 0,
    factor1: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _add_images_weighted as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image,
        factor0=float(factor0),
        factor1=float(factor1),
    )


@plugin_function
def add_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _add_image_and_scalar as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def binary_and(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _binary_and as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def binary_edge_detection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _binary_edge_detection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def binary_not(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _binary_not as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def binary_or(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _binary_or as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def binary_subtract(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _binary_subtract as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def binary_xor(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _binary_xor as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def block_enumerate(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    blocksize: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _block_enumerate as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image,
        blocksize=int(blocksize),
    )


@plugin_function
def convolve(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _convolve as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def copy(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _copy as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def copy_slice(
    input_image: Image,
    output_image: Image = None,
    slice: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _copy_slice as op

    return op(device=device, src=input_image, dst=output_image, slice=int(slice))


@plugin_function
def copy_horizontal_slice(
    input_image: Image,
    output_image: Image = None,
    slice: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _copy_horizontal_slice as op

    return op(device=device, src=input_image, dst=output_image, slice=int(slice))


@plugin_function
def copy_vertical_slice(
    input_image: Image,
    output_image: Image = None,
    slice: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _copy_vertical_slice as op

    return op(device=device, src=input_image, dst=output_image, slice=int(slice))


@plugin_function
def crop(
    input_image: Image,
    output_image: Image = None,
    start_x: int = 0,
    start_y: int = 0,
    start_z: int = 0,
    width: int = 0,
    height: int = 0,
    depth: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _crop as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        start_x=int(start_x),
        start_y=int(start_y),
        start_z=int(start_z),
        width=int(width),
        height=int(height),
        depth=int(depth),
    )


@plugin_function
def cubic_root(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _cubic_root as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def detect_label_edges(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _detect_label_edges as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def detect_maxima_box(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _detect_maxima_box as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def detect_minima_box(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _detect_minima_box as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def dilate_box(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _dilate_box as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def dilate_sphere(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _dilate_sphere as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def divide_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _divide_images as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def divide_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _divide_image_and_scalar as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _equal as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _equal_constant as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def erode_box(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _erode_box as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def erode_sphere(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _erode_sphere as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def exponential(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _exponential as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def flip(
    input_image: Image,
    output_image: Image = None,
    flip_x: bool = True,
    flip_y: bool = True,
    flip_z: bool = True,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _flip as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        flip_x=bool(flip_x),
        flip_y=bool(flip_y),
        flip_z=bool(flip_z),
    )


@plugin_function
def gaussian_blur(
    input_image: Image,
    output_image: Image = None,
    sigma_x: float = 0,
    sigma_y: float = 0,
    sigma_z: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _gaussian_blur as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        sigma_x=float(sigma_x),
        sigma_y=float(sigma_y),
        sigma_z=float(sigma_z),
    )


@plugin_function
def generate_distance_matrix(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _generate_distance_matrix as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def gradient_x(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _gradient_x as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def gradient_y(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _gradient_y as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def gradient_z(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _gradient_z as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def greater(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _greater as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def greater_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _greater_constant as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def greater_or_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _greater_or_equal as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def greater_or_equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _greater_or_equal_constant as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def hessian_eigenvalues(
    input_image: Image,
    small_eigenvalue: Image = None,
    middle_eigenvalue: Image = None,
    large_eigenvalue: Image = None,
    device: Device = None,
) -> list:
    from ._pyclesperanto import _hessian_eigenvalues as op

    return op(
        device=device,
        src=input_image,
        small_eigenvalue=small_eigenvalue,
        middle_eigenvalue=middle_eigenvalue,
        large_eigenvalue=large_eigenvalue,
    )


@plugin_function
def laplace_box(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _laplace_box as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def laplace_diamond(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _laplace_diamond as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def local_cross_correlation(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _local_cross_correlation as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def logarithm(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _logarithm as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def mask(
    input_image: Image,
    mask: Image = None,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _mask as op

    return op(device=device, src=input_image, mask=mask, dst=output_image)


@plugin_function
def mask_label(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    label: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _mask_label as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image,
        label=float(label),
    )


@plugin_function
def maximum_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _maximum_image_and_scalar as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def maximum_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _maximum_images as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def maximum_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _maximum_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def maximum_x_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_x_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def maximum_y_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_y_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def maximum_z_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _maximum_z_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def mean_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _mean_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def mean_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _mean_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def mean_x_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _mean_x_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def mean_y_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _mean_y_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def mean_z_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _mean_z_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def median_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _median_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def median_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _median_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def minimum_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _minimum_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def minimum_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _minimum_image_and_scalar as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def minimum_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _minimum_images as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def minimum_x_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_x_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def minimum_y_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_y_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def minimum_z_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _minimum_z_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def minimum_of_masked_pixels_reduction(
    input_image: Image,
    mask: Image,
    reduced_input_image: Image,
    reduced_mask: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _minimum_of_masked_pixels_reduction as op

    return op(
        device=device,
        src=input_image,
        mask=mask,
        reduced_src=reduced_input_image,
        reduced_mask=reduced_mask,
    )


@plugin_function
def mode_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _mode_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def mode_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _mode_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def modulo_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _modulo_images as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def multiply_image_and_coordinate(
    input_image: Image,
    output_image: Image = None,
    dimension: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _multiply_image_and_coordinate as op

    return op(
        device=device, src=input_image, dst=output_image, dimension=int(dimension)
    )


@plugin_function
def multiply_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _multiply_image_and_scalar as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def multiply_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _multiply_images as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def nan_to_num(
    input_image: Image,
    output_image: Image = None,
    nan: float = 0,
    posinf: float = 0,
    neginf: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _nan_to_num as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        nan=float(nan),
        posinf=float(posinf),
        neginf=float(neginf),
    )


@plugin_function
def nonzero_maximum_box(
    input_image: Image,
    output_image0: Image = None,
    output_image1: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _nonzero_maximum_box as op

    return op(device=device, src=input_image, dst0=output_image0, dst1=output_image1)


@plugin_function
def nonzero_maximum_diamond(
    input_image: Image,
    output_image0: Image = None,
    output_image1: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _nonzero_maximum_diamond as op

    return op(device=device, src=input_image, dst0=output_image0, dst1=output_image1)


@plugin_function
def nonzero_minimum_box(
    input_image: Image,
    output_image0: Image = None,
    output_image1: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _nonzero_minimum_box as op

    return op(device=device, src=input_image, dst0=output_image0, dst1=output_image1)


@plugin_function
def nonzero_minimum_diamond(
    input_image: Image,
    output_image0: Image = None,
    output_image1: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _nonzero_minimum_diamond as op

    return op(device=device, src=input_image, dst0=output_image0, dst1=output_image1)


@plugin_function
def not_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _not_equal as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def not_equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _not_equal_constant as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def paste(
    input_image: Image,
    output_image: Image = None,
    index_x: int = 0,
    index_y: int = 0,
    index_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _paste as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        index_x=int(index_x),
        index_y=int(index_y),
        index_z=int(index_z),
    )


@plugin_function
def onlyzero_overwrite_maximum_box(
    input_image: Image,
    output_image0: Image = None,
    output_image1: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _onlyzero_overwrite_maximum_box as op

    return op(device=device, src=input_image, dst0=output_image0, dst1=output_image1)


@plugin_function
def onlyzero_overwrite_maximum_diamond(
    input_image: Image,
    output_image0: Image = None,
    output_image1: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _onlyzero_overwrite_maximum_diamond as op

    return op(device=device, src=input_image, dst0=output_image0, dst1=output_image1)


@plugin_function
def power(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _power as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def power_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _power_images as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def range(
    input_image: Image,
    output_image: Image = None,
    start_x: int = 0,
    stop_x: int = 0,
    step_x: int = 0,
    start_y: int = 0,
    stop_y: int = 0,
    step_y: int = 0,
    start_z: int = 0,
    stop_z: int = 0,
    step_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _range as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        start_x=int(start_x),
        stop_x=int(stop_x),
        step_x=int(step_x),
        start_y=int(start_y),
        stop_y=int(stop_y),
        step_y=int(step_y),
        start_z=int(start_z),
        stop_z=int(stop_z),
        step_z=int(step_z),
    )


@plugin_function
def read_values_from_coordinates(
    input_image: Image,
    list: Image = None,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _read_values_from_coordinates as op

    return op(device=device, src=input_image, list=list, dst=output_image)


@plugin_function
def replace_values(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _replace_values as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def replace_value(
    input_image: Image,
    output_image: Image = None,
    scalar0: float = 0,
    scalar1: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _replace_value as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar0=float(scalar0),
        scalar1=float(scalar1),
    )


@plugin_function
def maximum_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: float = 0,
    radius_y: float = 0,
    radius_z: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _maximum_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=float(radius_x),
        radius_y=float(radius_y),
        radius_z=float(radius_z),
    )


@plugin_function
def minimum_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: float = 0,
    radius_y: float = 0,
    radius_z: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _minimum_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=float(radius_x),
        radius_y=float(radius_y),
        radius_z=float(radius_z),
    )


@plugin_function
def multiply_matrix(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _multiply_matrix as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def reciprocal(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _reciprocal as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def set(input_image: Image, scalar: float = 0, device: Device = None) -> Image:
    from ._pyclesperanto import _set as op

    return op(device=device, src=input_image, scalar=float(scalar))


@plugin_function
def set_column(
    input_image: Image, column: int = 0, value: float = 0, device: Device = None
) -> Image:
    from ._pyclesperanto import _set_column as op

    return op(device=device, src=input_image, column=int(column), value=float(value))


@plugin_function
def set_image_borders(
    input_image: Image, value: float = 0, device: Device = None
) -> Image:
    from ._pyclesperanto import _set_image_borders as op

    return op(device=device, src=input_image, value=float(value))


@plugin_function
def set_plane(
    input_image: Image, plane: int = 0, value: float = 0, device: Device = None
) -> Image:
    from ._pyclesperanto import _set_plane as op

    return op(device=device, src=input_image, plane=int(plane), value=float(value))


@plugin_function
def set_ramp_x(input_image: Image, device: Device = None) -> Image:
    from ._pyclesperanto import _set_ramp_x as op

    return op(device=device, src=input_image)


@plugin_function
def set_ramp_y(input_image: Image, device: Device = None) -> Image:
    from ._pyclesperanto import _set_ramp_y as op

    return op(device=device, src=input_image)


@plugin_function
def set_ramp_z(input_image: Image, device: Device = None) -> Image:
    from ._pyclesperanto import _set_ramp_z as op

    return op(device=device, src=input_image)


@plugin_function
def set_row(
    input_image: Image, row: int = 0, value: float = 0, device: Device = None
) -> Image:
    from ._pyclesperanto import _set_row as op

    return op(device=device, src=input_image, row=int(row), value=float(value))


@plugin_function
def set_nonzero_pixels_to_pixelindex(
    input_image: Image,
    output_image: Image = None,
    offset: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _set_nonzero_pixels_to_pixelindex as op

    return op(device=device, src=input_image, dst=output_image, offset=int(offset))


@plugin_function
def set_where_x_equals_y(
    input_image: Image, value: float = 0, device: Device = None
) -> Image:
    from ._pyclesperanto import _set_where_x_equals_y as op

    return op(device=device, src=input_image, value=float(value))


@plugin_function
def set_where_x_greater_than_y(
    input_image: Image, value: float = 0, device: Device = None
) -> Image:
    from ._pyclesperanto import _set_where_x_greater_than_y as op

    return op(device=device, src=input_image, value=float(value))


@plugin_function
def set_where_x_smaller_than_y(
    input_image: Image, value: float = 0, device: Device = None
) -> Image:
    from ._pyclesperanto import _set_where_x_smaller_than_y as op

    return op(device=device, src=input_image, value=float(value))


@plugin_function
def sign(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _sign as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def smaller(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _smaller as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def smaller_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _smaller_constant as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def smaller_or_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _smaller_or_equal as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function
def smaller_or_equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _smaller_or_equal_constant as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def sobel(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _sobel as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def square_root(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _square_root as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def std_z_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _std_z_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def subtract_image_from_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _subtract_image_from_scalar as op

    return op(device=device, src=input_image, dst=output_image, scalar=float(scalar))


@plugin_function
def sum_reduction_x(
    input_image: Image,
    output_image: Image = None,
    blocksize: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _sum_reduction_x as op

    return op(
        device=device, src=input_image, dst=output_image, blocksize=int(blocksize)
    )


@plugin_function
def sum_x_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _sum_x_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def sum_y_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _sum_y_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def sum_z_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _sum_z_projection as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def transpose_xy(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _transpose_xy as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def transpose_xz(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _transpose_xz as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def transpose_yz(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _transpose_yz as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def undefined_to_zero(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _undefined_to_zero as op

    return op(device=device, src=input_image, dst=output_image)


@plugin_function
def variance_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _variance_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def variance_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    from ._pyclesperanto import _variance_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )


@plugin_function
def write_values_to_coordinates(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    from ._pyclesperanto import _write_values_to_coordinates as op

    return op(device=device, src=input_image, dst=output_image)
