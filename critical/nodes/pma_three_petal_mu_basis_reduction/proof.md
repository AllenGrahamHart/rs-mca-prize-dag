# Proof - PMA three-petal mu-basis reduction

Write `R=K[X]` and use `deg_vec` for the maximum degree of the three
coordinates of a nonzero polynomial vector.

## 1. The syzygy dictionary

For `(F,W) in V_s`, put

```text
A_i=(W-c_iF)/L_i.
```

The numerator has degree at most `d=ell+s`, so `deg A_i<=s`. Set

```text
alpha_1=c_2-c_3,
alpha_2=c_3-c_1,
alpha_3=c_1-c_2.
```

The labels are distinct, so every `alpha_i` is nonzero. Also

```text
sum_i alpha_i=0,       sum_i alpha_i c_i=0.
```

It follows that

```text
sum_i L_i(alpha_iA_i)
 = sum_i alpha_i(W-c_iF)=0.
```

This gives a linear map `V_s -> Syz(L)_<=s`.

Conversely, let `B=(B_1,B_2,B_3)` be a syzygy of vector degree at most `s`,
put `A_i=B_i/alpha_i`, and set `G_i=L_iA_i`. Define

```text
F=(G_1-G_2)/(c_2-c_1),       W=G_1+c_1F.
```

The syzygy relation is

```text
(c_2-c_3)G_1+(c_3-c_1)G_2+(c_1-c_2)G_3=0.
```

Solving it for `G_3` gives `G_3=W-c_3F`; the first two identities hold by
construction. Since `deg G_i<=ell+s=d`, both `F` and `W` have degree at most
`d`. The two constructions are inverse. This proves the dictionary and (TP).

## 2. A reduced basis over `K[X]`

Because `gcd(L_1,L_2,L_3)=1`, the row map

```text
R^3 -> R,       B -> sum_i L_iB_i
```

is split surjective. Its kernel is therefore a free `R`-module of rank two.
Choose a basis `p,q`, ordered by

```text
mu=deg_vec(p)<=nu=deg_vec(q),
```

for which `mu+nu` is minimal.

The leading coefficient vectors of `p` and `q` are independent. Otherwise,
after scaling one could replace

```text
q by q-lambda X^(nu-mu)p
```

and lower its vector degree. This is a unimodular basis change and contradicts
minimality.

The independence gives the predictable-degree identity

```text
deg_vec(up+vq)=max(deg u+mu,deg v+nu).
```

Indeed, if the two displayed degrees differ, the larger leading term cannot
cancel. If they agree, cancellation would give a nontrivial dependence
between the two leading coefficient vectors.

Take the cross product `r=p x q`. Over the fraction field, both `r` and
`(L_1,L_2,L_3)` span the one-dimensional orthogonal complement of `p,q`, so

```text
r=h(L_1,L_2,L_3)
```

for some rational function `h`. A Bezout identity for the `L_i` shows that
`h` is in `R`.

In fact `h` is a unit. If an irreducible polynomial `pi` divided `h`, then
`p,q` would be dependent modulo `pi`. Lift a nonzero dependence to
`a,b in R`, not both divisible by `pi`. The vector

```text
z=(ap+bq)/pi
```

would be a polynomial syzygy. Expanding `z` in the basis `p,q` and using
uniqueness of coordinates would force both `a` and `b` to be divisible by
`pi`, a contradiction.

The independent leading vectors make `deg_vec(p x q)=mu+nu`. Since `h` is a
unit and every `L_i` has degree `ell`, the right side has vector degree
`ell`. Therefore

```text
mu+nu=ell.
```

After ordering, `mu<=floor(ell/2)` and `nu=ell-mu`. The predictable-degree
identity now shows that a syzygy has vector degree at most `s` exactly when

```text
deg u<=s-mu,       deg v<=s-nu.
```

Counting coefficients proves (HF). The least vector degree of a nonzero
syzygy is `mu`, so `mu` is basis-independent.

## 3. Saturation forces balance

Let `(F,W)` satisfy (SAT), and let `B` be its syzygy. The vector degree of
`B` is exactly `s`: if it were smaller, then every `G_i=L_iA_i` would have
degree at most `d-1`, and the reconstruction formulas would give
`deg F,deg W<=d-1`, contradicting `deg F=d`.

Suppose first that `s<nu`. Then the `q` term is unavailable and

```text
B=up,       deg u=s-mu.
```

If `mu<s`, the polynomial `u` is nonconstant and divides all three `B_i`,
hence all three `G_i`. The reconstruction formulas then show that `u` divides
both `F` and `W`, contradicting `gcd(F,W)=1`. Thus `mu=s`.

If `s>=nu=ell-mu`, then `mu>=ell-s`. This proves (BAL). Since
`mu<=ell/2`, the first alternative is forced when `s<ell/2`; when
`s>=ell/2`, the second alternative holds. Substitution in (HF) gives

```text
dim_K V_s=max(1,2s-ell+2).
```

In the upper-half branch, the coefficient bounds follow directly from (PB),
and their sum is `2s-ell=e-1`.

Finally, let `G_i=W-c_iF`. A common divisor of `G_i` and `G_j` divides

```text
G_i-G_j=(c_j-c_i)F.
```

It therefore divides `F`, and then also `W=G_i+c_iF`. Saturation makes that
divisor a unit. No `G_i` is zero, because `G_i=0` would give `W=c_iF` while
`deg F=d>=1`, again contradicting saturation. Thus the three `G_i` are
nonzero and pairwise coprime.

## 4. The determinant identity

Let the inverse syzygy dictionary send `p,q` to `(F_p,W_p)` and
`(F_q,W_q)`. Write `A_i^p=p_i/alpha_i` and similarly for `q`. For distinct
indices `i,j`, direct expansion gives

```text
(W_p-c_iF_p)(W_q-c_jF_q)
 -(W_q-c_iF_q)(W_p-c_jF_p)
 =(c_j-c_i)(F_pW_q-F_qW_p).             (1)
```

The left side is

```text
L_iL_j(A_i^pA_j^q-A_i^qA_j^p).
```

In the reduced-basis proof, `p x q=k(L_1,L_2,L_3)` for a unit `k`. Hence
the parenthesized minor is a nonzero scalar times the remaining locator
`L_k`. Equation (1) proves (DET).

The syzygy basis and the linear dictionary give the unique representation

```text
(F,W)=u(F_p,W_p)+v(F_q,W_q).
```

If a nonconstant polynomial divides both `u` and `v`, it divides both `F`
and `W`. Conversely, suppose `gcd(u,v)=1` and a polynomial `H` divides
`F,W`. The two determinant combinations show that

```text
H | u(F_pW_q-F_qW_p),
H | v(F_pW_q-F_qW_p).
```

Bezout for `u,v` gives `H | L_1L_2L_3`. If
`gcd(F,L_1L_2L_3)=1`, then `H` is a unit. This proves (PRIM).

## 5. PMA specialization

Three disjoint full petals have pairwise-coprime monic degree-`ell` locators.
The exact-defect PMA reduction supplies distinct source labels, `deg F=d`,
and `gcd(F,W)=1`. The theorem therefore applies to each of the four touched
triples in an `M=4,t=3` carried chart. It identifies the exact remaining
coefficient family. Since the core and petals are disjoint, its saturation
condition is exactly primitivity of `(u,v)`. The theorem still supplies no
growing-`e` count of primitive pairs for which `uF_p+vF_q` is a split core
divisor, so the critical target remains open.
