# Proof

The E14 router exhausts every candidate with four profiles on 1,321 affine
templates. Each census engine scans all `binom(124,3)` heavy supports and 64
relative signs. One engine forms oriented folded chord classes; the other
multiplies the sparse polynomial by its negacyclic reverse in
`Z[X]/(X^128+1)`. They agree on every profile count, conductor count, and
retained vector. A separate Python checker recomputes the direct negacyclic
profile and conductor of all 736 retained representatives.

The proper-conductor theorem removes 1,100 of the 1,836 actual vectors. For
the 736 full-conductor representatives, FLINT and PARI/GP independently
compute `abs(Res(X^128+1,F))` and agree entry by entry. Every norm is positive.

For each norm `R`, write `R=2^mu R_odd`. A pair-feasible row prime `p` is odd
and satisfies `p>2^250`, so `p|R` implies `p|R_odd`. The dual norm ledger puts
all but six odd parts below `2^250`. The six exceptions comprise three exact
integers, each in `[2^250,2^251)`. If `p` divided one of them, then
`1<=R_odd/p<2`, hence `R_odd=p` and that odd part would be prime.

The source-pinned candidate audit runs PARI `isprime` and FLINT `is_prime` on
all six exceptions. The engines agree that the three distinct odd parts are
composite. Thus no pair-feasible row prime divides any full-conductor norm.
The collision-norm criterion excludes all four routed profiles.

The proved prime-field reduction additionally gives `p=1 mod 256`; all three
exceptional odd parts happen to satisfy this congruence, so no congruence
shortcut is being used in place of the exact compositeness test.
