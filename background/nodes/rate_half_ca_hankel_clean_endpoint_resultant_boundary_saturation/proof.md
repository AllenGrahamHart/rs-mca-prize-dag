# Proof

The clean domain complement is

```text
Q V+P W=H,                                           (1)
```

where `H` is monic of degree `T`, `deg_z Q=m`,
`deg_z V<=3m+1`, and `deg_z W<=T`. Suppose `deg_z W<T`. The degree-`T`
coefficient of `(1)` would then read

```text
q_inf nu=1
```

for some polynomial `nu in Fbar[X]`. This is impossible because
`deg_X q_inf=rho>0`. Thus `deg_z W=T`. Taking the degree-`T` coefficient in
`(1)` gives

```text
q_inf nu+P omega=1.                                  (2)
```

Neither `nu` nor `omega` can vanish, so `deg_z V=3m+1` as well. Equation
`(2)` proves both coprimality assertions in `(RBS2)`.

The preceding gate proves

```text
deg_z K=T+b-m.
```

Take the highest parameter coefficient in

```text
W B-(X-x_0)=Q K.
```

This gives `omega beta=q_inf kappa`. Since `(2)` makes `omega` coprime to
`q_inf`, Euclid's lemma gives `q_inf|beta`, proving `(RBS4)`.

It remains to sharpen the resultants. Let `alpha` be any root of `q_inf`.
The coordinate choice in the unit-resultant gate makes `q_inf(x_0)!=0`, so
`alpha!=x_0`. It also places parameter infinity outside every root of
`Q(-;x)` for `x in D`, hence `P(alpha)!=0`. Equation `(2)` gives

```text
omega(alpha)=P(alpha)^(-1)!=0.                       (3)
```

At `X=alpha`, the projective parameter specializations of `Q` and `W` do
not share their point at infinity by `(3)`. They cannot share a finite
parameter root either: at such a root the weld would give
`0=alpha-x_0`, contrary to `alpha!=x_0`. Therefore

```text
Res_z(Q,W)(alpha)!=0.                                (4)
```

The preceding gate writes the two resultants as powers of `X-x_0` times
factors whose product is `q_inf^(T+b)`. Equation `(4)` makes the `W` factor
coprime to `q_inf`; unique factorization gives exactly `(RBS5)` after
absorbing constants.

Put `d_B=deg_X B<=N`. A resultant of a degree-`m` polynomial with
`X`-coefficient degree at most `rho` and a degree-`b` polynomial with
`X`-coefficient degree at most `d_B` satisfies

```text
deg_X Res_z(Q,B)<=b rho+m d_B.                       (5)
```

On the other hand `(RBS5)`, `gcd(q_inf,X-x_0)=1`, and
`deg_X q_inf=rho` give

```text
deg_X Res_z(Q,B)=(T+b)rho+1.                         (6)
```

Comparing `(5)` and `(6)` yields

```text
m d_B>=T rho+1
       =(4m+1)(4m-1)+1
       =16m^2=mN.
```

Thus `d_B>=N`; the existing upper bound forces `d_B=N`. QED.
