# Rate-half ordinary-list adjacent crossing

## Live target

For every admissible official rate-half row, with
`B*=floor(|F|/2^128)`, determine adjacent integers `a_L-1,a_L` satisfying

```text
L_1(a_L) <= B* < L_1(a_L-1).
```

Budgets `B*=1,2` are proved exactly at `a_L=3n/4`.  For `B*>=3`, the safe
anchor and unsafe floor do not meet, so this node remains `TARGET`.

## Sub-DAG packets

- `statement_sections/00-live-contract-and-base-reductions.md`: exact scope,
  endpoint convention, and budget-three reduction.
- `statement_sections/01-c2-one-antipodal-fourier-chain.md`: the current
  one-antipodal Fourier/support/collision chain.
- `statement_sections/02-fiber-two-cycle-c1-c2-chain.md`: matched and
  mismatch cycle, parity, torsion, and trace/Jacobi routes.
- `statement_sections/03-wave11-pin-v1.md`,
  `statement_sections/04-wave12-pin-v1.md`, and
  `statement_sections/05-wave13-pin.md`: first chronology-preserving pins.
- `statement_sections/06-wave11-pin-v2.md`,
  `statement_sections/07-wave12-pin-v2.md`, and
  `statement_sections/08-wave14-pin.md`: expanded audited pins.
- `statement_sections/09-wave11-pin-of-record.md` and
  `statement_sections/10-wave12-pin-of-record.md`: forward-facing pin bodies;
  earlier versions remain solely for provenance.
- `statement_sections/11-h1-s3-addendum.md`: later list-compiler addendum.
- `statement_addenda/12-round18-dsa-scope.md`: Round-18 DSA scope update.

Each mathematical supplier is already an independent DAG node.  This parent
does not absorb those theorems and does not become conditional on them.
`statement_sections/document.json` proves that the extracted packets preserve
the pre-refactor statement byte-for-byte.  Later addenda are indexed and
verified separately, so they do not rewrite that historical archive.
