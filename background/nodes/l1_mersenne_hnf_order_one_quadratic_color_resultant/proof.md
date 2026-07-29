# Proof - L1 Mersenne HNF order-one quadratic color resultant

Let `epsilon=E(x)=x^(p+1)` at a reduced root. Since `epsilon in mu_m` and
`p=-1 mod m` on every official row,

```text
epsilon^p=epsilon^(-1),       x^p=epsilon/x.         (1)
```

For an indeterminate `X`, put

```text
f_X(W)=A W^2+B W+C-X,
g_X(W)=(C^p X-1)W^2+B^p X^2 W+A^p X^3.             (2)
```

Taking the `p`th power of `E(x)=epsilon`, substituting (1), and multiplying
by `epsilon*x^2` shows

```text
f_epsilon(x)=g_epsilon(x)=0.                         (3)
```

For quadratics `aW^2+bW+c` and `dW^2+eW+f`, their resultant is

```text
(af-cd)^2-(ae-bd)(bf-ce).                            (4)
```

Applying (4) to (2) gives exactly `R_E=U^2-VT`. Its leading term comes only
from `U^2` and is `(A A^p)^2 X^6`, so `R_E` has degree six.

A quadratic fiber contains at most two reduced roots. The fourteen roots at
`h=15` therefore use at least seven distinct colors. By (3) they would give
seven distinct roots of the degree-six polynomial `R_E`, a contradiction.

Now take `h=7`, so there are six reduced roots. For a color used by `j`
distinct roots, the two degree-two polynomials in (2) have at least `j`
distinct common roots at that specialization. The standard local
intersection-multiplicity property of the Sylvester determinant gives

```text
(X-epsilon)^j divides R_E(X).                        (5)
```

Summing `j` over the color fibers gives six. Degree and leading-coefficient
comparison therefore proves (QCRS3). The roots of `X^8-1` are exactly the
eight colors, so deleting the missing colors and repeating the unique
double color gives (QCRS4) and (QCRS5). QED.
