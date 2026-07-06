# proof: m720_complete_calibration_certificates

This node follows from three proved predicates.

`m720_mitm_gate` proves the scanner's trade-detection and toral/non-toral
classification gate. `m720_certificate_semantics` proves that only outputs
with `complete=true` can be treated as full calibration-cell zero certificates;
window slices remain slice-local evidence. Finally,
`m720_off_laptop_zero_certificates` proves the actual complete-cell payload:
all complete cells under the Modal policy have zero unpaid non-toral anchored
cores, and all residual configured cells are either marked as `W<n` window
slices or handled by the over-ceiling toral-complement algebra.

Therefore the complete calibration certificates are sound: complete cells have
zero unpaid non-toral active cores, and incomplete slices are not used as
global zero certificates.
