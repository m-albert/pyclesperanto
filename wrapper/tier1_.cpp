
// this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
// Do not edit manually. Instead, edit the script and run it again.
    
#include "pycle_wrapper.hpp"
#include "tier1.hpp"

namespace py = pybind11;

auto tier1_(py::module &m) -> void {

    
m.def("_absolute", &cle::tier1::absolute_func, "Call absolute from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_add_images_weighted", &cle::tier1::add_images_weighted_func, "Call add_images_weighted from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"), py::arg("factor0"), py::arg("factor1"));

    
m.def("_add_image_and_scalar", &cle::tier1::add_image_and_scalar_func, "Call add_image_and_scalar from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_binary_and", &cle::tier1::binary_and_func, "Call binary_and from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_binary_edge_detection", &cle::tier1::binary_edge_detection_func, "Call binary_edge_detection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_binary_not", &cle::tier1::binary_not_func, "Call binary_not from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_binary_or", &cle::tier1::binary_or_func, "Call binary_or from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_binary_subtract", &cle::tier1::binary_subtract_func, "Call binary_subtract from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_binary_xor", &cle::tier1::binary_xor_func, "Call binary_xor from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_block_enumerate", &cle::tier1::block_enumerate_func, "Call block_enumerate from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"), py::arg("blocksize"));

    
m.def("_convolve", &cle::tier1::convolve_func, "Call convolve from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_copy", &cle::tier1::copy_func, "Call copy from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_copy_slice", &cle::tier1::copy_slice_func, "Call copy_slice from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("slice"));

    
m.def("_copy_horizontal_slice", &cle::tier1::copy_horizontal_slice_func, "Call copy_horizontal_slice from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("slice"));

    
m.def("_copy_vertical_slice", &cle::tier1::copy_vertical_slice_func, "Call copy_vertical_slice from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("slice"));

    
m.def("_crop", &cle::tier1::crop_func, "Call crop from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("start_x"), py::arg("start_y"), py::arg("start_z"), py::arg("width"), py::arg("height"), py::arg("depth"));

    
m.def("_cubic_root", &cle::tier1::cubic_root_func, "Call cubic_root from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_detect_label_edges", &cle::tier1::detect_label_edges_func, "Call detect_label_edges from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_detect_maxima_box", &cle::tier1::detect_maxima_box_func, "Call detect_maxima_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_detect_minima_box", &cle::tier1::detect_minima_box_func, "Call detect_minima_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_dilate_box", &cle::tier1::dilate_box_func, "Call dilate_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_dilate_sphere", &cle::tier1::dilate_sphere_func, "Call dilate_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_divide_images", &cle::tier1::divide_images_func, "Call divide_images from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_divide_image_and_scalar", &cle::tier1::divide_image_and_scalar_func, "Call divide_image_and_scalar from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_equal", &cle::tier1::equal_func, "Call equal from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_equal_constant", &cle::tier1::equal_constant_func, "Call equal_constant from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_erode_box", &cle::tier1::erode_box_func, "Call erode_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_erode_sphere", &cle::tier1::erode_sphere_func, "Call erode_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_exponential", &cle::tier1::exponential_func, "Call exponential from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_flip", &cle::tier1::flip_func, "Call flip from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("flip_x"), py::arg("flip_y"), py::arg("flip_z"));

    
m.def("_gaussian_blur", &cle::tier1::gaussian_blur_func, "Call gaussian_blur from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma_x"), py::arg("sigma_y"), py::arg("sigma_z"));

    
m.def("_gradient_x", &cle::tier1::gradient_x_func, "Call gradient_x from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_gradient_y", &cle::tier1::gradient_y_func, "Call gradient_y from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_gradient_z", &cle::tier1::gradient_z_func, "Call gradient_z from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_greater", &cle::tier1::greater_func, "Call greater from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_greater_constant", &cle::tier1::greater_constant_func, "Call greater_constant from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_greater_or_equal", &cle::tier1::greater_or_equal_func, "Call greater_or_equal from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_greater_or_equal_constant", &cle::tier1::greater_or_equal_constant_func, "Call greater_or_equal_constant from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_laplace_box", &cle::tier1::laplace_box_func, "Call laplace_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_laplace_diamond", &cle::tier1::laplace_diamond_func, "Call laplace_diamond from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_logarithm", &cle::tier1::logarithm_func, "Call logarithm from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_mask", &cle::tier1::mask_func, "Call mask from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("mask"), py::arg("dst"));

    
m.def("_mask_label", &cle::tier1::mask_label_func, "Call mask_label from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"), py::arg("label"));

    
m.def("_maximum_image_and_scalar", &cle::tier1::maximum_image_and_scalar_func, "Call maximum_image_and_scalar from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_maximum_images", &cle::tier1::maximum_images_func, "Call maximum_images from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_maximum_box", &cle::tier1::maximum_box_func, "Call maximum_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_maximum_x_projection", &cle::tier1::maximum_x_projection_func, "Call maximum_x_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_maximum_y_projection", &cle::tier1::maximum_y_projection_func, "Call maximum_y_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_maximum_z_projection", &cle::tier1::maximum_z_projection_func, "Call maximum_z_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_mean_box", &cle::tier1::mean_box_func, "Call mean_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_mean_sphere", &cle::tier1::mean_sphere_func, "Call mean_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_mean_x_projection", &cle::tier1::mean_x_projection_func, "Call mean_x_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_mean_y_projection", &cle::tier1::mean_y_projection_func, "Call mean_y_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_mean_z_projection", &cle::tier1::mean_z_projection_func, "Call mean_z_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_minimum_box", &cle::tier1::minimum_box_func, "Call minimum_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_minimum_image_and_scalar", &cle::tier1::minimum_image_and_scalar_func, "Call minimum_image_and_scalar from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_minimum_images", &cle::tier1::minimum_images_func, "Call minimum_images from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_minimum_x_projection", &cle::tier1::minimum_x_projection_func, "Call minimum_x_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_minimum_y_projection", &cle::tier1::minimum_y_projection_func, "Call minimum_y_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_minimum_z_projection", &cle::tier1::minimum_z_projection_func, "Call minimum_z_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_mode_box", &cle::tier1::mode_box_func, "Call mode_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_mode_sphere", &cle::tier1::mode_sphere_func, "Call mode_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_modulo_images", &cle::tier1::modulo_images_func, "Call modulo_images from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_multiply_image_and_scalar", &cle::tier1::multiply_image_and_scalar_func, "Call multiply_image_and_scalar from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_multiply_images", &cle::tier1::multiply_images_func, "Call multiply_images from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_nan_to_num", &cle::tier1::nan_to_num_func, "Call nan_to_num from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("nan"), py::arg("posinf"), py::arg("neginf"));

    
m.def("_nonzero_maximum_box", &cle::tier1::nonzero_maximum_box_func, "Call nonzero_maximum_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    
m.def("_nonzero_maximum_diamond", &cle::tier1::nonzero_maximum_diamond_func, "Call nonzero_maximum_diamond from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    
m.def("_nonzero_minimum_box", &cle::tier1::nonzero_minimum_box_func, "Call nonzero_minimum_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    
m.def("_nonzero_minimum_diamond", &cle::tier1::nonzero_minimum_diamond_func, "Call nonzero_minimum_diamond from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    
m.def("_not_equal", &cle::tier1::not_equal_func, "Call not_equal from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_not_equal_constant", &cle::tier1::not_equal_constant_func, "Call not_equal_constant from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_paste", &cle::tier1::paste_func, "Call paste from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("index_x"), py::arg("index_y"), py::arg("index_z"));

    
m.def("_onlyzero_overwrite_maximum_box", &cle::tier1::onlyzero_overwrite_maximum_box_func, "Call onlyzero_overwrite_maximum_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    
m.def("_onlyzero_overwrite_maximum_diamond", &cle::tier1::onlyzero_overwrite_maximum_diamond_func, "Call onlyzero_overwrite_maximum_diamond from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    
m.def("_power", &cle::tier1::power_func, "Call power from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_power_images", &cle::tier1::power_images_func, "Call power_images from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_range", &cle::tier1::range_func, "Call range from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("start_x"), py::arg("start_y"), py::arg("start_z"), py::arg("step_x"), py::arg("step_y"), py::arg("step_z"));

    
m.def("_read_intensities_from_positions", &cle::tier1::read_intensities_from_positions_func, "Call read_intensities_from_positions from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("list"), py::arg("dst"));

    
m.def("_replace_intensities", &cle::tier1::replace_intensities_func, "Call replace_intensities from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_replace_intensity", &cle::tier1::replace_intensity_func, "Call replace_intensity from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar0"), py::arg("scalar1"));

    
m.def("_maximum_sphere", &cle::tier1::maximum_sphere_func, "Call maximum_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_minimum_sphere", &cle::tier1::minimum_sphere_func, "Call minimum_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_multiply_matrix", &cle::tier1::multiply_matrix_func, "Call multiply_matrix from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_reciprocal", &cle::tier1::reciprocal_func, "Call reciprocal from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_set", &cle::tier1::set_func, "Call set from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("scalar"));

    
m.def("_set_column", &cle::tier1::set_column_func, "Call set_column from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("column"), py::arg("value"));

    
m.def("_set_image_borders", &cle::tier1::set_image_borders_func, "Call set_image_borders from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("value"));

    
m.def("_set_plane", &cle::tier1::set_plane_func, "Call set_plane from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("plane"), py::arg("value"));

    
m.def("_set_ramp_x", &cle::tier1::set_ramp_x_func, "Call set_ramp_x from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    
m.def("_set_ramp_y", &cle::tier1::set_ramp_y_func, "Call set_ramp_y from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    
m.def("_set_ramp_z", &cle::tier1::set_ramp_z_func, "Call set_ramp_z from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    
m.def("_set_row", &cle::tier1::set_row_func, "Call set_row from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("row"), py::arg("value"));

    
m.def("_set_nonzero_pixels_to_pixelindex", &cle::tier1::set_nonzero_pixels_to_pixelindex_func, "Call set_nonzero_pixels_to_pixelindex from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("offset"));

    
m.def("_set_where_x_equals_y", &cle::tier1::set_where_x_equals_y_func, "Call set_where_x_equals_y from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("value"));

    
m.def("_set_where_x_greater_than_y", &cle::tier1::set_where_x_greater_than_y_func, "Call set_where_x_greater_than_y from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("value"));

    
m.def("_set_where_x_smaller_than_y", &cle::tier1::set_where_x_smaller_than_y_func, "Call set_where_x_smaller_than_y from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("value"));

    
m.def("_sign", &cle::tier1::sign_func, "Call sign from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_smaller", &cle::tier1::smaller_func, "Call smaller from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_smaller_constant", &cle::tier1::smaller_constant_func, "Call smaller_constant from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_smaller_or_equal", &cle::tier1::smaller_or_equal_func, "Call smaller_or_equal from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_smaller_or_equal_constant", &cle::tier1::smaller_or_equal_constant_func, "Call smaller_or_equal_constant from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_sobel", &cle::tier1::sobel_func, "Call sobel from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_square_root", &cle::tier1::square_root_func, "Call square_root from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_subtract_image_from_scalar", &cle::tier1::subtract_image_from_scalar_func, "Call subtract_image_from_scalar from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    
m.def("_sum_reduction_x", &cle::tier1::sum_reduction_x_func, "Call sum_reduction_x from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("blocksize"));

    
m.def("_sum_x_projection", &cle::tier1::sum_x_projection_func, "Call sum_x_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_sum_y_projection", &cle::tier1::sum_y_projection_func, "Call sum_y_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_sum_z_projection", &cle::tier1::sum_z_projection_func, "Call sum_z_projection from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_transpose_xy", &cle::tier1::transpose_xy_func, "Call transpose_xy from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_transpose_xz", &cle::tier1::transpose_xz_func, "Call transpose_xz from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_transpose_yz", &cle::tier1::transpose_yz_func, "Call transpose_yz from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_undefined_to_zero", &cle::tier1::undefined_to_zero_func, "Call undefined_to_zero from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    
m.def("_variance_box", &cle::tier1::variance_box_func, "Call variance_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_variance_sphere", &cle::tier1::variance_sphere_func, "Call variance_sphere from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    
m.def("_write_values_to_positions", &cle::tier1::write_values_to_positions_func, "Call write_values_to_positions from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


}
