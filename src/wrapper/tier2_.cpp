
// this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
// Do not edit manually. Instead, edit the script and run it again.

#include "pycle_wrapper.hpp"
#include "tier2.hpp"

namespace py = pybind11;

auto tier2_(py::module &m) -> void {


m.def("_absolute_difference", &cle::tier2::absolute_difference_func, "Call absolute_difference from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));


m.def("_add_images", &cle::tier2::add_images_func, "Call add_images from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));


m.def("_bottom_hat_box", &cle::tier2::bottom_hat_box_func, "Call bottom_hat_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_bottom_hat_sphere", &cle::tier2::bottom_hat_sphere_func, "Call bottom_hat_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_clip", &cle::tier2::clip_func, "Call clip from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("min_intensity"), py::arg("max_intensity"));


m.def("_closing_box", &cle::tier2::closing_box_func, "Call closing_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_closing_sphere", &cle::tier2::closing_sphere_func, "Call closing_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_concatenate_along_x", &cle::tier2::concatenate_along_x_func, "Call concatenate_along_x from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));


m.def("_concatenate_along_y", &cle::tier2::concatenate_along_y_func, "Call concatenate_along_y from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));


m.def("_concatenate_along_z", &cle::tier2::concatenate_along_z_func, "Call concatenate_along_z from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));


m.def("_count_touching_neighbors", &cle::tier2::count_touching_neighbors_func, "Call count_touching_neighbors from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("ignore_background"));


m.def("_crop_border", &cle::tier2::crop_border_func, "Call crop_border from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("border_size"));


m.def("_divide_by_gaussian_background", &cle::tier2::divide_by_gaussian_background_func, "Call divide_by_gaussian_background from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma_x"), py::arg("sigma_y"), py::arg("sigma_z"));


m.def("_degrees_to_radians", &cle::tier2::degrees_to_radians_func, "Call degrees_to_radians from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


m.def("_difference_of_gaussian", &cle::tier2::difference_of_gaussian_func, "Call difference_of_gaussian from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma1_x"), py::arg("sigma1_y"), py::arg("sigma1_z"), py::arg("sigma2_x"), py::arg("sigma2_y"), py::arg("sigma2_z"));


m.def("_extend_labeling_via_voronoi", &cle::tier2::extend_labeling_via_voronoi_func, "Call extend_labeling_via_voronoi from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


m.def("_invert", &cle::tier2::invert_func, "Call invert from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


m.def("_label_spots", &cle::tier2::label_spots_func, "Call label_spots from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


m.def("_large_hessian_eigenvalue", &cle::tier2::large_hessian_eigenvalue_func, "Call large_hessian_eigenvalue from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


m.def("_maximum_of_all_pixels", &cle::tier2::maximum_of_all_pixels_func, "Call maximum_of_all_pixels from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));


m.def("_minimum_of_all_pixels", &cle::tier2::minimum_of_all_pixels_func, "Call minimum_of_all_pixels from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));


m.def("_minimum_of_masked_pixels", &cle::tier2::minimum_of_masked_pixels_func, "Call minimum_of_masked_pixels from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("mask"));


m.def("_opening_box", &cle::tier2::opening_box_func, "Call opening_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_opening_sphere", &cle::tier2::opening_sphere_func, "Call opening_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_radians_to_degrees", &cle::tier2::radians_to_degrees_func, "Call radians_to_degrees from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


m.def("_small_hessian_eigenvalue", &cle::tier2::small_hessian_eigenvalue_func, "Call small_hessian_eigenvalue from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


m.def("_square", &cle::tier2::square_func, "Call square from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


m.def("_squared_difference", &cle::tier2::squared_difference_func, "Call squared_difference from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));


m.def("_standard_deviation_box", &cle::tier2::standard_deviation_box_func, "Call standard_deviation_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_standard_deviation_sphere", &cle::tier2::standard_deviation_sphere_func, "Call standard_deviation_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_subtract_gaussian_background", &cle::tier2::subtract_gaussian_background_func, "Call subtract_gaussian_background from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma_x"), py::arg("sigma_y"), py::arg("sigma_z"));


m.def("_subtract_images", &cle::tier2::subtract_images_func, "Call subtract_images from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));


m.def("_sum_of_all_pixels", &cle::tier2::sum_of_all_pixels_func, "Call sum_of_all_pixels from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));


m.def("_top_hat_box", &cle::tier2::top_hat_box_func, "Call top_hat_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


m.def("_top_hat_sphere", &cle::tier2::top_hat_sphere_func, "Call top_hat_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));


}
