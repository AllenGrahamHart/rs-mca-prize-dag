# Source evidence

The load-bearing finite input and output are local and exact:

- producer:
  `experiments/prize_resolution/rate_half_kb_m4_degree15_passport_budget.py`
- producer SHA-256:
  `d8550fd0aed92b0dddd8271a3e6ca3c9d666b8a6ae5b10c7922f61d51bca83b5`
- canonical result:
  `experiments/prize_resolution/rate_half_kb_m4_degree15_passport_budget_result.json`
- canonical payload SHA-256:
  `fe9f11e88bd780e3e9b2d1b5c330b268e31411eabf2fb203081f26fd82208ae8`
- search universe: all 720 permutations of six letters;
- largest prefix search: 3,375 exact tuples;
- arithmetic: deterministic integer permutation composition only;
- compute: below one second and 110 MB under tiny RAMguard; no Modal.

The parent node pins the external primitive-group catalogue. This child does
not add another classification source: it reconstructs the complete `S6`
class table and every product-one tuple directly.
