# Cycle 128: quadratic extremal Forney gate (2026-08-11)

## Cycle pins

```text
our start:       2a7b3c2a2
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
upstream PR:     #1161 open as draft at 09152eb
compute:         tiny integer checks and one F_101 circuit audit
critical open:   28
```

## Three-center source partition

Subtract the codeword line through the exact three assigned centers in the
sole floor branch. Every noncore coordinate of its fixed support is a
nonzero parameter-linear source. The coordinates missing at the three line
slopes form disjoint classes of sizes

```text
p-1+r_alpha, p-1+r_beta, p-1+r_theta.
```

They cover the support when the total line deficit is one and leave exactly
one coordinate when it is zero. Thus the fixed source has only three named
parameter-root classes, plus at most one exceptional coordinate.

## Minimum circuits become reciprocal interpolation

At every zero triple-union excess slope, split its actual support into the
inside part and a monic outside locator `B_delta`. The outside support has
exactly `p+2` points. Comparing the minimum RS word values with the
contracted Hankel source gives

```text
omega_x(delta) B_delta(x)L_U0'(x)=kappa_delta
```

on `rho+1+r_delta` coordinates. The full form retains the padded factor and
is independently checked against the `d+1`-row Vandermonde nullspace. At
least `2e` slopes obey this gate, and at least `e+6+d_A` of them are clean
one-dimensional barycentric circuits. Officially the lower bounds are
`366503875926` and `183251937969`.

## Burn-down

```text
result:                  REDUCED the extremal branch to a three-class
                         reciprocal locator interpolation problem
DAG delta:               +2 PROVED leaves, +3 req edges, +2 ev edges
critical status delta:   narrowed, still TARGET
upstream terminal delta: no PR amendment; #1161 remains the pair-floor cut
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next exact task is to compare two clean outside locators through the
same three source classes. A useful closure must control their coordinate
scalars or force a low-rank locator pencil; counting minimum words alone is
now known to be insufficient.
