# Rate-quarter FPC5 `M=4,t=2` payment

- **status:** PROVED
- **consumer:** `l1_fpc5_m4_t2_payment`

At official rate `1/4`, fix one admissible maximal sunflower source with
`M=4`, petal size `ell`, and background size `b<ell`. Then

```text
4ell+b=3k+1.                                           (RQ1)
```

Every non-planted contributor touching exactly two full petals is determined
by its unordered touched pair. Consequently the first layout contains at
most

```text
binom(4,2)=6                                           (RQ2)
```

such contributors. General first-layout domination removes the multiplier
from all other maximal source layouts and adds at most the four anchors of
the first layout. Thus the complete source-admissible rate-quarter class has
size at most

```text
6+4=10.                                               (RQ3)
```

In particular, the rate-quarter `M=4,t=2` FPC5 residual is polynomially paid
with an absolute bound.
