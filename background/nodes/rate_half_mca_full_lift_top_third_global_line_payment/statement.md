# Full-lift top-third global-line payment

- **status:** PROVED
- **closure:** synchronize all top-third exact-deficit layers onto one line
- **scope:** the remaining pair-noncontained full-lift MCA branch

Use the preceding notation and put

```text
s=floor((e-K)/3),       H=e-s-1,       u=floor(e/2),
t=N-m.
```

All selected explanations with exact deficit `h=e-r` for any

```text
max(0,e-m)<=r<=s
```

lie on one common affine codeword line.  Their total number, and hence their
total slope contribution, is at most

```text
N-m+1=t+1.                                             (GL1)
```

If the punctured Johnson caps are positive through `H`, then

```text
|Z| <= (e-1)J_u+J_H+(t+1).                            (GL2)
```

Exact official evaluation proves the complete walls

```text
KoalaBear:   e<=95943,   endpoint bound 6336049;
Mersenne-31: e<=97908,   endpoint bound 6682339.
```

At the adjacent supports, the `H`-prefix denominators are respectively
`-1037` and `-965`.  The full-lift residual intervals become

```text
KoalaBear:   95944<=e<=1044238;
Mersenne-31: 97909<=e<=1044241.
```

## Nonclaims

This does not replace the failed prefix cap, claim that its sign change is
unsafe, or close either deployed row.
