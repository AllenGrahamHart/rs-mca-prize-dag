# Official-order template generator + survivor bound (CR-001)

- **status:** TARGET (minted 2026-07-19 at the C36 amber ceremony; alt leaf, gate=any)
- **consumer:** `f3_h3_mobius_excess_half` (alt)

An efficient official-order rich-prime template generator with a
survivor bound: via the audited coupled-ideal sieve (positive Y_18
forces p | Norm(alpha_F, alpha_G, theta, lambda) <= 6^{n/4}/4;
zero-coupling locus exactly {x,y,z} = {q,-q,-q^2}, w = q^4), enumerate
the official-order templates and bound the survivors below the
allowance — closing the C36 red on the fixed-order route. The compute
side is CR-001 (notes/PRIZE_COMPUTE_REQUESTS.md); the proved
infeasibility fence (>= 5.3e8 orbits at n=8192) means the generator
must be structural, not brute-force. FALSIFIER: a survivor census
provably exceeding the allowance.
