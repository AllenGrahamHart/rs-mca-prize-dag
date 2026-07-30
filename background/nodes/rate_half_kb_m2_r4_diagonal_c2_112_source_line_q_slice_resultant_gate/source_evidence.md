# Source evidence

- The colored quotient compiler identifies the two mixed common-`K` labels
  and their aligned/near-aligned locator.
- The finite reconstruction theorem supplies at most eight source-deck pairs
  on which the gate is evaluated.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_qslice_probe.py`
  gives a light exact `F_1009` aligned fixture. It tests `24` admissible
  internal-pair/sign choices, reconstructs `12`, and finds zero `(KBQS-1)`
  survivors. This is falsification evidence, not proof of generic deletion.

## Upstream custody

The theorem is vendored into the diagonal source-facet packet in draft PR
`przchojecki/rs-mca#1132` at commit
`e6bde40cbb2e438a8a7faca333a34d8a7681c6b3`:

```text
note blob:        a4e476ec50acca029868abc546396fca81afa97f3
verifier blob:    c3e011c7c31360d04dfa59ac2712928d341e6240
certificate blob: ed855d2ee936bdfcfc61937d449ec151227c0224
payload SHA-256:  66b83997ed25269d8d79e5d77291dcb3638835356cb895b827f90c9f287a86cf
```

The upstream replay checks all three complementary `J_1`-incidence
patterns and rejects `118` of `118` hostile mutations. The extension report
is PR comment `5131961677`.
