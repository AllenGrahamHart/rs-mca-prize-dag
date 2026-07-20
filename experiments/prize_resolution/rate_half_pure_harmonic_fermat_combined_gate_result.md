# Pure harmonic/Fermat combined toy gate

The exact pilot exhausts every four-point deleted support in the first two
toy dyadic rows. `harmonic` means that one quadratic pairing norm vanishes;
`fermat` means that the exact quotient has the required decomposition
`B^4+Z^4` with `B(0)=1` and `ord_0 Z=1`.

```text
d   p    supports  harmonic  fermat  combined
8   17         70        56       2         0
8   97         70         4       2         0
8  113         70         0       2         0
8  193         70         0       2         0
16  97       1820       312       0         0
16 193       1820       144       0         0
16 257       1820       128       0         0
```

At `d=8`, the two Fermat supports are the two cosets of the order-four
subgroup; neither is harmonic. At `d=16`, no support passes the Fermat test in
the three checked fields, even though harmonic supports occur in all three.

This is route-selection evidence only. It neither covers all characteristics
at either toy degree nor implies emptiness at the official `d=2^39` row.

Replay:

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/rate_half_pure_harmonic_fermat_combined_gate_pilot.py
```
