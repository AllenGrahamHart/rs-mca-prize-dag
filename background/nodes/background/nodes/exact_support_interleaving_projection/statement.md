# Exact-support properties survive a controlled interleaving projection

- **status:** PROVED
- **consumer:** `petal_small_scale_staircase_census`

Let `C<=F^n` be linear, `q=|F|`, and fix agreement `a`; put `r=n-a<q`.
Let `P` be any collection of subsets of the coordinate set. Write `L_P` for
the worst ordinary list size after retaining only codewords whose **exact**
agreement support belongs to `P`, and write `L_(m,P)` for the analogous
common-support `m`-interleaved list.

If `L_P=0`, then `L_(m,P)=0`. If `L_P>=1` and

```text
D=(q-r)^2-L_P q>0,
```

then, for every `m>=1`,

```text
L_P <= L_(m,P)
    <= floor(L_P q(q-r-1)/((q-r)^2-L_P q)).       (ESP)
```

No closure or monotonicity assumption on `P` is needed. In particular `P`
may be the family of supports with trivial stabilizer.

