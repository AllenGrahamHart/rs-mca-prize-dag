# Cycle 228: MCA full-lift global-line synchronization (2026-08-13)

The preceding node priced each top-third exact-deficit layer separately.
That is valid but unnecessarily weak.  If three explanations come from
layers with missed-coordinate allowances `r_1,r_2,r_3<=s`, then

```text
|S_1 intersect S_2 intersect S_3|
  >= e-(r_1+r_2+r_3)
  >= e-3s
  >= K.
```

Thus restriction injectivity synchronizes normalized pair directions across
different layers.  The entire high-deficit union lies on one affine
codeword line.  Its pair-noncontained total-core cap `N-m+1` is charged
once.

The resulting profile is

```text
|Z| <= (e-1)J_floor(e/2)+J_H+(N-m+1).
```

Exact scans pay

```text
KoalaBear:   e<=95943, endpoint 6336049;
Mersenne-31: e<=97908, endpoint 6682339.
```

The next prefix denominators are `-1037` and `-965`.  Both rows now stop at
the same clean proof-method wall rather than an over-budget exact profile.

```text
start:                   84b1ff8e2
canonical prize:         c8d48cd4b (no newer Fable commit)
result:                  NARROWED; one PROVED cross-layer compiler
DAG delta:               +1 PROVED node, +2 edges
critical status delta:   none; replacement target remains TARGET
full-lift residuals:     KoalaBear 95944<=e<=1044238;
                         Mersenne 97909<=e<=1044241
delta-star movement:     none
compute:                 exact local integer scans under RAMguard;
                         no Modal
next route action:       replace the common low-agreement Johnson prefix
                         at H while preserving the global-line high union
export:                  przchojecki/rs-mca PR #1165 head 9c708e2f7;
                         manuscript theorem, exact note, and verifier;
                         PR #1164 import comment 5276361990
```
