# pma_saturated_mixed_support_kernel

- **status:** PROVED
- **role:** exact mixed-support kernel and saturation reduction
- **consumer:** `petal_mixed_amplification`, hence `imgfib`

## Statement

Let `X` be an exact noncore agreement support, partitioned into nonempty
label classes `X_j` with pairwise distinct labels `c_j`. Put

```text
s=|X|=d+ell+lambda,       lambda>=0,
a_j=|X_j|,                a_*=max_j a_j,
a_j<=min(d,ell).
```

The background class, when present, has label zero and size strictly less
than `ell`. Petal classes have their nonzero source labels. For
`F` of degree at most `d`, let `I_X(alpha F)` be the unique degree-`<s`
polynomial interpolating `c_j F(x)` on each `X_j`. Define

```text
T_(X,d)(F)
 = coefficients of I_X(alpha F) in degrees d+1,...,s-1.
```

Then:

1. `T_(X,d)` is linear and has target dimension
   `s-d-1=ell+lambda-1`.
2. A pair `(F,W)` with `deg F,deg W<=d` satisfies
   `W(x)=alpha(x)F(x)` on `X` exactly when
   `F in ker T_(X,d)` and `W=I_X(alpha F)`.
3. Its rank satisfies

   ```text
   rank T_(X,d) >= a_*-1.
   ```

   If `s-a_*>d`, then `rank T_(X,d)>=a_*`. Equality
   `s-a_*=d` can occur only when `lambda=0` and `a_*=ell`; in the PMA
   source this is a full petal.
4. Put `w=s-d-1`. If `L_X` is the locator of `X` and

   ```text
   mu_m=sum_(x in X) alpha(x)x^m/L_X'(x),
   H_(j,t)=mu_(j+t),       0<=j<w, 0<=t<=d,
   ```

   then `T_(X,d)` and the `w`-by-`(d+1)` Hankel matrix `H` have the same
   kernel and rank. Equivalently, a row-rank defect in `H` produces
   nonzero polynomials `A,Q` of degree at most `w-1` with
   `A(x)=alpha(x)Q(x)` on `X`.
5. For an actual exact-defect PMA word, `F=L_D` is split, monic, and
   squarefree, while exactness gives `gcd(F,W)=1`. Consequently the nonzero
   fiber polynomials `W-c_jF` are individually coprime to `F` and pairwise
   coprime for distinct labels.
6. On such an actual saturated pair, the rank is maximal subject to the
   known kernel vector:

   ```text
   rank T_(X,d)=min(d,w).
   ```

   If `d<w`, the kernel is exactly the line spanned by `F`. If `d>=w`, the
   rows are independent.
7. Multiplying both `F` and `W` by a split core factor only re-encodes the
   same codeword with a non-exact larger defect. Such principal
   common-factor components are excluded by the exact-defect guard.
8. Fix the ordered source core `C`, of size `k-1`, and this exact support
   pattern `X`. The number of monic degree-`d` locators `L_D` with
   `D subset C` that lie in the saturated kernel is at most

   ```text
   binom(k-1,m-1)=binom(k-1,max(0,d-w)),
   m=dim ker T_(X,d).
   ```

   Indeed, each locator has a canonical subset of `m-1` roots whose
   vanishing cuts the kernel down to its one-dimensional span, and this
   subset determines the monic locator.

By `petal_reserve_rich_fiber_reduction`, a reserve-scale residual has
`a_*>=m_rich`, so

```text
rank T_(X,d) >= m_rich-1 = Omega(n/log^2 n).
```

This is an exact maximal-rank, saturation, and fixed-pattern split-locator
theorem. The binomial fixed-pattern bound need not be polynomial when `d-w`
grows, and it does not sum exact support patterns. The remaining consumer must
absorb or sharpen these root-pinned charges through natural-scale ownership
and aggregate them uniformly over defects, supports, and first-match profiles.
