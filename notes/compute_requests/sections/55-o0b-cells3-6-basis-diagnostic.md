## Preregistered O0b cells-3/6 global-basis one-case diagnostic

- **decision:** test whether one outside ideal becomes tractable when its
  initial generators include the proved 21-polynomial common basis
- **scope:** exactly case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=0,pairing=0)`
- **launcher SHA-256:**
  `5b7620a0c07b59b652c39efe6d61e481806243488d40ad0e9a6b713353c2a32f`
- **complete-unit checker SHA-256:**
  `614aea8cccfc02c1fe98b4320aa733de4cda278ed23ab692bae55719db51f03c`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **string-compiler core SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.05`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The initial ideal contains the 21 pinned `--` common-basis polynomials and
only the five case-specific outside equations. The ordinary guards and the
six-cofactor-ideal saturation are then replayed. The worker must print the
initial ideal dimension/size before any saturation, so a timeout after that
point still localizes the next obstruction.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_diagnostic_modal.py
```

A checked unit result authorizes a small multi-stratum basis-fed pilot. A
complete nonunit is retained in full and becomes the next algebraic target.
A timeout or error authorizes only decomposition of this one case. No outcome
from this single diagnostic closes an orbit or authorizes the 1,416-case run.
