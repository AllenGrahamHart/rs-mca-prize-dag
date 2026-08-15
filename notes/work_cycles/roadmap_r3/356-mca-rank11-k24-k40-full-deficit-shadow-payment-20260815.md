
# Cycle 356: MCA rank-11 K'=24..40 full-deficit shadow payment (2026-08-15)

Cycle 355 left an explicit wall at `K'=24`.  The loss came from using 45 as
the common rank-nine shadow baseline: circuits of supports seven through
eleven create strictly more marks, but no finite caps for the intermediate
support strata had been retained.

## Universal completion incidence

For an independent support-`c` deletion `A`, the space of corrections
vanishing on `A` has dimension `11-c`.  If `A` has `b` completions, locator
division gives `b<=q=K'-10`.  A selected rank-ten eleven-set cannot retain
two completion labels because those labels have private coordinates while
its annihilator intersection is one-dimensional.

Thus, recordwise and without a carrier premise,

```text
I_c<=floor(C(m,c-1)/c
           *max_(0<=b<=q) b C(m-c+1-b,11-c))
```

for every support `2<=c<=9`.

## Full 55-shadow ledger

A support-`c` circuit has `55-C(11-c,2)` rank-nine shadows.  Once supports
through nine have finite caps, the exact deficits can all be retained:

```text
c:             2  3  4  5  6  7  8  9
deficit d_c:  36 28 21 15 10  6  3  1.
```

If `G` is the one global rank-nine mark capacity, the complete full-rank
incidence is at most

```text
floor((G+R max_branch sum_c d_c L_c)/55).
```

This is one ledger; the deficits supplement marks already consumed inside
`G`.

## Finite payment

For every `24<=K'<=41`, the exact replay scans every core, every kernel
corank, both support-two-through-five branches, and every completion count
for supports six through nine.  Rows `24..40` close.  The smallest positive
gap is at `K'=40`:

```text
2272401814108959137912675549447888006236817090602808413697595.
```

The same formula first fails at `K'=41` by capacity excess

```text
4398836630793080990004182400858693750491819390616783425932508.
```

Modal app `ap-jz0QzMEaYA3hxi8XlnJPaF` supplied the parallel exploration.
The local primary verifier reproduces all 423 core charts, and an
independent verifier replays the integer payment.

```text
result:                PROVED K'=24..40 component-row closure
newly closed rows:     17
closed prefix:         10..40
remaining rank nine:  41..15528
new nodes:             3 PROVED
new premise:           none
next route action:     attack the explicit K'=41 floor-record deficit;
                       the full shadow baseline is now exhausted
```
