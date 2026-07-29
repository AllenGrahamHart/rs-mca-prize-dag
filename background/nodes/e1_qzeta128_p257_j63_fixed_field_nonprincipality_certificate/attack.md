# Attack

Preferred focused routes:

1. use the pinned polynomial `f_63` to construct a certified unramified
   character of the degree-32 CM field `E_63` and evaluate its Artin symbol
   at `p_66`;
2. export a proof-grade 21121-primary ideal-class coordinate for `p_66`;
3. certify non-solvability of the corresponding exact norm equation;
4. as a stronger fallback, run a complete unconditional class-group and
   principality computation in degree 32.

Retain relation matrices, class-character data, integral bases, and all
certification transcripts needed for independent replay. No degree-64 BNF is
required. The polynomial has only even powers and 17 nonzero coefficients;
no degree-64 setup is needed. Heavy computation remains external-only under
the repository RAM policy.
