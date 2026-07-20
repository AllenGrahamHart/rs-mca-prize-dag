# Audit

## Official arithmetic

| root | `A` | `H` | floor(`5A/8`) | `log_2(16n^3)` |
|---|---:|---:|---:|---:|
| RowC `1/4` | 261 | 6 | 163 | 34 |
| RowC `1/8` | 133 | 6 | 83 | 34 |
| RowC `1/16` | 67 | 4 | 41 | 34 |
| prize `1/4` | 558345748481 | 8589934594 | 348966092800 | 127 |
| prize `1/8` | 283467841537 | 8589934594 | 177167400960 | 127 |
| prize `1/16` | 141733920769 | 4294967298 | 88583700480 | 127 |

Every row also satisfies `2A<=N` and `16H<=A`.

## Scope guard

The verifier checks a separate small binary-code fixture and reconstructs its
constant-weight supports. No verifier asserts that these support families are
realized by Reed-Solomon codeword pairs.
