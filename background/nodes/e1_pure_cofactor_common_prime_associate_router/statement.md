# E1 pure-cofactor common-prime associate router

- **status:** PROVED
- **closure:** ideal factorization proof
- **scope:** prize-envelope `N=256` prime-field E1 collisions
- **consumer:** `e1_official_low_square_mass_pair_budget`

Let `R=Z[zeta_256]`, put `pi=1-zeta_256`, and fix one official quotient
root `r in F_p` of order `256`.  The reduction map

```text
theta_r:R -> F_p,       theta_r(zeta_256)=r
```

has kernel `P_r`, a prime ideal of norm `p`.

If a nonzero collision value `alpha in R` satisfies

```text
theta_r(alpha)=0,       |Norm(alpha)|=2^mu p,
```

then

```text
(alpha)=P_r (pi)^mu,    g_alpha=alpha/pi^mu is integral,
(g_alpha)=P_r,          |Norm(g_alpha)|=p.             (PCR1)
```

Consequently, if `beta` is another collision at the same row and quotient
root with `|Norm(beta)|=2^nu p`, there is a unit `u in R^x` such that

```text
beta/pi^nu = u alpha/pi^mu,
pi^mu beta = u pi^nu alpha.                            (PCR2)
```

Thus same-row pure-power-of-two cofactor collisions are not independent
principal-norm events: after removing their exact ramified factor at two,
they are unit associates generating the one fixed reduction prime.

For the currently surviving prize `N=256`, profile `(3,6,S=18)` branches,
the proved cofactor exclusions leave only

```text
m in {2,4,8,16};
```

the `m=16` once- and twice-divided support branches are also excluded.  Hence
all live vectors of this maximum-weight profile at a fixed `(p,r)` satisfy
`(PCR2)`, with `mu in {1,2,3,4}` and only the primitive multiplicity-four
support branch remaining at `mu=4`.

This is an aggregate coupling theorem, not a count.  The remaining payment is
to bound the number of coefficient-bounded unit associates whose products
with `pi^mu` have profile `(3,6,S=18)`, jointly with the lower-weight profiles
in the exact weighted-kernel ledger.

## Falsifier

Two same-root collisions of pure cofactor whose normalized principal ideals
are distinct, or a live profile-`(3,6)` cofactor outside `{2,4,8,16}` after
all stated exclusions are consumed.

