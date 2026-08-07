# Counterexample proof

Put `n=2^41` and `p=3n+1`.  The factor `2^41` of `p-1` exceeds
`sqrt(p)`, and base 5 satisfies

```text
5^(p-1) = 1 (mod p),
gcd(5^((p-1)/2)-1,p) = 1.
```

Pocklington's theorem therefore proves that `p` is prime.  Direct integer
comparison gives `p^6<2^256`, and `n|(p-1)`, so `q=p^6` is an official
admissible field row. Since `p=1 mod n`, `k=ord_n(p)=1`, while the ambient
extension degree is `e=6`.

At the nested full-group window, the exact F2 identity and kernel-index
lower bound give

```text
E_c[T_W(c)] >= 4^m / p^dim(L).                                  (1)
```

The proved trace collapse gives `dim(L)<=k|Lambda|`. At the balanced
full-group window, `|Lambda| log_2 p=m/e`, so `(1)` yields

```text
E_c[T_W(c)] >= 2^(m(2-k/e))=2^(11m/6).
```

The target scale is `2^(m+o(n))`; the excess exponent is `5m/6`. Under the
nested reading `m=n/2`, this is `5n/12`, a fixed positive fraction of `n`
that cannot be absorbed into `o(n)`. Therefore the all-admissible-row O1
claim is false. QED.
