# `A=1` shape-A all-excess degree-ledger rank route fence

- **status:** PROVED
- **closure:** exact block-supported `K_all` kernel with the complete `e=7`
  degree ledger
- **consumer:** `rate_half_band_crossing_location`

Work over `F_211`, where `2` has multiplicative order `210`. Put

```text
C={2^(35i):0<=i<4},
X={x in F_211^*:x^7 in C},
Gamma={0} union {delta in F_211^*:delta^5 in C}.   (DLF1)
```

Then

```text
|X|=28,                 |Gamma|=21.                (DLF2)
```

The biform

```text
G(t,X)=t^5-X^7                                      (DLF3)
```

has the exact `e=7` all-excess degree profile:

- every row `G(t,x)`, `x in X`, has exactly five distinct roots in
  `Gamma`;
- each nonzero `delta in Gamma` has seven distinct fiber roots in `X`;
- the zero fiber has no root in `X`.

Thus the excesses are

```text
a_0=7,              a_delta=0 for delta!=0,
sum_delta a_delta=7.                               (DLF4)
```

For nonzero `delta`, take

```text
D_delta(X)=X^7-delta^5,       C_delta(X)=-1,
```

and at zero take

```text
D_0(X)=1,                    C_0(X)=-X^7.          (DLF5)
```

Then every `C_delta` is nonzero and

```text
G(delta,X)=D_delta(X)C_delta(X).                   (DLF6)
```

The corresponding `K_all` matrix has `28` columns, rank `27`, and the
coefficient vector in `(DLF5)` is a block-supported kernel vector.

## Scope

This disproves a universal full-rank argument based only on the all-excess
row, fiber, and degree ledger. It is not an official Shape-A survivor or a
counterexample to the rate-half theorem: the construction does not impose
the three-center source pencil, two-slope spread, collision jets, official
positive padding, or the retained Hankel identities. Those constraints must
enter any valid rank closure.
