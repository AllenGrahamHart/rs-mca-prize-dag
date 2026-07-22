# L1 official checkpoint characteristic atlas

- **status:** PROVED
- **role:** exhaust the characteristic/domain pairs on which Frobenius
  checkpoints can occur
- **consumer:** `l1_mixed_petal_amplification`

Assume the official generated-field conditions

```text
n=2^s,       13<=s<=44,
n | p^f-1,   p^f<2^256,   p<n,   p>=3583.              (CAT1)
```

The condition `p<n` selects exactly the rows where a positive characteristic
checkpoint can occur below depth `n`. Then

```text
ord_n(p) in {1,2,4,8,16}.                               (CAT2)
```

For fixed `s`, every candidate residue is one of the 32 values

```text
+-5^(j 2^(s-6)) mod 2^s,       0<=j<16.                 (CAT3)
```

Filtering these finite candidates by primality, `p>=3583`, and
`p^ord_n(p)<2^256` gives exactly the 59 rows in `checkpoint_atlas.tsv`.
Writing `m=floor(n/p)`, their exact distribution is

| `m` | 1 | 2 | 3 | 4 | 5 | 7 | 8 | 16 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| rows | 33 | 10 | 4 | 4 | 2 | 1 | 4 | 1 |

Consequently:

```text
33 rows: m=1, so the t=p split-pair stratum is empty;
10 rows: m=2, so the complement-square compiler is exact;
16 rows: m>=3, so the higher-multiplicity Q/eliminant route remains. (CAT4)
```

Among the ten `m=2` rows, exactly four have the two-point complement
`n-2p=2`:

```text
(n,p)=(2^14,8191), (2^18,131071),
      (2^20,524287), (2^32,2147483647).                 (CAT5)
```

For each of these, the exact `m=2` classification gives precisely `n/2`
minimum-width pairs, indexed by antipodal complements. The other six `m=2`
rows have `n-2p>2`, so their `t=p` strata are empty. Consequently the atlas
routes the 59 pairs as

```text
39 theorem-empty at t=p, 4 explicit with n/2 pairs, 16 with m>=3 open.
                                                                    (CAT6)
```

No `m<=2` minimum-width computation remains.

This is an exhaustive arithmetic router, not a census of perturbations,
complements, or coarse fibers. Rows with `p>=n` are Newton-safe at every
depth and do not belong in a checkpoint atlas.
