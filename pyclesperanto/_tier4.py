
# this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
# Do not edit manually. Instead, edit the script and run it again.

from ._core import Device
from ._array import Image, Array
from ._decorators import plugin_function


@plugin_function
def relabel_sequential(
    input_image: Image,
	output_image: Image = None,
	blocksize: int = 0,
	device: Device = None
) -> Image:
    from ._pyclesperanto import _relabel_sequential as op
    # op = _cle._relabel_sequential
    
    return op(
        device=device,
		src=input_image,
		dst=output_image,
		blocksize=int(blocksize)
    )

