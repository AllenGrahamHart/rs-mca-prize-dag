# L1 marked constant-shift sub-two-ell exclusion

- **status:** PROVED
- **role:** first uniform marked-pencil stability theorem
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Let `K` be a field, let `P in K[X]` be monic of degree `ell`, and let
`a_1,...,a_t` be distinct elements of `K`, with `t>=3`. For each `i`, choose
a monic divisor

```text
V_i | P-a_i,       S_i=(P-a_i)/V_i,
```

and put

```text
J=product_i V_i,       v=deg J=sum_i deg V_i.
```

Suppose `F,W in K[X]` and `c_1,...,c_t in K` satisfy

```text
deg F=d,       deg W<=d,       gcd(F,W)=1,
S_i | W-c_iF                                      (MS1)
```

for every `i`. Then no such data exist in the marked strict strip

```text
ell<d,       d+v<2ell.                             (MS2)
```

Consequently, on the bounded-polarity L1 branch, any three dense marked
petals belonging to one common constant-shift pencil are impossible whenever
their total missing degree is `v`, `ell<d`, and `d+v<2ell`. In particular,
if their marks are charged to the polarized entropy `p`, the simpler pair

```text
ell<d,       d+p<2ell
```

is sufficient for exclusion.

## Scope

The theorem does not cover two dense petals, arbitrary petal locators, or the
boundary `d+v>=2ell`. It is an exclusion theorem in the first marked strip,
not the full uniform marked-pencil payment.

The proved `l1_marked_constant_shift_multistrip_exclusion` now extends this
rank argument to every strip; this node remains the sharp first-strip base
case and audit surface.
