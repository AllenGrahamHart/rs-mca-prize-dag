# Replay certificate

The current theorem verifier and independent consumer-backward audit pass
locally under RAMguard:

```text
RATE_HALF_CYCLIC_ROTATED_PREFIX_FLOOR_PASS
toy_d1=(5005, 313, 315) toy_d2=(3003, 2, 6)
cap_count_bits=251 cap_list_bits=243
q_boundary_bits=370.650300488320
cap_margin_bits=114.650300488 cap_list_log2=242.650300488
cap_uniform_extremality_checks=74

AUDIT_RATE_HALF_CYCLIC_ROTATED_PREFIX_FLOOR_PASS
support_checks=3472 constant_checks=21
historical_margin_bits=75.079624489
optimized_margin_bits=114.650300488
list_bits=243 extremality_checks=74
```

The optimized theorem has also been packaged in upstream draft PR `#1051`
using Przemek's Lane-L terminology. That packet adds a concrete
`F_6597069766657` Pocklington anchor and an independently written portable
audit. Upstream review is pending and is not a local proof dependency.

Historical provenance for the first `N=2^19,d=2048` instantiation remains in
Modal app `ap-YVuPe20N3lQuwNgedf0h5c`; its `75.079624489`-bit margin is still
replayed by the current audit. The old full-manifest apps
`ap-CRn9AwYF0xIGWOsvrDntDM` and `ap-NskxO6rRHUTOpV4yzReG5V` predate the
optimized statement and are retained only as provenance, not current-DAG
certificates.
