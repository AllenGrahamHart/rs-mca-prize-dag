# wz_results.md — F-round 1 exact census tables (WCL-ZONE-COVERAGE)

Pre-registration: `wz_falsifiers.md` (written before any computation).
Enumerator: `wz_census_modal.py`. Evaluator: `wz_eval.py` (kill lines).
Raw shard JSON: `wz_shard_*.json`; full Modal stdout: `wz_log_*.txt`;
aggregate: `wz_eval_report.json`. All W_cl values are exact fractions
(`fractions.Fraction` end to end); floats appear only in the Poisson null
predictions, as pre-registered.

## Modal app ids (one per shard, all exit 0)

| shard | app id | wall |
|---|---|---|
| pc_l1 | ap-EGT6mwe7R5sK8EmWfwhDYg | 13s |
| pc_l2 | ap-R8iQ9npiNt04IxAyHJsyfx | 24s |
| band_a17 | ap-lzuLrOLJv9nJ3m1VQvEefp | 2.6s |
| band_a19 | ap-X3riXydaaEP0C5uOxS7VgM | 1.1s |
| band_a21 | ap-ijzCwK9SHCiLOw1Ia2P4Tk | 1.2s |
| band_a23 | ap-qr9Fn8aVKa6bUEgGfZzaqR | 0.8s |
| band_b10 | ap-8lbe2ylUL9GfKipJfCNe8A | 2.7s |
| band_b1214 | ap-j50GMQM12ytM1RwqLUIzZu | 5.5s |
| band_c | ap-VfsyjQHxuWjzKHK2MrBU4N | 11.8s |
| xcheck64 (b=25, vacuous) | ap-PLoKJQt2cyY41bdOY9ZtBb | 4.8s |
| xcheck64b (b=21, nonempty) | ap-jdHfKeAdXSR3BmyK8IXGJh | — |

## Integrity gates (all green)

- 12/12 banked M2 cells reproduce EXACTLY (all 60 primitive orbit counts
  and all 12 W_cl fractions of `m2_c1prime_level_scaled_results.json`), on
  BOTH engines (direct M2-shape and mitm).
- M-1 mutation control tripped: primitive-off w=6 orbit counts 4712 (q=193)
  and 224 (q=7937) match banked M1 full spectra and differ from primitive
  4497/126.
- M-2 shadow control tripped on real data: ternary-multiplier shadows found
  at q=7937 L=1 from the two w=3 owners (round-7 solver, exact Z verify).
- Lift control tripped and clean: 6 companion (q,N=32) orbits across the C
  cells, all 6 doublings found in the (q,N=64) primitive ledgers, 0 misses.
- Orbit-closure invariant: 0 flags across every cell (every signed shift of
  every found vanisher was itself found — nontrivial completeness check).
- Engine cross-check at N=64: direct == mitm at q=2100097 on a NONEMPTY
  census (64 signed w=5 hits = 1 orbit). The first attempt at b=25
  (q=33555073) matched on empty sets and is recorded as vacuous.
- Nonemptiness guards (#137): saturated bands A/b17 (48/48), B/b10 (12/24),
  C/b21 (10/10) all nonempty.

## Positive-control table (direct engine, banked comparison)

L=1, N=32: q=193 (0/3/46/529/4497, W_cl=5763), 449 (0/1/20/228/1981, 2525),
769 (0/0/10/144/1193, 1521), 1409 (0/0/4/79/660, 834), 3137 (0/0/2/33/294,
368), 5569 (0/0/1/17/153, 191), 7937 (0/2/8/31/126, 236), 12289
(0/0/0/9/71, 89). L=2, N=32: 193 (0/0/4/24/176, 120), 257 (0/0/3/15/92,
67), 449 (0/0/0/1/33, 35/2), 577 (0/0/1/3/19, 29/2). All == banked.

## Band tables (mitm engine; per-band aggregates)

Columns: n = primes ("first n primes q ≡ 1 mod n' >= 2^b"), nonempty =
cells with nonzero post-dedup primitive window ledger, Phat, Ppred = mean
1-exp(-lambda_orb(q)), rho = Phat/Ppred, Wbar = mean exact W_cl (exact
fraction), Epred = volume-null mean, rho_W = Wbar/Epred, exc = cells with
W_cl > 1/32 (== nonempty everywhere, see wz-C7).

### Family A: L=1, N=32 (n'=64), window w=2..6

| band | q range | n | nonempty | Phat | Ppred | rho | Wbar | rho_W | exc |
|---|---|---|---|---|---|---|---|---|---|
| b17 | 131713-149441 | 48 | 48 | 1.000 | .973 | 1.027 | 409/48 | 2.076 | 48 |
| b19 | 524353-544129 | 48 | 39 | .812 | .614 | 1.324 | 13/8 | 1.511 | 39 |
| b21 | 2097857-2117953 | 48 | 14 | .292 | .214 | 1.361 | 7/16 | 1.605 | 14 |
| b23 | 8388673-8411201 | 48 | 3 | .062 | .059 | 1.065 | 1/16 | 0.914 | 3 |

### Family B: L=2, N=32 (n'=64), window w=3..7

| band | q range | n | nonempty | Phat | Ppred | rho | Wbar | rho_W | exc |
|---|---|---|---|---|---|---|---|---|---|
| b10 | 1153-7681 | 24 | 12 | .500 | .310 | 1.615 | 9/16 | 1.689 | 12 |
| b12 | 4289-10369 | 24 | 5 | .208 | .087 | 2.395 | 1/6 | 3.097 | 5 |
| b14 | 17729-25409 | 24 | 1 | .042 | .009 | 4.648 | 1/48 | 3.970 | 1 |

(b10/b12 overlap in q because primes ≡ 1 mod 64 are sparse there; the
per-prime null makes this harmless, as pre-registered.)

### Family C: L=1, N=64 (n'=128), window w=2..6 (post lift-dedup)

| band | q range | n | nonempty | Phat | Ppred | rho | Wbar | rho_W | exc |
|---|---|---|---|---|---|---|---|---|---|
| b21 | 2100097-2105729 | 10 | 10 | 1.000 | 1.000 | 1.000 | 197/5 | 1.989 | 10 |
| b23 | 8390273-8398721 | 10 | 9 | .900 | .905 | 0.995 | 43/5 | 1.734 | 9 |
| b25 | 33555073-33570049 | 10 | 5 | .500 | .445 | 1.125 | 6/5 | 0.967 | 5 |
| b27 | 134219009-134227073 | 10 | 3 | .300 | .137 | 2.194 | 3/5 | 1.934 | 3 |

## Extremes observed (exact)

- Largest band-cell W_cl: **50** (C/b21, q=2103041: 25 primitive w=6
  orbits; shadow-dedup unchanged). Runners-up 48 (q=2101249), 44
  (q=2105729, dedup 42; q=2100353, dedup 34; A/b17 q=142529).
- Largest overall: PC q=193 L=1, W_cl = **5763** (banked, reproduced).
- Smallest nonzero band-cell W_cl: **1/2** (B/b14, q=21569, single
  primitive w=7 orbit `0:+1,1:-1,12:-1,16:-1,19:+1,25:+1,27:-1`).
- Every one of the 264 band cells: W_cl > 1/32 iff ledger nonempty
  (quantization equivalence, wz-C1/C7); minimum possible nonzero analogue
  mass is 1/2 at these aspects.
- Shadow de-dup largest effect: W_cl 4 -> 1 (A/b21 q=2107073, 5 links);
  C/b21 q=2100353 44 -> 34 (10 links). 221 links in A/b17 alone.
- Known accident prime q=7937 reappears at L=2 (B/b12): W_cl = 2, shadow
  dedup -> 1 (4 links).

## Kill-line outcomes (pre-registered section 4)

- **KILL-1a:** no trip. No band with Ppred <= 0.25 had Phat >= 0.75
  (closest: A/b21 Phat=.292 vs .214).
- **KILL-1b:** no trip. 673 distinct orbit keys logged across sub-volume
  cells; ZERO recurred at >= 3 primes (none even at 2).
- **KILL-2:** no trip. A: rho non-monotone (1.03, 1.32, 1.36, 1.06), top
  band at the null. C: non-monotone (1.00, 0.99, 1.12, 2.19), top
  Poisson-consistent (3 vs 1.37 expected, P ~ .15). B: rho IS monotone
  (1.62, 2.40, 4.65) and rho_W (1.69, 3.10, 3.97), but top/bottom = 2.88 <
  4 and the top band has 1 nonempty (< 3 required): no trip, flagged as
  the round-2 target (wz-C4).
- **KILL-3:** no integrity failure.

**VERDICT: SURVIVED** (see wz_report.md for weight and round-2 design).
