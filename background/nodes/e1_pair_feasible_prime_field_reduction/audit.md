# Audit

Date: 2026-07-27.

The interval calculation is exact and bounded: only integer roots of 256-bit
endpoints are computed. No primality search, factorization, or Modal run is
used. The RowC square interval has four integers; all higher-degree RowC and
all prize extension intervals are empty.

This audit also repairs a scope ambiguity in the route narrative.
`kernel_lattice_reframing` assumes `p=1 mod N`; ambient generation alone did
not justify that assumption. The perfect-power interval reduction now does.
