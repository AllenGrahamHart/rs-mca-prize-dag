# Proof

Choose representatives so the two `AB` edge products are `+AB` and `-AB`.
At the `A` loop, orient both deck orbits by the shared endpoint `A`.  Their
products and sums satisfy

```text
p_A-p_+=-A(A+B),       p_A-p_-=-A(A-B).           (1)
```

Specialize `(KBNW-2)` to these two nonloop rows with loop anchor `k_A` and
other loop `k_C`.  Cancel the common nonzero edge sums using `(1)`.  If the
corresponding source lifts are `x_+,x_-`, the exact equation becomes

```text
x_+(k_--k_C)=x_-(k_+-k_C).                        (2)
```

Squaring, using `x_+^2=k_+`, `x_-^2=k_-`, and factoring gives

```text
(k_+-k_-)(k_C^2-k_+k_-)=0.
```

Distinctness proves `(KB43-1)`, and normalization gives `(KB43-2)`.

Now inspect the fifteen ways to choose one singleton and match the other
four roles into negative pairs.  The complete table is:

```text
singleton   matching 1   matching 2   matching 3
X           MN|LZ bad    ML|NZ X1     MZ|NL X2
M           XN|LZ M1     XL|NZ M2     XZ|NL M3
N           XM|LZ bad    XL|MZ N1     XZ|ML N2
L           XM|NZ bad    XN|MZ L1     XZ|MN bad
Z           XM|NL bad    XN|ML Z1     XL|MN bad
```

Reading `UV` as `U=-V` gives exactly the relations in `(KB43-3)`.  For
example `XN` is `M^2=-1`; `ML` is `L=-M`; and `NZ` is `Z=-M^2`.
The six bad cells contain either `XM` or `MN`, forcing `M=-1` and hence
`N=X`, except `XZ|MN` and `XL|MN`, which have the same `MN` collision.
Thus no bad cell has five distinct labels.  Conversely each retained row
has examples in odd characteristic after excluding its finite collision
set, so the nine-cell atlas is exact.

The direct `F_29` role replay checks all `5!=120` assignments and finds none
satisfying `(KB43-1)`.  This is an audit consequence, not an input to the
universal proof. QED.
