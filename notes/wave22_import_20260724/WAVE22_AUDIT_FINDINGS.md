# WAVE-22 fresh-context replay audit — v10 pin 22c4aab7

## 0. Pin verification
- v10 worktree: /home/u2470931/smooth-read-solomin/prize-codex-resolution-v10-20260722
- HEAD = 22c4aab7 "Cancel the order-one zero-value resultant factor" — MATCHES expected pin.
- Working tree clean except ONE untracked folder: background/nodes/l1_mersenne_hnf_colored_frobenius_gate/ (post-pin WIP, OUT OF SCOPE per brief — noted only).
- master (prize repo) = 85c9e5ae (wave-21 integrate). merge-base(v10, 85c9e5ae) = 85c9e5ae — NO lineage skew. Range = 47 commits (verified: git rev-list --count = 47).
- Tree archived to w22_tree/; dag.json sha256 e5c3c71e...537 identical worktree vs archive.

## 1. v9 SUPERSESSION — verdict: SUPERSEDED BY DIRECT ANCESTRY (not re-expression)
- v9 worktree HEAD 7af70a09, branch point 03116dee (wave-20), 33 commits.
- 7af70a09 IS AN ANCESTOR of 22c4aab7: v10 contains v9 via merge commit 59cc9b1b
  "Integrate Mersenne checkpoint campaign onto Wave 21" (parents 85c9e5ae + 7af70a09).
- v10 range 47 = 33 v9 commits + merge + 13 post-merge commits.
- Mechanical file check: all 314 v9-touched paths present in v10. 0 MISSING. 14 differ
  (post-merge evolution): dag.json, manifests, notes, orbit renders, l1_mixed_petal_amplification
  statement/attack, and ONE v9 node edited at merge time:
  - l1_coarse_pfree_tame_tail_distance_upgrade: consumer edge re-targeted at merge
    from l1_official_first_checkpoint_split_pencil_reduction -> l1_coarse_pfree_wronskian_neighbor_compiler
    (statement.md + verify.py + dependency_subdag.md). RESOLVED SOUND: the merge adopted master's
    wave-21-ratified bytes EXACTLY (blob-identical to 85c9e5ae for all three files) — v9 had been
    written against the pre-wave-21 node set; no content was invented at merge time.
- NOTHING in v9 needs separate import.

## 2. DAG delta base(85c9e5ae) -> pin(22c4aab7) — CONFIRMS pre-check
- base raw 1194 nodes / 2811 edges (2810 unique; ONE pre-existing duplicate edge
  petal_descent_classification_bridge -> petal_g1_k4_scale_reserve [ev] x2 — present in BOTH base and pin, pre-existing wart, not new).
- pin 1222 / 2884 raw (2883 unique). Delta: +28 nodes (ALL status=PROVED), 0 removed, 0 status flips,
  +73 unique edges, 0 edges removed, 0 non-status field changes on surviving nodes.
- Node composition: 20 l1_m4_h3_* + 1 l1_m4_positive_value_coset_certificate + 7 l1_mersenne_*.
  (Brief's "L1 20 / Mersenne-Belyi 8" = the 20 m4_h3 strata nodes vs the 7 mersenne_* + 1 m4 coset cert.)
- Edge structure: every one of the 28 new nodes sends exactly one [ev] edge into
  l1_mixed_petal_amplification (in-deg 89 -> 117 = +28, exact). All [req] edges either run among
  the 28 new nodes or FROM three old PROVED suppliers INTO new nodes
  (l1_official_broad_checkpoint_frobenius_periodicity_exclusion, l1_official_max_split_value_complement_census,
  l1_official_split_pencil_value_capacity). NO new req edge lands on any red/amber — no req-smuggle at edge level.
- l1_mixed_petal_amplification REMAINS TARGET (statement ends "...so this node remains TARGET").
- File diff master->pin: 300 added (28 node dirs x10 files + 20 experiments files), 8 modified
  (mixed_petal statement/attack, dag.json, verifier_replay.json, PRIZE_COMPUTE_REQUESTS.md,
  PRIZE_RESOLUTION_ROADMAP.md, KB_LOG.md, verifier_manifest.json), 0 deleted. No rewrites of
  master-held statements other than the consumer's additive closure section.

## 3. Campaign identity (priority 1a) — first-checkpoint NINE-ROWS lane, internal L1 work
- "Mersenne" = the nine surviving first-checkpoint rows have n=m(p+1), m in {4,8,16}, with p the
  Mersenne primes 8191(2^13-1), 131071(2^17-1), 524287(2^19-1), 2147483647(2^31-1=M31).
- "Belyi" arises INTERNALLY: the next-to-maximal residue is a degree-p polynomial Belyi map with
  critical values 0,1 (residual normal form), plus a Belyi-style normalization inside the (2,1)
  positive stratum (nu2 nodes). This is Track-C ("Track-C checkpoint refinement (proved, 2026-07-22)"
  header in roadmap) — the wave-21 first-checkpoint nine-rows residual lane, NOT a new lane.
- Upstream convergence/vendoring: see §upstream below.

## 4. What "Close the constant Mersenne cubic endpoint" closes (priority 1b)
- 7af70a09 adds l1_m4_h3_nu0_h0_auxiliary_fiber_exclusion + l1_m4_h3_nu0_h0_universal_packet_exclusion.
- It closes the constant (deg H=0), nonzero-b, nu=0 ENDPOINT stratum of the m=4,h=3 cubic branch:
  (i) universal packet (A,B)=(6,20) excluded on every characteristic by an Euler p-th-power
  multiplicity contradiction; (ii) the exceptional packet (844833809,2002167159) on p=2147483647
  excluded because the normalized shifted cubic would divide W^(4(p+1))-1 but the exact remainder
  is the nonzero constant 876663072. Result: entire nonzero-b deg H=0 endpoint empty on all four
  characteristics.
- NO DAG object flips: "close" = a stratum-emptiness theorem born as new PROVED background nodes;
  the aggregate l1_m4_h3_official_emptiness (added later by db3b1828 "Package official m4 h3
  emptiness") packages the exhaustive case split as a first-class green node. Consumer stays TARGET.
  Consistent with pre-check "0 flips".

## 5. L1 continuation verdict (priority 2)
- Which lane: ONLY the first-checkpoint nine-rows lane (wave-21 residual (ii)). Coarse, exact-shell,
  and F2-bridge lanes are untouched in this range (base->pin delta contains no coarse/exact/bridge
  nodes; v9's coarse commits were already in wave-21 master).
- Nine rows (verbatim from CR-L1-MCP table): (32768,8191,m=4) (65536,8191,8) (131072,8191,16)
  (524288,131071,4) (1048576,131071,8) (2097152,524287,4) (4194304,524287,8)
  (8589934592,2147483647,4) (17179869184,2147483647,8); n=m(p+1) arithmetic re-verified by hand.
- Do any of the NINE rows close? NO full (n,p) row closes. What closes is the ENTIRE m=4,h=3
  STRATUM on all four m=4 rows (l1_m4_h3_official_emptiness: "there is no first-checkpoint split
  pencil with exactly three complete degree-p fibers"). m=4 rows are thereby reduced to
  nonembedded h=2 only.
- Exact new residual, VERBATIM (consumer statement): "This closes m=4,h=3, not the full
  first-checkpoint endpoint. The exact residual is nonembedded m=4,h=2, the m=8 rows with
  2<=h<=7, and the single m=16 row with 2<=h<=15, after prepaying every embedded antipodal pair."
  Plus (aggregate node): "It does not classify nonembedded m=4,h=2, treat m=8,16, treat width
  above p, or close L1."
- Consistency with wave-21 strata: wave-21 residual (ii) said "nine rows ... plus uncontrolled
  widths t>p"; pin says "These theorems concern only the t=p first-checkpoint endpoint. They do
  not pay wider exchanges, the primitive coprime split-pencil census, or the full L1 exact shell,
  so this node remains TARGET." — t>p still open, no smuggle. In-deg 89->117 all [ev].
- The m4h3 chain (line-by-line spot-read of nu0_h3_tangent_multiplicity_exclusion proof.md:
  local-order comparison ord_x(correction)=2e+d+eps-1 > e for e>=2, phi'(y_0)!=0 exact order e,
  cubic H-kappa => r<=3 roots, multiplicities sum to deg T=p => p<=9 contradiction — SOUND).
- Independent third-path recomputation (my own code, not the repo's): companion/modular powering of
  W^(4(p+1)) mod P_A over F_(2147483647) gives (876663073,0,0) => remainder of W^N-1 = 876663072,
  matching both in-repo replays (verify.py modular powering + verify_audit.py companion matrix).

## 6. Mersenne-Belyi tail residuals (priority 1c) — verbatim disclaimers
- exceptional_reduction: "This is a strict reduction, not an emptiness theorem."
- belyi_shifted_value_gate: "the exact endpoint residue is genuinely non-prime-field normalized;
  the z=0 chamber is also empty by a direct local-order contradiction."
- hypergeometric_normal_form: "the remaining next-to-maximal outer classification is
  low-dimensional, but neither intersection is yet proved empty and no inner degree-p lift is
  supplied."
- hnf_frobenius_reciprocal_gate: "The identity is only necessary, so retained components still
  require the original cyclotomic and inner tests."
- hnf_order_one_frobenius_gate: "A retained component is only a necessary candidate"; contract
  open residue = "Components of the bounded system, the actual Frobenius/cyclotomic tests, and
  any inner lift"; excluded scope = "Order zero, lower h, m=4,h=2, wider widths, and full L1."
  "This gate does not assert that the bounded system is empty, treat order zero or lower h, or
  promote L1."
- 22c4aab7 ("Cancel the order-one zero-value resultant factor") adds NO node: it strengthens the
  order-one gate in place — "The known zero split value contributes an automatic factor, which is
  cancelled before saturation; the resultant system therefore has degree h-1, not h."
- Pilot disclaimers: CP-SAT "(INCOMPLETE) ... It supplies no mathematical evidence"; FRG-SAT-P31
  "Status is INCOMPLETE: there is no unit/nonunit result and no mathematical evidence";
  HNF-TOY-GCD "calibrates the proposed gcd route but proves nothing on an official
  characteristic"; (32,7,4) analog "this is evidence, not an official-row exclusion."

## 7. Upstream question (priority 1a cont.)
- notes/correspondence/UPSTREAM_IMPORT_LEDGER.md exists; NOT touched in range. No commit in range
  touches notes/correspondence/ or any import ledger. No new proof.md references upstream.
- UPSTREAM_HARVEST.md and UPSTREAM_IMPORT_LEDGER.md contain ZERO occurrences of
  "Mersenne"/"Belyi": upstream's M31 lane objects (M31 MCA / M31 list / M31 CIRCLE) share only the
  number 2^31-1 with this campaign; word-level overlap is coincidental. Nothing is vendored FROM
  upstream; attribution obligations: none triggered.
- Direction is OUTBOUND: new nodes' upstream_crosswalk.md files translate results into upstream's
  split-pencil-census vocabulary for future vendoring (e.g., official_emptiness: "the packet
  should be vendored with the depressed-pencil/Euler reductions and the three terminal local
  exclusions"). Convergence-track only in that outbound sense.

## 8. Governance (priority 3)
- "Record deferred Frobenius saturation request" (18602f80) = adds pre-registered bounded pilot
  FRG-SAT-P31 (1 CPU / 2 GiB / 120 s hard stop) + its launcher + INCOMPLETE result + CR update
  deferring the real saturation to contributors ("A contributor should use Singular, Magma, or a
  structure-aware two-variable elimination"). No status impact.
- $1/5-min law: explicit in ledger — "stop if the projected total is at least $1 or five minutes
  on the current account"; NMCE "must be delegated rather than launched on the current account";
  M4H2-C31 "must not run on the current account"; A8 "must not run on the current account".
- Modal launches in range (8 apps, 4 launchers, all bounded pilots, all disclosed):
  1 ap-X9B0VIv80tdRxDSfYnkG9o  l1_mersenne_checkpoint_analog  (32,7,4) full 3,365,856-subset census - complete
  2 ap-mLyev4aS4qOOhZhKqcpK5i  same launcher, classifier rerun - all 16 pairs embedded antipodal
  3 ap-31urbcd0fvVu1adNueXzSz  two_schur_cpsat  model-error repair 1
  4 ap-cwwCYjpZqT2nwd3vKu4XD6  two_schur_cpsat  model-error repair 2
  5 ap-m2tOKpIdLfCZOzoRUmRkyQ  two_schur_cpsat  validated run, hit 60-s cap - INCOMPLETE
  6 ap-zbyPpAZamkVE3AlXYQJzov  hnf_toy_gcd  setup failure (SymPy coercion) - no output
  7 ap-gT0DyToHmnD911PEFFilTd  hnf_toy_gcd  corrected retry - 2.805886 s, gcd=s-1, unit quotient
  8 ap-0EK5ErTdMIAYixk0Leq78F  frg_saturation_pilot  timeout at 120 s Groebner - INCOMPLETE
  All within pre-registered per-pilot authorizations incl. the "one corrected retry" clause.
- CR ledger delta: NEW CR-L1-MCP (parent, contributor request, launch-gated), CR-L1-MCP-A8
  (order-64 falsifier, outbound), CR-L1-MCP-NMCE (delegated, unknown-cost), CR-L1-MCP-M4H2-C31
  (nonembedded order-128 falsifier, outbound); RETIRED: CR-L1-MCP-C31, CR-L1-MCP-NU2,
  CR-L1-MCP-NU0-H0 (all retired BY THEOREM with "do not rerun/launch" fences).
- r3 pointer compliance: track named ("Track-C checkpoint refinement (proved, 2026-07-22)");
  falsifiers named and pre-registered (A8 "next useful donated-compute falsifier"; M4H2-C31
  "exact finite falsifier"; both pilots "Pre-registered bounded analogue pilot"). COMPLIANT.
- KB_LOG: master ends #149; pin adds #150-#180 (31 entries) — numbering CONTINUOUS, no wave-21-style
  collision (merge reconciled v9-side numbering).

## 9. Integrity battery
- Pin validator: tools/run_all_verifiers.py on archive: VERIFIER_MANIFEST_PASS scripts=1114
  remote_launchers=14 proof_assets=1430; --self-test RUN_ALL_VERIFIERS_SELF_TEST_PASS
  negative_controls=6/6.
- Replay battery (honest counts): 62 new/changed scripts in range = 56 node verify*.py (28x2) +
  6 experiments checkers; 4 *_modal.py launchers EXCLUDED. Result 62/62 PASS under ramguard tiny
  (max 2.65 s, l1_m4_h3_nu0_h0_projective_quarter_certificate/verify.py). 0 FAIL 0 TIMEOUT.
- Manifest delta: +112 entries = 28 nodes x 4 (statement/proof/verify/verify_audit). Launchers in
  experiments/ are outside manifest discovery scope by house convention (registry holds only
  node-tree verify_*_remote.py; 14 unchanged).
- verifier_replay.json at pin: per-wave scratch convention, 4 PASS entries only — full battery here
  compensates; regenerate at integration.
- Mutation controls (scratch copy, 6 designed, 6/6 killed):
  M1 status flip official_emptiness->TARGET => its verify.py FAILS.
  M2' delete ev edge cartier_resonance->mixed_petal => verify.py FAILS.
  M3 statement constant 876663072->876663073 => anchor check FAILS.
  M4 verify.py EXPECTED_REMAINDER tamper => FAILS (verifier genuinely recomputes).
  M5 delete req edge value_capacity->embedded_m2_family => verify.py FAILS.
  M6' manifest scripts-hash tamper => VERIFIER_MANIFEST_FAIL rc=1.
  (Original M2 on the order-one gate PASSED — exposing the wiring-pin gap below; original M6 was a
  harness error on my side, corrected.)

## 10. Pin lists
- CONSUMER BRACKET (117): NO verifier pins the total in-degree numerically. The bracket is pinned
  DISTRIBUTIVELY: 105 verify*.py scripts reference l1_mixed_petal_amplification, each asserting its
  own edge (+ consumer state); 25/28 new nodes assert their [ev] edge.
- WIRING-PIN GAP (flag): 3 of the 28 new nodes have NO dag.json assertions anywhere in their
  verify.py/verify_audit.py (pure math replay + text anchors only), and no other verifier reads
  them: l1_mersenne_next_to_maximal_hypergeometric_normal_form, l1_mersenne_hnf_frobenius_
  reciprocal_gate, l1_mersenne_hnf_order_one_frobenius_gate. Their PROVED statuses + 5 edges are
  machine-unguarded (math itself replays PASS). Recommend adding wiring assertions at import.
- MARKER-PINS carried forward intact (spot-grepped): atlas 59=33+10+16; nine rows n=m(p+1)
  m in {4,8,16}; n/2 antipodal pairs at depths p,p+1; floor(n/p)<=23 / 253 pairs; NEW wave-22
  constants: BCH window N+1<=weight=2N-2; two residue classes mod gcd(2b,m); eliminant degrees
  3,2,1,0 for nu=0..3; (A,B)=(6,20) + (844833809,2002167159); P_A coefficients
  (1800058023,664831389,573306971); remainder 876663072; deg T=h-2; deg(XR')=p-m; (c-1)^n=1;
  zeta=d^(p+1) in mu_m; degree h-1 after cancellation.
- REVERSE-CONSUMER-PINS / superseded statements: the 4 wave-21-superseded f3_h3 statements
  (pgl2_pair_identity, mobius_excess_half, dsp8_correlation_bound,
  quotient_galois_orbit_scalar_decomposition) are byte-identical master<->pin (no file in range
  touches f3_h3); NOTHING in the range reads them.
- Protected state: ceremony/descriptor/dli/bridge/N11 — zero files in range match; dag delta shows
  0 flips and 0 non-status field changes on all 1194 surviving nodes => wave-20/21 ratified state
  (bridge PROVED at re-posed scope, ww retirement, N11 sweep, L1 checkpoint campaign) INTACT.

## 11. Refusals / holds
NONE blocking. Flags (non-blocking):
1. Wiring-pin gap on the 3 newest gate nodes (see §10).
2. Contract-format drift: 0/28 new claim_contract.md files carry an explicit "## Falsifier"
   section (wave-21 nodes have them); the new table format carries "open residue"/"excluded
   scope" instead, with campaign falsifiers pre-registered centrally in CR entries. Harmonize or
   ratify the format at import.
3. Orbit renders (orbit/critical_orbit.html, both SVGs) are byte-identical to master =>
   STALE wrt the 28 new nodes. Regenerate + republish site at integration (standing rule).
4. verifier_replay.json per-wave scratch covers 4/62 (convention; compensated here).
5. Untracked post-pin WIP folder background/nodes/l1_mersenne_hnf_colored_frobenius_gate/
   (out of scope, not part of 22c4aab7; do not import).
6. Pre-existing duplicate edge petal_descent_classification_bridge->petal_g1_k4_scale_reserve
   (master hygiene, unchanged).
No packaging flips (all 28 born PROVED with self-contained proofs; the only "close"/"Close"
language refers to strata inside the reduction, statuses honest). No req-smuggle (no new req edge
into any red/amber; consumer edges all [ev]; consumer remains TARGET). No silent discharges. No
rewrites of master-held statements (consumer edits are additive closure section; the one v9-node
rewire at merge ADOPTED master's ratified bytes exactly).

## 12. Import spec
- Topology: master 85c9e5ae is an ANCESTOR of 22c4aab7 => integration is a FAST-FORWARD (no
  cherry-pick, no union-merge). v9 needs no separate import (fully contained).
- At integration: (a) regenerate orbit HTML/SVGs + publish site (standing rule); (b) regenerate
  full verifier_replay.json; (c) optionally add dag-wiring assertions to the 3 gate nodes and
  falsifier sections to the 28 contracts (or ratify formats); (d) exclude the untracked WIP folder;
  (e) KB numbering needs NO renumber (150-180 continuous after master's 149).
- Post-merge expected state: 1222 nodes / 2884 raw (2883 unique) edges; l1_mixed_petal in-deg 117;
  0 flips.
