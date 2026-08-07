# pma_petal_pattern_root_pinning_ledger

- **status:** PROVED
- **role:** field-independent aggregate petal-pattern ledger
- **consumer:** `petal_mixed_amplification`, hence `imgfib`

## Statement

Fix one maximal sunflower source with core `C`, `|C|=k-1`, pairwise disjoint
petals `T_1,...,T_M` of size `ell`, distinct labels `c_i`, and background of
size `b<ell`. Consider its non-planted listed codewords at agreement at least
`k+ell-1`. For such a codeword let

```text
D = exact missed-core set,       d=|D|,
S_i = exact agreement set in T_i,
I = {i:S_i nonempty},            t=|I|,
Y = disjoint_union_(i in I) S_i, h=|Y|.
```

Then `h>d`. For fixed integers `(d,t,h)`, the number `N_(d,t,h)` of these
codewords is at most

```text
N_(d,t,h)
 <= binom(M,t) binom(t ell,h)
    binom(k-1,e),

e=max(0,2d+1-h).                                      (PRP1)
```

This count includes every possible background-agreement set without a
background binomial factor.

More precisely, after fixing the exact petal pattern `(I,(S_i))`, put

```text
w_Y=h-d-1.
```

The selected-support interpolation map has maximal rank

```text
rank T_(Y,d)=min(d,w_Y),
```

and the monic split missed-core locators in its kernel number at most

```text
binom(k-1,max(0,d-w_Y))=binom(k-1,e).                  (PRP2)
```

Each such locator determines at most one residual numerator and hence at
most one codeword with the fixed petal pattern. Background agreements are
then the roots of that determined numerator, so they create no further
choice.

Put

```text
u=t ell-h.
```

For every fixed integer `E>=0`, the aggregate class satisfying

```text
u+e<=E                                                   (PRP3)
```

is polynomial at the L1 lower cutoff. If

```text
ell>=C_0 n/log_2 n,
```

then it has size at most

```text
(E+1)n^(E+2) 2^M <= (E+1)n^(E+2+1/C_0).               (PRP4)
```

In particular, for full-petal patterns (`u=0`) this closes every layer with

```text
2d+1-t ell<=E.
```

For `t>=3`, this includes growing-defect intervals not covered by a bounded
`d-ell` theorem.

## Scope

The theorem is field-independent and does not assume a Q/MI/MA input. It does
not bound the complementary family `u+e->infinity`, classify it as a natural-
scale profile, or prove `petal_mixed_amplification`.
