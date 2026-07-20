# Proof

Let `c,d` be the roots of `Y^2-SY+P` in an algebraic closure. Induction in
`(TFR1)` gives

```text
T_j=c^(2^j)+d^(2^j),       P_j=(cd)^(2^j).           (1)
```

At `j=40`, put `x=c^N` and `y=d^N`. The last two equations in `(TFR2)` say

```text
x+y=2,       xy=1.
```

Hence `x,y` are both roots of `(X-1)^2`, so `x=y=1`. The first equation in
`(TFR2)` similarly gives `t^N=1`. Therefore `t,c,d` all lie in `mu_N`.

Because `N` divides `q-1`, the full group `mu_N` lies in `F_q`; in
particular `Y^2-SY+P` splits there. More strongly, choose a generator `g` of
`F_q^*`. Every member of `mu_N` has the form

```text
g^(((q-1)/N)m).
```

The official divisibility `2N | q-1` makes `(q-1)/N` even, so every such
element is a square in `F_q`. This proves the first assertion. Notice that
the distinctness product is still needed: torsion alone permits repeated
roots.

The maximal-field collapse gives `e in {1,2}` and, in the quadratic case,
`p=+/-1 mod N`. For any `x in mu_N`,

```text
x^p=x       if p=1 mod N,
x^p=x^(-1) if p=-1 mod N.                           (2)
```

The same fixedness is automatic when `e=1`. This proves `(TFR3)--(TFR4)`.

In the reciprocal case, apply `(2)` to the four normalized roots. Then

```text
E(z)^p=product_(r in {1,t,c,d})(1-r^(-1)z).          (3)
```

On the other hand,

```text
z^4E(z^(-1))=product_r(z-r)
             =(product_r r) product_r(1-r^(-1)z)
             =E_4 E(z)^p.                           (4)
```

Dividing `(4)` by nonzero `E_4` proves the polynomial identity in `(TFR5)`;
coefficient comparison proves its second form.

Frobenius sends a valid packet to its conjugate. No descent theorem says that
the packet itself is fixed, and inversion of all three normalized parameters
is generally different from the selected-pair orientation involution
`(t,S,P)->(t^(-1),S/t,P/t^2)`. The theorem therefore makes no parity or
exclusion claim. QED.
