# Audit

The proof uses the second-derivative Wronskian, not the ordinary Wronskian.
That choice retains two orders from each fourth-power root while also exposing
the `d-2` contact forced by `Y^d` at zero.

Root overlap with `D` or with zero is not discarded. A root shared with the
squarefree `D` improves the local order by one. At zero, equation `(4)` adds
the fourth-power multiplicity to the `d-2` binomial contact because
`4m(d-4m)` is nonzero under the characteristic hypothesis.

After the exact degree conclusion, the lower divisor has degree `8r` and the
Wronskian has degree exactly `8r+1`; the nonzero leading coefficient is
`-4d beta(d-4)`. Thus the residual in `(PQ3')` is genuinely linear, not merely
of degree at most one.

The same one-degree slack is exhausted by multiplicity. The distinct-root
counts must be maximal, so `U,V` are squarefree. A root shared with `D` or
zero adds one local order; consequently at most one such overlap exists, and
it must be the root of the linear residual.

The boundary verifier exhausts the exact `d=8` antipodal positives over
`F_97`. None of the `192` positives even has centered `e_2=0`, and hence none
lies in the pure-quartic sublocus. Thus the special strata are not needed to
explain the known boundary examples; this is an audit observation, not an
all-scale emptiness claim. No official-scale census is used.
