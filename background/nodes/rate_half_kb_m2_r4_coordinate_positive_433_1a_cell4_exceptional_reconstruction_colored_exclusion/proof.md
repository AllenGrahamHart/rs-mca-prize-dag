# Proof

Write `D_j=A_2(w_j)`, `N_j=A_0(w_j)`, and
`Q_j=z_jB_1(w_j)`.  The necessary signed-pair equations are

```text
N_1D_0+N_0D_1=0,
Q_0^2D_1^2-Q_1^2D_0^2-4N_0D_0D_1^2=0.          (1)
```

If `x=Q_1D_0-Q_0D_1` vanished, the first two square terms in the second
equation would agree.  Since `4D_0D_1` is invertible, `(1)` would give
`N_0=0`, contradicting the nonzero `DE+` product and denominator guards.
Thus `x!=0` on every actual packet.

For a third squared label `w2`, direct specialization of the proved
target-free compiler gives the necessary equations

```text
2N_2D_0D_1-bD_2x=0,
(b^2D_2+N_2)^2-b^2w2 B_1(w2)^2=0.               (2)
```

The second row follows from the unsquared colored equation by elimination
and squaring, so it may add points but cannot remove an actual realization.
The exact `w2` resultant of `(2)` is plane-reduced fifteen times.  Removing
only univariate content gives a primitive polynomial of degrees
`(4,8,8,3,300)` in `(x,w1,w0,b,t)` with `177540` terms.

Coefficientwise pseudo-reduction modulo `H` and the generic linear `b` lift
takes 22 and 3 steps.  The primitive remainder has `16368` terms, and every
monomial has `x`-degree exactly four.  Dividing by `x^4` gives `C`.  The
removed coefficient content is factored exactly.  Its only admissible linear
roots are the two values in `(KBC4HX-3)`; its quadratic and cubic factors
have no base-field roots.

The exact resultant `E=Res_w0(H,C)` is nonzero.  Modular exponentiation in
`F_p[t]/(E)` followed by `gcd(E,t^p-t)` proves that its complete deployed
root set has size fifteen.  Specializing `H` and `C` at all fifteen roots,
factoring their gcd in `w0`, reconstructing `b`, and intersecting the two
polynomials in `(1)` gives the sealed finite atlas.  The five guard roots are
discarded.  On the generic lift, exactly four `(t,w0,b)` rows reach the pair
gcd, and all have `D_0=0`; their eight displayed `w1` roots also have
`D_1=0`.  At the two admissible content roots, direct factorization of `H`
before any division gives no linear `w0` factor.

It remains to justify every scale used above.  Replaying the exact
pseudo-Euclidean construction recovers six scales with shapes

```text
H lead             (0,0,8),
first lead          (7,0,197),
quadratic content   (0,0,182),
quadratic lead      (7,0,276),
linear content      (0,0,179),
A                    (7,0,688).                  (3)
```

For each scale `S`, compute `Res_w0(H,S)`, intersect it with `t^p-t`, and
specialize `gcd(H,S)` at every resulting `t`.  The union consists of 19
deployed `(t,w0)` points.  At each point the calculation starts over from
the original `P,L,M,F`, takes their univariate gcd in `b`, and then replays
`(1)`.  Every non-guard point either has no linear `b` factor or has
`D_0=0`.  Hence no quotient-leading, content, or `A=0` exception survives.

The preceding projection theorem already excluded the residual away from
`H`.  Therefore no admissible point of `L=M=0` carries the necessary colored
signed family.  Source root-sign symmetry transports the exclusion from cell
4 to cell 7. QED.
