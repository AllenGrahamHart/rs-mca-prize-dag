# Replay certificate

The verifier was shipped by content to Modal and replayed in app
`ap-IIoAHzTZDlJwszGuq4r5Cc`. It returned

```text
RATE_HALF_FIXED_TAIL_PREFIX_FLOOR_PASS
toy_total=5005 toy_pigeonhole=26 toy_bucket=45
cap_count_bits=524255 q_boundary_bits=255.9209759026303
cap_qcore_gap_bits=4.8285658
```

Peak worker RSS was `57 MB`. The replay checks the polynomial construction on
an order-64 multiplicative domain over `F_193`, including a prefix-removal
mutation, and recomputes the cap-row exact integer condition.

The refreshed full fleet passed `150/150` in Modal app
`ap-byMqI73C01JvwUwcKbaSBw`. All five integration gates passed in
`ap-lNJOEbhP8NSz5T93u1pV0l`, retaining the same eight open critical truth
leaves.
