def test_mode_sphere_2d():
    import pyclesperanto as cle

    image = cle.asarray(
        [
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 3, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 1, 1, 1],
        ]
    )

    reference = cle.asarray(
        [
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 1, 1, 1],
        ]
    )

    result = cle.mode_sphere(image, None, 1, 1, 1)

    assert cle.array_equal(result, reference)


def test_mode_sphere_3d():
    import pyclesperanto as cle

    image = cle.asarray(
        [
            [
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 3, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 1, 1, 1],
            ]
        ]
    )

    reference = cle.asarray(
        [
            [
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 1, 1, 1],
            ]
        ]
    )

    result = cle.mode_sphere(image, None, 1, 1, 1)

    assert cle.array_equal(result, reference)
