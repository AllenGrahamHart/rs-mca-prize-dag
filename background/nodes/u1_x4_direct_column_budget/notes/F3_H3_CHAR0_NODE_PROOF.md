# Proof candidate: f3_h3_char0_classification

Let `P={x1,x2,x3}` be a triple of roots of unity and write

```text
s_P = x1+x2+x3,
p_P = x1*x2*x3,
e2_P = x1*x2+x1*x3+x2*x3.
```

Since all `xi` lie on the unit circle,

```text
e2_P = p_P * conjugate(s_P).
```

For a second triple `Q`, equality of `e1` and `e2` gives

```text
(p_P - p_Q) * conjugate(s_P) = 0.
```

If `s_P != 0`, then `p_P=p_Q`; the two monic cubic locators have the
same `e1`, `e2`, and constant term, hence the same roots.  Thus any
distinct trade has `s_P=s_Q=0`.

A zero-sum triple of unit complex numbers is necessarily a rotated
equilateral triple.  Dividing by one element gives `1+u+v=0` with
`|u|=|v|=1`; then `|1+u|=1`, so `2+u+conjugate(u)=1`, hence
`Re(u)=-1/2`.  Therefore `u` and `v` are primitive cube roots.  This
proves the toral classification and the count `binom(n/3,2)` in `mu_n`.

For the norm-gate corollary, a non-toral shape has at least one nonzero
obstruction `Ei` among `E1,E2` in `Z[zeta_n]`.  If it activates modulo a
prime `p=1 mod n`, the chosen primitive `n`-th root modulo `p` gives a
prime ideal over `p` containing `Ei`, hence `p | Norm(Ei)`.  Every Galois
conjugate of `Ei` is a sum/difference of six roots of unity, so its
absolute value is at most `6`; therefore `|Norm(Ei)| <= 6^phi(n)`.  The
number of rational prime divisors `p >= n^2` is at most the displayed
logarithmic bound.

The exact replay script verifies the classification through `n=96` by
cyclotomic reduction modulo `Phi_n`, and verifies the banked norm-gate
shapes at `p=9601,13249,18433`.

