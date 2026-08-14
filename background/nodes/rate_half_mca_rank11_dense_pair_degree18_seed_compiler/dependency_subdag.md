# Dependency sub-DAG

```text
rate_half_mca_rank11_large_shared_pair_core_payment [PROVED]
                    |
                    v
rate_half_mca_rank11_heavy_pair_order32_seed_compiler [PROVED]
                    |
                    +-------------------------------+
                                                    |
rate_half_mca_rank11_order32_common_support_cancellation [PROVED]
                    |                               |
                    +-------------------------------+
                                    |
                                    v
rate_half_mca_rank11_dense_pair_degree18_seed_compiler [PROVED]
```

The new node changes the seed selection: eighteen records come from a
pigeonholed dense pair, while the remaining fourteen slots retain enough of
the heavy-pair component basis to keep the cancellable core below `K`.
