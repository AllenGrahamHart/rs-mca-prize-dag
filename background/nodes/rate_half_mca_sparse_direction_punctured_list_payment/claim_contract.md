# Claim contract

- **claim id:** `rate_half_mca_sparse_direction_punctured_list_payment`
- **status:** `PROVED`
- **input:** one codeword direction approximation with support size
  `1<=e<d`, plus exact pair-noncontained witnesses
- **output:** the bound `(SP1)` and two exact deployed first-residual gates
- **currency:** distinct finite slopes; multiplicity at most `e` per
  punctured ordinary-list word
- **nonclaims:** no payment outside the printed support-size gates and no
  full-row closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_sparse_direction_punctured_list_payment/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_sparse_direction_punctured_list_payment/verify_audit.py`
