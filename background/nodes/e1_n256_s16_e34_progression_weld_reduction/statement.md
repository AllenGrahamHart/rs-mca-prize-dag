# E1 N=256 E=34 progression-weld reduction

- **status:** PROVED
- **closure:** proof

Every residual progression template can be normalized to

```text
H={0,t,2t},          1 <= t <= 63,          t != 32.
```

The two outer heavy coefficients are opposite. After fixing global sign,

```text
(c_0,c_2t)=(2,-2),          c_t in {-2,2}.
```

Define the four residues modulo 128

```text
W_t={-2t,3t,-t,4t}.
```

They are distinct and nonheavy. The singleton outer-heavy chord class is
welded to a heavy-light chord exactly when `L intersect W_t` is nonempty.
Consequently each normal form has exactly

```text
binom(125,4)-binom(121,4)=1,195,965
```

necessary-condition light supports. The complete normalized enumeration
chamber contains

```text
62 * 1,195,965 * 2 * 16 = 2,372,794,560
```

signed vectors.

For every odd `u`, the cyclotomic automorphism `X -> X^u` preserves the
coefficient-magnitude profile, conductor, autocorrelation-magnitude profile,
and `M_3`. Its action collapses the 62 forms to five exact orbits:

```text
representative t          1    2    4    8   16
number of forms          32   16    8    4    2.
```

Thus a complete invariant census needs only the five representatives, or

```text
5 * 1,195,965 * 2 * 16 = 191,354,400
```

signed vectors.

This theorem does not exclude the progression template or assert that every
counted vector has `E=34`, profile `(6,7)`, full conductor, or pair-feasible
norm.
