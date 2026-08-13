# Cycle 222: MCA near-Johnson Gram-rank payment (2026-08-13)

Cycle 221 stopped exactly when the ordinary Johnson denominator became
nonpositive.  The adjacent strip still has a strong rank-stability estimate.

For an ordinary list represented by equal-size agreement blocks with
`|S_i|=A` and pairwise intersections at most `c`, let `B` be the
incidence matrix and put

```text
H=BB^T-cJ.
```

Equal row sums imply that the all-ones vector already lies in `col(B)`.
Hence `rank(H)<=rank(B)<=n`, not merely `n+1`.  If

```text
g=nc-A^2>=0,
G=(A-c)^2-cg>0,
```

the trace-rank inequality, Cauchy incidence lower bound, and
`delta^2<=c delta` give the field-general cap

```text
L <= floor(n*A*(A-c)/G).
```

For the sparse-direction MCA family, split explanations at deficit
`u=floor(e/2)`.  The low-deficit class uses the ordinary Johnson cap
`J_u`; every other explanation owns one slope.  Therefore

```text
|Z| <= (e-1)J_u+Q_e.
```

Exact arithmetic expands the paid prefixes to

```text
KoalaBear:   e<=64037, endpoint bound 198047217;
Mersenne-31: e<=65418, endpoint bound  16759641.
```

At `e=64038`, the KoalaBear Gram denominator is `-36911`, so the theorem
stops.  At `e=65419`, the Mersenne denominator is still positive, but the
valid bound `18212004` exceeds budget `16777215`.

The primary checker scans all 311 newly paid supports and four mutations.
An independent rational implementation reconstructs the records and checks
the rank placement on an explicit finite block family.

```text
start:                   b3e4f267d
canonical prize:         c8d48cd4b (no newer Fable commit)
result:                  NARROWED; one PROVED field-general compiler
DAG delta:               +1 PROVED node, +3 edges
critical status delta:   none; replacement target remains TARGET
full-lift residuals:     KoalaBear 64038<=e<=1044238;
                         Mersenne 65419<=e<=1044241
delta-star movement:     none
compute:                 exact local integer arithmetic under RAMguard;
                         no Modal
next route action:       strengthen the post-Johnson list cap beyond the
                         first centered-Gram denominator or exploit
                         full-lift near-MDS extension structure
```
