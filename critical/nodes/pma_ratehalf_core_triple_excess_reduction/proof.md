# Proof - PMA rate-half core triple-excess reduction

## 1. The core Reed-Solomon list

Normalize by subtracting one planted source codeword, so the received word is
zero on the core. All contributors for the fixed touched triple have the same
received values on its `3ell` points. Interpolation supplies their unique
degree-`<3ell` polynomial `P_*`.

For a contributor `P`, the difference `P-P_*` vanishes on those `3ell`
distinct points and is therefore divisible by `L=L_1L_2L_3`. Since
`deg P<=k-1=N` and `deg P_*<3ell`,

```text
P=P_*+LH,       deg H<=N-3ell=ell+b-2=K_0-1.
```

The quotient is unique. Conversely every such `H` gives a degree-at-most-`N`
polynomial with the fixed three-petal values, although the remaining PMA
guards can only reduce this ambient list.

The core and petals are disjoint, so `L(x)!=0` on `C`. Core agreement is

```text
P(x)=0
iff P_*(x)+L(x)H(x)=0
iff H(x)=-P_*(x)/L(x)=y(x).
```

An exact defect `d` misses `d` of the `N` core points and therefore gives
`m=N-d`. Substitution of `N=4ell+b-2` and `d=2ell-a` proves (CT2).

Finally,

```text
m^2-N(K_0-1)
 =(2ell+b+a-2)^2-(4ell+b-2)(ell+b-2)
 =ell(4a-b+2)+a^2+2ab-4a,
```

which is the projective-Johnson denominator from the preceding packet. Hence
the nonpositive-J tail is exactly the beyond-Johnson part of this core list,
not an arithmetic mismatch between the two reductions.

## 2. Three-codeword equality bonus

Fix three distinct `H_i` and one core word `y`. At a point `x`, at most one
of the `H_i` can agree with `y` if their three values are distinct, at most
two can agree if exactly one pair is equal, and at most three can agree if all
values are equal.

The all-equal set is `T`. Outside `T`, the three exact-pair sets are
`E_12,E_13,E_23`; they are pairwise disjoint. Summing the pointwise maximum
number of agreements gives

```text
sum_i |{x in C:H_i(x)=y(x)}| <= N+B_3.          (1)
```

If every list member has at least `m` agreements, (1) gives `B_3>=3m-N`.
The source arithmetic is

```text
3m-N
 =3(2ell+b+a-2)-(4ell+b-2)
 =2ell+2b+3a-4
 =2(K_0-1)+3a,
```

proving (CT5). The term `2(K_0-1)` is the unavoidable common-factor
baseline: three scalar multiples of one degree-`K_0-1` polynomial already
have that equality bonus. The tail forces a strict excess of `3a` above it.

## 3. The reduced three-fiber witness

Let `G=gcd(A,B)` and write `A=GA_0`, `B=GB_0`. The reduced polynomials are
coprime. The roots of `G` in the core are exactly `T`. On `C\T`,

```text
E_12={A_0=0},
E_13={B_0=0},
E_23={A_0/B_0=1}.
```

These are the disjoint `0`, `infinity`, and `1` fibers of `phi=A_0/B_0`.
The map is nonconstant: otherwise all equality outside `T` disappears and
`B_3=2|T|<=2 deg G<=2(K_0-1)`, contradicting (CT5).

Put `g=deg G` and `r=max(deg A_0,deg B_0)`. Since `deg A,deg B<=K_0-1`,
one has `g+r<=K_0-1`, while `|T|<=g`. If `S` is the union of the three
displayed fibers, then (CT5) gives

```text
|S|=B_3-2|T|
 >=2(K_0-1)+3a-2|T|
 >=2r+3a.
```

Each fiber has at most `r` distinct points, so `3r>=|S|>=2r+3a` and
`r>=3a`. This proves (CT6).

If no certificate (CT6) exists, a fixed `(a,touched triple)` list has size at
most two. There are four touched triples and fewer than `n` possible defects,
so the complete three-petal tail is then at most `8n` per source.

## 4. Why source coupling remains

The reduction uses a special received core word:

```text
y=-P_*/(L_1L_2L_3),
```

where `P_*` is the CRT interpolation of the three planted petal labels.
Arbitrary Reed-Solomon words can have positive three-fiber excess even on a
smooth multiplicative domain. The verifier constructs one at the first tail
arithmetic row by taking three degree-16 polynomials whose pair differences
share a degree-13 factor and whose reduced differences have three disjoint
split cubic fibers. It attains

```text
B_3=35=2(17-1)+3,
```

and gives three words with `28` agreements on a 49-point core. Its parameters
have `J=0`, so it lies in the actual nonpositive-denominator tail. The fixture
is constructed without imposing the displayed PMA rational-word constraint,
and no source lift is supplied or certified. It therefore does not refute the
consumer. It proves that a closure must use that coupling or a legitimate
natural-scale owner.
