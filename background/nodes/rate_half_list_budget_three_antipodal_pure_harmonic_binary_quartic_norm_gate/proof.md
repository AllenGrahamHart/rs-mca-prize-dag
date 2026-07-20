# Proof

For a binary quartic

```text
aX^4+bX^3Y+cX^2Y^2+dXY^3+eY^4,
```

the classical cubic invariant in the coefficient convention used here is

```text
72ace+9bcd-27ad^2-27b^2e-2c^3.                            (1)
```

Substitution of `(a,b,c,d,e)=(1,-s_1,s_2,-s_3,s_4)` gives
`(BQN1)`.

Suppose first that the four roots are distinct. A projective change of
variable sends them to the roots of

```text
XY(X-Y)(X-lambda Y).
```

For this form, `(1)` equals

```text
(1+lambda)(2lambda-1)(lambda-2).                           (2)
```

The zero locus of a relative invariant is preserved by an invertible
projective change. Since the characteristic is not `2` or `3`, `(2)`
vanishes exactly for `lambda=-1,1/2,2`, the harmonic cross-ratio orbit.
Pairwise distinct `b_i` ensures that every signed lift quartic has distinct
roots: equality of two signed lifts would make their squares equal.
Consequently `J(F_epsilon)=0` is equivalent to harmonicity of that signed
lift set.

Changing one chosen square root permutes the eight sign classes, and changing
all four signs leaves `(BQN1)` unchanged. Permuting the `b_i` merely permutes
the roots within every quartic and hence leaves every invariant unchanged.
It follows that the product `(BQN2)` is independent of all choices and is
symmetric in the `b_i`.

Every term in `J(F_epsilon)` has root degree six. The product of eight
factors has root degree forty-eight. Invariance under each individual sign
change makes every root exponent even, so the product lies in
`K[a_0^2,a_1^2,a_2^2,a_3^2]=K[b_0,b_1,b_2,b_3]` and has degree twenty-four
there. The fundamental theorem of symmetric polynomials then writes it in
the coefficients of `D`.

Fix the representative `epsilon_0=1` of every global-sign class. In the
quadratic algebra `A`, multiplication by `N_1`, then `N_2`, then `N_3`
multiplies `J(F_+)` over precisely the eight choices of the other three
signs. This proves `(BQN3)`. The result is also fixed by `sigma_0`: negating
`a_0` and then globally negating each root permutes those same eight
factors. Hence the iterated norm lies in `K` and equals `(BQN2)`.

Finally, a product in the field `K` is zero exactly when one of its factors
is zero. Combining this with `(2)` proves the harmonic equivalence.

For completeness, define the three pairing forms

```text
h_(ij|kl)=2(a_i a_j+a_k a_l)-(a_i+a_j)(a_k+a_l).
```

Direct expansion gives

```text
J(F)=-h_(01|23)h_(02|13)h_(03|12).                    (3)
```

Each pairing form vanishes exactly when that pairing realizes cross-ratio
`-1`. It remains to evaluate its sign norm. Write one pairing as
`(a,b)|(c,d)`, put `x=a^2,y=b^2,z=c^2,t=d^2`, and set
`A=a+b`, `P=2ab`. First norm in `d` and then in `c`:

```text
N_d(h)=(P-Ac)^2-t(2c-A)^2=C+Ec,
N_cN_d(h)=C^2-zE^2.                                  (4)
```

Now put `u=ab`, so `u^2=xy`. Reduction of `(4)` in the quadratic algebra
`K[u]/(u^2-xy)` gives exactly

```text
K_0+K_1u
```

with `K_0,K_1` from `(BQN4)`. Its last norm is
`K_0^2-xyK_1^2=P_(xy|zt)`. This is the product of `h` over all eight sign
classes, so it is intrinsically independent of the orders used in the
display. Taking sign norms in `(3)` proves `(BQN5)`; the eight minus signs
multiply to one. This also proves the radical-free evaluation formula. QED.
