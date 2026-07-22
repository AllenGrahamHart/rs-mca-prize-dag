# Proof - L1 band complement-dimension packing

## 1. Projective dimension

The balanced shifted-lattice theorem gives coefficient-space dimension

```text
omega-w+1=s+1.
```

Its first-coordinate map is injective under the degree caps.  Indeed, a
coefficient pair mapping to first coordinate zero would produce a module
element `(0,N)` of shifted degree at most `omega`.  The module congruence
forces `Omega|N`, while

```text
deg N<=omega+k-1=n-m+k-1<n
```

because `m>k`; hence `N=0`, and basis-coordinate uniqueness makes the
coefficient pair zero.  Thus the complement-locator pencil has projective
dimension exactly `s`.

## 2. Complement packing

Let `P_i` and `P_j` be distinct exact-shell codewords, with complete
agreement sets `A_i,A_j` of size `m`.  Reed--Solomon uniqueness gives

```text
|A_i intersect A_j|<=k-1.                            (1)
```

Their complement root sets `C_i=H\A_i` have size `omega`, and

```text
|C_i intersect C_j|
 =n-|A_i union A_j|
 =n-2m+|A_i intersect A_j|
 <=n-2m+k-1=s-1.                                    (2)
```

Therefore no `s`-subset of `H` is contained in two complement root sets.
Counting pairs `(T,C_i)` with `|T|=s` and `T subseteq C_i` yields

```text
Z_m(U) binom(omega,s)<=binom(n,s),
```

and integer rounding proves `(CP2)`.

Finally,

```text
binom(n,s)/binom(omega,s)
 <= (n/(omega-s+1))^s.
```

If `omega>=alpha n` and `s<=alpha n/2`, the denominator is at least
`alpha n/2`, proving `(CP3)` and its asymptotic reserve consequences.
