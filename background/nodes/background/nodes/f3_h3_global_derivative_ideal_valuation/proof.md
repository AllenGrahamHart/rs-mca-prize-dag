# Proof

Write `N=(n-1)^2=deg(Pcal)`.

## Nonvanishing and integral presentation

The proved dyadic shifted-product Sidon theorem says that every root of
`Pcal` in characteristic zero has multiplicity at most two: diagonal
products occur once and off-diagonal products occur twice. Therefore
`Pcal` and its first eighteen Hasse derivatives cannot vanish simultaneously
at any `gamma_uv`. This proves that every `I_uv` is nonzero.

Expanding at `gamma_uv=d_v/c_u` gives

```text
G_uv(U)
 =c_u^N Pcal(gamma_uv+U)
 =sum_j c_u^N Pcal^[j](gamma_uv) U^j.              (1)
```

Hence `D_uv,j=c_u^N Pcal^[j](gamma_uv)`. At dyadic order every
`Norm_K/Q(1-zeta^u)` is a power of two. Multiplication by `c_u^N` therefore
changes neither the odd localization nor the odd ideal norm, proving the
equivalence of `I_uv` and `J_uv` away from two.

## The perfect-power norm

Every Galois automorphism has the form `zeta -> zeta^r` for odd `r`. It sends
`J_uv` to `J_(ru,rv)`, with exponents reduced modulo `n`, so

```text
J_n=product_(u!=v) J_uv
```

is Galois invariant. The only rational prime ramified in the power-of-two
cyclotomic field `K` is two. For an odd rational prime `ell`, the primes of
`O` above `ell` form one Galois orbit, so invariance makes their valuations
in `J_n` equal. Since `ell` is unramified, its exponent in `Norm_O(J_n)` is
that common valuation times the sum of all residue degrees, namely `d`.
Every odd-prime exponent in `E_n` is therefore divisible by `d`, proving
`(GD1)`.

## Rich fibers force valuation

Fix `p=1 mod n`, a generator `g` of `H`, and the degree-one prime

```text
mathfrak P=(p,zeta-g)
```

of `O` above `p`. For one ordered pair `(u,v)`, let `t` be the reduction of
`gamma_uv`, and put `m=P(t)`. Exactly `m` roots of the ordered product
polynomial `Pcal` reduce to `t` at `mathfrak P`.

For a monic split polynomial with root multiset `{r_i}`, the Hasse formula is

```text
Pcal^[j](T)=sum_(|S|=j) product_(i notin S)(T-r_i). (2)
```

At `T=gamma_uv`, every summand in `(2)` retains at least `m-j` of the factors
that vanish modulo `mathfrak P`. Since `c_u` is a unit at this odd prime,
equation `(1)` gives

```text
v_mathfrakP(J_uv)>=max(m-18,0).                    (3)
```

As `(u,v)` ranges over `1<=u,v<n`, `u!=v`, the reduction of `gamma_uv`
ranges over every ordered nonidentity quotient representation exactly once.
Summing `(3)` therefore yields

```text
v_mathfrakP(J_n)
 >=sum_(t!=1)(P(t)-18)_+ R(t)
 =X_18.                                           (4)
```

Because `p=1 mod n`, it splits completely into `d` degree-one primes in
`O`. Galois invariance gives valuation at least `X_18` at each of them, so

```text
p^(d X_18) divides E_n=e_n^d.
```

Dividing prime exponents by `d` proves `(GD2)`. If `p` does not divide
`e_n`, then `(GD2)` forces `X_18=0`. In general
`X_18 log(p)<=log(e_n)`; either displayed size hypothesis in the statement
therefore implies `17X_18<=300n^2`.
