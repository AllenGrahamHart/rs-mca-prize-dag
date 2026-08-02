# Pro's adversarial self-audit of the Brief-5 (F2) dossier — 2026-08-01

> **Provenance:** Pro's adversarial audit of its own F2 dossier (same
> thread), relayed by the maintainer. Checker:
> `verify_adversarial_audit_brief5_f2.py` (replayed under ramguard, all
> nine fixtures PASS). **Fable verification:** the hidden-modulation
> scale, slice reversal, 2p Myhill-Nerode bound, and the carry-DFT
> product identity re-derived by hand. **Addendum recorded on
> `BRIEF5_DOSSIER_AUDIT.md`.** No DAG changes; nothing minted (the
> carry-DFT identities are abstract-model exact — the F2 bijection F2A.1
> is the unproven seam, same precedent as the C2'' nullity route).

## Retired (with exact fixtures)

The spine "first descent -> bounded carry compression -> block transfer
matrices -> one bit per 43 coordinates -> owners -> transport":

- **Hidden modulation reinterprets the 1/3 target:** w = 1 + 2^(-m/6)
  epsilon (full parity) saturates 2^(m/3) EXACTLY while every proper
  weight marginal is constant 1 and every below-full-degree sign Fourier
  coefficient is zero. The target is weak in exponent but requires
  excluding joint bias at scale 2^(-n/6) — invisible to every local,
  bounded-degree, or finite-depth test. Doubling delta violates the
  target while max/mean stays 1 + 2^(-m/6+1).
- **The slice reversal (the most severe fence):** epsilon = (-1)^|x| has
  full-cube alignment ZERO but is CONSTANT on every Hamming slice —
  sqrt(C(60,30)) ~ 2^28 at the central slice. Full-window theorems are
  logically useless at fixed b; the campaign's b-resolved satellite was
  a type guard, not decoration.
- **Bounded carry compression is generically impossible:** the carry
  square wave on Z/(2p) has NO merging pair of residues (the
  half-interval has no translation stabilizer), so the exact automaton
  needs all 2p ~ 2^32 states — 2p(b+1) at fixed size. PP5.4 is re-typed:
  prove a severe restriction on the reachable continuation sumset, or
  compression is dead. Also strategic: epsilon*exp(S) is ONE real
  cyclotomic product — the carry may be a coordinate artifact.
- **Pairing needs exponential precision** (eta <= sqrt(2)*2^(-m/6)); the
  chamber route hits order-p complexity even in dimension one; proper
  order-two sector marginals can all be flat while the full interaction
  is maximal (transport is its own theorem); coherent sectors cost
  sqrt(s) (2^20 sectors = 10 bits — PP5.0 must print s); unit structural
  drift per orbit at M = 2^40 costs 2^20 (the j=4 correction was
  load-bearing).

## Retained

The executable target (weighted parity alignment), PP5.0 as the absolute
gate, the exact toy compilers, structural-drift bookkeeping, orbit and
stabilizer quotienting, the falsifier programme.

## The salvage route: diagonalize the carry, don't compress it

Exact carry DFT: hhat_p(k) = 0 (even k), 4/(1 - e^(-pi i k/p)) (odd k) —
all p odd modes nonzero (no sparse compression) but normalized L1 mass
only logarithmic. State-free product identity (verified on a toy):

  A = 1/(2p) sum_k hhat_p(k) prod_i M_i(k),
  M_i(k) = sum_tau (-1)^u_i a_i e^(pi i k s_i / p),

with the local contraction dial |M|^2/(a+b)^2 = 1 - [4ab/(a+b)^2]
sin^2((alpha-beta)/2): weight BALANCE times PHASE SPREAD, per mode. The
theorem shape: every nonstructural odd mode accumulates linear
contraction, or has one finite algebraic resonance owner. Typed as
DIFFERENT from the closed E3 Fourier no-go (one-dimensional transform on
the carry residue, not the census-frequency space) — a hypothesis to
audit, not assert.

**The new central black hole: the b-resolved slice coefficient theorem.**
Fixed size forces a generating variable z in every multiplier and
coefficient extraction couples all local choices; crude contour bounds
recreate the annealed loss. A full-window mode theorem without the slice
version is worthless (the slice-reversal fence).

## Posture

Conditional exploratory GO for F2A.0-F2A.4 only: PP5.0 seam; exact
bivariate first-descent normal form (CF-5); carry reachability audit
(decides compression vs DFT definitively); exact carry-DFT node; mode
contraction compiler with balance/phase-spread fields. Kill lines K1-K7;
K2/K4/K5 (generic modes fail to contract / order-p bad-mode classes /
coefficient extraction loses a linear exponent) retire the strategy.
Mutation battery gains: the hidden-modulation trap, the Hamming-slice
trap, and the exponential-pairing-precision fixture.

## The pattern (three adversarial rounds)

Third instance of the same structure: local/bounded statistics cannot see
a full-degree/global object; the replacement is an exact diagonalization
of the global obstruction (doubling cycles for C1; cross-junction nullity
for C2''; the carry DFT for F2). Each round also produced a sharpened
statement of what the empirical evidence can and cannot certify — here,
that no enumeration can probe correlation at the 2^(-n/6) scale the
finite target actually demands.

> **[AMENDED 2026-08-02 — F2A.5 slice pilot
> (`notes/pilots_20260802/f2_slice_coefficients/`, 11/11 + 3/3 exact
> validations, coordinator-replayed).]** The b-resolved object has an
> exact per-mode product form governed by one new invariant: the
> modified difference multiset Delta_i = sigma_i^+ - sigma_i^- in
> Z/2p, with phase law arg r_i(k) = pi*k*Delta_i/p. Consequences
> BINDING on F2A.2/F2A.4 as adopted above: (1) Sharp Law A
> (full sumset = Z/2p) does NOT survive b-resolution — fixed-b
> reachability is governed by the difference subgroup
> D = <Delta_i - Delta_j>, and the reachability audit must be re-run on
> D; (2) the F2A.4 exceptional-owner list is Ann(D), strictly larger
> than Ann(G), and the k=p pair-contraction health criterion from
> resonance.py is exactly INVERTED at fixed b (all-odd-Delta windows:
> maximal full-window contraction, slice floor pinned at 1/p via
> hhat_p(p)=2); (3) the slice theorem cannot be uniform over coordinate
> subsets (half the coordinates at every frequency carry odd Delta) and
> needs a parity-inhomogeneity hypothesis, phase-SPREAD (not alignment)
> formulation, and normalisation by log2 C(n,b). The hidden-modulation
> fence is VISIBLE at slice resolution (extremal modulation is uniquely
> the parity — fences (i) and (ii) are one object), so the black hole
> is a PRECISION problem, not a blindness problem. The 1/3 budget is
> marginal on generic windows and dead on parity-homogeneous ones
> (fails at n > 3*log2 p, ~93 coordinates at official scale). Slope
> caveat: cancellation slopes ride the balanced-weight integer proxy;
> the structural laws are exact with true weights.
