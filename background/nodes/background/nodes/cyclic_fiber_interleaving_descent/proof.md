# Proof

Write `k=MK_0`. Every polynomial `f in F[X]` of degree less than `k` has a
unique residue-class decomposition

```text
f(X)=sum_(r=0)^(M-1) X^r f_r(X^M),       deg f_r<K_0.       (1)
```

The degree bound is uniform because `M|k`: the exponents congruent to `r`
modulo `M` below `k` are exactly `r,r+M,...,r+(K_0-1)M`.

Let `zeta` generate `K`. For each `y in H^M`, choose `x_y in H` with
`x_y^M=y`. On the fiber `x_yK`, equation (1) gives

```text
f(zeta^j x_y)=sum_r zeta^(jr) x_y^r f_r(y).      (2)
```

The matrix `(zeta^(jr))_(j,r)` is the Fourier matrix of `K`. It is
invertible because the field characteristic does not divide `M`. The
additional diagonal factors `x_y^r` are nonzero. Thus the `M` values of `f`
on a fiber are in bijection with the component vector

```text
(f_0(y),...,f_(M-1)(y)).                          (3)
```

Apply the inverse of this fiberwise linear map to the values of the received
word `U`, obtaining a vector word `U'` on `H^M`. A codeword `f` agrees with
`U` at every point of the fiber above `y` if and only if all `M` component
codewords `f_r` agree with `U'` at `y`.

If the exact agreement set of `f` is `K`-invariant and has size `A`, it is a
union of exactly `A/M` full fibers. Hence the tuple `(f_0,...,f_(M-1))`
belongs to the common-support `M`-interleaved list of `C'` around `U'` at
agreement `A/M`. Decomposition (1) is injective, so this gives

```text
N_M(U,A)<=L_M(C',A/M).
```

The final two bounds are the proved
`list_subsqrt_interleaving_collapse` theorem applied to `C'`.

Finally suppose `K=Stab_H(S)` is intrinsic. The stabilizer of the quotient
support `S/K` in `H/K` is `Stab_H(S)/K`, hence is trivial. The transformed
interleaved tuple has exact common agreement support `S/K`. The proved
`exact_support_interleaving_projection` theorem can therefore be applied with
`P` equal to the aperiodic supports, retaining this primitive designation in
the resulting ordinary quotient-row bound.
