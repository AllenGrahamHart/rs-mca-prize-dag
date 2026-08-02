# DRAFT: the crossing-lane succinct certificate contract — for Pro's adversarial round

**Status: DRAFT, not frozen, not a node.** Written by Fable 2026-08-02
from the Brief-6 adversarial round's succinctness mandate and the
one-packet pilot's requirements report
(`notes/pilots_20260802/crossing_packet/REPORT.md` section 7, banked
same day; PK1 is the calibration instance throughout). This is the
contract the Brief-6 exploratory GO called for; it governs what counts
as a certified crossing claim. Freeze only after Pro's attack.

## 1. Scope and claim types

A crossing certificate asserts, for a ROW (q, beta, n, k; H the
multiplicative coset x^n = beta) and a WORD CLASS [U] (received words
mod the code C — never a raw word; shells are invariant mod C and low
parts are never transmitted), one of:

- **SAFE(a):** the exact shell of every word in the class at agreement
  >= a is empty (list = 0 above the threshold).
- **UNSAFE(a, B):** some word in the class has exact-shell count at
  agreement a strictly exceeding the budget B.
- **CENSUS(a):** the exact-shell count at a equals a stated
  counted-object (section 3).

The certified quantity is ALWAYS the guarded (first-owner /
exact-agreement) count. Raw section counts are inadmissible: at the
PK1 calibration instance the raw maximum is 21 against a true list of
7 (pilot IS1); a contract accepting raw counts over-reports by a
factor growing with shell depth.

## 2. Descriptor grammar

- Row descriptor: (q, beta, n, k) — O(log q + log n) bits.
- Word-class descriptor: the Toeplitz window support pattern + the
  window coefficients up to the mod-C invariance, INCLUDING every
  affine target. Omitting an affine target is a KILL: the same
  homogeneous row carries fibres 0 and C(n,r)/n depending on the
  target (mutation M1, the rank-one Toeplitz fence). Two claims whose
  descriptors coincide must have equal certified counts; the mutation
  suite's M1 is the standing collision test.
- Packet descriptor (for CENSUS/UNSAFE): (template-id, index datum) —
  e.g. PK1's (pure-product, s) with s in Z/n. O(log n) bits.

## 3. Certificate primitives (the admissible vocabulary)

1. **Theorem invocation**: a banked node id + the hypothesis checks
   (each check poly(log q, log n): support-pattern tests, nonzero
   tests, one-exponentiation realizability tests like
   ((-1)^(r+1) c)^n = beta^r, gcd(r, n)).
2. **Counted-object**: a SYMBOLIC cardinality (e.g. C(n,r)/n as a
   formula, never expanded — at the razor row it has ~2^41 bits)
   together with a poly-size INEQUALITY DERIVATION CHAIN against the
   budget (e.g. C(n, n/2-1)/n >= 2^n/(2n(n+1)), each chain step a
   checkable algebraic inequality). Comparisons happen on the chain,
   never on expanded integers.
3. **Member spot-check** (optional, strengthening): one packet member
   presented as an index mask, verified through the packet's
   closed-form template in poly(n, log q).
4. **Exactness-guard discharge BY THEOREM ONLY**: the guard
   (gcd(Q_M, M) = 1 / first-owner condition) must be discharged by a
   proved statement (as PK1's Lemma 4 does automatically), never
   member-by-member.

## 4. Forbidden moves (the succinctness clause, operational form)

A certificate is REJECTED if any verification step requires:
enumerating received words (q^n), enumerating a fibre or packet
(2^n-scale), enumerating split divisors (C(n,r)-scale), per-member
guard discharge, or any per-shell claim without either a ceiling
theorem (nothing above a) or an explicit shell-compatibility theorem
(per-shell caps do not compose: 35 + 7 = 42, mutation M7). Rationale:
finite oracles are brute-force trivial (the Brief-6 adversarial
mandate); every check must be poly(n, log q).

## 5. Operational q-independence (definition)

Fix H ~ Z/n by a generator. A packet is q-INDEPENDENT iff its index
family (a set of subsets of Z/n) and its cardinality formula depend
only on (n, k, template-id, index datum) — testable by replaying the
family in at least two characteristics (PK1: identical families over
F_17, F_41, F_97, F_9). A packet whose cardinality merely coincides
numerically while its members move with q is NOT q-independent and is
not certifiable under this contract (mutation M9: generic windows have
no template and their index families differ between q = 17 and
q = 41). SCOPE FACT (PK2, certified): within monomial windows,
q-independent packets exist only at codimension w = 1 (agreement
k+1); any w >= 2 claim must either carry its own q-uniformity theorem
or be certified per-field.

## 6. The B* = 0 scope pin

SAFE clauses hold verbatim at B* = 0. UNSAFE clauses at B* = 0 use
the trivial-sentinel convention of the banked frontier ledger; the
PK1 word class discharges the pin budget-uniformly (its packet
exceeds every B* < 2^128 once n >= 140 at rate 1/2, and its ceiling
gives the safe side at k+2) — no separate B* = 0 branch is needed
where a PK1-shaped instance exists.

## 7. Compliance obligations

- Every new certificate class must be run against the standing
  mutation suite (M1-M9, `notes/pilots_20260802/crossing_packet/
  verify_mutations.py`) and survive: the fence (M1), realizability
  (M2), gcd-guard splitting (M3), the w=2 q-dependence boundary (M4),
  section-vs-fibre inflation (M5), guard necessity (M6), shell
  compatibility (M7), the same-word traps (M8), and the
  no-template killer (M9).
- Frontier accounting per the ledger discipline: every certified
  claim prices itself on the U/S frontier ledger or is explicitly
  background (PK1 prices at zero — recorded, not hidden).
- Subtraction (hard law 5) before novelty claims: PK1's lower half is
  the rotated-prefix floor's boundary case (upstream #1101);
  contracts must cite dominated content as dominated.

## 8. The ask to Pro

(a) Attack the primitive set: is there a crossing claim shape the
lane will need that CANNOT be expressed with primitives 1-4 (e.g.
w >= 2 censuses, which PK2 shows are q-dependent — does the lane need
a per-field certificate mode, and can it stay succinct)? (b) Attack
the q-independence definition: is two-characteristic replay
sufficient, or can index families coincide at two characteristics and
diverge at a third? (c) Attack the counted-object primitive: can an
adversary smuggle a false count through an inequality chain whose
steps are individually checkable? (d) The scope question PK2 opens:
should the lane's frontier program accept per-field certification at
w >= 2, or is there a different word class whose w >= 2 packets are
q-free (the vanishing-sum clause suggests structured Lam-Leung
families as candidates)?
