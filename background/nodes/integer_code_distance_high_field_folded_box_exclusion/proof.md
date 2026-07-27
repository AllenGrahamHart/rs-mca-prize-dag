# Proof

Let `omega` be a complex primitive `128`th root of unity. Fold a ternary
vector `v` across antipodes by putting

```text
w_i=v_i-v_(i+64),       0<=i<64,
W(X)=sum_(i=0)^63 w_i X^i.                            (1)
```

Since `zeta^(i+64)=-zeta^i`, the kernel equation for `v` is `W(zeta)=0`.
Every `w_i` lies in `{-2,-1,0,1,2}`. If `w` is nonzero, then
`W(omega)` is nonzero because `deg W<64=deg Phi_128` and
`Phi_128=X^64+1`.

By the collision-norm criterion, `W(zeta)=0` forces the odd prime `p` to
divide the nonzero integer

```text
N(W)=Norm_(Q(omega)/Q)(W(omega)).                     (2)
```

Put `S=sum_i w_i^2`. Orthogonality over the 64 odd residues modulo 128 gives

```text
sum_(u mod 128, u odd) |W(omega^u)|^2=64S.
```

Arithmetic-geometric mean applied to these 64 squared absolute values yields

```text
|N(W)|<=S^32.                                         (3)
```

There are two exhaustive cases.

1. Some `w_i` is odd. The other 63 squares are at most four and that odd
   square is at most one, so `S<=63*4+1=253`. Equations `(HFB1)` and `(3)`
   give `0<|N(W)|<p`, contradicting `(2)`.

2. Every `w_i` is even. Write `W=2B`, where the 64 coefficients of `B` lie
   in `{-1,0,1}`. If `w` is nonzero, so is `B(omega)`. Applying the same
   argument with `T=sum_i (w_i/2)^2<=64` gives

   ```text
   |N(B)|<=64^32<253^32<p.
   ```

   But `N(W)=2^64 N(B)`. Since `p` is odd, `(2)` would force `p|N(B)`, again
   impossible.

Therefore `w=0`. By `(1)`, this is exactly
`v_i=v_(i+64)` for every `i`, which is the antipodal relation module in
`(HFB2)`. Conversely every such vector is in the kernel because
`zeta^(i+64)=-zeta^i`. This proves equality and the theorem. QED.
