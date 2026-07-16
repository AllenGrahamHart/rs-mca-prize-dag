# Proof - PMA sigma-one defect-three full-petal payment

Fix the exact missed-core set `D`. Since `r=0`, the residual polynomial `W`
has degree at most three and must have at least

```text
d+1+sigma-r=5
```

petal agreements. Suppose at least one petal is full. Choose the first full
petal in the fixed chart order. It supplies two distinct interpolation points.
At least three agreements lie outside that petal, so choose the first two of
them. The values at all four selected points are fixed by

```text
W(x)=c_i L_D(x).
```

A degree-at-most-three polynomial is uniquely determined by four values at
distinct points. Thus the certificate

```text
(D, first full petal, first two outside agreement points)
```

determines `W`, hence the source codeword. There are `binom(k-1,3)` choices
of `D`, `M` choices of the full petal, and at most `binom(L-2,2)` choices of
the two outside points. This proves the first line of `(D30F)`.

Using

```text
binom(k-1,3)<k^3/6,
M=L/2,
binom(L-2,2)<L^2/2,
kL<=n^2/4,
```

gives

```text
B_30^full
 < k^3 L^3/24
 = (kL)^3/24
 <= n^6/(64*24)
 = n^6/1536.
```

The previous theorems give

```text
B_31<n^6/9216,
B_low<n^5/1024<=n^6/8388608
```

on the official grid. Since

```text
1/1024-1/1536-1/9216=1/4608>1/8388608,
```

their sum is strictly below `n^6/1024`.

Finally, a defect-three, background-free source object outside this theorem
has no full petal. Its five required agreements therefore occupy at least five
distinct petals, proving the stated residual description.

