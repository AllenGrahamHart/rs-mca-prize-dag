# Claim contract - L1 tangent Hasse root-pinning census

## Inputs

- a squarefree split domain locator;
- the exact-shell factorization `U-P=LQ` with `deg P<k`;
- the Pade-remainder Jacobian formula.

## Outputs

- canonical tangent owner `T=gcd(L,Q)`;
- fixed-root equivalence `D|Q` iff `D^2|U-P` when `D|L`;
- rank `min(k,2r)` for the value/first-Hasse-derivative map at `r` roots;
- fixed-owner multiplicity at most `q^max(k-2r,0)`;
- aggregate exact tangent census `(TH5)` without support-subset overcount;
- full remainder rank `a-r` and Pade Jacobian corank at most `min(w,r)`.

## Consumer rule

Stratify every same-locator tangent member by its exact gcd before any
summation.  A computation may enumerate feasible exact owners `D`, but must
not rerun the confluent-rank calculation or count one member through proper
subdivisors of its gcd.

## Nonclaims

The binomial sum is not asserted to fit the prize reserve.  No collective
sparsity of feasible root sets, quotient classification, primitive
split-point bound, or closure of `l1_mixed_petal_amplification` is proved.

## Falsifier

A split squarefree example violating `(TH2)`, a confluent evaluation rank
different from `min(k,2r)`, more than `q^max(k-2r,0)` exact members with one
exact tangent gcd, duplicate exact-gcd ownership, or Pade Jacobian corank
larger than `min(w,r)`.
