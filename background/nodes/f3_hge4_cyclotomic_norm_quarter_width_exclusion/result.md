# Result

The official condition `p>=n^2` is strong enough to delete every primitive
exact-ratio width at or above one quarter of its ratio level:

```text
E_h^prim(m,p)=0       for m/4<=h<m/3.
```

The proof converts the first power-sum difference into a nonzero cyclotomic
integer. Its reductions at `floor(h/2)` distinct primes above `p` force a
large norm, while odd-frequency Parseval gives an incompatible upper bound.

Combined with the complement-third gate, the live level sum is now only

```text
sum_(h=4)^(m/4-1) E_h^prim(m,p).
```

In particular, the Kummer trace-to-pencil fiber is no longer an HGE4 proof
obligation. Passing scalar traces such as `(m,p)=(16,593)` and `(32,1249)`
cannot support primitive pencils in the deleted strip. The lower-quarter
aggregate remains open.
