# Cycle 119: near-rational support-wise two-anchor repair (2026-08-11)

## Cycle pins

```text
our start:       a1ed95f27
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
upstream PRs:    39 open through #1160
compute:         local tiny verifier only
critical open:   28
```

## Harvested repair

Upstream PR `#1160` closes the exact gap left by our proved pair-proximity
node and REFUTED support-wise sibling. For `m=K+w`, `w>=1`, and
`3w<=n-K`, two anchors put every near-codeword residual on a common support
of size at most `2w`. Minimum distance identifies all near codewords with
the anchor codeword line. The actual bad witness support then injects its
slope into one coordinate ratio on that common error support. Hence

```text
N_near-rational,support-wise-MCA-bad <= 2w.
```

An independent smooth `RS[F_17,F_17^*,8]`, `w=2` regression has two bad
slopes while every line word is `w`-near the zero codeword. This upgrades
the old route cut: the printed `+1` inequality itself is false, not merely
its common-support proof.

## Burn-down

```text
result:                  REPAIRED false +1 payment by proved 2w theorem
DAG delta:               +1 PROVED leaf, +1 req edge, +3 ev edges
critical status delta:   unchanged; local charge only
upstream terminal delta: harvested PR #1160 theorem independently
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Do not globalize a common support or charge the complementary far stratum.
The next MCA ledger using this leaf must print its first-owner order and
reserve with the literal `2w` term.
