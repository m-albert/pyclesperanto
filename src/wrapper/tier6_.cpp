
// this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
// Do not edit manually. Instead, edit the script and run it again.
    
#include "pycle_wrapper.hpp"
#include "tier6.hpp"

namespace py = pybind11;

auto tier6_(py::module &m) -> void {

    
m.def("_dilate_labels", &cle::tier6::dilate_labels_func, "Call dilate_labels from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"));

	
m.def("_erode_labels", &cle::tier6::erode_labels_func, "Call erode_labels from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"), py::arg("relabel"));

	
m.def("_masked_voronoi_labeling", &cle::tier6::masked_voronoi_labeling_func, "Call masked_voronoi_labeling from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("mask"), py::arg("dst"));

	
m.def("_voronoi_labeling", &cle::tier6::voronoi_labeling_func, "Call voronoi_labeling from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


}
