# PMA rate-half core triple-excess reduction

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **role:** exact reduction of the nonpositive-J `M=4,t=3` tail

## Statement

Work over a field `K`. Consider a normalized rate-half maximal source with

```text
|C|=N=k-1=4ell+b-2,       0<=b<ell,
```

and fix three touched full petals with pairwise-coprime locators
`L_1,L_2,L_3` of degree `ell`. Put `L=L_1L_2L_3`. Let `P_*` be the unique
polynomial of degree less than `3ell` having the received values on those
three petals, and define on the core

```text
y(x)=-P_*(x)/L(x).
```

Every normalized degree-`<k` codeword `P` agreeing on all three petals has a
unique representation

```text
P=P_*+LH,       deg H<=K_0-1,       K_0=ell+b-1.       (CT1)
```

Core agreement of `P` at `x` is equivalent to `H(x)=y(x)`. Consequently an
exact defect

```text
d=2ell-a
```

has core agreement

```text
m=N-d=2ell+b+a-2.                              (CT2)
```

Thus one fixed touched triple injects into one ordinary
`RS[K,C,K_0]` list at agreement `m`. Its Johnson denominator is exactly

```text
m^2-N(K_0-1)
 =ell(4a-b+2)+a^2+2ab-4a.                      (CT3)
```

For three distinct polynomials `H_1,H_2,H_3` of degree at most `K_0-1`, put

```text
A=H_1-H_2,       B=H_1-H_3,
T=Z_C(A) intersect Z_C(B),
E_12=Z_C(A)\T,
E_13=Z_C(B)\T,
E_23=Z_C(B-A)\T,
B_3=2|T|+|E_12|+|E_13|+|E_23|.                 (CT4)
```

If all three agree with one word on at least `m` core points, then

```text
B_3>=3m-N=2(K_0-1)+3a.                         (CT5)
```

Let `G=gcd(A,B)`, `A=GA_0`, and `B=GB_0`. The three sets outside `T` are
the disjoint `0`, `infinity`, and `1` fibers of the nonconstant rational map

```text
phi=A_0/B_0.
```

If `r=max(deg A_0,deg B_0)`, then (CT5) implies

```text
|phi^-1({0,1,infinity}) intersect (C\T)| >= 2r+3a.    (CT6)
```

In particular `r>=3a`. Therefore a fixed tail cell contains at most two
contributors unless the source-coupled core admits the explicit positive
three-fiber excess certificate (CT6). If no such certificate exists for the
core at any `a>=1`, all four touched triples and all tail defects contribute
at most `8n` codewords per carried source.

## Scope

This theorem does not assert that every smooth core has the required
order-three property. A smooth order-100 fixture at the first `J=0` tail row
already realizes equality in (CT5) for
`(ell,b,a,N,K_0,m)=(11,7,1,49,17,28)`. Its received word is chosen as an
arbitrary core word; no rational-word source lift is supplied or certified.
It is therefore a route cut rather than a PMA counterexample. The remaining target is the
source-coupled positive three-fiber excess, not another pairwise Johnson
bound.
