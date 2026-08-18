# Rank-eleven `2 x 5` factor-flag recursive router

- **status:** PROVED
- **row:** KoalaBear MCA, post-near affine error rank eleven
- **input:** the full-span rich-container terminal at `tau=1679`, `h=38384`

Assume the full correction space has a factor-flag presentation

```text
C'=span(PB),  dim P=2,  dim B=5,
```

and every promoted rich container `W_i` is contained in one rank-one slice
`g_iB`, with nonzero `g_i in P`. Define the residual subspace

```text
B_i={b in B:g_i b in W_i},
```

so `W_i=g_iB_i` and `dim B_i` is two or three.

Every unsafe line then has one of two exact outputs:

1. **common pencil base:** some anchor-good coordinate is a common zero of
   every polynomial in `P`, hence of every polynomial in `C'`; or
2. **deeper residual flag:** for some `B_i`, a proper subspace of `B_i^perp`
   contains at least `18166` labelled evaluation columns of `B` at common
   zeros of `B_i`. Equivalently, `B_i` extends strictly inside `B` to a
   subspace `B_i'` of dimension at least `dim(B_i)+1` whose every polynomial
   vanishes on those `18166` actual coordinates.

In particular, a primitive base-free `2 x 5` factor flag whose every residual
`B_i` is `18165`-transverse is paid. The exact charge at factor-root cutoff
`T=408` is

```text
fixed-g dimension-five classes       2763267104042675
residual dimension-two classes      11330947785633956
residual dimension-three classes    51071925374444624
----------------------------------------------------
nontransverse union                 65166140264121255
transverse envelope                209812758437679617
total                              274978898701800872
slack                                1829409594215.
```

The adjacent residual threshold `18166` is over budget by
`15983178478905`. An exact scan over every factor cutoff proves `18165` is
the largest payable residual transversality threshold, attained at
`T=408` and `T=411`; `T=408` has the larger slack.

## Nonclaim

This theorem does not prove that an arbitrary full-span survivor has a
`2 x 5` factor presentation, does not pay the common-base or deeper-flag
outputs, and is not the general base-field-normalized split-pencil census.
