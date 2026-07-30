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

## Upstream custody

The theorem packet is exported in
[`przchojecki/rs-mca` PR #1132](https://github.com/przchojecki/rs-mca/pull/1132)
at exact head
`4e33c7be8b3b29848e0ceb8fd7f50dce45fb2eed`:

- note blob: `4aeeebd65f321fcdfe070b6c78f4ce0ca1c501be`
- certificate blob: `c9be4609a28f4c4b89c099e09a359f833dbf7e1b`
- verifier blob: `beb62c55287279d095e7162fa2ac2da9ac211fec`
- certificate payload SHA-256:
  `c9cfbbf394e479f93d8d8378d886331c8afbbaf338e6fc6b21f55e3e1c485fd7`

The upstream verifier binds the parent route-cut object by historical Git
blob and canonical payload, reconstructs the complete class and tuple census,
and rejects 15 of 15 semantic mutations.
