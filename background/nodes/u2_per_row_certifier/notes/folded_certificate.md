# The folded short-vector certificate (shared: integer_cert, u2, e1_fullness)

## The reduction (via kernel_lattice_reframing, PROVED)
For 2-power N', zeta^{N'/2} = -1, so sum_x v_x zeta^x (v ternary) folds to
sum_{x<N'/2} w_x zeta^x with w_x = v_x - v_{x+N'/2} in {-2..2}. "Cyclotomic"
(antipodal) = w == 0. THE CERTIFICATE QUESTION for BOTH certifier nodes (and
the finite side of e1_fullness) is identical:
    is there a NONZERO w in {-2..2}^{N'/2} with sum_x w_x zeta^x == 0 mod p?
YES => a genuine collision (falsifier fires, survivable/charged). NO =>
CERTIFIED (only cyclotomic vectors; value set full mod quotient).

## The procedure (proved-correct)
fold (proved) + complete short-vector search over {-2..2}^{N'/2}. A complete
search finding nothing IS a machine-checkable certificate.

## TOY EXEMPLAR (the format the node asks for; verified exhaustively)
- N'=16, p=60161: 0 non-cyclotomic collisions -> CERTIFIED (matches zone_b's
  exact-quotient equality 3281=3281).
- N'=16, p=10177: 48 collisions, min support 5 -> falsifier fires (bad prime;
  matches zone_b ratio 0.951). BOTH verdicts demonstrated.
- N'=32: MITM (dim 16), 96-256 collisions, min support 10-11 (support GROWS
  with N').

## THE REMAINING WORK (precisely characterized — a computation, not a theorem)
Exhaustive/MITM is feasible to N' ~ 40 (5^{N'/2}). The prize open cells
N'=128/256 fold to dimension 64/128 lattices (det p ~ 2^250). The certificate
is then a LATTICE SHORT-VECTOR ENUMERATION in dim 64/128 -- feasible with
fplll-class exact-SVP/enumeration tools (dim 64 is in range), NOT a new
theorem. Two honest caveats: (i) needs the pinned official exhibit cell
(N', prime) from piece A's window arithmetic; (ii) the answer may be
"collision found" (survivable, charged) rather than "certified" -- a
per-prime accident, as p=10177 shows. The STRUCTURAL alternative that
certifies ALL good primes at once is e1_fullness (the density theorem).
