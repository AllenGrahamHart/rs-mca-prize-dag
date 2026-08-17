## Preregistered O0b cells-3/6 six-case basis-fed cross pilot

- **decision:** test the validated basis-fed architecture across both lane
  orbits and all three represented missing-record orbit types
- **scope:** six unclosed representatives, one per
  `{S0,SDE/SDF} x {xi=0,xi=2,xi=6}`, with varied outside/source signs
- **launcher SHA-256:**
  `b5ee2cd7bb5233547498dafb4140a3dd776c6f30cdcfc2cc11304fa2483b3599`
- **outcome-neutral checker SHA-256:**
  `734801c516cd79790133f2116ea6319a3bef23ab5c7dd1109b3ed121e283031c`
- **case manifest SHA-256:**
  `dfbbee76c4d04f71d65b2c3b9fea83b9fbdb8e86cd0ff26f76fef591e1d49fbc`
- **ordered case-list SHA-256:**
  `2e1eea3589e0737e9efa7a3a49a0492d6fece4577b93a36eb1f6badf0b499b42`
- **basis-program core SHA-256:**
  `2298a72b7d45f6e920244836f4e7fa3589c80a8e5a254ca03ee9971053a57670`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **envelope:** at most six one-CPU workers, 4 GiB each, 240-second
  Singular child wall and 300-second container wall; projected cost below
  `$0.35`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 360-second external hard stop

The already closed diagnostic representative is excluded. Every worker starts
from the correct 21-polynomial source-sign common basis and adds five outside
equations. The output-neutral checker accepts exact complete unit or nonunit
rows and exact timed rows, while still requiring complete six-row collection,
ordered case reconstruction, source custody, and distinct program hashes.
The unordered map prevents a preempted low-index input from blocking later
checkpoints.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_cross_pilot_modal.py
```

All-unit completion authorizes the full pinned 24-representative pilot after
subtracting already closed rows. A nonunit becomes the next algebraic target.
Timeouts authorize only a stratum-specific decomposition. This six-case run
does not authorize the 1,416-case campaign.

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-HONZUndkEeMfHPJ450zO9c` returned all six pinned rows, each with status
`TIMEOUT`; result SHA-256:
`ebf5de0ff545dbba76db9f638aea5cd2bf0a013be51896c51aec5a7418ab3f11`.
The outcome-neutral checker accepts the complete ordered collection and
rejects all three hostile mutations. Rows 1 and 3 finished their initial
ideals, respectively at dimension/size `(3,114)` and `(3,120)`, then timed
out before completing the first guard saturation. Rows 0, 2, 4, and 5 did
not finish the initial basis within 240 seconds. Thus this result says
nothing about emptiness of any row. It rejects the six-case uniform campaign
as the next endpoint and authorizes only equation-order and first-guard
diagnostics on representatives of the two observed timeout modes.
