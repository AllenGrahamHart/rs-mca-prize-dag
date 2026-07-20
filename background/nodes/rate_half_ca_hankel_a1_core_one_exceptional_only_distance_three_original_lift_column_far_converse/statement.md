# `A=1` core-one distance-three original-lift column-far converse

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_corrected_square_converse`

Retain the exact distance-three split design and let `s` be the stripped
fixed-core point. The original rate-half parameters are

```text
rho=r+1,       R=2rho=2r+2.                           (OLC1)
```

For arbitrary endpoint scalars `tau_0,tau_1`, lift each contracted moment
sequence by

```text
y_(ell,0)=tau_ell,
y_(ell,k+1)=s y_(ell,k)+h_(ell,k),       0<=k<=2r.   (OLC2)
```

Then the full locator

```text
(X-s)Q(z;X)                                           (OLC3)
```

annihilates the lifted syndrome at every slope. At every internal or
external supported slope it is a squarefree split degree-`rho` locator. At
the exceptional slope it is a split degree-`rho-1` locator and may be padded
by one domain point. Thus every one of the `4e+1` required slopes is close at
radius `rho` for every choice of `(tau_0,tau_1)`.

Every lifted endpoint pair is column-far:

```text
ker M_rho(y_0) intersect ker M_rho(y_1)
          contains no degree-rho split domain locator.               (OLC4)
```

Consequently, on the official profile `e>1`, existence of the exact
pair-Lagrange external split design would produce a genuine far-CA
counterexample, because

```text
4e+1>rho+1=2e+3.                                     (OLC5)
```

Conversely, every distance-three counterexample in the exceptional-only
profile has already been reduced to that design by the preceding proved
routers. Therefore exclusion of the official pair-Lagrange external split
design is exactly the remaining distance-three task. No endpoint-lift,
column-far, Hankel, complement, weld, or reciprocal qualification remains.

This theorem does not exclude the design or address the
quotient-distance-at-least-four branch.
