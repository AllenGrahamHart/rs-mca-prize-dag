# XR window-system descent

- **status:** PROVED
- **scope:** exact algebra for `H=mu_n`, plus official-row arithmetic
- **provenance:** round-12 SL-2 pilot, independently narrowed here to its
  theorem-grade content

Let `u` be represented by its polynomial of degree `<n` on
`H=mu_n`. Fix a depth `d`, put `r'=n-k-d`, and for `T subset H` with
`|T|=r'` write

```text
E_T(X)=prod_{t in T}(X-t).
```

The following statements hold.

1. **Window lemma W.** A unique `f` of degree `<k` agrees with `u` on
   `H\T` if and only if the coefficients in degrees `n-d,...,n-1` of
   `uE_T mod (X^n-1)` vanish. For a received pair `(u,v)`, the joint
   condition is the intersection of the two `d`-equation systems.
2. **Descent D.** If `M|gcd(n,k,d)`, then `T` is a union of
   `mu_M`-cosets exactly when `E_T(X)=G(X^M)`. The window equations
   separate by residue class modulo `M`. If the syndrome window of `u`
   is supported in one class `rho`, the scale-`M` solutions are in
   bijection with the quotient window system on `mu_{n/M}` at depth
   `d/M`. This validates syndrome descent for this exact system.
3. **Single-word rank R.** Under the tangent gate, each single-word
   `d`-row Toeplitz window matrix has rank exactly `d`. On the scale-`M`
   locus a one-class word has rank `d/M`; an additional nonzero residue
   block contributes positive rank. No joint rank of exactly `2d` is
   asserted: the two full-rank row spaces can intersect.
4. **Periodic liveness L.** Suppose `M=2^j`, `M|gcd(n,k,d)`, and the two
   syndrome windows are individually supported in residue classes
   `a,b mod M`. If an `M`-coset-union depth-`d` pair carries an exact-`A`
   pencil member and `h` is odd, then

   ```text
   M <= floor((n-k-d)/(h-d)).                         (L)
   ```

   At all three prize rows `(L)` excludes every such sub-depth scale
   `M>=2^21` throughout the high band. Common-class quotient-periodic
   systems are additionally owned by strip P3 through D.

These are representation and exclusion theorems, not an occupancy
bound. In particular, small-scale mixed-class systems and genuinely
aperiodic systems remain in the SL-2 residual.

## Not Claimed

- The two word systems have joint codimension exactly `2d`.
- A first-moment estimate is a worst-case count.
- Every divisor satisfying the window equations is a maximal depth-`d`
  core or carries two selected live slopes.
