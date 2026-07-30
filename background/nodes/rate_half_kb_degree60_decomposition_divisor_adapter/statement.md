# KoalaBear degree-60 decomposition divisor adapter

- **status:** PROVED
- **scope:** residual actual KoalaBear `Q=6,s=6,u=2` branch
- **dependency:** `rate_half_kb_q6_u2_primitive_subdegree4_route_cut`
- **consumer:** `rate_half_band_closure`

Let `K=F_(p^6)`, `p=2130706433`, and let the retained endpoint map be

```text
f=V_act/A^5,       deg(f)=60,
```

where `V_act` has 60 distinct roots in `K` and `A` has 12 distinct roots in
`K`, with the two root sets disjoint. If a residual actual component forces
a geometric decomposition

```text
f=F composed h,    m=deg(h),    n=deg(F),    mn=60,
```

then the reduced active divisor is the pullback of the reduced zero divisor
of `F`. Thus the 60 active roots split into exactly `n` complete unramified
fibers of `h`, each containing `m` distinct `K`-points.

The source divisor is likewise a complete pole pullback. The eight necessary
profiles have the following exact source-fiber forms:

```text
m   n    source fibers of h
2   30   6 unramified fibers of size 2
3   20   4 unramified fibers of size 3
4   15   3 unramified fibers of size 4
5   12   2 unramified fibers of size 5; 2 points of index 5
6   10   2 unramified fibers of size 6
10   6   1 unramified fiber of size 10; 2 points of index 5
12   5   1 unramified fiber of size 12
30   2   2 fibers, each 6 points of index 5
```

This proves preservation of the local 60-point active set and 12-point source
set as geometric fiber divisors. It does not descend `h` to `K`, preserve the
full deployed evaluation domain or witness data, construct a same-record
owner, move the ledger, or close `u=2` or the KoalaBear row.

## Falsifier

A decomposition profile in which an active root is ramified, an `h`-fiber
over an outer zero contains a nonactive point, or the printed source-fiber
ledger fails.
