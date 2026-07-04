# census_exact_counts

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

With N' <= ~400 absolute, the deciding class counts K are exactly computable big integers (binomial-sum sized ~2^400 at worst). At candidate points, EXACT K replaces the leading+second-order expansion entirely: the knife-edge condition sharpens from 'estimate cannot decide' to the exact Diophantine condition B* = floor(q/2^128) in [L, K), where L is the certified lower bound strength. (acl_second_order remains needed only for corridor WIDTH/candidate localization, not for tie decisions.)
