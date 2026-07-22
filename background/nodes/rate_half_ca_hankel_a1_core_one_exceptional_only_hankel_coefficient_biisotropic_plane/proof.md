# Proof

The middle-Hankel theorem gives one right minimal index `e`. In the canonical
`L_e` block, the coefficients of its degree-`e` primitive minimal vector are
the `e+1` standard basis vectors. Strict equivalence and a projective change
of parameter preserve their rank. Hence `q_0,...,q_e` are linearly
independent, proving `(HBI3)`.

The coefficients of `M(z)q(z)=0` give

```text
M_0q_0=0,
M_0q_k+M_1q_(k-1)=0       (1<=k<=e),
M_1q_e=0.                                           (1)
```

Write `B_(i,j)=q_i^TM_1q_j`. Symmetry and `(1)` imply, whenever
`i<e` and `j>0`,

```text
B_(i,j)=q_i^TM_1q_j
       =-q_(i+1)^TM_0q_j
       = q_(i+1)^TM_1q_(j-1)=B_(i+1,j-1).          (2)
```

If `i+j<=e`, iterate `(2)` to `B_(i+j,0)`. This vanishes by pairing the
equation for `q_(i+j+1)` with `q_0` when `i+j<e`, and by `M_1q_e=0` when
`i+j=e`. If `i+j>e`, iterate to `B_(e,i+j-e)=0`. Thus all `B_(i,j)` vanish,
which proves `(HBI4)` for `M_1`. Equation `(1)` then gives the same result
for `M_0`; the cases involving `q_0` use `M_0q_0=0`.

The kernel-plane theorem gives

```text
ker M_0=span{q_0,v},       v^TM_1v!=0.              (3)
```

If `v` belonged to `W_q`, `(HBI4)` would force `v^TM_1v=0`. Hence the first
intersection in `(HBI5)` is exactly `span{q_0}`. The Hankel-factor pin says
the only finite rank drop is at `z=0`. At the projective point `z=infinity`,
`M_1` therefore has rank `2e+1`; its one-dimensional kernel contains the
nonzero leading minimal coefficient `q_e` by `(1)`. This proves the second
intersection.

The `M_1` form has a one-dimensional radical inside `W_q`; after quotienting
it, `(HBI3)--(HBI4)` give an `e`-dimensional isotropic subspace in a
nondegenerate space of dimension `2e+1`. It is maximal, so `W_q` is maximal
for `M_1` and hence maximal among common isotropic planes. Finally, expanding
the Hankel pairing gives `(HBI6)`, and substituting a finite source
representation gives `(HBI7)`. QED.
