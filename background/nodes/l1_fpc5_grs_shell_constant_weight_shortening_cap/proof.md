# Proof: constant-weight shortening cap

The GRS syndrome-shell theorem identifies every primitive locator in the
fixed chart with a weight-`d` vector in one syndrome coset of an MDS code.
The parity-check count is `H-1`, so the kernel code has minimum distance
`H`. A monic squarefree locator is determined by its root support, hence the
map from shell members to their `d`-subsets of the core is injective.

Let `S` and `T` be two distinct locator supports. The difference of their
syndrome vectors is a nonzero kernel codeword. Its support is contained in
`S union T`, and therefore

```text
H <= wt(e_S-e_T) <= |S union T|=2d-|S cap T|.
```

Thus `|S cap T|<=2d-H`, and

```text
|S triangle T|=2d-2|S cap T|>=2(H-d)=2sigma.           (1)
```

Complementing every support preserves symmetric difference. We may
therefore work with a family `C` of `w=min(d,N-d)` subsets of an `N`-set,
still with distance at least `2sigma`.

Fix `j`. Count pairs `(C,J)` with `C in C`, `J subset C`, and `|J|=j`.
Some `j`-set `J` is contained in at least

```text
|C| binom(w,j)/binom(N,j)                               (2)
```

members. Delete `J` from those members and delete its coordinates. The
result is a constant-weight family of length `N-j`, weight `x_j=w-j`, and
the same minimum distance `2sigma`.

If `x_j<sigma`, two such sets cannot exist because their distance is at
most `2x_j<2sigma`. Hence the shortened family has size at most one.

Otherwise every pair intersects in at most `x_j-sigma`. For a shortened
family of size `m`, let `r_z` be the number of members containing coordinate
`z`. Then

```text
sum_z r_z=m x_j,
sum_z binom(r_z,2)<=binom(m,2)(x_j-sigma).              (3)
```

Cauchy gives `sum_z r_z^2>=m^2 x_j^2/(N-j)`. Substituting
`sum binom(r_z,2)=(sum r_z^2-mx_j)/2` into `(3)` yields

```text
m Delta_j <= (N-j)sigma.                               (4)
```

When `Delta_j>0`, `(4)` gives `m<=P_j`. Combining this with `(2)` and
integrality proves `(CW4)`. The trivial `binom(N,w)` bound and minimization
are immediate.

There is one owner-free chart when `u<0`. When `0<=u<=b`, the proved
fixed-background incidence cover has exactly `binom(b,u)` required-set
charts. Applying `(CW4)` to each and summing proves `(CW5)`. QED.
