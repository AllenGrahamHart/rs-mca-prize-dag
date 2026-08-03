# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Canonical matchings 4 and 5 are respectively

```text
(de,-de), (de,bf),         (sigma_o ef,sigma_c cf),
(de,-de), (de,sigma_c cf), (sigma_o ef,bf).
```

Let `F(x,y)=paired(x,y)`. Formal expansion proves that `F` is symmetric and
biquadratic. Put `q=de`, `m=df`, and `s=(d+f)^2`. Both representatives impose
the even quartic

```text
P(q)=F(q,-q)=p_2 q^4+p_1 q^2+p_0=0.
```

Set `x=q^2`, so `P_x(x)=p_2 x^2+p_1 x+p_0`. The second matching-4 equation is
`F(q,bf)=0`; the second matching-5 equation is `F(q,sigma_c cf)=0`. In either
case write it as

```text
A(q,f)=a_2(f)q^2+a_1(f)q+a_0(f)=0.
```

Each `a_i` has degree at most two in `f`. Multiplying `A(q,f)` by
`A(-q,f)` eliminates the sign of `q` and gives the quadratic-in-`x` necessary
cut

```text
H(x,f)=(a_2 x+a_0)^2-a_1^2 x=0.
```

The exact quadratic resultant `J(f)=Res_x(P_x,H)` is

```text
J(f) = (p_2 h_0-p_0 h_2)^2
       -(p_2 h_1-p_1 h_2)(p_1 h_0-p_0 h_1),
```

where `H=h_2 x^2+h_1 x+h_0`. It has degree at most eight and uses no
leading-coefficient division, so degree-drop branches are retained.

The missing-record identity is the monic quartic

```text
M(f)=f^4+(2m-s)f^2+m^2=0.
```

Monic polynomial division reduces `J` modulo `M` to a polynomial `R` of
degree at most three without introducing an inverse guard. The division-free
4-by-4 Bezout determinant of `M` and `R` is a common-root eliminant. Its norm
is computed through the quadratic-over-cubic tower in the basis
`1,t,t^2,b,bt,bt^2`.

Every field root of the norm numerator and denominator, every inverse-guard
numerator and denominator, and the base-cubic leading coefficient is lifted
through the base cubic, the `b` quadratic, linear `c` recovery, product-rank
cofactors, and compact kernel. At each source point all roots of `M(f)` are
enumerated. For each such root the original cuts `F(q,-q)` and
`F(q,lambda f)` are intersected by an exact gcd and every field root is
enumerated. An identically zero gcd is recorded as unresolved, never
discarded. Since `m` is guarded nonzero, every target is reconstructed by

```text
d=m/f,       e=qf/m.
```

The missing relation and both defining paired equations are replayed
directly. Pairing 4 then checks all four equations
`F(sigma_o ef,sigma_c cf)`; pairing 5 checks both equations
`F(sigma_o ef,bf)` for its anchored `sigma_c`.

Across 12 rows there are 200 candidate `r` values, 296 source points, 928
enumerated `f` rows, 184 reconstructed targets, and 480 final colored-pair
evaluations. Every final evaluation is nonzero. The witness, target-boundary,
free-gcd, and unresolved ledgers are empty. This proves all 32 computed raw
cases for matchings 4 and 5 empty.

The transposition of residual positions zero and one exchanges records that
are both exactly `de`. Formal matching enumeration maps 4 to 9 and 5 to 12.
Symmetry of `F` preserves every paired equation, while the missing relations
and target guards are unchanged. Hence the 32 computed exclusions transport
to all 32 cases for matchings 9 and 12. All 64 stated cases are empty. QED.
