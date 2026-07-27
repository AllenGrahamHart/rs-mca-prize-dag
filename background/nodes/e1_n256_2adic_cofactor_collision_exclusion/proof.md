# Proof

Put `K=Q(zeta)` and `pi=zeta-1`. The prime two is totally ramified:

```text
2=u pi^128 for a unit u,         Norm((pi))=2.
```

Write the integral expansion

```text
F(1+T)=sum_(j=0)^127 b_j T^j.
```

The reduction `bar F` is nonzero because each live profile has singleton
coefficients. If `mu=ord_(X=1)(bar F)`, then `mu<128`,
`b_0,...,b_(mu-1)` are even, and `b_mu` is odd. In the
`pi`-adic expansion of `F(zeta)=F(1+pi)`:

- every term below degree `mu` has valuation at least `128+j>mu`;
- the degree-`mu` term has valuation exactly `mu`;
- every later term has valuation strictly above `mu`.

Thus

```text
v_pi(F(zeta))=mu,
v_2(|Norm_(K/Q)(F(zeta))|)=mu.                         (1)
```

The folded-L2 theorem gives `|Norm(alpha)|<=S^64`. Suppose the odd row
prime `p>=2^250` divides this nonzero norm, and write its absolute value
as `p m`. Since no prime equals the power of two `2^250`, in fact
`p>2^250`.

For profile `(3,4,0)`, `S=16`, and hence

```text
m <= 2^256/p < 64.
```

The integer `m` therefore has 2-adic valuation at most five. Equation
(1) gives `mu<=5`.

For profile `(4,2,0)`, `S=18`. The exact integer inequality

```text
18^64 < 2^267
```

gives `m<2^17`, so `v_2(m)<=16` and (1) gives
`mu<=16`.

Finally, modulo two only the singleton terms remain. With two singleton
exponents `r<s`,

```text
bar F=X^r(1+X^(s-r)).
```

If `s-r=2^t q` with `q` odd, then in characteristic two

```text
1+X^(s-r)=(1+X^q)^(2^t),
```

and `1+X^q` has a simple root at one. Therefore
`mu=2^t=2^v_2(s-r)`. The bound `mu<=16` is equivalent to
`32 not dividing s-r`.
