# WCL slot 4,11 emptiness (extended window)

- **status:** TARGET (minted 2026-07-19 at the C1'-r3 adoption)
- **consumer:** `dli_wcl_zone_coverage` (req; ten-slot leaf set)

See the dag statement for the exact claim and falsifier; the
weight-3/4 norm-census machinery is the named attack; bookkeeping of
record = ../dli_wcl_zone_coverage/official_terminal_attack.md.

The proved `dli_wcl_extended_six_slot_sparse_divisor_endpoints` replaces the
blind census by the exact six-variable divisor

```text
G=YA^2-B^2 | Y^1024-1,       deg A=5, deg B<=1, B(0)=1,
```

and a pruned `142`-variable, `147`-equation straight-line unit ideal.
Computing and excluding the prime divisors of a checked integer certificate
remains open; status stays `TARGET`.
