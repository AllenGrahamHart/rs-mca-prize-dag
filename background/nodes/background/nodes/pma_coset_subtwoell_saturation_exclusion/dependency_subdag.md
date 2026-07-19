# Dependency sub-DAG - PMA constant-shift-pencil sub-two-ell exclusion

```text
l1_coset_chart_residue_bridge [PROVED]
                  |
                  | req: full-petal locators X^ell-a_i
                  v
pma_coset_subtwoell_saturation_exclusion [PROVED]
                  ^
                  | req: exact gcd(F,W)=1
                  |
pma_saturated_mixed_support_kernel [PROVED]

pma_coset_subtwoell_saturation_exclusion
                  |
                  | ev: scoped below-band exclusion; source bridge open
                  v
petal_mixed_amplification [TARGET]
```

The evidence edge is intentional. Promoting it to a required global supplier
would silently assume that every surviving carried source has one common
constant-shift locator pencil. The coset bridge supplies only the special case
`P=X^ell`.
