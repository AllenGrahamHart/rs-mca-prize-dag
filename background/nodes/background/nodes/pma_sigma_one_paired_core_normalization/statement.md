# PMA sigma-one paired-core normalization

- **status:** PROVED
- **consumer:** `pma_wide_residual`, `petal_mixed_amplification`
- **role:** canonical global index for maximal-sunflower source layouts

## Statement

Let `H` be a set of `n` distinct field elements, let `2<=k<n`, assume
`n-k=2M`, and fix a received word `U:H->F`. For every `(k-1)`-subset
`C subset H`, put

```text
L_C(X)=product_(z in C)(X-z)
```

and let `Q_C` be the unique polynomial of degree at most `k-2` with
`Q_C|_C=U|_C`. Define the quotient-value map

```text
phi_C(x)=(U(x)-Q_C(x))/L_C(x),       x in H\C.          (PC1)
```

Call `C` a **paired core** when the fibers of `phi_C` consist of exactly one
singleton and `M` doubletons. Then paired cores are in bijection with
unordered maximal `sigma=1` source layouts

```text
H=C disjoint_union {y} disjoint_union T_1 ... disjoint_union T_M,
|T_i|=2,

U=P_0                  on C union {y},
U=P_0+c_i L_C          on T_i,                            (PC2)
```

where the `c_i` are distinct and nonzero and `deg P_0<k`. The maps in the
bijection are explicit:

```text
a_0=phi_C(y),
P_0=Q_C+a_0 L_C,
T_i=phi_C^(-1)(a_i),
c_i=a_i-a_0,                                             (PC3)
```

where `{y}` is the unique singleton fiber and the `a_i` are the doubleton
fiber values. Conversely, every layout `(PC2)` produces exactly this fiber
partition. In particular, for fixed `U` and `C`, the background point,
petals, base polynomial, and labels are unique up to ordering of the petals.

Put `P_i=P_0+c_iL_C`. Any two distinct planted codewords `P_i,P_j` determine
the affine polynomial line

```text
P_0+F L_C,
```

their difference has domain-root set exactly `C`, and this line together
with `U` recovers the unique layout. Consequently two distinct source layouts
cannot share two planted codewords.

Finally, after global owners are removed and a total order is put on paired
cores, let `E_C` be the Post codewords whose first carried layout has core
`C`. Then

```text
Post(U)=disjoint_union_(C paired) E_C,
#Post(U)=sum_(C paired) #E_C.                             (PC4)
```

Thus every proved per-sunflower payment is a per-paired-core summand. The
remaining finite PMA composition problem is exactly a weighted census of the
paired cores carrying nonempty `E_C`, or a chart-free owner replacing those
summands.

## Scope

This theorem removes background, normalization, petal-pairing, and repeated
two-anchor ambiguity. It does not bound the number of paired cores, the
weighted sum in `(PC4)`, or any remaining Post source class. Fibers larger
than two and nonmaximal source layouts are outside this exact `sigma=1`
normalization.
