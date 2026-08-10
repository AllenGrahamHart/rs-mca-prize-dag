# FPC5 guarded Hankel probe result

- **preregistration:** commit `468f04f1d`
- **Modal run:** `ap-DlZD96lRzxt52OuV2msERv`
- **completion:** all 280 requested configurations and 504 fixed charts
- **classification:** `NO_SEPARATION`
- **scope:** route evidence only; no theorem or DAG status change

The fixed-chart result is:

| cell | charts | max rational | max random | ratio | median guarded/primitive |
|---|---:|---:|---:|---:|---:|
| `t4e2` | 64 | 15 | 17 | 0.882 | 0.917 |
| `t4e3` | 128 | 5 | 6 | 0.833 | 1.000 |
| `t4e4` | 96 | 2 | 2 | 1.000 | 1.000 |
| `t5e2` | 48 | 24 | 23 | 1.043 | 0.947 |
| `t5e3` | 96 | 8 | 8 | 1.000 | 1.000 |
| `t5e4` | 72 | 2 | 1 | 2.000 | 1.000 |

Neither preregistered event fired. No cell exceeded the matched random
maximum by a factor of sixteen, neither fixed-`t` ratio sequence grew
monotonically by a factor above four, and no cell had median guard survival
below one quarter.

The small analogues therefore show no exceptional concentration caused by
the rational FPC5 moment sequence. They also show that one untouched petal
does not strongly suppress primitive split locators. The next proof route
should attack the generic support-determinant/split-divisor incidence and
retain the background guards, but should not budget a decisive saving from
those guards without a separate many-untouched-petal argument.

The complete emitted payload has 78,469 bytes and SHA-256
`bc9ec288a00a35790dd157dc44fb2c078751e3cb1b85d7867107b34089aba05d`.
The compact machine-readable summary is
`fpc5_hankel_guard_probe_result.json`; the deterministic launcher and seeds
reconstruct every individual record.

The compact certificate and its three hostile mutations replay with

```text
./tools/ramguard tiny -- python3 \
  experiments/prize_resolution/verify_fpc5_hankel_guard_probe_result.py \
  --tamper-selftest
```
