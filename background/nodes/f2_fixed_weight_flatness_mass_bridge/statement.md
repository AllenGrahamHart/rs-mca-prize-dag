# F2 fixed-weight flatness to full-cube mass bridge

- **status:** PROVED
- **closure:** proof

Let `A:F_p^S -> V` be linear. For `0<=b<=S`, put

```text
N_b(v)=#{x in {0,1}^S: |x|=b and Ax=v},
M_b=max_v N_b(v),
B_b=binom(S,b).
```

Let `G` be any set of good weights, let

```text
T_G=sum_(b notin G) B_b,
```

and suppose that, for some `Q,L>=1`, every `b in G` obeys the discrete
mean-plus-one estimate

```text
M_b <= L(1+B_b/Q).                                  (FW-1)
```

Then the full-cube weighted ternary kernel mass satisfies

```text
Z(A) <= 3 T_G^2/2^S + 3L(S+1+2^S/Q).               (FW-2)
```

If every weight is good, the sharper bound is

```text
Z(A) <= 2L(S+1+2^S/Q).                              (FW-3)
```

Also `M_b=M_(S-b)` and the fixed-weight collision sums agree under
complementation. Thus only weights through `floor(S/2)` need independent
control.

Consequently, if `log L=o(S)`, `2^S/Q=2^o(S)`, and
`T_G=2^(S/2+o(S))`, then `Z(A)=2^o(S)`. In particular, it is enough to
prove `(FW-1)` on a central binomial band whose omitted tails have binary
entropy at most `1/2+o(1)`.

For the F2 branch maps the natural value is `Q=p^d`, where `d=rank(A)`.
This theorem proves the passage from fixed-weight flatness to full-cube
mass. It does not prove `(FW-1)`. Upstream `prob:capfr1-master-flatness`
and `prob:capfp-Q` have the same mean-plus-one shape, but concern their own
unweighted or pruned first-match maps; a weighted-map and owner transport
is required before either can instantiate `(FW-1)` here.
