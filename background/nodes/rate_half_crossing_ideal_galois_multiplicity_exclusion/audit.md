# Audit

## Written proof audit

1. `p` is odd, so it is unramified in the dyadic cyclotomic field.  The
   decomposition group at every prime above `p` is `<sigma_p>` and has order
   `ord_n(p)`.
2. Odd moment indices are units modulo `n`, hence genuine Galois conjugates
   of `x_1`.  Even indices are used only to propagate the ideal containment.
3. Distinct primes are counted modulo the decomposition group; counting
   closure elements without dividing by `ord_n(p)` and then restoring each
   residue degree is what yields the exponent `|Z_w^odd|`.
4. The antipodal count is ordered.  Each antipodal pair contributes two,
   exactly matching the odd-embedding orthogonality identity.
5. The norm ceiling can be sharp, so no unprinted constant-factor saving is
   inferred from AM-GM.
6. The periodic reduction preserves **odd-prime support**, not the complete
   ideal norm: powers of two and extension-degree multiplicities change.

## Catches during transport

- The imported `71.16%` headline used `log_2 p=256`.  It is not uniform in
  the ambient size `q=p^e`; this packet makes only a rowwise claim.
- The imported tower display discarded floors.  Top-level propagation is
  automatic for `w=2^v`; arbitrary `w` uses each exact `(IG5-a)` test.  The
  audit fixture `w=6,a=1` rejects the old coefficient identity.
- The source bisection returned the first excluded integer
  `170,752,922,588` but described exclusion only above it.  The corrected
  last unexcluded integer is `170,752,922,587`.

## Independent replay

The first preregistered Modal run failed on the boundary-label error and is
preserved.  After a separate remediation registration, app
`ap-JNBoN1s1INvr1ovkHvbf8h` passed:

- 816 exact multiplication-matrix norm ceilings;
- 1,104 finite-field vanishing/divisibility checks over `F_9`, `F_17`, and
  `F_49`;
- 1,008 fixtures rejecting `p^(|Z_w^odd|+1)`;
- 272 nonzero sharp norm-ceiling fixtures;
- 65 exact power-of-two tower identities; and
- exact recovery of both benchmark boundary integers.

These checks support the audit but are not used as proof of the general
statement.
