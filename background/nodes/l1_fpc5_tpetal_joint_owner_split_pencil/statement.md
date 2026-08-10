# Joint-owner split-pencil reduction

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix one nonempty full-petal cell, one exact primitive monic anchor `(F,W)`,
and one distinct exact primitive monic candidate `(G,B)`. Put

```text
Lambda=product_i L_i,       r=2d-deg Lambda,
H=(F B-G W)/Lambda.                                  (SP1)
```

Let `R_0` be the anchor background zero set and define the exact joint owner

```text
D=gcd(F,G),       E=gcd(B,L_(R_0)),
Q=gcd(H,F L_(R_0))=D E,       q=deg Q.               (SP2)
```

The core and background are disjoint, so `D` and `E` are coprime. Define

```text
A=F/D,       C=G/D,       U=W/E,       V=B/E,
K=H/(D E).                                             (SP3)
```

These divisions are exact and the original determinant identity cancels to

```text
A V-C U=Lambda K,       0<=deg K<=r-q.                (SP4)
```

Here `K` is nonzero. The polynomials `A,C` are monic squarefree split
locators on the core,

```text
gcd(A,C)=gcd(A,U)=gcd(C,V)=1.                         (SP5)
```

For every touched petal with value `c_i`, the reduced columns retain the
exact congruences

```text
E U == c_i D A (mod L_i),
E V == c_i D C (mod L_i).                             (SP6)
```

Since `D` and `E` are units modulo every `L_i`, these are equivalently

```text
U == c_i D E^(-1) A (mod L_i),
V == c_i D E^(-1) C (mod L_i).                        (SP7)
```

Thus an exact owner of co-deficiency `c=r-q` produces a primitive
determinantal representation with a nonzero tail of degree at most `c`.

There is also an exact collective coordinate inside each fixed owner
chamber. Fix one member `(C_0,V_0,K_0)`. Every other member satisfies, for a
unique polynomial `T`,

```text
K_0 C-K C_0=A T,       K_0 V-K V_0=U T,
deg K<=c,               deg T<=c.                    (SP8)
```

Hence the chamber injects into bounded-degree coefficient pairs `(K,T)` in
one two-generator rational pencil. At top ownership `q=r`, `K,K_0,T` are
constants. Monicity of `A,C,C_0` then gives, with
`lambda=K/K_0`,

```text
(C,V)=lambda(C_0,V_0)+(1-lambda)(A,U),
lambda is a nonzero field scalar with lambda!=1,
A V-C U=K Lambda.                                  (SP9)
```

Thus the top-owner chamber is an ordinary affine pencil of primitive
locators split on the core, coupled to a nonzero scalar determinantal
representation of the disjoint touched-petal locator.

In particular, at top ownership `q=r`,

```text
A V-C U=gamma Lambda,       gamma is a nonzero field scalar. (SP10)
```

For fixed canonical owner `Q`, the reduction is injective: `H=QK` and the
anchor Pade chart reconstructs the unique original pair.

## Scope

This is a dual-domain pencil. Its natural determinant parent is the
touched-petal locator `Lambda`, while `A,C,C_0` split on the disjoint core.
It is therefore not a direct instance of a census in which the varying
locator divides the determinant parent. The theorem is a forward reduction
and does not assert that every reduced representation lifts to an exact
guarded FPC5 candidate. It does not count representations, aggregate
distinct owners, pay the remaining background-root equations, provide
first-owner chronology, or pay a source cell.
