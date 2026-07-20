# Proof

Use indices `0,...,r` for the rows and columns of `M_1`. The two padded
coefficient shifts from the kernel-plane theorem satisfy

```text
u_i=a_i       (0<=i<r),       u_r=0,
v_0=0,        v_(i+1)=a_i     (0<=i<r).               (1)
```

Substitute the Hankel entries `(QMP1)` into the three pairings. Directly,

```text
u^T M_1 u
 =sum_(i,j=0)^(r-1)a_i a_j h^(1)_(i+j)
 =Theta_0,                                                (2)

v^T M_1 u
 =sum_(i,j=0)^(r-1)a_i a_j h^(1)_(i+j+1)
 =Theta_1,                                                (3)

v^T M_1 v
 =sum_(i,j=0)^(r-1)a_i a_j h^(1)_(i+j+2)
 =Theta_2.                                                (4)
```

The kernel-plane transversality theorem proves that the first two pairings
vanish and the third does not. Equations `(2)--(4)` therefore prove
`(QMP3)`. Notice that the largest moment index used is `2r`, exactly the last
entry available in the `(r+1) x (r+1)` middle Hankel matrix.

It remains to translate the convolution to source coordinates. Before
contraction, each endpoint syndrome is a finite moment sum over the
evaluation domain. Contracting by the fixed core factor multiplies its source
weights by the value of that factor, and changing to the local parameter
`z` takes a field-linear combination of the two endpoint sequences. Hence
the coefficient of `z` still has a representation `(QMP4)` for some field
weights `omega_x` on the residual domain.

Using this representation and interchanging finite sums gives

```text
Theta_s
 =sum_x omega_x x^s sum_(i,j)a_i a_j x^(i+j)
 =sum_x omega_x x^s (sum_i a_i x^i)^2
 =sum_x omega_x x^s A(x)^2.                            (5)
```

This identity is valid in every characteristic. The exceptional generator
is squarefree and split over `D_res`; each `x` in its root set `R_A` has
`A(x)=0`, so deleting those terms does not change `(5)`. This proves all
assertions. QED.
