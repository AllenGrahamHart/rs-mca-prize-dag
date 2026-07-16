# Dependency sub-DAG - pma_exact_periodic_owner

```text
petal_g2_support_forcing [PROVED] ------------------+
petal_g3_full_support_codeword_injectivity [PROVED] +--> pma_exact_periodic_owner [PROVED]
qa22_m_le_t_extension [PROVED] ---------------------+

pma_exact_periodic_owner --req--> imgfib [CONDITIONAL]
pma_exact_periodic_owner --ev----> petal_mixed_amplification [TARGET]
pma_exact_periodic_owner --ev----> pma_wide_residual [REFUTED]
```

The node is a proved supplier, not a logical premise below the red leaf. The
red target retains the stabilizer-one quotient-closure and primitive residual
obligations.
