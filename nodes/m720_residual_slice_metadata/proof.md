# proof: m720_residual_slice_metadata

The verifier mechanically replays the Modal window-selection rule over the
configured grid:

```text
h = 7..20
n in {16,32,64,128,256,1024}
q_exp in {2,3}
```

The window rule starts at `W=2h` and then increases `W` while

```text
C(W-1,h-1) + C(W,h) <= 6,000,000.
```

The complete under-ceiling cells are exactly the six cells handled by
`m720_wsl_complete_zero_subcertificates`. The verifier also detects the edge
case where the initializer already has `W=n` but its cost exceeds the ceiling:
this happens exactly at `n=32,h=16`, for both q-exponents. Every other residual
cell has `W<n` and is therefore a window slice.

Thus the residual cell set is fully classified into slices plus the two
over-ceiling complete-window obligations.
