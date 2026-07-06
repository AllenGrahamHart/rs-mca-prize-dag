# proof: dli_truncated_log_transfer

Let

```text
F(theta) = -log |mu_hat(theta)|^2
```

be the nonnegative logarithmic Dirichlet loss after the DLI normalization, and
let `F_T = min(F,T)` be its truncation at height `T`.

For any finite sequence `theta_y`,

```text
sum_y F(theta_y) >= sum_y F_T(theta_y).
```

The truncated-log discrepancy hypothesis says that the empirical average of
`F_T` along the odd-evaluation sequence is within the stated error of the
circle average of `F_T`. The peak-mass tail hypothesis says that the missing
tail between `F_T` and `F` near the singular Dirichlet peaks contributes only
the stated additional error. Hence

```text
sum_y F(theta_y)
  >= (#y) * int F(theta) dtheta - error_j.
```

Using the circle constant proved in `dli_circle_log_integral_constant`, the
circle integral is the model value that becomes

```text
2 L_j log q
```

under the DLI normalization. Writing the total truncated-discrepancy and
peak-tail error as `2 eps_j log q + O(1)` gives

```text
-sum_y log |mu_hat_y(P_lambda(sigma(y)))|^2
    >= 2(L_j - eps_j) log q - O(1).
```

If the per-profile errors satisfy `sum_j eps_j=o(t)`, the DLI
odd-evaluation discrepancy predicate follows. This is a deterministic
truncation transfer; all arithmetic content is in the peak-mass discrepancy
predicate.
