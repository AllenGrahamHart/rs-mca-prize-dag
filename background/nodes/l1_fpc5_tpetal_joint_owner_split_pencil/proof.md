# Proof: joint-owner split-pencil reduction

By the joint-owner theorem,

```text
gcd(H,F L_(R_0))=gcd(G,F) gcd(B,L_(R_0))=D E.         (1)
```

The factors on the right have roots in the disjoint core and background,
respectively, so they are coprime. Because `R_0` is the zero set of `W` on
the background, `L_(R_0)|W`; hence `E` divides both `W` and `B`. By
definition, `D` divides both `F` and `G`. All divisions in `(SP3)` are
therefore exact. Equation `(1)` also gives `H=DEK`.

Substitution in the anchor determinant identity gives

```text
Lambda D E K
 =F B-G W
 =(D A)(E V)-(D C)(E U)
 =D E(A V-C U).
```

Cancellation in the polynomial domain proves `(SP4)`. Since the candidate
is distinct from the anchor, its anchor coordinate `H` is nonzero, so `K`
is nonzero. Also `deg H<=r`, whence `deg K<=r-q`.

Exact ownership gives `D=gcd(F,G)`. Dividing the monic squarefree split
locators `F,G` by their full common divisor makes `A,C` monic squarefree
split locators with `gcd(A,C)=1`. Original primitivity gives
`gcd(F,W)=gcd(G,B)=1`; taking divisors proves
`gcd(A,U)=gcd(C,V)=1`. This proves `(SP5)`.

The anchor and candidate petal equations are

```text
W == c_i F (mod L_i),       B == c_i G (mod L_i).
```

Substituting `(SP3)` proves `(SP6)`. Petal roots are disjoint from both the
core and background, so `gcd(DE,L_i)=1`; multiplying by the inverse of `E`
modulo `L_i` proves `(SP7)`.

Now fix an exact owner chamber and one member `(C_0,V_0,K_0)`. The factors
`D,E`, and hence `A,U`, are fixed by the owner and anchor. Multiply the
equation for `(C,V,K)` by `K_0`, multiply the reference equation by `K`, and
subtract:

```text
A(K_0 V-K V_0)=U(K_0 C-K C_0).                       (2)
```

Because `gcd(A,U)=1`, there is a unique `T` such that

```text
K_0 C-K C_0=A T,       K_0 V-K V_0=U T.
```

Writing `a=deg A=deg C=deg C_0`, the first identity has numerator degree at
most `a+c`; division by the degree-`a` polynomial `A` gives `deg T<=c`.
This proves `(SP8)`.

At `q=r`, all of `K,K_0,T` are constants. Put `lambda=K/K_0`. Comparing
the leading coefficients in `K_0 C-K C_0=A T` gives
`T/K_0=1-lambda`, proving `(SP9)`. Both `K` and `K_0` are nonzero, so
`lambda!=0`; that excluded value would give the anchor `(A,U)`. The member
under consideration is different from the fixed reference, so `lambda!=1`.
Equation `(SP10)` is `(SP4)` with constant nonzero `K`.

Finally, at fixed canonical `Q`, the pair determines `K=H/Q`, while `QK=H`
and the proved anchor chart reconstructs the unique candidate. Equivalently,
relative to the fixed reference member, `(K,T)` determines `(C,V)` through
`(SP8)`. QED.
