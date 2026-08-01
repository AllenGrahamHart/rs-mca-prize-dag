# Pro's adversarial self-audit of the inverse-flatness strategy — 2026-08-01

> **Provenance:** Pro's 1,226-line adversarial audit of its own strategy
> document (same thread, same day), relayed by the maintainer. Checker:
> `verify_adversarial_audit_inverse_flatness.py` (replayed under
> ramguard, all six fixtures PASS). **Fable verification:** the
> Cayley-Hamilton tautology, pigeonhole vacuity, scale mismatch, direct
> product arithmetic, and the doubling identity were independently
> re-derived by hand; the coboundary identity's symbolic proof
> (A(C)D(C) = prod(1-zeta^2ch) = D(2C)) is one line and now a PROVED
> node with an exact integer verifier.

## Retired (with exact fixtures)

The spine "inverse-LO/BSG -> GAP -> lambda-rigidity -> Cayley-Hamilton ->
Booleanisation -> resultant sieve" is dead in its proposed form:
qualitative CERP (pigeonhole-vacuous), uniform inverse-LO engine (blind
at 1+2^-213), adjacent-overlap => invariant GAP (travelling window),
dyadic Cayley-Hamilton (tautological: #blocks = phi(ord) at every dyadic
block size), automatic Booleanisation (lambda=3 has no squarefree signed
form), L=1 gate-surplus transfer (32 bits at L=1, zero at top).

## Survives

The exact identities and owner ledger (both minted); the adversarial
weight-9/10 packet census (now with mandatory ACTIVITY and REPAYMENT
fields — positive owner increments can be repaid by later negative ones,
so positive-only packet bounds can fail); exact q-independent-height
certificate discipline; the eight-wise trap and the direct-product
multiplicity lesson as permanent mutation controls.

## The replacement (minted): doubling-coboundary

The binary alphabet's own algebra (1+x = (1-x^2)/(1-x)) selects
multiplication by 2 on F_q^*/H as the canonical dynamic — not
lambda=omega^4. A(C) = D(2C)/D(C) exactly; products around every doubling
cycle equal 1; C1-ZERO at L=1 becomes an exponential-moment problem for
the discrete derivative of the cyclotomic potential L along doubling
orbits. Small orbits route to finite resultants (q | 2^(512r)-1); r=1
rows are EXACTLY flat (verified: q=257, X = 1/65792 on the nose) —
explaining the known exact-equidistribution classification (Gaitanas:
+-2-geometric progressions). The open core: bound the exponential moment
on LONG doubling cycles, using the special cyclotomic form of D (an
arbitrary positive cycle function admits no such bound).

## Revised sequencing (kill lines K1-K6 as in the audit)

1. Doubling compiler + small-orbit sieve [Codex-shaped].
2. Zero-surplus analogue campaign (v_2(q-1) = v_2(root order)) — the
   transfer test the L=1 lab otherwise cannot provide.
3. Engineered weight-9/10 packet census with activity/repayment fields.
4. Non-dyadic-block owner variants (b in {5,6,7}: blocks < cyclotomic
   degree) if operator rigidity is ever retried — with the four gates
   (stationary return, rank defect, height bound, Graver output).
5. Large-orbit level-set falsification; only then a theorem attempt.
Fallback if no stable descriptor emerges: redirect to the thinner xr
external-zero compression problem.
