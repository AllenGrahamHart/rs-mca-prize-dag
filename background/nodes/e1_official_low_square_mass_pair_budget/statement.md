# E1 official low-square-mass collision-pair budget

- **status:** TARGET
- **closure:** open
- **compiler:** `e1_low_square_mass_plotkin_coloring_compiler`
- **exact vector dictionary:** `e1_low_square_mass_weighted_kernel_dictionary`

For every pair-feasible prime-field row at the six named RowC/prize
envelopes, let `E_low` count unordered pairs of distinct
antipodal-rearrangement classes with equal reduced E1 value and square mass
`S<=2ell`. Prove the row-specific bounds:

| row | required `E_low` upper bound |
|---|---:|
| RowC `1/4` | 2132541774042092125849554674828524585055987163412031204420185928301781984965 |
| RowC `1/8` | 5198328219133082279450279571536097879858211 |
| RowC `1/16` | 34251385177613611176287134568778412711317979539714751534312745145 |
| prize `1/4` | 35712526268255974159379339912208386438781917770706964119574629107623252261 |
| prize `1/8` | 62622678770648913918718317914905517790930 |
| prize `1/16` | 573589463880641840437695913758879780711186889526196156445743653 |

By the proved second-moment compiler, each bound forces more than `B*`
distinct E1 values and supplies a direct `V` payload. The binding prize
rate-`1/8` budget is about `1.648K`; maximum low-mass collision degree three
is sufficient but not required.

Equivalently, the proved weighted-kernel dictionary rewrites the left side as

```text
E_low=(1/2) sum_{d in D_p(ell)} M_ell(a(d),b(d)).
```

On the binding prize rate-`1/8` row, the weaker uniform sufficient statement
is `|D_p(33)|<=66866`, with oriented, non-orbit-normalized vectors. The exact
weighted sum remains the actual target.

## Falsifier

An admissible row whose exact unordered low-mass collision-pair count exceeds
its table entry, or a purported proof that counts normalized coefficient
vectors without their class-pair multiplicities.
