# Replay certificate

The theorem verifier and independent consumer-backward audit were shipped by
content to Modal and passed together in app
`ap-YVuPe20N3lQuwNgedf0h5c`:

```text
RATE_HALF_CYCLIC_ROTATED_PREFIX_FLOOR_PASS
toy_d1=(5005, 313, 315) toy_d2=(3003, 2, 6)
cap_count_bits=524255 cap_list_bits=204
q_boundary_bits=256.036659972895
cap_margin_bits=75.079624489 cap_list_log2=203.079624489

AUDIT_RATE_HALF_CYCLIC_ROTATED_PREFIX_FLOOR_PASS
support_checks=3472 constant_checks=21
cap_margin_bits=75.079624489 q_boundary_bits=256.036659972895
```

The complete verifier manifest passed `178/178` in Modal app
`ap-CRn9AwYF0xIGWOsvrDntDM`, with no failure, timeout, hash mismatch, or remote
error. After the final result reference was added, all five integration gates
passed again in `ap-NskxO6rRHUTOpV4yzReG5V`.

The resulting full DAG has `661` nodes and `1172` edges, with `496` nodes
marked `PROVED`. The critical orbit is
`208 PROVED / 30 CONDITIONAL / 9 UNPROVED`; the nine red leaves are unchanged,
and `rate_half_band_closure` is now MCA/CA-only.
