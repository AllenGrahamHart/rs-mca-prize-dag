# Proof - L1 full-locator Pade section

## 1. Quotient coefficients

In reversed high-coefficient coordinates, multiplication of the ordinary
polynomials is multiplication of the corresponding series.  The condition
`deg(U-LQ)<k` is therefore

```text
Qhat Lhat = Uhat mod T^(d+1),       d=h-k.           (1)
```

Since `Lhat(0)=1`, there is a unique quotient series
`Uhat/Lhat mod T^(d+1)`.  An ordinary cofactor of degree `e=h-a` has exactly
the reversed coefficients in degrees `0,...,e`.  Equation `(1)` holds for
such a cofactor if and only if all subsequent quotient coefficients through
degree `d=e+w` vanish.  These are exactly `(FA1)`, and `(FA2)` recovers the
unique cofactor.

## 2. Exactness

If `P` is an exact-shell codeword with agreement locator `L`, then
`U-P=LQ` and Step 1 puts `L` in `V_(U,a)`, recovering the same `Q`.
At a domain point outside the roots of `L`, an additional agreement occurs
exactly when `Q` vanishes.  Hence exactness is equivalent to
`gcd(Q,Omega/L)=1`.

Conversely, for a split locator in the right side of `(FA3)`, Step 1 gives
`P=U-LQ_L` of degree below `k`.  It agrees on every root of `L`, and the gcd
guard excludes every other domain point.  This proves `(FA3)`.

## 3. Below the cap

Suppose `e<k`.  Then

```text
d=e+w=e+a-k<a.
```

The quotient coefficients through degree `d` depend only on
`l_1,...,l_d`.  By `l1_cofactor_prefix_pade_graph_normal_form`, their
solutions form a graph of size `q^e`: `l_1,...,l_e` are free and
`l_(e+1),...,l_d` are determined.  The remaining `a-d=k-e` locator
coefficients do not occur in `(FA1)` and are arbitrary.  This proves `(FA4)`.

## 4. At and above the cap

For `e>=k`, `d>=a`, so the quotient recursion in `(FA1)` continues after all
`a` locator coefficients have entered.  The derivation in Steps 1--2 did not
use `d<a`, and therefore the same section and bijection remain valid.  The
triangular graph cardinality argument no longer applies, so no dimension or
cardinality claim is made in this range.
