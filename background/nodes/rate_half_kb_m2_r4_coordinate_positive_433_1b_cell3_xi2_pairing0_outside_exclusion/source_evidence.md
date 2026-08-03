# Source Evidence

Pinned exact compilers and outputs:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_cut_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_cut_census_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_root_replay_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_root_replay_census_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi2_pairing0_outside_solver_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi2_pairing0_outside_solver_result.json`

Final Modal apps:

```text
six-basis norm census:  ap-4q1oBdbGCX2yS2bdw8ZDyZ
root replay census:     ap-Ff2XsYkZr5Q28iAnywqwiG
finite outside solver:  ap-NrA3EZi5KT9lzjhxIdR8q0
```

SHA-256 pins:

```text
1f9b877b0c03ebd96c6042a88a8688d88e7b065ff04b59894c6ee75f24af0227  xi2_pairing0_six_basis_cut_modal.py
50330a5695e05ff284124b15e8d0db127e058b5879f2468ead6d97a52eddb1f6  xi2_pairing0_six_basis_cut_census_result.json
9b3ad92a52a6756ad9245ee4b69cf966bb150c2846416e2dbdc75b63fe1c03ad  xi2_pairing0_six_basis_root_replay_modal.py
6bf8d58a8af1fc37d153ed71ad506d27974d06249d4165983bc8bc264e893b57  xi2_pairing0_six_basis_root_replay_census_result.json
c88059ff1cc2d0845cde6c44434678b254c2e0ad9b1231cc79510d7e41842185  xi2_pairing0_outside_solver_modal.py
e1344a96ba48ddf6ca73360749dd7eb20e924bf153b42dab13599be6a09d8fbe  xi2_pairing0_outside_solver_result.json
```

The primary verifier checks all source hashes, custody links, signs, norm
roots, guarded lifts, target lanes, and finite gcd decisions.  The independent
audit checks the negative-`DE` and `(u-v)^2` sign changes directly in source.
