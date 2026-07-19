# `A=1` core-one trace-free weld exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_trace_free_allocation_rigidity`

On the official core-one maximal-degree sharp cap, the trace-free branch of
the nonzero weld is impossible.

First, if `D_*=1`, the exceptional factor cannot have the `Z_W=E_Z`
allocation. Indeed, the reduced first complement would be

```text
Q V_1+P_X W_1=P_cl,                                  (TFE1)
```

while `R_0=gcd(Q(gamma_0;X),P_X)` has degree at least `e+3b>0`. Evaluating
`(TFE1)` at a common root and at `gamma_0` gives
`0=P_cl(gamma_0)!=0`.

Thus `Z_B=E_Z` when `D_*=1`; for `D_*=0`, both exceptional factors are one.
In either case the reduced complement square contains

```text
Q A_1+P B_1=P_X.                                     (TFE2)
```

At every supported slope `gamma`, equation `(TFE2)` makes `Q_gamma` divide
`P_X`. Consequently a root `x` of `B_X` cannot be a supported parameter root
of `Q(U,V;x)`. Every nonsaturated row therefore has

```text
v_x=0,       delta_x=e_*,       C_*=c e_*.            (TFE3)
```

But

```text
C_*=e-5b-1+D_*<=e-b=e_*,                              (TFE4)
```

with equality only when `b=0,D_*=1`. Since `c>=1`, equations
`(TFE3)--(TFE4)` force

```text
b=0,       D_*=1,       c=1.                          (TFE5)
```

In that sole numerical profile, allocation rigidity proves that the
exceptional fiber `q_0=Q(gamma_0;X)` is squarefree of degree `r-1`. Specialize
`(TFE2)` at `gamma_0`:

```text
q_0 A_1(gamma_0;X)=P_X.                               (TFE6)
```

Since `deg P_X=D_0-1`, equation `(TFE6)` requires

```text
deg_X A_1(gamma_0;X)=D_0-r.                           (TFE7)
```

On the other hand `B_X|A`, `deg B_X=1`, and the original complement has
`deg_X A=D_0-r`, so globally

```text
deg_X A_1<=D_0-r-1,                                   (TFE8)
```

a contradiction. Hence every official profile has at least one active
defect trace of `K`. The active-trace branch remains open; this theorem does
not close `rate_half_band_closure`.
