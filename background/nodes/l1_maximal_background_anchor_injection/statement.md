# L1 maximal background-anchor injection

- **status:** PROVED
- **role:** jointly charge a fixed mixed-support layer to its largest petal or
  its exact background agreement
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`
- **upstream source:** `przchojecki/rs-mca@18cfc199`, Lemma B3 and
  Proposition B4 in
  `experimental/notes/l1/l1_full_list_quotient_proof_program.md`

## Fixed-pattern theorem

Work in a maximal sunflower chart. Its petals `T_i` have size `ell`, their
nonzero labels `c_i` are pairwise distinct, and the unused background `R`
satisfies `b=|R|<ell`. Fix an exact core defect `d`, exact background agreement
`R_0 subset R`, exact touched-petal set `I`, and nonempty exact supports
`S_i subset T_i` for `i in I`. Put

```text
r=|R_0|,       a_i=|S_i|,       h=sum_(i in I) a_i,
a_*=max_(i in I) a_i.                                  (BA1)
```

Among non-planted listed codewords in this fixed layer, the map to the
cofactor on any selected petal,

```text
A_i=(W-c_i F)/L_(S_i),       F=L_D,                    (BA2)
```

is injective. The map to the exact background quotient

```text
V=W/L_(R_0)                                           (BA3)
```

is also injective. Consequently the layer has size at most

```text
q^max(0,d-max(r,a_*)+1).                               (BA4)
```

The exponent in `(BA4)` is the minimum of the largest-petal cofactor
dimension and the background-quotient dimension. It strictly improves the
petal-only charge whenever `r>a_*`.

## Stratum ledger

At the L1 lower cutoff, fix integers

```text
E>=0,       t>=2,       u>=0,       r>=0.
```

The number of non-planted listed codewords satisfying

```text
d<=ell+E,
|R_P|=r,
#{i:S_i nonempty}=t,
sum_i (ell-|S_i|)=u
```

is at most

```text
binom(b,r) binom(M,t) binom(t ell,u) (ell+E+1) q^gamma, (BA5)

gamma=min(E+floor(u/t)+1, max(0,E+ell-r+1)).            (BA6)
```

As usual, impossible binomial choices contribute zero. Formula `(BA5)` is an
upper ledger: its support-pattern factor deliberately includes choices that
empty a touched petal.

## Scope

This theorem is per maximal source chart. It does not sum unbounded
`(t,u,r,E)` strata, establish a polynomial number of non-intrinsic charts, or
pay the aggregate first-owner cells. It does not promote either open mixed-
petal consumer.
