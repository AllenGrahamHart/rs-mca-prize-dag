# Proof - L1 official checkpoint characteristic atlas

The rate and dimension cap give `n<=2^44`, while the official smooth-row
range gives `n>=2^13`. This proves the range for `s` in `(CAT1)`.

Let `o=ord_n(p)`. Since `n|p^f-1`, one has `o|f`. The group of units modulo a
power of two is a 2-group, so `o` is a power of two. Also `p>=3583>2^11` and
`p^f<2^256` imply `f<=23`. Therefore the power of two `o` dividing `f` is at
most 16, proving `(CAT2)`.

For `s>=3`, the standard decomposition is

```text
(Z/2^s Z)^x = {+-5^j:0<=j<2^(s-2)}.
```

The elements whose order divides 16 are precisely
`+-5^(j 2^(s-6))`, `0<=j<16`, proving `(CAT3)` for the official `s>=13`.
Because `p<n`, the characteristic itself is the least positive representative
of one of these residues.

An actual row must satisfy `p^o<=p^f<2^256`. Conversely, if a prime candidate
has `p^o<2^256`, the generated field `F_(p^o)` contains the order-`n`
subgroup and respects the strict field cap. Thus the exact finite filter is

```text
p prime,       3583<=p<n,       p^o<2^256.
```

`verify.py` enumerates the 32 residues at each of the 32 exponents
`13<=s<=44`, computes the order in `{1,2,4,8,16}`, and applies the
deterministic seven-base Miller-Rabin test valid below `2^64`. Here every
candidate is below `2^44`. The generated set is compared entry-for-entry
with `checkpoint_atlas.tsv`, and the histogram is recomputed. It contains 59
rows with the distribution printed in the statement.

Finally, `l1_official_split_pencil_value_capacity` proves that `m=1` admits
no pair and that `m=2` has the exact complement-square compiler. Subtracting
`33+10` from 59 leaves 16 higher-multiplicity rows. This proves `(CAT4)`.

Filtering the ten `m=2` tuples by the recorded remainder `n-2p` leaves the
four rows in `(CAT5)`. On those rows, `(SPV13)` is
`binom(n,n-2p)=binom(n,2)`. The exact classification `(SPV14)--(SPV17)`
sharpens this to `n/2` antipodal pairs. The remaining six remainders are
`1026,4098,8190,524290,524286,2147483646`, all greater than two, so `(SPV14)`
makes their minimum-width strata empty. Together with the 33 `m=1` rows this
proves `(CAT6)`.
