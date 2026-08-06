# Proof

Since `n|p^e-1`, `k=ord_n(p)` divides `e`. In the assumed branch
`p=1 mod 4`, the standard 2-adic order calculation gives
`k=2^(41-e_p)` when `e_p<41`, and `k=1` otherwise. As `e<=6`, only
`k in {1,2,4}` occur, so `D<=2`.

Let `y` have order `2^a`. Two powers `y^u,y^v` are proportional over
`F_p` exactly when `y^(u-v)` lies in `F_p^*`. The intersection of the
dyadic group with `F_p^*` has order `2^min(a,e_p)`, so this is equivalent
to `u=v mod 2^(a-e_p)_+`. This gives the printed class counts.

Inside a class choose `zeta in F_p^*` so its representatives are
`y^i zeta^s`, `0<=s<S`. For each odd exponent `l`, a dual vector obeys

```text
sum_(c,s) eps_(c,s)(y^i_c zeta^s)^l
 = sum_c y^(i_c l) u_c(l),
u_c(l)=sum_s eps_(c,s)(zeta^s)^l in F_p.                       (1)
```

The class representatives in `(1)` are independent over `F_p` when
`D<=2`: the two-class ratio has dyadic order larger than `2^e_p`, and in the
four-class case `1,y^l,y^(2l),y^(3l)` is a basis of the degree-four
extension because `l` is odd. Thus `(1)` vanishes exactly when every
`u_c(l)` vanishes, proving the direct sum.

On a run `l=2b+1,...,2b+2R-1`, each class matrix is a diagonal scaling of

```text
((zeta^(2s))^j)_(0<=j<R,0<=s<S).
```

The points `zeta^(2s)` are distinct, so this is a Vandermonde parity-check
matrix of rank `min(S,R)`. Its kernel is the stated GRS/MDS code. Summing
ranks gives the dimension formula; additivity of Hamming weight across the
direct sum makes the weighted ternary enumerator multiply, giving `Z_1^C`.

Finally, every moment equation has entries in `F_p(mu_n)=F_(p^k)`.
Expanding `|Lambda|` equations in an `F_p` basis gives at most
`k|Lambda|` independent scalar equations, proving `(TRACE)`. Replacing
each evaluation point `x` by `gx` multiplies its `l`-th moment by nonzero
`g^l`, so it does not alter any kernel equation. QED.
