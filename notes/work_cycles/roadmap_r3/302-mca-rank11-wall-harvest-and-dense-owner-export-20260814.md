# Cycle 302: MCA rank-11 wall harvest and dense-owner export (2026-08-14)

The canonical prize tree advanced to `659319780` while this worktree was on
the later Shape-A branch. Its intervening review commit imported upstream PR
`#1168` as the proved route-cut node
`rate_half_mca_rank11_pair_core_route_cut_import` and wired it as evidence to
`rate_half_band_crossing_location`.

The import was reconciled here at commit `3782181f6`. Its primary replay and
independent `L(19737)` recomputation pass:

```text
RANK11_PAIR_CORE_ROUTE_CUT_IMPORT_OK wall_excess=538948390820518297
RANK11_WALL_AUDIT_OK L(19737)=808527428378681053
```

An independent local derivation had reached the same exact-layer profile and
the same optimum total

```text
813929118931913384
```

before the upstream sweep. This is overlap, not a second theorem, so no
duplicate DAG node was minted. The route decision is sharper: almost the
entire current miss is the deficiency-one pair-core layer, and #1168 already
pre-registers the required escape as a same-line cross-pair coupling theorem
or a chronology-correct owner for dense parallel pair cores.

The user-ratified coordinator directive was then executed as Package A on a
fresh branch stacked on exact #1168 head
`6a5dcdae1591fc7f044eda6a942bfe178521a48c`:

```text
worktree: /home/u2470931/smooth-read-solomin/
          rs-mca-codex-dense-core-owner-post-1168-20260814
branch:   codex/kb-dense-core-owner-substrate-post-1168
head:     b4bad860750f91955dbaead8f2b5a0fdef1f1343
status:   clean, READY-BUT-UNPUSHED for coordinator audit
```

The packet vendors four public, exact-commit/tree-pinned proof nodes in
Przemek's terminology:

1. separate-`2w` reserve repricing, with the exact target
   `B*-(2w+31)-(n-g)` and both endpoint rows;
2. the explicit `(1_E,X^k)` counterexample to silent `k -> k+1` badness and
   owner transport;
3. the exact degree-`<k` shifted-lattice guard plus executable same-support
   pair-noncontainment test;
4. the typed deployed pole-line witness, retaining Q, BC, and `U_new` as
   `UNASSIGNED`.

The bridge to #1168 is an acceptance contract, not an owner claim: any S/A/E
chronology owner for the forced `delta<=4`, `200632`-slope terminal must meet
the repriced target, preserve the actual line/support/slope chronology, pass
the degree and pair tests, accept the typed pole line, and reject the
unguarded transport mutation.

Verification at the unpushed head:

```text
primary:     PASS (36015 toy records; official endpoints; d1=67473)
mutations:   PASS 8/8
independent: PASS 4/4
TeX:         PASS, 123 pages
git diff:    clean/check PASS
```

The public source commits were confirmed reachable in
`AllenGrahamHart/rs-mca-prize-dag` before pinning. No Modal computation was
used. The critical census and deployed ledger are unchanged.

```text
start:                   8fb5d52d4
result:                  #1168 wall harvested; guarded dense-owner substrate
                         packaged at b4bad8607
DAG delta:               +1 PROVED imported route-cut node, +1 evidence edge
critical status delta:   none
upstream terminal delta: owner interface repriced and witness-sound; owner
                         existence/chronology theorem remains open
delta-star movement:     none
compute:                 exact local arithmetic only; no Modal spend
next route action:       coordinator replay/push Package A, then attack the
                         same-line cross-pair/chronology theorem against the
                         shipped acceptance contract
```
