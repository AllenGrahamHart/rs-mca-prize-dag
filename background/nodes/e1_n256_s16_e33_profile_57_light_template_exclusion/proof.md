# Proof

By the profile/parity/diameter reduction, exactly one of the six light-light
chords is a diameter. Profile `(5,7)` has five odd autocorrelation
coefficients. Modulo two, these are exactly the classes occupied an odd number
of times by the five remaining unit chords. Hence those five chords occupy
five distinct non-diameter classes: the diameter-Sidon condition.

Translate the diameter to `{0,64}`. Enumerate the remaining pair `x,y`, reject
a second diameter, and retain exactly the supports whose five other distance
classes are distinct. This gives 7,200 normalized supports. An affine map
between two normalized supports must preserve the unique diameter, so after
normalization it has the form

```text
z -> u z + t,       u odd,       t in {0,64}.          (2)
```

Canonicalizing all 7,200 supports under (2) gives exactly 100 orbits. The
independent checker reconstructs both numbers without reading a census
packet.

For each orbit representative, choose the three heavy positions from the
remaining 124 positions. Global coefficient negation changes no chord
product, so fixing the first heavy sign positive leaves 64 sign patterns.
Odd-unit substitution and monomial translation preserve the autocorrelation
profile and `M_3`; any wrap signs are included among those 64 patterns. Thus
the exact representative coverage is

```text
100 * binom(124,3) * 64 = 1,984,793,600.               (3)
```

The production implementation accumulates the 21 unordered signed folded
chords. The audit implementation independently forms the ordered product
`F(X)F(X^-1)` in `Z[X]/(X^128+1)` and checks its anti-palindromic
coefficients. They agree template by template on all profile counts,
full-conductor counts, and maxima, yielding (1).

The conductor recorded by the census is

```text
gcd(256,{i-r:i in support}),
```

because the normalized support contains `r=0`. Odd units and translations
preserve this gcd. The unrestricted maximizer has positions

```text
(36,48,60,0,4,24,64)
```

and conductor four, so its `M_3=1758` is not live. The proved
proper-conductor collision exclusion removes every census vector with gcd
greater than one. The maximum over all remaining vectors is exactly 1416.

Finally, the exact cubic-Hermite certificate at `V=66` has strict positive
norm margin through `M_3=1732`. Since `1416<1732`, every full-conductor
candidate has collision norm below `2^250`, contradicting pair feasibility.
QED.
