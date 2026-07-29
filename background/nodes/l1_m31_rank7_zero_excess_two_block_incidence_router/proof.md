# Proof

## 1. Exact two-block support

The source class has

```text
f_i=f_*+L_S a_i,             deg(a_i)<k,
Q_i=P/G_i divides f_i,
H_i=gcd(L_0,Y-f_i),          S subset Z(H_i),
deg(H_i)=deg(G_i)=g-q_i.
```

The planted and external domains are disjoint. Since `L_S` is nonzero on
`Z(P)`, every root of `Q_i` is an agreement of `a_i` with the combined
received table. After deleting `S`, every root of `H_i/L_S` is an external
agreement. Their sizes are

```text
|A_i|=q_i,
|B_i|=deg(H_i)-|S|=g-q_i-282544=72428-q_i.
```

If `i!=j`, then `a_i-a_j` is a nonzero polynomial of degree below
`k=4981`. Every point of

```text
(A_i intersect A_j) disjoint_union (B_i intersect B_j)
```

is a root of this difference. This proves (TB1).

## 2. Uniform constant-weight tail lemma

Let `C_1,...,C_M` be `d`-subsets of an `R`-point set with pairwise
intersections at most `t`, and assume `d^2>Rt`. If `r_x` is the number of
sets containing `x`, then

```text
sum_x r_x = Md,
sum_x binomial(r_x,2) <= binomial(M,2)t.
```

Cauchy-Schwarz gives

```text
sum_x r_x^2 >= M^2 d^2/R.
```

Combining the three displays and rearranging gives

```text
M <= R(d-t)/(d^2-Rt).                                 (1)
```

For every member with `q_i<=4980`, choose any `67448` points from `B_i`.
Apply (1) with `(R,d,t)=(698585,67448,4980)`. The exact numerator and
denominator are

```text
R(d-t) = 43637207780,
d^2-Rt = 1070279404,
```

whose integer quotient is `40`.

For every member with `q_i>=67448`, choose any `67448` points from `A_i`.
Now `(R,d,t)=(354972,67448,4980)`, and

```text
R(d-t) = 22174390896,
d^2-Rt = 2781472144,
```

whose integer quotient is `7`. This proves (TB2).

## 3. Whole-family mean confinement

Let `x_alpha` be the load of planted point `alpha` among the `A_i`, and let
`y_beta` be the external load among the `B_i`. Put `Q=sum_i q_i`. Then

```text
sum_alpha x_alpha = Q,
sum_beta y_beta = Mm-Q.
```

Summing (TB1) over unordered member pairs and applying Cauchy-Schwarz in
the two blocks gives

```text
Q^2/g + (Mm-Q)^2/E - Mm <= M(M-1)t.                  (2)
```

Complete the square using `N=g+E`:

```text
q^2/g + (m-q)^2/E
 = m^2/N + N/(gE) (q-mg/N)^2.
```

Substitute `q=Q/M` in (2), clear denominators, and obtain (TB3). Direct
integer expansion gives

```text
Nt-m^2=898676,
24402 < mg/N < 24403.
```

For `M>=2157929`, the half-width in the completed-square inequality is
strictly below `457`. One exact form of that comparison is

```text
gE (N(m-t)+2157929(Nt-m^2))
  < 457^2 * 2157929 * N^2.
```

The half-width decreases with `M`, so (TB4) follows.

## 4. Distinct middle locators

By (TB2), a family of size at least `M0` has at least `M0-47=2157882`
members in `4981<=q_i<=67447`.

Two members in the same fixed-`G` slice have the same `Q=P/G`. Their
difference is `L_S(a_i-a_j)` and is divisible by `Q`. Since
`gcd(Q,L_S)=1`, the polynomial `a_i-a_j` is divisible by `Q`. But

```text
deg(a_i-a_j)<k<=deg(Q).
```

It must vanish, so the members coincide. Hence all middle-band members have
distinct `G_i` and `Q_i`, proving (TB5). QED.
