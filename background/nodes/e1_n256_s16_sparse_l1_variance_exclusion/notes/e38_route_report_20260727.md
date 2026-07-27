# E=38 route report

Date: 2026-07-27.

## Certified starting point

The exact relaxed slack recurrence gives `L<=22` at `E=38` (`V=76`).
There are 32 compatible integer magnitude profiles. The largest abstract
nested-layer cap is

```text
M_3<=3012,
```

attained only by `(n_1,...,n_6)=(6,8,0,0,0,0)`. The best continuous
two-contact cubic Hermite majorant has contacts approximately
`(14.1671023,57.4645043)` and misses the six-bit target by approximately
`0.0025927093`. Thus the earlier integer-contact miss was not a grid artifact.

The same finite-interval quartic dual also collapses to a cubic. This remains
true after adding the elementary exact bounds

```text
-16<=x<=44,       -16V<=M_3<=3012,
M_4>=V^2,         M_4<=28M_3+704V.
```

No claim is made that every quartic or higher-moment route fails.

## Exact additive target

For the worst magnitude profile write the absolute full autocorrelation as
`b=1_A+1_B`, where `A=-A`, `B=-B`, `0,64` lie in neither set,
`|A|=28`, and `|B|=16`. The abstract third-moment cap is the weighted Schur
count

```text
T(A,B)=(b*b*b)(0)
      =R(A,A,A)+3R(A,A,B)+3R(A,B,B)+R(B,B,B).
```

The already certified rational Hermite cubic with contacts `(14,57)` closes
`V=76` as soon as

```text
T(A,B)<=2806.                                        (E38-Schur)
```

Exact substitution has positive margin at 2806 and negative margin at 2807.
The continuously optimized contacts at the original cap 3012 provide a
slightly smaller miss, but are not needed in the proposed proof.

A complete census inside the order-32 subgroup `4 Z/128 Z` gives maximum
2718, with component counts

```text
(R_AAA,R_AAB,R_ABB,R_BBB)=(678,390,234,168).
```

The maximizing displayed layers are

```text
A/+-={8,12,16,20,24,28,32,36,40,44,48,52,56,60},
B/+-={8,16,24,32,36,44,52,60}.
```

The separate proved node
`e1_n256_s16_autocorrelation_subfield_exclusion` removes every `V=76`
candidate whose nonzero autocorrelation support lies in `4 Z/128 Z`, by
placing `F(zeta)conjugate(F(zeta))` in `Q(zeta_64)` and bounding its
small-field norm by `60^32<2^250`. Thus the displayed extremizer is no
longer part of the live route. The weighted inequality remains unproved for
nonperiodic layers.

## Exact quotient closure

The nonperiodic branch is now closed by a two-stage mod-16 quotient bound.
For symmetric zero-free nested layers `X,Y,Z`, write `x_r,y_r,z_r` for
fiber sizes modulo 16. For each target residue `r`, the exact zero-pair
subtraction and the per-target representation capacity give

```text
R(X,Y,Z) <= sum_r min(
    sum_s x_s y_(-r-s) - 1_(r=0) min(|X|,|Y|),
    z_r sum_s min(x_s,y_(-r-s))
).
```

Taking the minimum over the three choices of target layer preserves an upper
bound. A complete 80-shard census checked 43,153,083 admissible layer
allocations and obtained

```text
profile       group Z/128 Z       divided group Z/64 Z
(6,8)              2782                    2760
(2,9)              2580                    2422
|outer|=30          R(A,A,A)<=840           R(A,A,A)<=840.
```

The third exceptional profile `(9,5,1)` has abstract cap 2828. Removing its
870-point outer term and its impossible two-point top-layer triple leaves
1956, so its quotient cap is `840+1956=2796`. Every other magnitude profile
has abstract cap at most 2668.

If the outer support contains an odd distance, the order-128 column applies.
If it lies in `2 Z/128 Z` but not `4 Z/128 Z`, division by two preserves the
Schur count and the order-64 column applies. The proved autocorrelation-
subfield node excludes support in `4 Z/128 Z`. Thus every live candidate has

```text
M_3<=2796<2806.
```

The pinned packet, source, and independent checker are
`e38_mod16_quotient_census_result.json`,
`e38_mod16_quotient_census.cpp`, and
`e38_mod16_quotient_census_check.py`. Final Modal run
`ap-n57PHWIhpfTIODFu1x2CMu` produced the complete transcript. The proved node
`e1_n256_s16_e38_quotient_schur_exclusion` therefore excludes `V=76` and
moves the residual to positive even `V<=74`.

## Falsification and solver record

Run `ap-bDo6kFt30u0J0bzjgZQYcZ` tested a direct integer-product CP-SAT
formulation. It found objective 2496 but left the useless upper bound 21822;
that formulation is fenced off.

Run `ap-eCqesJqxkTyu6IjhX8ExqM` used a stronger pure pseudo-Boolean threshold
encoding, sharded by the minimum 2-adic valuation of a weight-two residue.
The substantive shards `0,1,2` timed out without a witness at the stronger
threshold 2804; shards
`3,4,5` are trivially infeasible because fewer than eight representatives
remain. These are resistance data only, not a completeness certificate.

Run `ap-81TfPfdv09oDwETD5F9PQR` searched actual seven-term vectors in eight
parallel workers. Across 9,348 exact visits to `E=38,L=22`, the largest
sampled signed third moment was 816. This large gap from 2806 supports using
the chord-origin constraints rather than spending further on generic SAT.

A mod-8 residue-capacity relaxation reached 2958. The first mod-16 CP-SAT
formulation found 2866 in the non-`4Z` chamber but retained upper bound 3152;
run `ap-w0BCehAMjrwWVEI80ATZvz` found 2782 after requiring odd support, with
the same weak solver bound. These incomplete runs motivated, but do not
support, the deterministic census above.

Run `ap-4E8RkbLTDjcmSeJq2sTI7y` exhaustively checked the one-odd reflected
family. It found 119,040 mixed-parity vectors with vanishing odd
autocorrelations, including the exact witness

```text
{0:-2,1:2,2:2,4:-1,6:-1,124:-1,126:-1},
```

so the unrestricted claim "vanishing odd autocorrelation forces parity-pure
support" is false. None of that reflected family has `E=38,L=22`. This is a
route fence only; the final quotient proof does not use it.

## Slack equality reduction

Exact local enumeration of equality in the relaxed recurrence gives only 24
signatures at `E=38,L=22`. Every signature has zero unit diameters, between
zero and three magnitude-two diameters, and at most four positive-slack
non-diameter classes. The only positive class types `(delta,r,t,S)` are

```text
(4,1,1,1), (8,2,0,0), (8,2,1,1), (8,3,0,2),
(12,3,1,1), (16,4,0,0), (16,4,1,1), (16,5,0,2).
```

Because the relaxed minimum equals the actual target energy, every omitted
nonnegative charge must vanish: zero-slack magnitude-four classes must have
sum zero, zero-slack unit classes have absolute sum one, and zero-slack
magnitude-two classes have absolute sum two. This is the finite entry point
for a support-specific proof.

## Closed route and next task

The weighted cyclic inequality is proved with the stronger global live-row
cap `M_3<=2796`. Do not continue the E=38 SAT, parity, or slack-signature
searches. The next endpoint is `V=74` (`E=37`): recompute its exact `L`
ceiling and magnitude profiles, then decide whether the same quotient-Schur
mechanism has sufficient cubic margin before launching any new census.
