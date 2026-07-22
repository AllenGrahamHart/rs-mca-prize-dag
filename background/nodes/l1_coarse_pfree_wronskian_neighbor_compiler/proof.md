# Proof - L1 coarse p-free Wronskian neighbor compiler

## 1. Degree and support

The Wronskian supplier gives equality of all moments through depth `d`, the
upper degree in `(WNC2)`, and nonvanishing. The tame-tail distance supplier
upgrades the collision endpoint from `tau_0` to `tau_p`.

At a root `x` of `F_X`,

```text
W_(X,Y)(x)=F_X'(x)F_Y(x) !=0,
```

because `F_X` is squarefree and `X,Y` are disjoint. Similarly, at a root
`y` of `F_Y`,

```text
W_(X,Y)(y)=-F_X(y)F_Y'(y) !=0.                       (1)
```

Thus the certificate has full support on `X union Y`.

## 2. Fixed-X injectivity

Suppose two monic degree-`t` polynomials `G_1,G_2` give the same Wronskian
with `F_X`. Put `H=G_1-G_2`, so `deg H<t`. Subtraction gives

```text
F_X'H-F_XH'=0.                                       (2)
```

Modulo `F_X`, equation `(2)` says `F_X'H=0`. Since `F_X` is squarefree,
`gcd(F_X,F_X')=1`, so `F_X|H`. The degree bound forces `H=0`. Hence
`G_1=G_2`, proving the unique-certificate claim in every characteristic.

## 3. Exact certificate census

Let `V_D` be the `D+1` dimensional space of polynomials of degree at most
`D`. Inclusion-exclusion over the `t` forbidden zero coordinates gives

```text
sum_(j=0)^t (-1)^j binom(t,j) q^max(D+1-j,0).        (3)
```

Indeed, vanishing on `j<=D` specified points leaves dimension `D+1-j`,
while vanishing on at least `D+1` points leaves only the zero polynomial.
This proves `(WNC3)`.

For fixed `X`, injectivity and `(1)` bound the possible `Y` by
`R_q(t,D_t)`. Independently, `Y` is a `t`-subset of `H\A`, giving the other
term in `(WNC4)`. There are `binom(a,t)` choices for `X`. Distinct neighbors
have one well-defined `t` and `X`, so summing and adding the anchor `A`
proves `(WNC5)`.

## 4. Parity

If `d=2u`, then `tau_0=u+1`; substituting `t=tau_0+j` gives `D_t=2j`. If
`d=2u+1`, then `tau_0=u+2` and `D_t=2j+1`. For `D=0`, every nonzero constant
is full-support, so `R_q(t,0)=q-1`. For `D=1<t`, formula `(3)` gives

```text
R_q(t,1)=q^2-1-t(q-1)=(q-1)(q+1-t),
```

proving `(WNC6)--(WNC7)`.

The tame-tail supplier removes every formal stratum with
`j<tau_p-tau_0`; this changes the lower endpoint of `(WNC5)`, not the parity
identity.
