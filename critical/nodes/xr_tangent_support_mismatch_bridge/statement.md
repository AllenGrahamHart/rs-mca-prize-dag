# XR support-wise tangent/mismatch scope bridge

- **status:** PROVED
- **scope:** the six `(RowC, prize) x (1/4,1/8,1/16)` candidates
- **consumer:** `xr_smallcore_spread_count`

Fix a received pair and the existing quotient-first convention. There is an
exhaustive dichotomy.

## Generic branch

If no codeword pair jointly explains `(u,v)` on an `A`-support, select one
exact-`A` support-wise bad ray per live slope. The proved strip/classification
rung leaves selected agreement supports with pairwise intersections at most
`K`. They split disjointly into

```text
Gamma_hi={z: some z'!=z has |S_z intersect S_z'|=K},
Gamma_lo=Gamma\Gamma_hi.
```

Thus `Gamma_hi` is P-A1 and every member of `Gamma_lo` intersects every other
selected support in at most `K-1`, which is P-B. Assuming the two printed
`8n^3` bounds gives `16n^3` for this branch.

## Nongeneric branch

If a joint explanation `(c_0,c_1)` exists, write

```text
u=c_0+e_0,       v=c_1+e_1,
q_z=p_z-(c_0+z c_1)
```

for each selected bad ray. The branch `q_z=0` is genuinely tangent to the
recovered codeword line and is paid by
`xr_true_tangent_coordinate_injection`. Every `q_z!=0` support mismatch
remains live. Global joint proximity on another support is not a payment.

For each retained slope, select one exact-`A` witness/codeword by a fixed
first-match order and put

```text
E_z=supp(u+zv-p_z),       S_z=D\E_z.
```

Support-wise nontriviality on `S_z` is equivalent to

```text
{Hu,Hv} is not contained in H(F^E_z).
```

The full retained mismatch population routes to P-A2, whose obligation is
one combined `16n^3` bound. No separate `8n^3` high/low allocation is imposed
on this branch.

Therefore P-A1, P-A2, and P-B imply the exact post-strip `16n^3` bound for
every received pair. This bridge proves the dichotomy, support-wise tangent
ownership, and routing only; it proves none of those numerical clauses.

The canonical full-external-zero descent remains the principal alternative
attack on P-A2. Its depth, terminal breadth, and low-rank parts are proved.
