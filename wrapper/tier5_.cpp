
// this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
// Do not edit manually. Instead, edit the script and run it again.
    
#include "pycle_wrapper.hpp"
#include "tier5.hpp"

namespace py = pybind11;

auto tier5_(py::module &m) -> void {

    
m.def("_combine_labels", &cle::tier5::combine_labels_func, "Call combine_labels from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    
m.def("_connected_components_labeling_box", &cle::tier5::connected_components_labeling_box_func, "Call connected_components_labeling_box from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


}
