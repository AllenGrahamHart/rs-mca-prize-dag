# proof: m720_off_laptop_zero_certificates

The complete zero-certificate payload is assembled from two proved predicates.

The node `m720_wsl_complete_zero_subcertificates` proves all configured cells
whose Modal window is complete and under the count ceiling:

```text
n=16, h=7, q_exp in {2,3}
n=32, h=7, q_exp in {2,3}
n=16, h=8, q_exp in {2,3}
```

Each has `complete=true` and zero unpaid non-toral anchored cores.

The node `m720_residual_off_laptop_zero_certificates` proves that every other
configured h=7..20 cell is either a `W<n` window slice or one of the two
over-ceiling `n=32,h=16` complete-window cells; those two cells have only the
paid toral even/odd coset partition.

Therefore every complete certificate cell has the required zero unpaid
non-toral count, and every slice is explicitly marked non-complete. This proves
the certificate packet.
