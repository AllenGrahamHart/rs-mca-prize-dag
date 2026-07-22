# L1 exact-shell fixed-cofactor prefix transport

- **status:** PROVED
- **role:** separate locator-Q shells from growing-cofactor list interior
- **consumer:** `l1_mixed_petal_amplification`

## Degree gate

Work on an `n`-point domain with locator `Omega`, and represent the received
word by `U` of degree below `n`. Since adding a degree-below-`k` codeword does
not change agreement supports, remove the coefficients of `U` below degree
`k`. If the resulting polynomial is zero, `U` is a codeword and has no exact
agreement shell of size below `n`.

Otherwise put `h=deg U`. For an exact shell of size `a>k`, write

```text
U-P=L_A Q,       deg P<k.                              (FC1)
```

Then necessarily

```text
a<=h,       e:=deg Q=h-a,       lc(Q)=lc(U).           (FC2)
```

Thus every shell above `h` is empty, and the cofactor degree is not an
independent chart parameter.

## Fixed-cofactor transport

Fix `a<=h`, put `w=a-k` and `e=h-a`, and fix a degree-`e` cofactor

```text
Q=q_e Z^e+...+q_0,       q_e=lc(U).
```

For a monic degree-`a` locator

```text
L=Z^a+l_1 Z^(a-1)+...+l_a,
```

the equations `deg(U-QL)<k` determine successively the first

```text
d=min(a,h-k)=min(a,w+e)                               (FC3)
```

nonleading coefficients `l_1,...,l_d`. Hence all exact-shell locators with
this fixed `Q` lie in one depth-`d` locator-prefix fiber. If `e>=k`, then
`d=a`, so there is at most one locator for that `Q`.

There are exactly `q^e` degree-`e` polynomials with prescribed nonzero leading
coefficient. Therefore, writing `N_loc(a,d)` for the maximum size of a
depth-`d` locator-prefix fiber among monic degree-`a` divisors of `Omega`,

```text
|E_a(U)| <= q^e N_loc(a,w+e)       if e<k,             (FC4)
|E_a(U)| <= q^e                    if e>=k.             (FC5)
```

The exactness condition `gcd(Q,L_(H\A))=1` only deletes members of these
fibers.

## Top-shell equality

When `e=0`, `Q=lc(U)` is a nonzero scalar, `d=w`, and there is no complement
gcd restriction. In this case `(FC4)` sharpens to an exact bijection:

```text
E_h(U)
 <-> {monic degree-h divisors L|Omega whose first h-k
      nonleading coefficients equal the recursively prescribed prefix}.  (FC6)
```

For every such `L`, the codeword is `P=U-lc(U)L`; outside the roots of `L`,
the difference is nonzero, so its agreement set is exact.

## Consequence

The top exact shell is literally upstream locator Q, not merely analogous to
it. For `e<k`, every fixed cofactor contributes one depth-`w+e` locator
prefix fiber and there are `q^e` possible cofactors. This is an exact union
statement, not yet a budget verdict. The proved
`l1_cofactor_depth_budget_cancellation` shows that `q^e` cancels against the
`e` additional equations under an ambient-normalized deeper-prefix bound,
but remains as the effective-image collapse/rounding penalty under ordinary
image normalization. At the deployed rows that sparse-image obstruction
appears after one or two extra coordinates. The follow-on
`l1_cofactor_prefix_pade_graph_normal_form` proves that these `q^e` targets
are distinct and form one codimension-`w` reciprocal-series graph.

This theorem does not prove row-sharp locator Q, a depth-uniform transport,
or divisor/graph transversality. The `e>=k` range is represented, but not
bounded, by `l1_full_locator_pade_section_all_cofactors`.
