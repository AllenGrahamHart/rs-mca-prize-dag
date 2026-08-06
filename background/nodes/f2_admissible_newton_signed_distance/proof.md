# Proof

The plus-branch admissible direct-sum theorem identifies each class, after a
harmless nonzero coordinate scaling of the moment equations, with the half-system
`zeta^s`, `0<=s<S`, where `zeta` has exact order `2S` in `F_p^*`.
In particular,

```text
2S divides p-1,  so p>=2S+1>S.                         (1)
```

Let `eps` be a nonzero ternary class-kernel word of weight `w`, with
distinct support indices `e_1,...,e_w` and nonzero signs `s_i`.  Form the
reduced signed polynomial

```text
P(X)=sum_(i=1)^w s_i X^e_i.
```

The first `R` odd moment equations say exactly

```text
P(zeta^(2j-1))=0,  j=1,...,R.                         (2)
```

If `w<=2R`, equations `(1)` and `(2)` meet every hypothesis of the proved
DLI Newton short-window exclusion with `N=S` and `ell=R`: the exponents are
distinct in `{0,...,S-1}`, the coefficients are signs, and
`char(F_p)=p>w`.  That theorem says no such reduced signed polynomial
exists.  Hence `w>=2R+1`; if `2R>=S`, no nonzero word can exist at all.
The displayed form of `Z_1` follows by separating its zero word. QED.
