# Source evidence

Exact artifacts:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_rankdrop_fglm_profile_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_rankdrop_fglm_profile_result.json`

The final 40-row FGLM and factor run is Modal application
`ap-FSzYrPk1tCjYa0m2NRgjfm`.  Singular performs the exact FGLM conversion;
SymPy 1.14.0 factors only the resulting univariate polynomials over the same
prime field because Singular's packaged factorizer refuses characteristics
above `2^29`.  Each task had one CPU, 3072 MiB RAM, a 240-second subprocess
cap, and a 270-second container cap.  Every task completed.
