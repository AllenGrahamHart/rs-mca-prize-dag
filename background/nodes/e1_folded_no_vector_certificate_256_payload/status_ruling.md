# Status ruling

`TARGET`. This node requires a complete zero-vector certificate in one named
field. The banked `PRO_W3_e1_density.md` argument proves neither that statement
nor a substitute with the same quantifier.

The density calculation averages bounded norm divisors over primes and gives
an almost-all-primes estimate for the number of folded coefficient vectors.
It does not certify the named Pocklington field, does not return zero vectors,
does not convert folded-vector counts to the consumed collision multiplicity,
and uses asymptotic prime-counting without a finite error term at the printed
250-bit scale. The prior BKZ observation was explicitly inconclusive.

The DAG had silently changed this leaf's description to the density estimate
while retaining a `req` edge into
`e1_folded_certificate_cell_256_payload`, whose conditional proof still
requires a complete no-vector certificate. That is a type and quantifier
mismatch, not consumer tolerance.

The useful almost-all-primes estimate remains partial evidence. Closure now
requires either the literal complete named-field certificate, or a separate
finite family-uniform density theorem together with a proved rewire of every
consumer. Until one of those routes is banked, this leaf remains red.

## Bounded falsification campaign

Modal app `ap-uImvgijoKNeruVABf32Cc9` ran four deterministic LLL/BKZ plus
negacyclic-shift-combination workers against the exact named field/root. All
four completed within `125.33 s`; none found a box vector. The best observed
basis-vector infinity norm was `5`, and the best signed-shift pair infinity
norm was also `5`. The exact campaign checker reports `INCOMPLETE`, not
`CERTIFIED`. See `falsification_report_20260726.md`.
