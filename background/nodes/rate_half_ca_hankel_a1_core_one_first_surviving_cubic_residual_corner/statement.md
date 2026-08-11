# `A=1` core-one first surviving cubic-residual corner

- **status:** PROVED
- **closure:** exact endpoint arithmetic and adjugate-pole divisor ledger
- **consumer:** `rate_half_band_crossing_location`

On the official row `m=2^37`, retain a core-one profile at the first degree
not excluded by carrier descent:

```text
rho=4m,       e=floor(16m/13)=169155635042,
d=rho-1,      Delta=d-2e=211444543803.                (CRC1)
```

Every possible failure is forced into the single slope corner

```text
ell=126866726279,       T=rho+2=549755813890.          (CRC2)
```

If `p` is the pole-scheme length, `O` the root-omission count, and
`c_gamma` the residual rank losses, then

```text
Delta-3<=p<=O<=sum_gamma c_gamma<=Delta.              (CRC3)
```

Hence every gap in this chain and their total are at most three. For the
general middle-Hankel factorization

```text
adj M=D q q^T,       deg D=Delta,
```

the pushed-forward pole divisor consumes all but at most a cubic factor:

```text
D=P_p E_3,       deg E_3<=3.                          (CRC4)
```

At least

```text
T-Delta=2e+3=338311270087                             (CRC5)
```

supported slopes are clean, squarefree, and completely split over the
residual domain.

## Scope

This is an exact corner reduction, not an exclusion. Higher core-one degrees
and the core-free branch remain open.
