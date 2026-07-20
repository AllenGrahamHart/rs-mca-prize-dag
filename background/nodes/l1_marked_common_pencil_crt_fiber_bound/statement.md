# L1 marked common-pencil CRT fiber bound

- **status:** PROVED
- **role:** remove numerator multiplicity from the bounded-polarity
  common-pencil branch
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Work in one bounded-polarity L1 chart with `p<ell`. Suppose all `t` dense
petals belong to one constant-shift pencil and lie in strip `m`:

```text
m ell<d,       d+p<(m+1)ell.                         (CF1)
```

Fix the source chart, every exact support and mark, and the exact defect
locator `F`. For the selected dense petals write

```text
P-a_i=S_iV_i,
S=product_i S_i,       v=sum_i deg V_i<=p,
deg S=t ell-v.                                         (CF2)
```

The congruences

```text
S_i | W-c_iF                                           (CF3)
```

determine one residue class `W_0 mod S`, with `deg W_0<deg S`. Every
degree-at-most-`d` solution is uniquely

```text
W=W_0+SH,       deg H<=d-(t ell-v),                    (CF4)
```

where a negative upper bound means that at most the representative `W_0`
can occur.

The Forney survivor window makes this exhaustive:

1. If `t>=m+1`, then `deg S>d`, so there is at most one `W` for the fixed
   locator and marks.
2. If `t=m`, put `eta=d-m ell`. The exact list threshold gives

   ```text
   1<=eta<=p-1,
   d-deg S=eta+v<=2p-1.                               (CF5)
   ```

   Hence there are at most

   ```text
   q^(eta+v+1)<=q^(2p)                                (CF6)
   ```

   possible numerators.

For every fixed `P`, if `p<=P` and the generated field satisfies
`q=poly(n)`, the per-locator numerator multiplicity is polynomial in `n`,
uniformly in the strip index and `d`. Together with the canonical marked
reduction, each numerator reconstructs at most one listed codeword. Thus the
only non-polynomial common-pencil issue left on the bounded-`p` branch is the
number and first-match multiplicity of admissible squarefree defect locators
`F`, not a hidden numerator fiber.

## Scope

The theorem does not count defect locators, prove their split realizability,
or treat arbitrary petal locators. The polynomial exponent depends on the
fixed polarity bound `P`.
