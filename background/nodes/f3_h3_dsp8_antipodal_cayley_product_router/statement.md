# DSP8 antipodal Cayley-product router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_dsp8_primitive_shift_pair_adapter`,
  `f3_h3_antipodal_tail_distance_six_split`

Let `H` be a dyadic subgroup in odd characteristic and put

```text
C(h)=(1+h)/(1-h),       B=C(H\{1,-1}).               (ACP1)
```

Fix the canonical sign `a` of an antipodal target

```text
t=1-a^2,       t notin {0,1},                         (ACP2)
```

and define the ordered multiplicative-fiber count

```text
M_a=#{(alpha,beta) in B^2:alpha beta=C(a)}.           (ACP3)
```

Then the complete ordered shifted-product fiber satisfies the exact identity

```text
P(1-a^2)=2+M_a.                                       (ACP4)
```

The two omitted records are exactly the two orders of the antipodal pair
`{a,-a}`. In particular,

```text
P(1-a^2)>=25       iff       M_a>=23.                 (ACP5)
```

There is also an exact graph form for the antipodal DSP8 term. Let `V_a` be
the set of unordered factor pairs `{alpha,beta}` in `B` with product `C(a)`
whose inverse Cayley images, after multiplication by `a`, form a small
generic shifted-product representation. Join two distinct vertices in both
orders when their original three-coordinate signed supports are disjoint,
and write `E_a` for the number of ordered edges. Put

```text
L_a=#{z in H\{1}:1-(1-a^2)(1-z) in H\{1}}.           (ACP6)
```

If `A_H` contains one canonical sign from every pair `{a,-a}`, then

```text
K_25^A=sum_(a in A_H, M_a>=23) E_a L_a.              (ACP7)
```

Thus the expensive DSP8 class is exactly a quotient-line-weighted
multiplicative energy of the Cayley image `B`, restricted by the signed-
support graph. This router supplies no bound for `(ACP7)`. A marginal bound
for `M_a`, an unweighted multiplicative-energy estimate, or a cotangent
reciprocity identity that discards `L_a` does not prove DSP8.
