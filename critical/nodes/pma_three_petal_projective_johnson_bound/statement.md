# PMA three-petal projective Johnson bound

- **status:** PROVED
- **role:** aggregate split-core-divisor count for three-petal mu-basis modules
- **consumer:** `petal_mixed_amplification`, hence `imgfib`

## Statement

Use the notation of `pma_three_petal_mu_basis_reduction`. Let `C` be the
source core, `N=|C|=k-1`, and suppose the three petal locators have no root in
`C`. In the upper mu-basis branch, write

```text
F=uF_p+vF_q,
deg u<=r_u,       deg v<=r_v,
r_u+r_v=e-1,
e=2d+1-3ell>=1.                                  (PJ1)
```

Consider projective primitive pairs `[u:v]`, meaning `gcd(u,v)=1` modulo a
common nonzero scalar, for which `F` is a monic degree-`d` polynomial with
`d` distinct roots `D(u,v) subset C`.

### 1. Root-set intersection

For distinct projective primitive pairs,

```text
|D(u_1,v_1) intersect D(u_2,v_2)|<=e-1.          (PJ2)
```

### 2. Projective Johnson count

Let `L` be the number of such pairs in one fixed touched-petal module. If

```text
J=d^2-N(e-1)>0,                                   (PJ3)
```

then

```text
L <= N(d-e+1)/J.                                  (PJ4)
```

Since all quantities are integers, the right side may be rounded down.

### 3. Complete rate-quarter `M=4,t=3` payment

At rate `1/4`, `M=4`, every upper-branch three-petal cell satisfies (PJ3).
Indeed, with `N=k-1` and `e-1=2d-3ell`,

```text
J=(N-d)^2+N(3ell-N)>0.                            (PJ5)
```

The source equation `3k+1=4ell+b`, `b<ell`, gives `N<3ell`. Combining
(PJ4), the four touched triples, all defect degrees, and the one-projective
lower branch gives the uniform per-source bound

```text
#(rate-quarter M=4,t=3 contributors) <= 16n^3.    (PJ6)
```

Thus the entire rate-quarter `M=4,t=3` full-petal branch is paid.

### 4. Rate-half residual tail

At rate `1/2`, `M=4`, write

```text
N=4ell+b-2,       d=2ell-a,       a>=1.
```

Then

```text
J=ell(4a-b+2)+a^2+2ab-4a.                         (PJ7)
```

All `M=4,t=3` cells with `b<=6` satisfy `J>0` and are paid. Any cell not paid
by (PJ3) must lie in the explicit tail

```text
b>=7,
1<=a<=floor((b-3)/4),
J<=0.                                             (PJ8)
```

The theorem does not count the tail (PJ8), the two-petal branch, larger source
scales, or partial petals. It therefore narrows but does not promote
`petal_mixed_amplification`.
