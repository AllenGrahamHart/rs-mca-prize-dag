# Proof

Put `ell=log2(p)`, so `log2(q)=e ell` and `log2|B0|=k ell`.
The generated-field consumer guard is exactly

```text
t k ell >= N.                                         (1)
```

The fixed-depth statement follows from
`f2_generated_field_ambient_invariance`: after scaling the domain, all
moments and syndrome fibers at the same exponent set are unchanged. That
theorem does not change the integer `t`, so it cannot transport a separate
rule that recomputes `t` from `q`.

Let `t_C=ceil(N/(e ell))`. If `k=e`, then

```text
t_C k ell = t_C e ell >= N,
```

so the guard holds. If `k<e`, the ceiling gives

```text
t_C e ell < N + e ell < N + 256.
```

Hence

```text
t_C k ell < (k/e)(N+256).
```

For the official types, `e<=6` and `k<e`. Therefore

```text
(1-k/e)N >= N/e >= 2^41/6 > 256 > 256k/e,
```

which implies `(k/e)(N+256)<N`. Thus the guard fails whenever `k<e`.
The proved degree/order classification makes these two cases exhaustive.

Finally, suppose `t e ell<N`. Since `k<=e`,

```text
t k ell <= t e ell < N,
```

so the generated-field guard fails on every type. The exact-slice `(T*)`
calibration has precisely this strict deficit. Applying an F2 mass identity
at that depth remains algebraically legitimate, but consuming its result in
the guarded F2 branch is not. This proves all claims. QED.
