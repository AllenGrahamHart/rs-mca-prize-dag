# Attack surface

## Route 1: strip-free raw aggregate

Let `N_h^raw` count every F-4-minimal, non-full-fiber x83 norm-gate record in
the same record convention, before applying any of the five deletion strips.
Deletion is monotone, so

```text
N_h^strip <= N_h^raw.
```

Consequently the stronger theorem

```text
sum_(h=4)^H_max N_h^raw <= 14n^3              (RAW-NG)
```

implies NG-COUNT. This is the preferred interface because it is independent of
the two currently non-operational U2 and DLI/skew strip definitions.

## Route 2: width cap

Prove that no raw primitive norm-gate record exists above an explicit
`H*(row)`, then sum exact per-width bounds. The first-moment vacancy curve
`H_vac=8..16` is evidence only. Do not claim zero: the model predicts
p-specific events below the vacancy threshold.

## Route 3: norm-divisor aggregate

The x83 keys are cyclotomic integers. A p-specific event forces the row prime
to divide at least one nonzero cleared norm. A viable proof must aggregate
this divisibility over supports or torsion components; the existing
per-support norm bound is too weak by itself.

## Route 4: primitive shift-pair orbit aggregate

The proved `f3_hge4_primitive_shift_pair_aggregate_adapter` identifies the
relevant record currency with a subset of the ordered primitive top
shift-pair ledger. With

```text
B_h=binom(n,h)(binom(n,h)-1)/p^(h-1),
```

it is enough to prove, uniformly in the complete width band,

```text
SP_h^prim<=7000n max(1,B_h).
```

The adapter sums this directly below `14n^3` at every official row. The proved
scaling-orbit router sharpens the finite target further. If `O_h^prim` is the
number of scaling orbits of ordered primitive top shift pairs, then

```text
SP_h^prim=n O_h^prim,
sum_(h=4)^H_max O_h^prim<=14n^2
```

is sufficient. This quadratic orbit aggregate is now the preferred finite
route. The per-width `7000` estimate is a stronger analytic route useful for
comparison with second-moment flatness.

The same router proves that a naive Q maximum-fiber argument followed by a
uniform local-degree sum can meet the per-width tolerance only by proving
primitive emptiness. A nonzero route must exploit average falling-factorial
mass, scaling orbits, or sparse active supports. Do not route HGE4 through an
unqualified max-fiber Q theorem.

The proved near-square union router is the preferred exact generator front
end. Enumerate an anchored `2h`-support once, recover the unique centered
square candidate from its locator, and test whether the remainder is a
nonzero scalar square. This removes the `binom(2h-1,h-1)` choices of an
`h|h` partition exactly. Preserve the free-union versus antipodal-swap
stabilizer flag; otherwise the ordered-orbit count can be wrong by a factor
of two.

The proved swap odd-moment router removes that branch entirely at even `h`.
At odd `h`, enumerate selected antipodal pairs, fix one sign modulo global
sign, and solve

```text
sum_i epsilon_i r_i^(2m+1)=0,       0<=m<=(h-3)/2.
```

An anchored swap scan has at most `binom(n/2-1,h-1)` candidate unions. Keep
this branch separate from free unions: the parity theorem gives no discount
for the free class, and the displayed candidate count is not itself an HGE4
bound.

For implementation, use the stronger proved half-order square descent. If
`Y subset mu_(n/2)` is the selected set of antipodal pairs and
`c_Y=prod(Y)`, retain it exactly when

```text
(L_Y+c_Y)/Z
```

is a monic polynomial square and `Y` has trivial scaling stabilizer. This
reconstructs the signs uniquely up to exchanging the two sides, so a sign
enumeration is now a conformance oracle only, not an acceptable production
generator.

For a theorem attack, the same objects are exactly the divisors
`ZT(Z)^2-c` of `Z^(n/2)-1` with trivial root-set stabilizer. This is a useful
classification interface. Do not turn it into a `p^((h-1)/2)` coefficient
scan without a further proved compression and a measured cost bound.

For fixed-cell characteristic sieving, use the proved straight-line lift:
repeatedly square `Y` modulo `YT^2-c` and impose terminal remainder one. The
pruned system is cubic and avoids expanding `Y^N mod (YT^2-c)`. Its
characteristic-zero unit-ideal property makes a checked integer
Nullstellensatz identity a complete bad-characteristic endpoint for that
cell. A Groebner run without an identity checker, factor plan, resource
ceiling, and cross-cell purpose is not a proof route.

The odd swap system sits exactly at the sharp Newton boundary
`h=2*((h-1)/2)+1`; the existing `w<=2ell` exclusion misses it by one.
Therefore any emptiness argument must use dyadic root order, the official
field-size condition, primitivity, or the divisor scheme, rather than only
repeating the odd-moment induction.

For the free class, use the proved non-full near-square selector. Present
`D=S^2-a^2 | X^n-1` by repeated squaring and impose that some intermediate
coefficient `s_1,...,s_(h-1)` of `S` is nonzero, either with one global
selector equation or one of `h-1` inverse charts. The characteristic-zero
full fibers have all these coefficients zero, so every chart is a unit ideal
over `Q`. This is now the preferred fixed-cell certificate interface for the
whole non-full residue. Selector variables are existential coverage
witnesses and must not be included in any trade count.

The target counts records, not raw support pairs or moments. Every proposed
bound must include the exact pairs-to-records and anchoring convention.

The proved cyclotomic-norm quarter-width theorem supersedes the earlier
`floor(2m/7)` cap. Any exact-level generator, certificate family, or aggregate
argument must stop at

```text
h=m/4-1.
```

Do not allocate support or elimination shards at `h>=m/4`. The Kummer
midpoint, trace-power, and trace-gcd packets remain independent conformance
fixtures, but their entire near-third strip is now empty on the official
consumer scope. The live theorem attack is only the lower-quarter range

```text
4<=h<=m/4-1,       e=m-3h>=h+4.
```

Within that range, write `h=m/4-d`, put `R=log m`,
`x=4(d+1)R/m`, and define

```text
Y_3=4((d+1)R-d)-8(d+1)^2R^2/m
       +(32/3)(d+1)^3R^3/m^2.
```

Whenever

```text
x<=1,       Y_3<=floor((h-1)/2)+2,
```

apply the Vandermonde-defect exclusion before any generator and skip the cell
entirely at both parities. At `m=2^41` this full deletion applies to
`1<=d<=2,677,220,820`. The former linear Vandermonde condition and the
cyclotomic-Haar exact band are proved sub-bands. The Haar theorem supplies
the strict defect lemma used by this stronger router; it is no longer the
production cutoff.

Outside that overlap, let `s=log_2(m)`. Whenever

```text
s(d+1)<=m/2,
```

allocate only the free-class generator: the swap class is empty. At
`m=2^41` this free-only zone continues through `d=26,817,356,774`. Only
below that cutoff may a production campaign allocate both free and swap
shards.

In particular, a raw binary-necklace scan, extension-field midpoint branch,
or trace-to-pencil campaign no longer targets a live HGE4 width. The preferred
routes are a direct lower-quarter free/swap orbit aggregate, a uniform
prime-factor payment for the fixed-cell certificates, or another theorem
that deletes or amortizes this remaining range.
