# WCL `(1,5)` pruned Singular route pilot

- **Modal app:** `ap-o5JxJJpiYoJnPSIaUkeV2b`
- **planned resources:** one CPU, 2 GiB, one container, 60-second function cap
- **outcome:** image-route cancellation; no mathematical verdict

The exact generator produced the pruned `52`-variable, `54`-equation system
locally. The Modal image then attempted Debian
`apt_install("singular")`. That package pulled a disproportionate Sage,
Jupyter, Java, graphics, and development dependency stack. The run was
cancelled during image initialization, before `pilot()` started, before the
system hash checkpoint was emitted, and before any Groebner computation.

This is a packaging fence only. Do not retry the Debian meta-package image.
A responsible follow-up must use an already cached minimal Singular image,
a contributor machine with Singular installed, or another CAS with a compact
deployment. The mathematical input remains the exact pruned system proved by
`dli_wcl_fixed_divisor_straight_line_lift`; no larger slot should run before
the `(1,5)` modular basis has a measured resource envelope.
