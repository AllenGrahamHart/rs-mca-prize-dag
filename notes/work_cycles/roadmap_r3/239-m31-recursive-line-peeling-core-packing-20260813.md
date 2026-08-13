# Cycle 239: M31 recursive line-peeling core packing (2026-08-13)

The one-shot boundary-line-bank theorem ended with the crude charge
`e*M_e` for every unsynchronized low explanation.  Reusing the proved
weighted prefix immediately pays the first new rows.  When that prefix no
longer pays, rerun the exact-layer line bank on the residual family: an
unsafe residual forces another affine line, charge the line by
`Q=N-m+1`, remove it, and repeat.

The new invariant is geometric.  A peeled line has a codeword pair `(a,b)`
and a forced common core.  At least `u_i` core coordinates lie in the fixed
`e`-coordinate gauged support.  Distinct peeled lines have distinct
codeword pairs, so their inside cores meet in at most `K-1=5` coordinates.
Consequently

```text
sum_i u_i-C(r,2)*5 <= e.
```

If the replay produces the strict reverse inequality, the assumed unsafe
family is impossible.  Otherwise core absorption lowers the residual
deficit ceiling and the suffix-minimum prefix can pay it.

The source-bound endpoint verifier, independent audit, and constant-memory
C replay prove every support

```text
124806<=e<=130198.
```

The exact census is `5,393` paid rows: `3,837` terminate by weighted prefix
and `1,556` by distinct-line core packing.  The line-count distribution is
`3534,397,1397,59,6` for one through five peeled lines.  At the last row,
five inside-core lower bounds give

```text
37718+33617+28204+20729+12942-10*5 = 133160 > 130198.
```

At adjacent `e=130199`, nine legal peels give packing lower bound `126052`,
while the next residual target is `7947054` and the certified base charge
is `8154082`.  The current pigeonhole cannot force another line.  This is a
method wall, not an unsafe certificate.

```text
start:                   038a1a001
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ 9af5123a
result:                  NARROWED; one PROVED interval payment
DAG delta:               +1 PROVED node, +5 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       130199<=e<=1044241
delta-star movement:     none
compute:                 4.3-second constant-memory C replay under RAMguard;
                         no Modal
next route action:       replace the residual-base obstruction at e=130199,
                         or bridge toward the high-support interval
export target:           extend przchojecki/rs-mca PR #1165
```
