# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_exceptional_trace_allocation`
- **mathematical statement:** the first active-core complement is always
  `QV_a+P_XW_a=P`; a zero exceptional trace must allocate `E_Z` to `B`, has
  no zero domain trace, and gives the third exact system in `(ETA4)`
- **scope:** only the official `A=1,s=1,e=2^38-1,ell=0` face
- **dependency:** the exact active-core reduction
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the three active systems `(ETA4)`
- **falsifier:** a `Z_W=E_Z` active core, a zero exceptional trace with
  `X_0!=1`, or failure of the full first complement `(ETA1)`
- **nonclaims:** no exclusion of an active system
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_trace_allocation/verify.py`
- **upstream mapping:** exact SPI ledger / exceptional shift-pair allocation
