# F2 selector-face primitive reduction

- **status:** PROVED
- **closure:** proof

Let `K=F_q` have odd characteristic, let `theta` have order `2m`, with
`m` a power of two, and assume `char(K)>2R`. For

```text
A(x)_r = sum_(s=0)^(m-1) x_s theta^(s(2r-1)),  1<=r<=R,
F_v = {x in {0,1}^m : A(x)=v},
```

take a nonempty fiber `F_v`. Let `I_v` be the coordinates which are
constant on `F_v`, put `c=|I_v|`, and let `G_v` be the product of the
selector roots forced by those coordinates. If `c=m`, then `|F_v|=1`.
Otherwise division by `G_v` injects `F_v` into the aperiodic, gcd-trivial
part of one split-locator prefix fiber

```text
A_v intersect Dloc_(m-c)(mu_(2m) \ Z(G_v)).              (FACE-1)
```

Here `A_v` fixes the top `s=min(2R,m-c)` nonleading coefficients of a
monic degree-`m-c` polynomial and has codimension `s`. Every locator in the
embedded selector family is antipodal-free and hence aperiodic. No point of
the punctured domain is a common root of the embedded family, so the full
intersection in `(FACE-1)` is gcd-trivial whenever it is nonempty.

Consequently, suppose a primitive version of upstream
`prob:capfr1-master-flatness`, uniform under these punctures, gives

```text
|A_v intersect Dloc_j(D_v)_ap|
  <= P(|D_v|) * (1 + binom(|D_v|,j)/q^s).                (FACE-2)
```

Write `Delta=m-R log_2 q` and
`P_*(2m)=max_(u<=2m) P(u)`. Then every F2 fiber satisfies

```text
|F_v| <= max(1, P_*(2m) * (1 + 2^(2 max(Delta,0)))).     (FACE-3)
```

Thus polynomial primitive master flatness gives a polynomial F2 max-fiber
bound whenever `Delta=O(log m)`, and gives `2^o(m)` whenever
`log P_*(2m)+max(Delta,0)=o(m)`. By the proved max-fiber sandwich, the same
asymptotic bound pays the plus and coupled-minus weighted-mass terminals.

This is an exact common-divisor and normalization bridge. It does not prove
`(FACE-2)`, identify upstream's deployed pruned first-match `Q` atom, settle
PP5.0 accounting, or establish the finite `n^3` F2 budget.
