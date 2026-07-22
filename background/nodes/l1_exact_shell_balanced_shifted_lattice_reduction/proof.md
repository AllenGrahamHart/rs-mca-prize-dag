# Proof - L1 exact-shell balanced shifted-lattice reduction

## 1. Module and census

Every `(W,N) in M_U` has

```text
N=W Uhat-C Omega
```

for some polynomial `C`.  Hence `(1,Uhat),(0,Omega)` is a basis.  Its
determinant is `Omega`, of shifted degree `n-k+1`; the predictable-degree
theorem for a shifted weak-Popov basis gives `(BL2)`.

Let `T` be an `m`-support on which `U` agrees with a degree-below-`k`
polynomial `P`, and put `W=Omega/L_T`, `N=WP`.  Then `(W,N) in M_U`, `W` is
monic of degree `omega`, and `sdeg(W,N)<=omega`.

Conversely, let `W|Omega` be monic, split, squarefree, and of degree
`omega`, with `(W,N) in M_U` and `sdeg(W,N)<=omega`.  At every root of `W`,
the module congruence gives `N=0`; squarefreeness gives `W|N`.  Write `N=WP`.
The shifted cap gives `deg P<k`.  At every point outside the roots of `W`,
the congruence can be divided by `W`, so `P=U`.  These constructions are
inverse and prove the census description.

## 2. Low minimal degree

Suppose `d_1<=w`.  From `(BL2)`,

```text
d_2>=n-k+1-w=omega+1.                               (1)
```

Predictable degrees imply that every module element of shifted degree at
most `omega` is a polynomial multiple of `g_1`.

If no such multiple has a monic split first coordinate of degree `omega`,
the census is empty.  Otherwise the standard cancellation argument gives
`deg W_1=d_1`, `W_1` split and squarefree up to scaling, and `W_1|N_1`.
Put `P_0=N_1/W_1`; its degree is below `k`.  The module identity shows that
`P_0` agrees with `U` outside the `d_1` roots of `W_1`.  Minimality of `d_1`
shows that it agrees nowhere else: a smaller disagreement locator would be a
nonzero module element of shifted degree below `d_1`.  Thus its agreement
size is exactly `n-d_1`.

It is unique.  Two codewords each differing from `U` in at most `w`
positions would differ in at most `2w` positions.  From `(BL3)`,

```text
2w=2m-2k<=n-k-1<n-k+1,
```

contradicting the Reed--Solomon minimum distance unless they are equal.
Every census element is a multiple of `g_1`, so its support is precisely an
`m`-subset of the `n-d_1` agreement points of `P_0`; every such subset gives
one element.  This proves the first equality in `(BL4)`.

Finally, `(BL3)` and `d_1<=w` give

```text
n-d_1>=n-w>=m+1.                                    (2)
```

Therefore the sole explaining codeword never has complete agreement size
`m`.  By the support-moment inversion, or directly by the complement gcd
guard, the exact level-`m` shell is empty.

## 3. Balanced parameterization

If the exact shell is nonempty, the previous part forces `d_1>=w+1`.
A census element has shifted degree `omega`, so `d_1<=omega`.  Since
`d_2=omega+w+1-d_1`, the same inequalities give `d_2<=omega`; this proves
`(BL5)`.

Predictable degrees now say that every element of shifted degree at most
`omega` is uniquely `Ag_1+Bg_2` with the caps `(BL6)`.  The number of scalar
coefficient slots is

```text
(omega-d_1+1)+(omega-d_2+1)
=2omega+2-(omega+w+1)=omega-w+1,
```

proving `(BL7)`.  The census description from section 1 imposes monicity,
exact degree, and `W|Omega`.

For the guard, the module identity and `N=WP` give

```text
W(Uhat-P)=C Omega=CWL,       L=Omega/W.
```

Cancellation yields `Uhat-P=LC`; thus `C=Q` is the agreement cofactor.
The roots of `W` are exactly the complement of the chosen `m`-support.
That support is complete precisely when `Q` has no root in the complement,
which is `(BL8)`.
