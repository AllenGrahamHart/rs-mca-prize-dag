# Audit

## Verdict

The arithmetic router is exact on its full-core, zero-baseline scope. It
removes all odd arities and makes the four-row support extension rigid. It is
not an aggregate count.

## Load-bearing scope

- `Delta<=0` comes from using every active row as a block of the minimal
  Maxwell core. A proper local circuit does not inherit it automatically.
- `D_0=0` is exact. A negative baseline may pay positive defect charges.
- Oddness of `h` forces even arity. Odd arities can occur arithmetically when
  `h` is even.
- `H=0` permits multiplicity two; it excludes multiplicity at least three.
- The rank floor uses disjointness of the active zero fibers, not only the
  extension collision ledger.
- The continuous `P>=0` bound is insufficient: each row's private count has
  one residue modulo `t-3`. The exact table enforces `P>=tr`.
- Arity candidates whose necessary rank exceeds `k` are impossible because
  the inherited flat-nullity parameter has `a<=k`.

## Remaining frontier

Strictly negative baselines, surviving even divisor arities, proper local
four/five-block circuits, higher trade rank, nonuniform cells, and cross-core
aggregation remain open. No compute request is promoted by this theorem.
