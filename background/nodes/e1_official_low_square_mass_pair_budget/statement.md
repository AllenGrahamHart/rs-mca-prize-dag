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
| prize `1/4` | 36339061816821868442877223068562919534199144398263226647988219091967519844 |
| prize `1/8` | 65127585921474870475467050631501738502567 |
| prize `1/16` | 592092349812275448193750620654327515572838079510912161492380545 |

By the proved second-moment compiler, each bound forces more than `B*`
distinct E1 values and supplies a direct `V` payload. The binding prize
rate-`1/8` budget is about `1.714K`; maximum low-mass collision degree three
is sufficient but not required.

Equivalently, the proved weighted-kernel dictionary rewrites the left side as

```text
E_low=(1/2) sum_{d in D_p(ell)} M_ell(a(d),b(d)).
```

On the binding prize rate-`1/8` row, the weaker uniform sufficient statement
is `|D_p(33)|<=69541`, with oriented, non-orbit-normalized vectors. The exact
weighted sum remains the actual target.

For the current maximum-weight profile `(3,6,S=18)`, the proved pure-cofactor
associate router supplies an additional exact coupling. At one fixed prize
row and quotient root, every still-live collision has cofactor

```text
m in {2,4,8,16}
```

and, after division by the exact power of `1-zeta_256`, all such values are
unit associates generating the same reduction prime ideal. Thus this
profile's vectors must be counted as one bounded unit-associate family, not
as unrelated norm-divisibility events. Within a fixed cofactor, the unit and
its inverse have explicit power-basis coefficient bounds
`1006,503,251,125` for cofactors `2,4,8,16`. The router itself does not count
that finite family. Modulo the 256 negacyclic shift/sign associates, it
injects into an explicit `L1` body in the full rank-63 algebraic-unit log
lattice. The exact profile charge makes 367 the necessary total orbit cap;
368 such orbits already exceed the complete edge budget. This does not pay
the lower-weight profiles.

The high-cofactor Schinzel collapse and the cofactor-`2` Smyth collapse now
show that every branch `m=2,4,8,16` contributes at most one shift/sign orbit.
Thus the entire maximum-weight profile contributes at most four such orbits
at one fixed row and quotient root. This is far below its former necessary
cap `367`, but is not sufficient for the complete pair budget because lower
profiles remain.

The exact weighted payment for those four possible orbits is

```text
709758113888498314287146042668908462080.
```

After subtracting it, `(2,10,S=18)` is the largest remaining profile and the
residual uniform sufficient cap is `104955` oriented vectors. The exact
weighted sum remains the actual target.

The profile-`(2,10)` ideal router first gives ten pure and 384 split-prime
families, one orbit each. Exact moment and resultant analysis then excludes
the full `m=1538` branch, leaving at most `266` orbits and `68096` oriented
vectors. The remaining split-prime cofactors are `514` and `1028`, both above
`257`.

Subsequent exact payments close profiles `(2,10)`, `(1,14)`, and `(0,18)`
inside the serial weighted ledger. The current residual is

```text
515126704564295620156155116913120291239,
```

and the next dictionary profile is `(4,4,S=20)`, with a sharp cap of `1971`
oriented vectors, hence at most seven complete 256-vector shift/sign orbits.
Its exact local-norm route fence leaves fourteen possible local valuations
and `1133` cofactor values after all current necessary sieves. This does not
count collisions, but it rules out a direct reuse of the former
one-orbit-per-ideal-family strategy as a closing argument.

Exact low-energy resultant analysis now excludes every abstract
autocorrelation spectrum of energy at most four on the binding row. Hence
every actual profile-`(4,4)` collision has `E>=5`, or conjugate-square
variance `V>=10`. Combining that floor with the energy-adaptive product
majorant forces

```text
m<=932364.
```

The exact local-norm frontier therefore contracts from `1133` to `657`
cofactor values and the pure `2^20` branch disappears. Thirteen pure powers
still remain, so this is not an orbit payment and the seven-orbit target is
unchanged.

A complete joint census of the four singleton positions further couples the
local valuation to autocorrelation parity. On valuations
`{3,5,6,9,10,12,17,18,20}` it forces `E>=6`, hence `V>=12` and the sharper
branchwise ceiling `m<=853574`. This excludes twelve more cofactors, leaving
an exact current frontier of `645` values. The refinement remains a norm
classification, not a collision-orbit count.

The complete next energy layer is also empty. Energy five has only two
integer autocorrelation shapes; restricting their odd masks to those
realized by four singleton positions leaves exactly `64808` signed spectra.
Two independent exact resultant censuses find no integer official cofactor
interval. Thus every collision has `E>=6` and `V>=12` globally, not only on
the nine parity-forced valuations, and the current exact cofactor frontier is
`608` values. Further energy-layer enumeration is not the selected closing
route because even substantially larger energy floors leave hundreds of
cofactors without controlling orbit multiplicity.

## Falsifier

An admissible row whose exact unordered low-mass collision-pair count exceeds
its table entry, or a purported proof that counts normalized coefficient
vectors without their class-pair multiplicities.
