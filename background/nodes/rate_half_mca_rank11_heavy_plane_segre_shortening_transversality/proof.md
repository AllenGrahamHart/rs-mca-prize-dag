# Proof

Let `Z` be the complete common-zero set of the heavy plane after triple
cancellation and put `z=|Z|`. Every associated correction lies in `PB_*`
and therefore vanishes on `Z`. Since `Z` is anchor-good, the same-record
exchange argument and common-core adapter cancel its squarefree locator,
preserving first-owned slopes and pair noncontainment.

Division gives a two-space `Q=B_*/L_Z` with no common zero on the remaining
universe. The correction rank was proved to be exactly four. Multiplication
by `L_Z` is injective, so

```text
dim span(PQ)=4=dim(P tensor Q).
```

The multiplication map is surjective by definition and hence is an
isomorphism. Since its image lies in `F[X]_{<K}`, the ambient dimension gives
`K>=4`. The root lower bound gives `K<=1048573-37733=1010840`, proving
`(HS1)` and `(HS2)`. The factor pencil `P` was base-free in the parent
branch, and `Q` is base-free by maximality of `Z`.

Choose bases `(p_0,p_1)` and `(q_0,q_1)`. The four products form a basis of
the correction space, and evaluation at every remaining coordinate is
exactly the tensor product of the two evaluation rows. This proves `(HS3)`.
Every associated residual container with factor `g in P` becomes the ruling
plane `gQ`. For one fixed projective `g`, all assigned corrections lie in
one two-dimensional correction space, whose complete chronology-safe mass
is at most `R_2=248644099`. First-match ownership partitions by the used
factor, and

```text
40 R_2=9945763960<M_*,
```

so at least 41 projective factors are used. This proves `(HS4)`.

It remains to apply support-local transversality. Put

```text
R=1048576, d=67472, s=K,
(N,K,m)=(R+s,s,d+s).
```

For correction rank four and margin `theta`, the compiler gives

```text
C_s(theta)=floor(max{
 (R+s)_5/((d+s) theta (d+1)^(3)),
 (R+4)_5/(theta (d+1)^(4))
}),                                                     (1)
```

where the numerator products are falling and the denominator products are
rising. The second term is independent of `s`. For the first term, the
successive ratio is at most one exactly when

```text
4s+5d-R+4<=0.                                          (2)
```

Thus it decreases and then increases, with its minimum turn at `s=177803`;
the maximum on `4<=s<=1010840` occurs at an endpoint. Exact endpoint
evaluation gives the uniform sharp transition for this compiler:

```text
max_s C_s(11)=10166508078 >= M_*,
max_s C_s(12)= 9319299072 <  M_*.                       (3)
```

If the support-local discrepancy were at least 12, `(1)` and `(3)` would
cap the complete bucket strictly below its retained integer mass. Hence the
untruncated discrepancy is at most 11, proving `(HS5)`. QED.
