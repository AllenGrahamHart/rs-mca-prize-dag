# Official FPC5 prefixes paid by GRS support shortening

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

On the smallest official row `n=8192`, apply the exact `(PF6)` prefilter,
the GRS constant-weight shortening cap, and canonical first-layout
domination to every residual cell.

For rate `1/8`, the complete residual prefix

```text
M=29,30,31,32
```

contains `126` fixed defect cells in five `(M,t)` groups and has total global
cap

```text
G_8=195112047344632914122867933361797765038.           (OP1)
```

It is therefore paid whenever

```text
q >= 2^128 G_8.                                       (OP2)
```

The threshold in `(OP2)` has 256 bits and is strictly below `2^256`.

For rate `1/16`, the complete residual prefix

```text
M=57,58,...,67
```

contains `374` fixed defect cells in twelve `(M,t)` groups; `M=60` is empty.
Its total cap is

```text
G_16=2444555448501019158442942184801171570,            (OP3)
```

so the prefix is paid whenever

```text
q >= 2^128 G_16.                                      (OP4)
```

This threshold has 249 bits.

The same exact compiler returns caps above `floor((2^256-1)/2^128)` for

```text
rate 1/2:   M=5,
rate 1/4:   M=13,
rate 1/8:   M=33,
rate 1/16:  M=68.                                     (OP5)
```

Thus `(OP5)` is the sharp stopping frontier of this replay, not a claim that
those classes are large.

## Scope

This is a finite-row payment at `n=8192` on the printed upper field slices.
It neither pays lower field sizes nor transports the prefix to larger `n`.
It does not close the large-source target because all later source scales,
rate `1/4` from `M=13`, and rate half from `M=5` remain live.
