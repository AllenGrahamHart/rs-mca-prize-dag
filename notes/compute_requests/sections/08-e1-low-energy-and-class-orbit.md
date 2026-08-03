## E1 profile-(2,10), cofactor-1028 low-energy certification

**Status:** superseded by proof. **Do not launch.**

The proved node `e1_s18_m1028_energy4_cubic_exclusion` replaced all 8,385
resultants by a complete cubic-moment screen. Its maximum cubic index is 24,
which gives the exact norm deficit `512/729` and puts every type below
`1028*p_min`. The launcher may be retained as an optional independent audit,
but it is no longer authorized serial-path compute.

The proved route originally left `m=1028=4*257` at autocorrelation energies
`E in {2,3,4,5,6}`. Exact small screens showed:

```text
E=2: four 257-compatible Galois types, all Norm/1028 above p_max
E=3: 329 compatible types, all exact Norm/1028 above p_max
E=4: 8,385 compatible types, all diagnostic log norms below p_min
```

Historical launcher command, no longer required:

```text
~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/e1_profile210_m1028_e4_norm_modal.py
```

The launcher submits 60 first-lag shard calls to one 512 MiB container with a
60-second per-call limit, and rewrites a local checkpoint after every returned
shard. It uses nine trial-division-certified 31-bit primes and CRT to
reconstruct every exact degree-64 resultant below the `18^64` AM-GM ceiling.
This is the same engine already certified on all 329 energy-three types and
five independent Bareiss norms. The expected terminal census is `8385` exact
quotients, all below `p_min`. Preserve partial JSON if the run is interrupted.

Launch log, 2026-07-29: one launch attempt was rejected before any container
started because workspace `ac-WIsI8fedhlHGSBu0g8EiyG` had exceeded its spend
limit. No app id was allocated and no credit was spent. Do not retry on this
workspace until its spend limit is explicitly restored.

Energies two, three, five, and six no longer require computation. The proved nodes
`e1_profile210_m1028_energy2_log_exclusion` and
`e1_profile210_m1028_energy56_log_exclusion` use the integral
autocorrelation bound `sum |A_d|<=E` and exact logarithm bounds to put energy
two above `1028*p_max` and energies five/six below `1028*p_min`. Do not launch
support classifiers for them. The 329-type energy-three ledger is now an
exact CRT-resultant certificate with digest
`d462adc241981e2e3aa9747a5ba582808d8ebf505e2df6a86fdad2df52a7d3cc`.
The only unpromoted computation in this request is the energy-four
certificate above. Reuse the modular engine rather than the slower Bareiss
fleet. A useful independent replay is a direct degree-128 negacyclic
resultant implementation.

## E1 profile-(0,18) joint low-energy/root falsification probe

**Status:** superseded by class descent. **Do not launch on the serial
route.**

The active weighted route needs at most five occupied cofactor-514 ideals.
The conditional class-descent theorem now gives at most two from one exact
`Q(zeta_128)` class-orbit certificate, without enumerating collision
profiles. The route-deciding compute is therefore
`CR-E1-QZETA128-P257-CLASS-ORBIT` below.

Historical rationale follows. It remains useful only as an adversarial audit
if compute is donated after the class certificate is replayed.

The proved singleton-completion no-go shows that local multiplicity one and
`F(s)=0 mod 257` alone admit all 128 ideals. The first useful experiment must
therefore impose the all-singleton realization and live energy window
`E=5,...,10` simultaneously. The all-unit energy-eleven and energy-twelve
profiles are excluded analytically and must not be retained.

Staged launcher:

```text
~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/e1_profile018_m514_low_energy_root_search_modal.py \
  --shards 16 --seconds 55
```

Resource cap: 16 containers, one CPU and 256 MiB each, at most 55 search
seconds per shard under a 70-second hard timeout. This is under 15 aggregate
CPU-minutes and is intended to remain well below `$1`; verify current Modal
pricing before launch. Every shard returns its best state even with no hit,
and canonical hits are retained in the final JSON.

Interpretation is deliberately narrow:

- a hit proves that the joint realization/root/energy gate is nonempty;
- no hit is heuristic evidence only and proves no emptiness statement;
- neither outcome proves or refutes five-ideal occupancy;
- the retained-hit filter omits the analytically excluded magnitude profiles
  `(9;1,2,0)`, `(10;6,1,0)`, and `(11;7,1,0)` while allowing the annealer to
  traverse them;
- exact resultant computation and grouping by `p=Norm/514` is a separate
  second stage, authorized only after genuine canonical low-energy hits;
- six equal exact official-prime quotients in distinct diagonal Galois orbits
  would be a true falsifier.

## CR-E1-QZETA128-P257-CLASS-ORBIT: J_63 fixed-field certificate - CLOSED

**Status:** RESOLVED LOCALLY; DO NOT LAUNCH. The exact Jacobi-sum residue
certificate supersedes the proposed degree-32 BNF computation.

### Mathematical decision and interface

The original 17-primary test is closed:

```text
J_65=(257,zeta_128-9)(257,zeta_128-248)
```

is nonprincipal by `e1_qzeta128_p257_j65_harbater_nonprincipality`.
Dembele's published Hilbert-class-field polynomial is irreducible modulo
257. Do not recompute this half.

Put

```text
beta=zeta_128-zeta_128^(-1),
E_63=Q(beta),
p_66=(257,beta-66).
```

Use the exact defining polynomial

```text
f_E63=Y^32+32Y^30+464Y^28+4032Y^26+23400Y^24+95680Y^22
      +283360Y^20+615296Y^18+980628Y^16+1136960Y^14
      +940576Y^12+537472Y^10+201552Y^8+45696Y^6
      +5440Y^4+256Y^2+2.
```

The repository verifies that it has 32 distinct roots modulo 257 and that 66
is one of them. It is obtained from
`Res_Z(Z^64+1,Z^2-YZ-1)=f_E63(Y)^2`.

The repository now certifies unconditionally that `p_66` is nonprincipal in
the degree-32 field `E_63`. Exact contraction gives
`p_66 O_(Q(zeta_128))=q_1q_63`; the ambiguous class-number calculation proves
that `E_63` has odd class number, so this transfer is injective on ideal
classes.

The certificate proves the last premise of
`e1_qzeta128_p257_two_involution_nonprincipality_certificate`; the 2-group
reduction promotes the 64-prime class orbit, class descent, and exact
profile-018 payment.

The proof constructs a 32-term Jacobi product `alpha` with
`(alpha)=(q_1q_63/(q_127q_65))^(2*21121)`. At
`r=5406977=256*21121+1`, a product of 32 power-residue characters kills the
full unit group and all `21121`st powers but maps `alpha` to `500235 != 1`.
Direct-character-sum and coefficient-polynomial verifiers agree.

### Superseded historical primary packet

The following BNF packet is no longer requested. It remains a possible
independent audit only:

1. construct `E_63` and its full ring of integers;
2. construct `p_66` and check that roots 9 and 57 both give fixed-field
   residue 66;
3. certify `p_66` nonprincipal unconditionally;
4. emit its exact nonzero class coordinate, certified class-character image,
   or another proof-producing obstruction, together with software versions,
   commands, relation data, and immutable hashes.

A direct PARI/GP primary should use a defining polynomial and integral basis
for the degree-32 fixed field, followed by:

```text
B = bnfinit(f_E63,1);
bnfcertify(B) == 1;
P = idealprimedec(B,257);
\\ identify p_66 by beta=66 in its residue field
\\ test bnfisprincipal(B,p_66,0)
```

The packet must check `#P=32`, the fixed-field identity, and one nonzero
certified class coordinate. The default `bnfcertify(B)` is required.
`bnfcertify(B,1)` only certifies that the true class group is a quotient of
the computed group and is insufficient for nonprincipality. Pin the PARI
version and official function contracts.

An alternative focused route may construct a certified ideal-class character
that is nonzero on `p_66`. `subcyclopclgp(128,21121)` can rigorously certify
the relevant minus-part size, but does not locate this ideal and is
insufficient alone. A class group computed under GRH is `INCOMPLETE`.

### Independent audit - satisfied

The primary verifier evaluates every Jacobi sum directly at all auxiliary
embeddings. The audit independently builds coefficient polynomials and
re-evaluates them. Both obtain `Psi(alpha)=500235`.

### Resource law

No container launch is authorized or needed. Both exact verifiers run in
well under one second with negligible memory.

Semantics:

- `PASS`: achieved - unconditional `p_66` nonprincipality plus independent
  exact audit;
- `FAIL`: an exact principal generator for `p_66`;
- `INCOMPLETE`: timeout, GRH-only output, unresolved principality, or one
  implementation only; evidence with no DAG status change.
