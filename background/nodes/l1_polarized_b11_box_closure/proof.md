# Proof - L1 polarized B11 box closure

Fix `P,E` and a word in `(PB1)`. If `ell<=P`, every petal deficit is at most
`ell`, so the sum of the two smallest deficits satisfies

```text
G_2<=2ell<=2P.                                           (1)
```

Assume henceforth that `ell>P`. Call a touched petal dense when
`a_i>ell/2` and sparse otherwise. On a sparse petal
`min(a_i,ell-a_i)=a_i`; on a dense petal it equals `ell-a_i`.

The reserve reduction gives total petal agreement `h>=ell`. If every petal
were sparse, then

```text
h=sum_i a_i=p<=P<ell,
```

a contradiction. Hence at least one dense petal exists.

If at least two petals are dense, they are the two largest support classes.
Their deficits are therefore `v_(1),v_(2)`, and

```text
G_2=v_(1)+v_(2)<=p<=P.                                  (2)
```

It remains to treat exactly one dense petal. Let its size be `ell-v`, and let
`S` be the sum of all sparse support sizes. Then

```text
p=v+S.                                                   (3)
```

The list threshold gives

```text
(ell-v)+S+r >= ell+d,
r >= d+v-S.                                              (4)
```

The non-planted per-petal cap gives `d>=ell-v`. Since the unique dense petal
is the largest support class, `v_(1)=v`; equations (3) and (4) give

```text
G_R=(ell-r)+v
   <= ell-d+S
   <= v+S
    = p
   <= P.                                                 (5)
```

Equations (1), (2), and (5) prove `(PB2)`. Together with
`d<=ell+E`, every word is in the paid `J/A2/AR` union of
`pma_b11_first_match_router`, with fixed gate parameters

```text
E_d=E,       V_2=2P,       V_R=P.
```

That union is polynomial at the L1 lower cutoff. This proves `(PB1)`. Taking
the complement of `(PB1)` for arbitrary fixed `P,E` gives `(PB3)`.
