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

This proves that the lower-`h` frontier is genuinely nonempty and gives a
polynomial explicit payload. It does not classify all `h=2` records, prove
that one normalized pencil has only two split values, exclude `h>=3`, treat
other depths or higher widths, or close L1.
