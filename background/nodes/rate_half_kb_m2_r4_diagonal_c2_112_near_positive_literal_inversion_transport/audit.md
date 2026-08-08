# Audit

Two exact implementations agree.

1. The primary Modal probe checks out upstream PR #1140 at commit
   `9e1d96cbf997c30efa448bbce9a7f48c2bea9643`, verifies source SHA-256
   `c382adee5be3b72dcb675b4932a681f65ae958f58e24c3f5fdb8163d4d1508b7`,
   and reuses its explicit positive source reconstruction for all twelve
   literal assignments.
2. `near_literal_assignment_transport_audit.sage` imports none of that
   compiler. It rebuilds each source form by a generic `5 x 5 solve_right`
   over `QQ(b,c,d)` and derives the residuals and localizer factors afresh.

Both runs pass all 288 residual/target/localizer checks and report the same
`42/12/30` orbit census. The primary run used peak child RSS `494600 KiB`;
the independent run used `480340 KiB`. Both ran on Modal, not on the WSL
host.

Pinned artifact SHA-256 values:

```text
probe wrapper  f9d502b5c6e48b3ce2989c1b0846bf82e73a7c188f083a9b97bbc7e6b9843086
audit source   2ebf44346600507f6d0db3f9f502fdd0c4e45e5350ff34a03b80d9a212f1754f
output         bc82dbe4721afd5d7d626268e97b8060ea2f9b3398c972d44fcd44a483828292
```

The first attempted independent output failed only because Sage integers are
not JSON serializable by the standard encoder. All mathematical assertions
had completed. The serializer was repaired with `default=int`, and the
independent audit then returned `PASS` in 37.119488 seconds.
