# Exact all-arity rate-half list crossing at budgets one and two

- **status:** PROVED
- **closure:** proof
- **consumers:** `list_grand`, `list_large_m_scope_closure`

Let `C=RS[F,D,k]` be an official rate-half row with

```text
n=|D|,       k=n/2,       B*=floor(q/2^128) in {1,2},
q=|F|.
```

For every common-support interleaving arity `m>=1`, write `L_m(a)` for the
worst list size at agreement at least `a`. Then

```text
L_m(3n/4)<=B*<L_m(3n/4-1).                         (LA12)
```

Thus the exact certified agreement and closed integer radius are

```text
a_L(C,m)=3n/4,       r_L(C,m)=n/4,
delta_L(C,m)=1/4,                                      (LA13)
```

for every `m>=1`. Increasing the radius numerator by one reaches agreement
`3n/4-1` and is unsafe.

The theorem determines the complete list-prize object on these two
field-budget branches. It makes no claim for `B*>=3` or for MCA/CA.
