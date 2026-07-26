# E1 clean-anchor exact collision allowance

- **status:** PROVED
- **closure:** proof plus exact arithmetic

At each of the six clean candidate predecessors, let `N` be the actual
2-power quotient order, `h=N/2` its folded dimension, and
`ell=rho N+1`. The characteristic-zero E1 class count is

```text
K=A_2(N,ell)
 = sum_{u>=0, t=ell-2u>=0, u<=h-t} binom(h,t) 2^t.
```

This is a count of antipodal-rearrangement classes, not raw subsets and not a
further quotient by global sign.

Reduce the class values `-e_1` into the actual ambient MCA slope field. If a
finite-field value has class-fiber size `r_y`, put

```text
L = number of distinct reduced values,
P = sum_y binom(r_y,2).
```

Then

```text
K-L = sum_y (r_y-1) <= P.
```

Consequently the exact sufficient condition for a direct-value `V` payload is

```text
P <= g_max := K-B*-1,
```

because it implies `L>=B*+1`. At the six clean anchors the exact data are:

| row | `N` | `h` | `ell` | `K` | `B*` | `g_max=K-B*-1` |
|---|---:|---:|---:|---:|---:|---:|
| RowC `1/4` | 256 | 128 | 65 | 1146852336572689151906730465296195854216377730651578907904 | 5316911983139663491615228241121378304 | 1146852336572689151901413553313056190724762502410457529599 |
| RowC `1/8` | 256 | 128 | 33 | 38001322036274275320505631960233903602944 | 5316911983139663491615228241121378304 | 37996005124291135657014016731992782224639 |
| RowC `1/16` | 512 | 256 | 33 | 3413962861332812601133559951042096138635313539480064 | 5316911983139663491615228241121378304 | 3413962861332807284221576811378604523407072418101759 |
| prize `1/4` | 256 | 128 | 65 | 1146852336572689151906730465296195854216377730651578907904 | 317494674775468773183020924238786383963 | 1146852336572689151589235790520727081033356806412792523940 |
| prize `1/8` | 256 | 128 | 33 | 38001322036274275320505631960233903602944 | 317494674775468773183020924238786383963 | 37683827361498806547322611035995117218980 |
| prize `1/16` | 512 | 256 | 33 | 3413962861332812601133559951042096138635313539480064 | 317494674775468773183020924238786383963 | 3413962861332495106458784482268913117711074753096100 |

Here `P` counts unordered collisions between distinct characteristic-zero
classes. The paid antipodal rearrangements of raw subsets have already been
collapsed in `K`. The theorem supplies the exact finite target but does not
bound `P` on any row.

There is also an exact generated-field gate. If `Q` is the quotient root set
and `B=F_p(Q)`, every E1 value lies in `B`, so `L<=|B|`. Therefore

```text
|B| <= B*
```

rules out a direct-E1 `V` payload. The pointwise E1 collision target is posed
on the complementary candidate class `|B|>B*`; the universal unsafe router
must pay the small-generated-field branch by another supplier.
