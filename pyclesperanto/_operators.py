import numpy as np
import numbers

from typing import Optional

cl_buffer_datatype_dict = {
    bool: "bool",
    np.uint8: "uchar",
    np.uint16: "ushort",
    np.uint32: "uint",
    np.uint64: "ulong",
    np.int8: "char",
    np.int16: "short",
    np.int32: "int",
    np.int64: "long",
    np.float32: "float",
    np.complex64: "cfloat_t",
    int: "int",
    float: "float",
    np.float64: "float",
}

_supported_numeric_types = tuple(cl_buffer_datatype_dict.keys())


def astype(self, dtype: type):
    if dtype not in _supported_numeric_types:
        raise ValueError(
            "dtype "
            + str(dtype)
            + " not supported. Use one of "
            + str(_supported_numeric_types)
        )
    if dtype == self.dtype:
        return self

    from ._tier1 import copy
    from ._memory import create_like

    result = create_like(self, dtype=dtype)
    copy(input_image=self, output_image=result)
    return result


def max(self, axis: Optional[int] = None, out=None):
    from ._tier2 import maximum_of_all_pixels
    from ._tier1 import maximum_x_projection
    from ._tier1 import maximum_y_projection
    from ._tier1 import maximum_z_projection

    if axis == 0:
        result = maximum_z_projection(self)
    elif axis == 1:
        result = maximum_y_projection(self)
    elif axis == 2:
        result = maximum_x_projection(self)
    elif axis is None:
        result = maximum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + axis + " not supported")
    if out is not None:
        from ._memory import pull
        from ._array import Image

        if isinstance(out, Image):
            np.copyto(out, pull(result).astype(out.dtype))
        else:
            out = result
    return result


def min(self, axis: Optional[int] = None, out=None):
    from ._tier2 import minimum_of_all_pixels
    from ._tier1 import minimum_x_projection
    from ._tier1 import minimum_y_projection
    from ._tier1 import minimum_z_projection

    if axis == 0:
        result = minimum_z_projection(self)
    elif axis == 1:
        result = minimum_y_projection(self)
    elif axis == 2:
        result = minimum_x_projection(self)
    elif axis is None:
        result = minimum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + axis + " not supported")
    if out is not None:
        from ._memory import pull
        from ._array import Image

        if isinstance(out, Image):
            np.copyto(out, pull(result).astype(out.dtype))
    return result


def sum(self, axis: Optional[int] = None, out=None):
    from ._tier2 import sum_of_all_pixels
    from ._tier1 import sum_x_projection
    from ._tier1 import sum_y_projection
    from ._tier1 import sum_z_projection

    if axis == 0:
        result = sum_z_projection(self)
    elif axis == 1:
        result = sum_y_projection(self)
    elif axis == 2:
        result = sum_x_projection(self)
    elif axis is None:
        result = sum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + axis + " not supported")
    if out is not None:
        from ._memory import pull
        from ._array import Image

        if isinstance(out, Image):
            np.copyto(out, pull(result).astype(out.dtype))
    return result


def __iadd__(x1, x2):
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import add_image_and_scalar

        return add_image_and_scalar(temp, x1, scalar=x2)
    else:
        from ._tier1 import add_images_weighted

        return add_images_weighted(temp, x2, x1, factor0=1, factor1=1)


def __sub__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import add_image_and_scalar

        return add_image_and_scalar(x1, scalar=-x2)
    else:
        from ._tier1 import add_images_weighted

        return add_images_weighted(x1, x2, factor0=1, factor1=-1)


def __div__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(x1, scalar=1.0 / x2)
    else:
        from ._tier1 import divide_images

        return divide_images(x1, x2)


def __truediv__(x1, x2):
    return x1.__div__(x2)


def __idiv__(x1, x2):
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
    else:
        from ._tier1 import divide_images

        return divide_images(temp, x2, x1)


def __itruediv__(x1, x2):
    return x1.__idiv__(x2)


def __mul__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(x1, scalar=x2)
    else:
        from ._tier1 import multiply_images

        return multiply_images(x1, x2)


def __imul__(x1, x2):
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(temp, x1, scalar=x2)
    else:
        from ._tier1 import multiply_images

        return multiply_images(temp, x2, x1)


def __gt__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import greater_constant

        return greater_constant(x1, scalar=x2)
    else:
        from ._tier1 import greater

        return greater(x1, x2)


def __ge__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import greater_or_equal_constant

        return greater_or_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import greater_or_equal

        return greater_or_equal(x1, x2)


def __lt__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import smaller_constant

        return smaller_constant(x1, scalar=x2)
    else:
        from ._tier1 import smaller

        return smaller(x1, x2)


def __le__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import smaller_or_equal_constant

        return smaller_or_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import smaller_or_equal

        return smaller_or_equal(x1, x2)


def __eq__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import equal_constant

        return equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import equal

        return equal(x1, x2)


def __ne__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import not_equal_constant

        return not_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import not_equal

        return not_equal(x1, x2)


def __pow__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import power

        return power(x1, exponent=x2)
    else:
        from ._tier1 import power_images

        return power_images(x1, x2)


def __ipow__(x1, x2):
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import power

        return power(temp, x1, exponent=x2)
    else:
        from ._tier1 import power_images

        return power_images(temp, x2, x1)


def __iter__(self):
    class MyIterator:
        def __init__(self, image):
            self.image = image
            self._iter_index = 0

        def __next__(self):
            import numpy as np
            from ._memory import create
            from ._tier1 import copy_slice

            if not hasattr(self, "_iter_index"):
                self._iter_index = 0
            if self._iter_index < self.image.shape[0]:
                if len(self.image.shape) < 3:
                    result = np.asarray(self.image)[self._iter_index]
                elif len(self.image.shape) == 3:
                    output = create(self.image.shape[1:])
                    result = copy_slice(self.image, output, self._iter_index)
                else:
                    raise ValueError("Only 1D, 2D or 3D array are supported.")
                self._iter_index = self._iter_index + 1
                return result
            else:
                raise StopIteration

    return MyIterator(self)


def __getitem__(self, key):
    # enforce key to be iterable tuple
    if not isinstance(key, tuple):
        key = (key,)

    # replace Elipsis by emplty slices if any
    if any(x is Ellipsis for x in key):
        key = tuple(slice(None, None, None) if x is Ellipsis else x for x in key)

    # define default index as slices(0, shape, 1), and iterate over keys and replace when relevant
    index = [[0, x, 1] for x in self.shape]
    for x in range(len(key)):
        if isinstance(key[x], slice):
            start = key[x].start if key[x].start else 0
            stop = key[x].stop if key[x].stop else self.shape[x]
            step = key[x].step if key[x].step else 1
            start = self.shape[x] + start if start < 0 else start
            stop = self.shape[x] + stop if stop < 0 else stop
            index[x] = [start, stop, step]
        elif np.issubdtype(type(key[x]), np.integer):
            start = key[x]
            stop = key[x] + 1
            if key[x] < 0:
                start = self.shape[x] + key[x]
                stop = start - 1
            index[x] = [start, stop, 1]
    key = index

    # step is not equal to 1, we are dealing with a range operation
    if any([abs(index[2]) != 1 for index in key]):
        from ._tier1 import range as gpu_range

        x_range = [0, 0, 0]
        y_range = [0, 0, 0]
        z_range = [0, 0, 0]
        if len(key) == 1:
            x_range = key[0]
        elif len(key) == 2:
            x_range = key[1]
            y_range = key[0]
        elif len(key) == 3:
            x_range = key[2]
            y_range = key[1]
            z_range = key[0]
        result = gpu_range(
            self,
            start_x=x_range[0],
            stop_x=x_range[1],
            step_x=x_range[2],
            start_y=y_range[0],
            stop_y=y_range[1],
            step_y=y_range[2],
            start_z=z_range[0],
            stop_z=z_range[1],
            step_z=z_range[2],
        )
    else:
        # all steps equal to 1, we are dealing with a sub-region operation

        # we define the sub-region origin and region size
        origin = [index[0] for index in key]
        region = [abs(index[1] - index[0]) for index in key]
        transpose = [x == 1 for x in region]

        # if region size equal to 1, we are returning a scalar
        if np.prod(region) == 1:
            result = self.get(origin, region)
        else:
            # we are returning a buffer that we first need to create
            from ._memory import create

            result = create(
                region, dtype=self.dtype, mtype=self.mtype, device=self.device
            )

            # we copy sub-region inside our new buffer to return
            self.copy(result, origin, (0, 0, 0), region)

            # if new_shape different than tmp.shape, we need to reshape
            if any(transpose):
                from ._tier1 import transpose_xy, transpose_yz, transpose_xz

                if transpose[2]:
                    # x is empty we move it to the end
                    result = transpose_xy(result)
                    result = transpose_yz(result)
                if transpose[1]:
                    # the y is empty, we exchange axis z and y
                    result = transpose_yz(result)

            # if an axis step was negative, we flip along this axis
            flip_bool = [index[2] < 0 for index in key]
            if any(flip_bool):
                from ._tier1 import flip

                result = flip(
                    input_image=result,
                    flip_x=flip_bool[2],
                    flip_y=flip_bool[1],
                    flip_z=flip_bool[0],
                )
    return result


def __setitem__(self, key, value):
    from ._array import Image, Array

    if not isinstance(value, Image):
        value = np.array(value)

        # enforce key to be iterable tuple
    if not isinstance(key, tuple):
        key = (key,)

    # replace Elipsis by emplty slices if any
    if any(x is Ellipsis for x in key):
        key = tuple(slice(None, None, None) if x is Ellipsis else x for x in key)

    # define default index as slices(0, shape, 1), and iterate over keys and replace when relevant
    index = [[0, x, 1] for x in self.shape]
    for x in range(len(key)):
        if isinstance(key[x], slice):
            start = key[x].start if key[x].start else 0
            stop = key[x].stop if key[x].stop else self.shape[x]
            step = key[x].step if key[x].step else 1
            start = self.shape[x] + start if start < 0 else start
            stop = self.shape[x] + stop if stop < 0 else stop
            index[x] = [start, stop, step]
        elif np.issubdtype(type(key[x]), np.integer):
            start = key[x]
            stop = key[x] + 1
            if key[x] < 0:
                start = self.shape[x] + key[x]
                stop = start - 1
            index[x] = [start, stop, 1]
    key = index

    if any([abs(index[2]) != 1 for index in key]):
        raise NotImplementedError("Steps in slicing is not supported yet")
    else:
        # all steps equal to 1, we are dealing with a sub-region operation

        # we define the sub-region origin and region size
        origin = [index[0] for index in key]
        region = [abs(index[1] - index[0]) for index in key]

        if isinstance(value, Array):
            # we copy from device to device and size matches
            if value.size != np.prod(region):
                raise ValueError(
                    f"Input dimensions mismatch the indexed region: {value.size} != {np.prod(region)} ({value.shape} != {region})"
                )

            if self.dtype == value.dtype:
                # if dtype are the same we can copy
                self.copy(value, origin, (0, 0, 0), region)
            else:
                # otherwise we copy with cast using paste
                from ._tier1 import paste

                paste(
                    value,
                    self,
                    index_x=origin[-1] if len(origin) > 0 else 0,
                    index_y=origin[-2] if len(origin) > 1 else 0,
                    index_z=origin[-3] if len(origin) > 2 else 0,
                )
        else:
            # we copy from host to device
            if value.size == 1:
                # value is a scalar, we repeat it to match the region size before writing
                value = np.repeat(value, np.prod(region))
                value = value.reshape(region)
            if value.size != np.prod(region):
                raise ValueError(
                    f"Input size mismatch the indexed region: {value.size} != {np.prod(region)} ({value.shape} != {region})"
                )
            # we write from host to device, if shape matches
            self.set(value, origin, region)


# adapted from https://github.com/napari/napari/blob/d6bc683b019c4a3a3c6e936526e29bbd59cca2f4/napari/utils/notebook_display.py#L54-L73
def _plt_to_png(self):
    """PNG representation of the image object for IPython.
    Returns
    -------
    In memory binary stream containing a PNG matplotlib image.
    """
    import matplotlib.pyplot as plt
    from io import BytesIO

    with BytesIO() as file_obj:
        plt.savefig(file_obj, format="png")
        plt.close()  # supress plot output
        file_obj.seek(0)
        png = file_obj.read()
    return png


def _png_to_html(self, png):
    import base64

    url = "data:image/png;base64," + base64.b64encode(png).decode("utf-8")
    return f'<img src="{url}"></img>'


def _repr_html_(self):
    """HTML representation of the image object for IPython.
    Returns
    -------
    HTML text with the image and some properties.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from ._functionalities import imshow

    size_in_pixels = np.prod(self.size)
    size_in_bytes = size_in_pixels * self.dtype.itemsize

    labels = self.dtype == np.uint32

    # In case the image is 2D, 3D and larger than 100 pixels, turn on fancy view
    if len(self.shape) in (2, 3) and size_in_pixels >= 100:
        imshow(self, labels=labels, continue_drawing=True, colorbar=not labels)
        image = self._png_to_html(self._plt_to_png())
    else:
        return "<pre>" + repr(self) + "</pre>"

    units = ["B", "kB", "MB", "GB", "TB", "PB"]
    unit_index = 0
    while size_in_bytes > 1024 and unit_index < len(units) - 1:
        size_in_bytes /= 1024
        unit_index += 1
    size = "{:.1f}".format(size_in_bytes) + " " + units[unit_index]

    histogram = ""
    if size_in_bytes < 100 * 1024 * 1024:
        if not labels:
            from ._tier3 import histogram

            num_bins = 32
            h = np.asarray(
                histogram(self, nbins=num_bins, min=self.min(), max=self.max())
            )
            plt.figure(figsize=(1.8, 1.2))
            plt.bar(range(0, len(h)), h)
            # hide axis text
            # https://stackoverflow.com/questions/2176424/hiding-axis-text-in-matplotlib-plots
            # https://pythonguides.com/matplotlib-remove-tick-labels
            frame1 = plt.gca()
            frame1.axes.xaxis.set_ticklabels([])
            frame1.axes.yaxis.set_ticklabels([])
            plt.tick_params(left=False, bottom=False)
            histogram = self._png_to_html(self._plt_to_png())
        min_max = (
            "<tr><td>min</td><td>"
            + str(self.min())
            + "</td></tr>"
            + "<tr><td>max</td><td>"
            + str(self.max())
            + "</td></tr>"
        )
    else:
        min_max = ""
    all = [
        "<table>",
        "<tr>",
        "<td>",
        image,
        "</td>",
        '<td style="text-align: center; vertical-align: top;">',
        '<b><a href="https://github.com/clEsperanto/pyclesperanto_prototype" target="_blank">cle._</a> image</b><br/>',
        "<table>",
        "<tr><td>shape</td><td>"
        + str(self.shape).replace(" ", "&nbsp;")
        + "</td></tr>",
        "<tr><td>dtype</td><td>" + str(self.dtype) + "</td></tr>",
        "<tr><td>size</td><td>" + size + "</td></tr>",
        min_max,
        "</table>",
        histogram,
        "</td>",
        "</tr>",
        "</table>",
    ]
    return "\n".join(all)
