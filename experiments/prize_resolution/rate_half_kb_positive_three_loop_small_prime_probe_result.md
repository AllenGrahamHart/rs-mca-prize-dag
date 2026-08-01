# Positive three-loop small-prime probe

The bounded pure-Python probe
`rate_half_kb_positive_three_loop_small_prime_probe.py` exhausts common
placements and admissible common kernels, then asks whether each of the
seven required outside `(product,squared-sum)` records occurs at a distinct
outside quotient label.

```text
F_13 complete:
  common tuples 25,600; singular matrices 1,996;
  admissible kernels 1,716; outside assignments 82,368;
  seven-record survivors 0;
  maximum records present: 442 lanes 1/7, 433 lanes 2/7.

F_17 complete:
  common tuples 112,896; singular matrices 6,628;
  admissible kernels 6,036; outside assignments 2,897,280;
  seven-record survivors 0;
  maximum records present: 442 lanes 2/7, 433 lanes 3/7 or 4/7.

F_19, 45-second partial:
  common tuples 195,438; singular matrices 10,348;
  admissible kernels 9,426; outside assignments 9,048,960;
  seven-record survivors observed 0.
```

These are route diagnostics only.  Small-characteristic nonexistence does
not prove emptiness over the geometric closure in the official
characteristics, and the probe tests the complete Vieta graph rather than
all source-component conditions.  Its value is the repeated stronger
failure mode: no tested assignment even realizes all seven records before
the pairwise-label matching gate.
