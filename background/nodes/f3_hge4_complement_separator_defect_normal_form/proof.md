# Proof

The complement-third proof gives

```text
deg A=deg B=c,       lc(A)=lc(B)=dh/m,
P(B-A)+dB=2.                                         (1)
```

Set `G=B-A`. If `G=0`, equation `(1)` gives `dB=2`, contradicting `c>0`.
Thus `G` is nonzero. Since `deg(dB)=c`, cancellation in `(1)` forces

```text
h+deg G=c.
```

This proves `deg G=c-h=e`. Comparing the degree-`c` leading terms in `(1)`
and using that `P` is monic gives

```text
lc(G)+d lc(B)=0,
lc(G)=-d(dh/m)=-d^2h/m,
```

which is `(SDN2)`.

Equation `(1)` immediately gives

```text
B=(2-PG)/d.
```

Since `A=B-G` and `Q=P+d`, this also gives

```text
A=(2-PG-dG)/d=(2-QG)/d,
```

proving `(SDN3)`. Finally,

```text
H-1=PA=(2P-PQG)/d,
H+1=QB=(2Q-PQG)/d.
```

Adding and dividing by two yields

```text
dH=P+Q-PQG.                                          (2)
```

Substitute `H=(d/m)XP'R` into `(2)` and multiply by `m` to obtain `(SDN4)`.

The complement-third theorem gives `e=c-h>=0`. At dyadic `m`, equality
would say `m=3h`, which is impossible, so `e>=1`. The residues of `m` modulo
three give the two closest-width values. QED.
