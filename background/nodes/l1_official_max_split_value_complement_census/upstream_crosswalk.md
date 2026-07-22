# Upstream crosswalk - maximal split-value complement census

In upstream split-pencil terminology, this is an exact finite complement
compiler for every split-value stratum of one normalized Frobenius pencil.
The primitive payload is indexed by the unused domain divisor `C`, not by
independent value parameters or by an unrestricted perturbation `Q`. Its
concrete polynomial payoff is the **maximal split-value stratum**.

For a constants-first handoff, retain

```text
u=n-hp,       ell_h=u-d+p,
#Q_h<=floor(binom(n,ell_h)/binom(u,ell_h)),
#pairs_h<=binom(h,2)floor(binom(n,ell_h)/binom(u,ell_h)).
```

The maximal stratum is empty on every official `m>=3` row by the printed
Frobenius multiplicity test `(n-mp)(-m^(-1) mod p)>p`. This does not solve the
base-field-normalized split-pencil census: the lower value degrees
`2,...,m-1` remain the portable open endpoint, with only degree two left when
`m=3`. Their depressed inner polynomial satisfies
`ord_0(R)<=n-(h+1)p`; retain this valuation field in any handoff.
