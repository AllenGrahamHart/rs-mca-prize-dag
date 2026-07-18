# Proof

Put `a=3n/4`. The proved low-budget ordinary theorem gives

```text
L_1(a)<=B*<L_1(a-1).                                  (1)
```

At the safe coordinate, `L_1(a)<=B*<=2`. Since every official field here has
`q>2^128`,

```text
L_1(a)^2<=4<q.                                         (2)
```

If `L_1(a)=0`, no component codeword can reach agreement `a`, so no
common-support tuple can reach it. Otherwise the proved
`list_subsqrt_interleaving_collapse` theorem applies to `(2)` and gives

```text
L_m(a)=L_1(a)<=B*                                      (3)
```

for every `m>=1`.

At the predecessor, choose the explicit ordinary received word and its
`B*+1` codewords from the low-budget theorem. Repeat the received word in all
`m` rows and send each codeword `c` to the diagonal tuple `(c,...,c)`. Every
tuple has the same common agreement support as `c`, so

```text
L_m(a-1)>=L_1(a-1)>B*.                                 (4)
```

Equations `(3)--(4)` prove the exact adjacent crossing for every arity. The
safe error count is `n-a=n/4`; adding one error changes the required
agreement to `a-1`, where `(4)` is unsafe. This proves `(LA12)--(LA13)`.
QED.
