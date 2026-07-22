# L1 Mersenne next-to-maximal hypergeometric normal form

- **status:** PROVED
- **dependency:** `l1_mersenne_next_to_maximal_belyi_shifted_value_gate`
- **consumer:** `l1_mixed_petal_amplification`

Retain the notation of the dependency and normalize

```text
y=Y/r_0,          g(y)=r_0^(-h)G(r_0y),
A=a/r_0^2,        ell=lambda/r_0^(h-1),       c=z/r_0.       (HNF1)
```

Then `A,c,c-1` are nonzero, `g_h=1`, `g_(h-1)=0`, `g_(h-2)=A`, and

```text
2A(g-ell y)=(y-1)(y-c)(hg-yg').                       (HNF2)
```

Writing `g=sum_(k=0)^h g_k y^k`, with `g_(-2)=g_(-1)=0`, gives the exact
coefficient recurrence

```text
[2A-c(h-k)]g_k
  =(h-k+2)g_(k-2)-(1+c)(h-k+1)g_(k-1)
    +2A ell 1_(k=1).                                  (HNF3)
```

Starting with the three printed top coefficients, the equations for
`k=h,h-1,...,2` determine `g_(h-3),...,g_0`; the equation for `k=1`
determines `ell`; and the last equation is

```text
[2A-ch]g_0=0.                                         (HNF4)
```

The recurrence also has a closed generating form. Put

```text
rho=2A/[c(c-1)],
U(t)=(1-t)^(c rho)(1-ct)^(-rho).
```

The powers denote their generalized-binomial series through degree `h`;
all required factorials are invertible because `h<p`.

Then, for `0<=r<=h`,

```text
g_(h-r)=[t^r]U(t).                                    (HNF4a)
```

Consequently the two local-order chambers have the following exact forms.

1. If `ord_0(T)=0`, then `g_0!=0`, `2A=ch`, and `theta=h`. Put

   ```text
   s=h/(c-1).
   ```

   The shifted split-value polynomial is the one-parameter polynomial

   ```text
   P_s(W)=sum_(r=0)^h binom(s+r-1,r) W^(h-r),          (HNF5)
   ```

   and its differential constants are

   ```text
   b=-h-s,
   K=(h+s)binom(s+h-1,h).                              (HNF6)
   ```

   Every survivor must satisfy the single exact cyclotomic congruence

   ```text
   P_s(W) divides W^n-1,       s notin F_p.            (HNF7)
   ```

2. If `ord_0(T)=1`, then `g_0=0` and `g_1!=0`. Thus this chamber is the
   explicit hypergeometric plane curve

   ```text
   Phi_h(rho,c)=[t^h](1-t)^(c rho)(1-ct)^(-rho)=0      (HNF7a)
   ```

   produced equivalently by the top-down recurrence (HNF3), with `ell` then
   fixed by its `k=1` equation. Its known
   zero split value has normalized coordinate `-1/(c-1)`, so

   ```text
   (c-1)^n=1.                                         (HNF8)
   ```

   The shifted polynomial from the dependency still divides `W^n-1`, and
   at least one of `c,2A/c` lies outside `F_p`.

This converts the remaining outer classification into a univariate
hypergeometric divisibility problem and a torsion intersection with one
explicit hypergeometric plane curve. It does not prove either intersection empty,
construct the inner degree-`p` Belyi map, treat lower `h`, or close L1.
