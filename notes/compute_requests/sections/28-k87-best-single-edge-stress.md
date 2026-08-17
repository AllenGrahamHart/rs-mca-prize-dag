## Preregistered K'=87 best-single-edge stress falsifier

- **decision:** test whether the best of the raw price and each available
  single adjacent edge pays every deduplicated carrier profile below the exact
  K'=87 raw-safe leader on four route-deciding offsets
- **ordered scope:** offsets `9` (the raw-safe leader), `1` (largest lane),
  `23` (interior stress), and `43` (last raw-unsafe lane), evaluated in one
  paired deployment
- **primary adapter SHA-256:**
  `f2ef06960e42febe620dcfa7ecddf2d7207532462e764e0b767a98416f45de53`
- **independent-pricing adapter SHA-256:**
  `d4c6baed6e30a3acea25b808a6320589fc1b7aadd401da1a4fac0566b17df627`
- **shared K'=87 traversal core SHA-256:**
  `53b1d80cabff9cf1995043195b91e8b1e96013ffcb8aaacf5642591a88cd3e0a`
- **K'=85 primary formula adapter SHA-256:**
  `2c94b7432cd4c9d37a49288298761cbff9227a07f694fe80ec259ef19e724505`
- **K'=85 independent formula adapter SHA-256:**
  `f9a01624b5a11fbc30f58a4f4afca2aa75d9af96b35c69edddcdc7eef5e1fa1f`
- **K'=85 residual base SHA-256:**
  `cd1e9d2706c48be390387953c4abeea46958af258f132700809cf2393a5e4a90`
- **dispatcher SHA-256:**
  `951b2c2f3b560fd4df4dadf2da51d896c81207a8bd6890d468007f896144514d`
- **checker SHA-256:**
  `d03a0018a439f1fdde77fc8f74cd7388aef4520cdab9b5b5bdcce6179b0b1d7e`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** eight jobs, one CPU and 256 MB each, 360-second child wall
  and 375-second container wall; projected total cost below `$0.15`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The adapters alter only `K'=87`, `q=77`, `m'=67559`, `n'=1048663`, the
derived exact ceiling, and the exact raw-safe offset-9 leader. They retain the
proved K'=85 carrier formulas. Both implementations share the explicit
row-generic source-unit traversal, while the adjacent-edge prices are rebuilt
by the primary router and the separately implemented audit formulas.

`FALSIFIED` requires a paired exact over-leader witness and blocks a full
best-single campaign. `SURVIVED` requires paired agreement on all four lanes,
1,411,488 completed source units, and every carrier profile at or below the
leader. `INCOMPLETE` retains partial checkpoints and changes no mathematical
status. Survival authorizes a separately preregistered completion wave over
offsets `1..43`; this stress campaign alone cannot promote `K'=87`.

**Outcome:** `FALSIFIED`. Modal app `ap-LHOZ5HAjGEZi9RzlEHSHZH` completed all
eight jobs at 30--34 MB peak RSS. The paired checker accepted 1,111,080
completed source units and 4,333,348 deduplicated carrier profiles per
implementation. Offsets 9, 23, and 43 survived exhaustively, while both
implementations returned the same first offset-1 witness:

```text
m2=27, m3=28, s2=50, s3=49, s4=48, s5=47
case=F23__N4_t2__N5_t0
charges=(32,7),(36,5), high=c6F/c7F/c8F/c9F
```

Its raw premium is
`46081464205190838687203932464720858867144442465`. The best single adjacent
edge leaves
`41535717484613459403166619514559682376379208865`, above the exact raw-safe
leader by `74818359138015565285572829536920044880164170`. Capture SHA-256:
`28384df190292e49aeb22ded3194f83037700654293fe5ba4518ffd2680a5501`.

The full best-single wave is therefore blocked. This witness has available
edges 4, 5, and 6, so the next bounded action is to print the complete
support-disjoint option table and test whether edge set `4+6` supplies the
minimal valid repair.
