# Proof

Let `O` be the symmetric set of the six non-diameter light-light difference
classes. The E30 reduction proves that these classes are distinct. In profile
`(4,2,2)`, four positive classes have magnitude one, two have magnitude two,
and two have magnitude three. Hence the odd classes are exactly the four
magnitude-one and two magnitude-three classes, so they are exactly `O`.

For each odd mask choose the two classes `P` promoted from magnitude one to
three and the two classes `E`, outside `O`, having magnitude two. On the full
cyclic group the absolute autocorrelation is therefore

```text
b = 1_O + 2*1_(P union E).                            (1)
```

Translation and odd-unit multiplication preserve `M_3=(b*b*b)(0)`. Complete
enumeration of the 280,720 normalized six-odd light supports gives 1,234
distinct odd masks modulo odd units. For each mask there are
`binom(6,2)*binom(57,2)` choices in (1), for 29,541,960 assignments.

The production engine expands the cyclic trilinear form around `1_O+2*1_P`.
The audit engine independently enumerates the light supports in positive-gap
coordinates and evaluates the expansion through a precomputed signed-triple
kernel. Their four shards agree row by row. Only three assignments have
`M_3>1087`; all have `M_3=1146`, and they are the primitive assignment in the
statement and its two dyadic dilates. Every other assignment has
`M_3<=1087`, so the proved cubic-Hermite criterion puts its norm below
`2^250`.

Each exceptional odd mask has exactly one affine light-support orbit. The
folded-chord engine and an independent direct-negacyclic engine choose all
three heavy positions from the other 124 positions and all 64 relative sign
vectors. Each therefore tests

```text
3*binom(124,3)*64 = 59,543,808
```

vectors. They agree on exactly two vectors in each orbit. The scale-two and
scale-four vectors have support gcd two and four, respectively, so the proved
proper-conductor theorem excludes them.

The two primitive vectors are

```text
F_1(x)=1+x+2x^2+2x^3-2x^4+x^6-x^8,
F_2(x)=1-x+2x^2-2x^3-2x^4+x^6-x^8=F_1(-x).
```

Thus their norms agree by the odd Galois automorphism `zeta -> -zeta`.
Independent FLINT and PARI resultants give the integer in the statement for
both vectors. Exact comparison gives `447*N_max<2^250`, so neither can vanish
modulo a pair-feasible row prime. These cases exhaust profile `(4,2,2)`.
QED.
