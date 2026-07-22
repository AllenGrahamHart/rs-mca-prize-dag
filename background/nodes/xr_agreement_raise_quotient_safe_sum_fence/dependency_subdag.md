# Dependency sub-DAG

```text
census_bounded_scales [PROVED] -----------------------------+
xr_target_budget_audit [PROVED] -----------------------------+-->
xr_mismatch_terminal_tangent_agreement_raise [PROVED] ------+
                                                                  \
       xr_agreement_raise_quotient_safe_sum_fence [PROVED]
                                      |
                                      +--ev--> xr_tangent_support_mismatch_bridge
```

The census pins the deciding quotient sizes, the budget audit supplies the
fixed-threshold comparison, and the agreement-raise theorem explains why a
threshold-union quotient payment is needed. The evidence edge kills one
payment method but does not settle the bridge.
