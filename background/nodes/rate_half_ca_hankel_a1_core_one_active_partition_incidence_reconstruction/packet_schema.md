# Prime-field pilot packet schema

`check_packet.py` is the independent prefilter for bounded CR-003 prime-field
pilots. Run it under the local memory guard with

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/check_packet.py \
  PACKET.json
```

The packet is one JSON object with:

- `p`: the declared odd prime modulus;
- `e,b,e_star,r`, satisfying `e_star=e-b` and `r=2e_star+1`;
- optional `expected_separation_rank`;
- `clean_fibers`: records `{"slope": gamma, "roots": [...]}` with exactly
  `r` distinct roots;
- `saturated_fibers`: records `{"row": x, "roots": [...]}` with exactly
  `e_star` distinct supported slopes.

All field elements use canonical integer representatives in `[0,p)`. The
checker verifies both directions of every core incidence, recovers the unique
nonincidence potentials, rejects inconsistent cycles, runs all `r+1`
coefficientwise Reed--Solomon tests, and compares the clean-locator,
saturated-locator, and core-value ranks. A PASS record includes a canonical
packet SHA-256 hash.

This tool deliberately materializes the bounded pilot core matrix. It is not
an official-scale launcher. It performs arithmetic modulo the declared `p`
but does not certify primality, ambient domain/support completeness, the
Hankel chain, the adjugate identity, irreducibility, complement equations, or
active traces. A final positive CR-003 certificate must verify those items
independently. `toy_packet.json` is the exact `Q(t,X)=X^3-t` example over
`F_97` used by the checker audit.
