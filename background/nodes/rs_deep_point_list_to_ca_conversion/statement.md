# RS deep-point list-to-CA conversion

- **status:** PROVED
- **source:** `tex/cs25_cap_v13_2.tex`, Theorem `thm:A`

Let

```text
C=RS[F,D,K],       C+=RS[F,D,K+1],
q=|F|,             N=|D|,             q>N.
```

For `delta in (0,1)`, put `f=floor(delta N)` and assume

```text
f<=N-K-1.                                             (DP1)
```

If `0<=eta<1` and the finite-slope correlated-agreement error obeys

```text
epsilon_ca(C,delta)
  <=eta(1/K-N/(Kq)),                                  (DP2)
```

then the ordinary worst-case list size satisfies

```text
List(C+,delta)
  <=ceil(q epsilon_ca(C,delta)/(1-eta)).               (DP3)
```

In particular, if the CA bad-slope numerator is at most the integer `Q` and

```text
KQ<q-N,                                               (DP4)
```

then

```text
List(C+,delta)
  <=ceil(Q(q-N)/(q-N-KQ)).                             (DP5)
```

## Scope

This is a self-contained finite-field theorem, not a conjectural import. It
uses ordinary lists for `C+` and support-wise finite-slope CA for `C`. It does
not turn a list bound into an MCA bound, remove `(DP1)`, or assert that a
bound for a generalized or interleaved code transfers without an explicit
code identification.
