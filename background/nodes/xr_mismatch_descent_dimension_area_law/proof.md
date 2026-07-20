# Proof

The proved invariant-excess descent gives, for every transition,

```text
N_j-N_(j+1)>=K_j+h.                                  (1)
```

Summing `(1)` over `j<L` telescopes. The final state is live, so

```text
N_L>=A_L=K_L+h>=h+1=H.
```

Therefore

```text
sum_(j<L)(K_j+h)
 <=N_0-N_L
 <=N_0-H,
```

which proves `(XDA1)`. Since `K_(j+1)=K_j-d_j`, the external-zero drops
telescope independently:

```text
sum_(j<L)d_j=K_0-K_L<=K_0-1.
```

This is `(XDA2)`.

Because `K_j+h=(K_j-1)+H`, subtracting `LH` from `(XDA1)` proves `(XDA3)`.

Fix `kappa>=1`. Every index counted by `L_kappa` contributes at least
`kappa+h` to the left side of `(XDA1)`. All other contributions are
nonnegative, so

```text
L_kappa(kappa+h)<=N_0-H.
```

Taking the integer floor proves `(XDA4)`. The layer-cake identity `(XDA5)`
is exact because a positive integer `K_j` contributes once to `L_kappa` for
each `1<=kappa<=K_j`.

Finally, write `N_0-H=DH+r` with `0<=r<H`. If `L=D-s`, then `(XDA3)` gives

```text
sum_(j<L)(K_j-1)
 <=DH+r-(D-s)H
 =r+sH,
```

which is `(XDA6)`. Substituting the six official parameter triples into
`(XDA4)` gives the printed table. QED.

