# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Canonical matchings 7 and 8 are respectively

```text
(de,sigma_o ef), (de,bf),         (-de,sigma_c cf),
(de,sigma_o ef), (de,sigma_c cf), (-de,bf).
```

Let `F(x,y)=paired(x,y)`. Formal expansion proves that `F` is symmetric and
biquadratic. Put `q=de`, `m=df`, and `s=(d+f)^2`. For matching 7, two defining
equations are

```text
F(q,bf)=0,       F(-q,sigma_c cf)=0.
```

For matching 8, exchange `b` and `sigma_c c` in these two equations. In either
case write the resulting quadratic polynomials in `q` as

```text
Q_1(q,f)=u_2(f)q^2+u_1(f)q+u_0(f),
Q_2(q,f)=v_2(f)q^2+v_1(f)q+v_0(f).
```

Their exact quadratic resultant is

```text
J(f) = (u_2 v_0-u_0 v_2)^2
       -(u_2 v_1-u_1 v_2)(u_1 v_0-u_0 v_1).
```

It has degree at most eight in `f`. This formula uses no leading-coefficient
division, so every finite common `q` root forces `J(f)=0`, including
degree-drop branches.

The missing-record identity is the monic quartic

```text
M(f)=f^4+(2m-s)f^2+m^2=0.
```

Monic polynomial division reduces `J` modulo `M` to a polynomial `R` of
degree at most three without introducing an inverse guard. The division-free
4-by-4 Bezout determinant of `M` and `R` is a common-root eliminant; because
`M` is monic, no unguarded leading coefficient is lost. Its norm is computed
through the quadratic-over-cubic tower in the basis
`1,t,t^2,b,bt,bt^2`.

Every field root of the norm numerator and denominator, every inverse-guard
numerator and denominator, and the base-cubic leading coefficient is lifted
through the base cubic, the `b` quadratic, linear `c` recovery, product-rank
cofactors, and compact kernel. At each source point all roots of `M(f)` are
enumerated. For each such root the two quadratic `q` cuts are intersected by
an exact gcd and every field root is enumerated. An identically zero gcd is
recorded as unresolved, never discarded. Since `m` is guarded nonzero,

```text
d=m/f,       e=qf/m
```

reconstructs every target. The missing relation and both defining paired
equations are replayed directly before evaluating both remaining equations
`F(q,sigma_o ef)` for `sigma_o in {+-1}`.

Across 16 rows there are 152 candidate `r` values, 176 source points, 512
enumerated `f` rows, 64 reconstructed targets, and 128 final colored-pair
evaluations. Every final evaluation is nonzero. The witness, target-boundary,
free-gcd, and unresolved ledgers are empty. This proves all 32 computed raw
cases for matchings 7 and 8 empty.

The transposition of residual positions zero and one exchanges records that
are both exactly `de`. Formal matching enumeration maps 7 to 10 and 8 to 13.
Symmetry of `F` preserves every paired equation, while the missing relations
and target guards are unchanged. Hence the 32 computed exclusions transport
to all 32 cases for matchings 10 and 13. All 64 stated cases are empty. QED.
