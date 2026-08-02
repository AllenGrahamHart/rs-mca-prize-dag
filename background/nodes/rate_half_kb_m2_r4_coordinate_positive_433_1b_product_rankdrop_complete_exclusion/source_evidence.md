# Source evidence

Exact artifacts:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_rankdrop_outside_product_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_rankdrop_outside_product_result.json`

The final 6,720-case run is Modal application
`ap-w5UjgTm3WmulNXbk9mdqtT`.  It uses one CPU and 1024 MiB per lane task,
a 210-second container cap, and a three-second cap on each small Singular
standard-basis calculation.  All 64 lane tasks and all 6,720 case
calculations completed; none used the fallback FGLM branch because every
primary ideal was already the unit ideal.
