# C36' fifth product-orbit moment compiler

- **status:** PROVED
- **consumer:** `f3_h3_mobius_excess_half`

For a nonzero target `t`, let the swap involution act on its ordered product
representations `(a,b)` and put

```text
D(t)=#{a in A:a^2=t},
U(t)=(P(t)+D(t))/2.
```

Thus `U(t)` is the number of unordered product representations of `t`. Define

```text
M_5^rich=sum_(t!=1,P(t)>=19) binom(U(t),5) R(t).
```

Then

```text
X_18 <= (2/231) M_5^rich.                        (O5)
```

Consequently the estimate

```text
M_5^rich <= (34650/17)n^2                        (O5-BOUND)
```

would imply the critical target `17X_18<=300n^2`. The compiler is proved;
`(O5-BOUND)` is not claimed here.

Unlike the full factorial moment, `M_5^rich` retains only `P(t)>=19` and
counts five distinct unordered product representations and one oriented
quotient representation. Equal, swap, repeated-representation, and low-fiber
components are absent by definition.
