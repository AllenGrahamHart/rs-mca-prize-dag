# Mersenne residue-zero common-core absorption payment

- **status:** PROVED
- **scope:** Mersenne-31 full-lift support `e=98232`

Assume for contradiction that the support is unsafe.  The residue-zero
direction router supplies a synchronized top affine line `T` with

```text
|T|>=343071,       g>=67452=m-2,
```

where `g` is its total common agreement core.  Its nonzero degree-`<K`
line direction has at most `c=K-1=5` zeros outside the direction support
`E`.  Hence the inside common core has size at least

```text
u=g-c>=67447.
```

Every selected slope whose assigned explanation has inside agreement size

```text
h>=h_sync=e-u+K=30791
```

lies on the same affine line.  The remaining explanations have deficit at
most `h_sync-1=30790`.  After puncturing `E`, they form an ordinary list at
agreement at least `36664`, whose Johnson cap is `26`.  Charging each of
those explanations by the crude owner cap `e` and charging the enlarged
line once gives

```text
|Z| <= e*26+(N-m+1)
     = 3535161
     < 16777215.                                      (RA1)
```

This contradicts the unsafe assumption.  Therefore Mersenne-31 support
`e=98232` is safe, and the full-lift residual starts at `e=98233`.

## Nonclaims

This does not pay `e=98233`, close the deployed row, or provide an adjacent
unsafe certificate.
