# WCL `(1,6)` extension-row MITM preregistration

## Question

Does an official generated extension-field row falsify
`dli_wcl_slot_1_6_emptiness`?  Probe the first 64 prime characteristics in
each of these two exact classes:

```text
p = k 2^39 + 1, k odd: ord_(2^41)(p) = 4, q = p^4;
p = k 2^40 + 1, k odd: ord_(2^41)(p) = 2, q = p^2.
```

Every selected row has `q < 2^256`.  In both classes `mu_512` lies in the
prime field, so a reduced signed weight-six relation can be tested exactly
modulo `p`.

## Fixed test

Normalize one exponent to zero and forbid equality and antipodality.  Store
all 129,540 legal pairs and scan all 21,849,080 legal triples, accepting only
a compatible pair/triple whose six roots sum to zero.  The compiler is a
separate copy of the hash-pinned first-64 split-prime implementation; the only
mathematical scope change is replacing the unnecessary `2^41 | p-1` check by
the required `512 | p-1` check.

The deterministic 64-bit Miller-Rabin basis selects the panel.  A hit must be
replayed independently and receive an exact primality certificate before it
is used to refute the critical node.  A no-hit is finite evidence only and
does not change node status.

## Resource and stop rules

- Phase zero: run only the smallest degree-four characteristic.
- Continue to the 128-row panel only if phase zero returns a valid record.
- Each worker has one CPU, 1 GiB RAM, a 60-second Modal timeout, and no retry
  dependency.
- At most 64 containers run concurrently; expected worker time is under two
  minutes total and expected cost is well below one dollar.
- The local entry point rewrites the result after every returned row, so a
  client interruption preserves a partial packet.
