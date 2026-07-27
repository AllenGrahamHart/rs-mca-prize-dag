# L1 Mersenne HNF order-zero quadratic collision router

- **status:** PROVED
- **closure:** proof
- **dependency:** `l1_mersenne_next_to_maximal_hypergeometric_normal_form`
- **consumer:** `l1_mixed_petal_amplification`

Retain an official next-to-maximal order-zero row

```text
n=m(p+1),       (m,h) in {(8,7),(16,15)},
P_s(W)=sum_(r=0)^h binom(s+r-1,r)W^(h-r),
P_s | W^n-1,    s notin F_p.                         (QCR1)
```

Let `E_s` be the degree-less-than-`h` interpolant

```text
E_s(a)=a^(p+1)       for every root a of P_s.         (QCR2)
```

Suppose `deg E_s=2`, and call a color repeated when two roots of `P_s` have
that value under `E_s`. Then:

1. if at least two distinct colors are repeated, the quadratic collision
   center is zero, so every repeated fiber is an antipodal pair `{a,-a}`;
2. on each of the four `m=8,h=7` rows, at most one color is repeated.

Equivalently, every `m=8,h=7` quadratic survivor takes at least six distinct
colors on its seven roots. On the `m=16,h=15` row, any quadratic survivor
with at least two repeated colors must have the even form

```text
E_s(W)=A W^2+C.                                      (QCR3)
```

The theorem does not exclude a quadratic interpolant, the collision-free or
single-collision branches, the even multi-collision `m=16` branch, higher
color degrees, the order-one chamber, or any inner lift.
