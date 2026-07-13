# Generic MDS residual-kernel ray bound

- **status:** see `dag.json` (single source of truth)

Let `H_U:F^U->F^R` be an MDS parity-check restriction with

```text
|U|=R+d,       dim ker(H_U)=d.
```

Fix `h>=1`, put `r=R-h`, and fix a syndrome line `y_0+gamma*y_1`.
Assume the line is generic at radius `r`: there is no set `E subset U` with
`|E|<=r` for which both `y_0` and `y_1` lie in `span(H_E)`.

If every `gamma` in a finite set `Z` has a lift supported on at most `r`
coordinates of `U`, then

```text
|Z| * C(d+h,d) <= C(R+d,d) * R,                 (GRK)
```

and hence

```text
|Z| <= floor(C(R+d,d) R / C(d+h,d)).
```

For an RS row, `R=n-k` and `h=A-k`, while `r=n-A`. The genericity hypothesis
is exactly the exclusion of a codeword pair jointly agreeing with the
received pair on at least `A` coordinates, which is tangent-paid in the XR
consumer.

