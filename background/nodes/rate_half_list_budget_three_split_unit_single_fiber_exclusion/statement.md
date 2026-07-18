# Budget-three split-unit single-fiber exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Let a nonzero constant relation among block locators have support `I`, and put

```text
c_i=d-deg A_i>0       for i in I.                   (SFE1)
```

Assume each supported block is one degree-`d` quotient fiber with exactly
`c_i` exceptional points removed: there are monic polynomials `R_i` with
pairwise-disjoint simple root sets such that

```text
deg R_i=c_i,       R_i A_i=X^d-tau_i.              (SFE2)
```

If

```text
C=sum_(i in I)c_i<=d,                               (SFE3)
```

then the polynomials `{A_i:i in I}` are linearly independent over the base
field. Consequently `(SFE2)` is impossible for every one of the nine
split-unit B*=3 chambers at official scale. Their relation-support deficit
ledgers are

| chamber | relation support | supported deficits | `C` |
|---|---|---|---:|
| 4-cycle | `0123` | `(1,1,1,1)` | 4 |
| linear `K_4-e` | `0123` | `(2,2,1,1)` | 6 |
| `K_4` | `0123` | `(2,2,2,2)` | 8 |
| path plus singleton | `013` | `(1,1,1)` | 3 |
| triangle plus singleton | `0123` | `(1,1,1,2)` | 5 |

Thus no split-unit chamber is obtained by assigning each related large block
to one `d`-point quotient fiber and moving only the at-most-eight exceptional
points. This excludes the most direct quotient-periodic construction; it does
not exclude primitive or multi-fiber block configurations.
