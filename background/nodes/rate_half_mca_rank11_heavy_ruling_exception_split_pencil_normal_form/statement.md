# Heavy-ruling exception split-pencil normal form

- **status:** PROVED
- **scope:** the rational output of the core-saturated triple-owner packet

Let `H_0` be the residual anchor pair core and put

```text
e=m'-|H_0|.
```

Then `1<=e<=11`. For at least 20 distinct anchor slopes, the exact support
has the unique form

```text
S_gamma'=H_0 disjoint_union E_gamma,       |E_gamma|=e,
```

and the `E_gamma` are pairwise disjoint. Let `L_0` and `L_{E_gamma}` be the
corresponding monic locators. The rational certificate admits the exact
factorization

```text
A'-Q a_0'=L_0 u,
B'-Q b_0'=L_0 v,
u+gamma v=(c_0+c_1 gamma)L_(E_gamma).                (SPI11)
```

It satisfies

```text
deg u,deg v<=e,        max(deg u,deg v)=e,
gcd(u,v)=1,
c_0+c_1 gamma !=0     on every anchor slope,
gcd(Q,L_0)=1.
```

Every `L_{E_gamma}` is a split squarefree degree-`e` divisor of the residual
domain locator, and these locators are pairwise coprime. Thus `(SPI11)` is an
exact degree-`1..11` split pencil with at least 20 disjoint split fibers,
separated from the rational denominator on the anchor core.

No count or classification of such pencils is claimed.
