# Result

At `n=2^41,k=2^40`, the exact safe-anchor table includes:

| `B*` | `a_IJ` | `a_IJ-k` |
|---:|---:|---:|
| `1` | `1649267441664` | `549755813888` |
| `3` | `1649267441664` | `549755813888` |
| `2^32-1` | `1554944256063` | `455432628287` |
| `332114441761` | `1554944255989` | `455432628213` |
| `332114441762` | `1554944255988` | `455432628212` |
| `2^128-1` | `1554944255988` | `455432628212` |

The last value is exactly `floor(sqrt(n(k-1)))+1`. Both verifiers run under
`ramguard tiny`; no Modal resource is used.
