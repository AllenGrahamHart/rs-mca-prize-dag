# Audit

## Verdict

The set decomposition is exact. Its substantive consequence is `(QMF3)`:
the remaining quotient compiler may range over full agreement sets only.

## Scope checks

- `Q_c(A)` uses supports of size exactly `A`.
- Exclusion from `B_(A+1)` is global over all codewords, so any selected
  witness codeword has exactly `A` agreements.
- Cross-scale or multiple-codeword representations are deduplicated by an
  arbitrary fixed order after truth of the union containment is established.
- A quotient slope with higher agreement is not discarded; it is carried to
  the complete next-threshold first-match partition.

## Limitations

Full agreement sets with a nonempty quotient tail can still have trivial
stabilizer and may be numerous. The PMA exact-periodic owner therefore does
not close this packet. A full-agreement image theorem or a certified compiler
is still required.
