# Paired-PGL2 small-row falsification sweep

Date: 2026-07-12.

The bounded Modal fleet `ap-bHp1Epb9jC5BdW4xeXfB7l` exhaustively enumerated
every prime `p=1 (mod n), p>=n^2` in the shard ranges printed by
`experiments/prize_resolution/f3_h3_paired_sweep_modal.py`. It covered 7,090
rows at orders `64,128,256,512,1024,2048,4096`; all 116 shards completed and
none hit its 48-second internal cutoff.

## Paired result

No parameter with `R(t)>0` violated `P(t)+2R(t)<=37`, equivalently
`I_inv(t)+2I_aff(t)<=39`.

| n | rows | max `P+2R` |
|---:|---:|---:|
| 64 | 3,077 | 28 |
| 128 | 1,795 | 24 |
| 256 | 1,145 | 26 |
| 512 | 648 | 26 |
| 1,024 | 279 | 28 |
| 2,048 | 100 | 32 |
| 4,096 | 46 | 32 |

The global extremizer was

```text
(n,p,t)=(2048,4638721,625),  (P,R)=(18,7).
```

Its exact nine unordered product pairs and seven oriented quotient pairs are
emitted by the replay. They do not form the single telescoping pattern seen in
the earlier maximum-product official row, so no classification theorem is
claimed from this datum.

## Aggregate result

Every row had `X_35=0`. The largest exact non-swap moments were:

| n | max `S_ns/n^2` |
|---:|---:|
| 64 | 3.824218750 |
| 128 | 0.770996094 |
| 256 | 1.223175049 |
| 512 | 1.017730713 |
| 1,024 | 0.990592957 |
| 2,048 | 0.994569302 |
| 4,096 | 0.996755958 |

The sufficient theorem allows `S_ns<=68n^2`. Together with the sixteen
previous boundary rows at `n=8192,16384`, this supports the aggregate moment
route much more strongly than its printed constant suggests.

## Route verdict

This sweep is evidence, not a proof or a finite-row certificate for the prize.
The pointwise route remains close to the open constant-fiber Mobius subgroup
problem at the square-root boundary. Its survival justifies retaining it as a
background route, but the primary analytic target should be the weaker
non-swap aggregate moment, where the observed margin is much larger and a
constants-explicit rich-line/energy argument could plausibly fit.

Replay:

```bash
uvx modal run experiments/prize_resolution/f3_h3_paired_sweep_modal.py
```
