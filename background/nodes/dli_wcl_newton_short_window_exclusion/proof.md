# Proof

Set

```text
r_i = s_i omega^e_i,
p_m = sum_i r_i^m,
```

and let `a_m` be the `m`th elementary symmetric function of the `r_i`, with
`a_0=1`. Because every `s_i` is `+1` or `-1`, the odd-power hypotheses are
exactly

```text
p_1=p_3=...=p_(2ell-1)=0.
```

We prove by induction that `a_m=0` for every odd `m<=min(w,2ell-1)`.
Newton's identity at an odd index `m` is

```text
m a_m = sum_(i=1)^m (-1)^(i-1) a_(m-i) p_i.
```

If `i` is odd, then `p_i=0`. If `i` is even, then `m-i` is an earlier odd
index and `a_(m-i)=0` by induction. Every term on the right is therefore
zero. The characteristic assumption makes `m` invertible, proving the
claim.

If `w` is odd and `w<=2ell`, then in fact `w<=2ell-1`, so the claim gives

```text
a_w = product_i r_i = 0,
```

contrary to all roots being nonzero.

If `w` is even and `w<=2ell`, every odd elementary coefficient through
`a_(w-1)` vanishes. Hence

```text
prod_i(T-r_i) = T^w + a_2 T^(w-2) + a_4 T^(w-4) + ... + a_w
```

is even. Its distinct nonzero roots are stable under negation and therefore
split into antipodal pairs. Encode a negative sign by the full exponent
`e_i+N` and a positive sign by `e_i`. Since `-1=omega^N`, antipodal full
exponents differ by `N` modulo `2N` and reduce to the same exponent modulo
`N`. This contradicts reduced support.

For an official row, `q>2^41`, while `ell<=2^32` and
`w<=ell+5`; thus `q>w` throughout the tower. If `ell>=8`, then
`ell+5<=2ell`, so the whole WCL window is excluded. Direct substitution gives
the three low-level rows in the statement.
