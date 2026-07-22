# L1 Mersenne-checkpoint embedded two-fiber family

- **status:** PROVED
- **dependencies:** `l1_official_split_pencil_value_capacity`,
  `l1_mersenne_checkpoint_cyclotomic_normal_form`
- **consumer:** `l1_mixed_petal_amplification`

Let `N=p+1`, let `m in {4,8,16}`, put `n=mN`, and let `H` be a
multiplicative coset of order `n`. The unique subgroup of order `2N`
partitions `H` into `m/2` multiplicative cosets `H_j`, each of order
`2p+2`.

For every antipodal pair `{x,-x}` in `H_j`, put

```text
b=x^2,
C=Z^2-b,
R=Z C^((p-1)/2).                                     (EM2-1)
```

The exact two-fiber theorem supplies a nonzero `delta` such that

```text
F_-=R-delta,       F_+=R+delta                         (EM2-2)
```

are coprime monic degree-`p` locators split completely in `H_j`. They differ
by a nonzero constant, so they form a first-checkpoint split-pencil pair in
the full domain `H`.

Each `H_j` has exactly `N` antipodal complements. Different cosets and
different complements give different unordered fiber pairs. Therefore every
one of the nine Mersenne rows has the explicit family

```text
# embedded unordered pairs=(m/2)N=n/2.                (EM2-3)
```

Moreover `deg(R-Z^p)=p-2`, so these pairs occur at exactly the checkpoint
depths

```text
d=p, p+1.                                             (EM2-4)
```

The normalized inner polynomial `R` is odd. Its nonzero split values occur in
pairs `{beta,-beta}`, while zero is not a split value because `R=0` has only
the two distinct nonzero roots of `C` in the multiplicative domain. Hence the
total split-value degree of every embedded pencil is even. Since maximal
degree `h=m` is already impossible, the exact possibilities are

```text
m=4:       h=2,
m=8:       h in {2,4,6},
m=16:      h in {2,4,6,8,10,12,14}.                  (EM2-5)
```

This proves that the lower-`h` frontier is genuinely nonempty and gives a
polynomial explicit payload. It does not classify all `h=2` records, prove
that the displayed higher even values occur, exclude nonembedded `h>=3`,
treat other depths or higher widths, or close L1.
