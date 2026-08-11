# Cycle 143: paired scalar-weld cross-ratio cycle certificate (2026-08-11)

## Local cycle criterion

On a nonincidence edge put `c_(delta,x)=P_x(delta)/F_delta(x)`. A nonzero
weld kernel exists exactly when these labels are a multiplicative
coboundary. Hence every even-cycle product must be one.

For the extremal profile, every three selected fiber neighborhoods share at
least `6+d_A` classified rows. All cycle consistency therefore reduces to
the four-cycle identities

```text
c_(delta,x)c_(epsilon,y)
 =c_(delta,y)c_(epsilon,x).
```

For the strict profile, pairwise overlap gives the same rectangle tests; the
additional complete conditions are the transition triangles
`q_(delta,epsilon)q_(epsilon,theta)q_(theta,delta)=1`.

One failed local identity forces full weld rank and excludes the boundary.
If all tests pass, they reconstruct the unique projective `lambda`, leaving
only `Krow lambda=0` and the retained source/Hankel identities.

## Burn-down

```text
result:                  PROVED local cross-ratio cycle certificate
DAG delta:               +1 PROVED
critical status delta:   none
delta-star movement:     none
new assumptions:         none
compute requests:        none
next route-deciding:     derive or falsify a rectangle identity from the
                         oriented gcd/heavy-incidence source structure
```
