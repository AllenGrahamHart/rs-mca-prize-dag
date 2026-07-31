# Proof

The parent atlas shows that the five `K` labels consist of two antipodal
pairs and the singleton `M`.  Reading the product normalization in `M2` and
`M3` gives exactly `(KB43O-1)`.

For a product pair `(y,z)`, the paired-product gate uses the row

```text
[yz,-(y+z),-1].                                   (1)
```

Take the cross product of the two rows supplied by `(KB43O-1)`.  In both
signs it is `(Gamma,Alpha,Beta)` from `(KB43O-3)`, proving `(KB43O-2)` for
the two known pairs.  Direct expansion gives `(KB43O-4)`.  Every factor on
its right is nonzero: `b,c` and their required signed pairs are distinct,
and `bc!=-1` because the `BC` and `A` products are distinct.  Thus the
involution is nontrivial and nonsingular.  The two known rows are
independent, so they span the plane cut out by `(KB43O-2)`.

The source-facet signature proves that `I` is antipodal.  It contains the
five-set `K`, whose only unpaired member is `M`, so its sixth member is
`xi=-M`.  This is `(KB43O-5)`.

The common-`K` product rows determine one Mobius map `F`.  Evaluating the
maximal-cofactor vectors used in the `M2/M3` classifier at `-M` gives

```text
M2: F(-M)=-b[b(M-1)^2+(M+1)^2]
             /[b(M+1)^2+(M-1)^2],

M3: F(-M)= b[b(M-1)^2-(M+1)^2]
             /[b(M+1)^2-(M-1)^2].                 (2)
```

These are the two signs of `(KB43O-6)`.  Let
`B_epsilon=4b^2+epsilon A b+4`.  Exact elimination gives, for each sign,

```text
Res_M(P_6,Res_b(B_epsilon,H_epsilon,b),M)=2^32,
Res_M(P_6,Res_b(B_epsilon,N_epsilon/(epsilon b),b),M)=2^32. (3)
```

Since `b!=0` and the characteristic is odd, `(3)` proves that `(2)` is
finite and nonzero at every classified root.  The five common points make
`F` a nonconstant Mobius map.  The label `-M` is distinct from all five
members of `K`, so injectivity makes `F(-M)` distinct from their products.

Conjugating label negation by `F` gives the product involution.  Therefore
`(-c^2,F(-M))` obeys `(KB43O-2)`.  Independently, cross-multiplication of
that assertion reduces to zero modulo the three equations `(KB43M-3)`.

There are six antipodal source-label pairs in total.  Two lie wholly in
`K`; the singleton `M` pairs with `xi`; hence three pairs remain wholly
outside `K`.  Necessity of `(KB43O-2)` for their product rows follows from
the paired-product theorem.  Conversely every row satisfying
`(KB43O-2)` lies in the plane spanned by the two independent known rows,
which is exactly the rank-at-most-two gate.  This proves the compiler.

Finally, `K=I intersect L` and `xi=I minus K`.  If `L=I`, `xi=eta` and the
source-facet census makes its edge `I-I`.  Otherwise `xi` is in `L^c`,
where the census permits `I-I` or `I-J`; the colored-divisor theorem says
the latter records are exactly its two roots. QED.
