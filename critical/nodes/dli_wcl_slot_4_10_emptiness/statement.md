# WCL slot 4,10 emptiness (extended window)

- **status:** TARGET (minted 2026-07-19 at the C1'-r3 adoption)
- **consumer:** `dli_wcl_zone_coverage` (req; ten-slot leaf set)

See the dag statement for the exact claim and falsifier; the
weight-3/4 norm-census machinery is the named attack; bookkeeping of
record = ../dli_wcl_zone_coverage/official_terminal_attack.md.

The proved `dli_wcl_extended_six_slot_sparse_divisor_endpoints` replaces the
blind census by the exact six-variable divisor

```text
G=E^2-YB^2 | Y^1024-1,       deg E=5, deg B=0,
```

and a pruned `129`-variable, `133`-equation straight-line unit ideal.
Computing and excluding the prime divisors of a checked integer certificate
remains open; status stays `TARGET`.
