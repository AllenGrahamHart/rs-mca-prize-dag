# Claim contract

- **claim id:**
  `rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer`
- **mathematical statement:** the nonharmonic matched-cycle parity compiler
  at `M=2^36` has six exact trace gcds per fixed `epsilon` (at most twelve
  total), two coverage-equivalent six-gcd degree-`M` even-Jacobi norm
  packets, and a torsion-only prefilter consisting of one order-`2^39` norm
  and a 37-level tower through order `2^38`
- **scope:** matched `c=0`, two-antipodal-denominator, generic minimum-degree
  cycle survivors after the corrected post-field compiler
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependencies:** corrected post-field compiler and the
  parameter-uniform Chebyshev/Gegenbauer, trace-gcd, even-Jacobi, and
  cyclotomic-norm transformations
- **new open content:** a compressed implementation and measured pilot for
  the doubled torsion norms, evaluation of the relevant six signed gcds for
  each surviving `(p,epsilon)`, other matched denominator geometries, and
  `c=1,2`
- **falsifier:** an index, degree, sign, field, norm, or tower mismatch; a
  complete scoped survivor not represented in its six-gcd Jacobi packet
- **nonclaims:** no norm is evaluated, no dense polynomial or integer
  resultant is affordable, no large computation is authorized, and a
  nontrivial torsion gcd is not a full survivor
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer/verify.py`
- **upstream mapping:** exact base-field-normalized split-pencil
  trace/Jacobi/cyclotomic certificate interface
