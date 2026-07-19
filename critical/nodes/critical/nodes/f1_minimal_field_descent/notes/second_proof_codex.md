# proof: f1_minimal_field_descent

- **status:** PROVED
- **closure:** proof

Let `F = F_{p^N}`. Its subfields are exactly the fields `F_{p^d}` with `d | N`,
and this identifies the subfield lattice with the divisor lattice:

```text
F_{p^a} cap F_{p^b} = F_{p^gcd(a,b)},
F_{p^a} F_{p^b}    = F_{p^lcm(a,b)}.
```

In particular the subfields of `F` are closed under intersection and compositum.

Let `x = [a_0:...:a_m]` be the projective pencil datum over `F`, with the usual
common-scaling ambiguity. Define

```text
Stab(x) = { sigma in Gal(F/F_p) : sigma(x) = x as a projective point }.
```

Equivalently, after choosing any nonzero coordinate `a_j`, `sigma` fixes all
ratios `a_i/a_j`. This is a subgroup of the cyclic Frobenius group
`Gal(F/F_p)`. Let

```text
K_0 = F^{Stab(x)}.
```

The datum is defined over `K_0`, because its projective coordinate ratios are
fixed by `Stab(x)` and hence lie in the fixed field. Conversely, if `x` is
defined over an intermediate field `K'`, then every element of `Gal(F/K')` fixes
the same coordinate ratios, so

```text
Gal(F/K') <= Stab(x).
```

By the Galois correspondence this implies

```text
K_0 = F^{Stab(x)} <= F^{Gal(F/K')} = K'.
```

Thus `K_0` is contained in every field of definition of `x`, and is itself a
field of definition. It is therefore the unique minimal field of definition over
`F_p`; the feared composite ambiguity cannot occur in finite-field descent.

Now write `B = F_{p^b}`. The minimal field of definition containing the base
field is

```text
K = B K_0.
```

In divisor-lattice notation, if `K_0 = F_{p^d}`, then

```text
K = F_{p^lcm(b,d)}.
```

This is a subfield of `F`, contains `B`, and is contained in every field of
definition that contains `B`; hence it is the unique minimal such field. If
`B = F`, then the interval `[B,F]` is a singleton and the datum is already in the
base case. Otherwise `B < F`, and since `K` lies in `[B,F]`, exactly one of the
following holds:

```text
K = B,
B < K < F,
K = F.
```

This proves the claimed exhaustive case split.
