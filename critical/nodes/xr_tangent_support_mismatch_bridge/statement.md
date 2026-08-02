# XR support-wise tangent/mismatch scope bridge

- **status:** PROVED
- **scope:** the six `(RowC, prize) x (1/4,1/8,1/16)` candidates
- **consumer:** `xr_smallcore_spread_count`

Fix a received pair and the existing quotient-first convention. There is an
exhaustive dichotomy.

## Generic branch

If no codeword pair jointly explains `(u,v)` on an `A`-support, select one
exact-`A` support-wise bad ray per live slope. [R2 + ROUTE T PARTITION OF
RECORD, ratified 2026-08-02 — supersedes the former `= K` split, which
rested on an unproved core cap; see `notes/FLAG_ADJUDICATION_20260802.md`.]
The selected supports split disjointly BY DEFINITION into three classes
(symbol pinned: `k`, the code dimension; core = pairwise support
intersection):

```text
Gamma_band={z: some z'!=z has |S_z intersect S_z'|>=k+1},
Gamma_hi ={z not in Gamma_band: some z'!=z has |S_z intersect S_z'|=k},
Gamma_lo =Gamma\(Gamma_band union Gamma_hi).
```

The partition is exhaustive and disjoint by construction, with no core-cap
premise. Participation in a `>=k+1` core is symmetric, so after removing
`Gamma_band` all remaining pairwise cores are at most `k`. `Gamma_band`
(band depths `[1,h-1]`, the depth-`h-1` cascade tier included and named) is
charged by the third generic column (`xr_graded_tangent_band_charge`,
`<=4n^3` from the `13n^3` headroom); `Gamma_hi` is P-A1 (its exact-`k`
form and machinery unchanged); `Gamma_lo` intersects every other selected
support in at most `k-1`, which is P-B. The strip rung supplies the FORCING
(cores `>=k+1` force a codeword pair on `>k` points) and, with genericity,
the core ceiling `A-1` — it does not remove the band. Assuming the two
printed `8n^3` bounds plus the band column gives `20n^3` for this branch,
inside the proved `29n^3` allowance.

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

Therefore P-A1, P-A2, P-B, and the band column imply the exact post-strip
residual bound for every received pair. This bridge proves the dichotomy,
support-wise tangent ownership, and routing only; it proves none of those
numerical clauses.

The canonical full-external-zero descent remains the principal alternative
attack on P-A2. Its depth, terminal breadth, and low-rank parts are proved.
