def test_indexing():
    import pyclesperanto as cle

    import numpy as np

    data = np.asarray([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]).astype(np.float32)

    cl_data = cle.push(data)

    assert cl_data[0, 0] == 1
    assert cl_data[0, 1] == 2
