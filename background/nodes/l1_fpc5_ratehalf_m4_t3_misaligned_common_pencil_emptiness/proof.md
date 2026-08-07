# Proof: misaligned common-pencil emptiness

Put

```text
e_2=(z_2-z_1)^(-1),       e_3=lambda(z_3-z_1)^(-1).
```

The complement-slice residues say that `Etilde` takes the constant values
`e_2,e_3` modulo `P-z_2,P-z_3`, respectively. The unique degree-below-`2ell`
representative is affine in `P`:

```text
Etilde=A P+B,
A=(e_3-e_2)/(z_3-z_2),       B=e_2-Az_2.             (1)
```

Condition `(MP2)` is exactly `e_3!=e_2`, so `A!=0`. Set `z_0=-B/A`, proving
`(MP3)`. The multiplier is a unit modulo `(P-z_2)(P-z_3)`, hence
`z_0` differs from both `z_2,z_3`.

Now suppose a guarded divisor existed and write its Euclidean division as in
`(MP4)`. The degree bounds follow from

```text
deg D=2ell-a,       deg Etilde=ell,       deg(L_2L_3)=2ell.
```

Reduce `(MP4)` modulo `P-z_0`. Its left side vanishes, while

```text
L_2L_3==(z_0-z_2)(z_0-z_3)=:m_0       mod (P-z_0).
```

Therefore `m_0Q+V` is divisible by `P-z_0`. Both `Q` and `V` have degree at
most `s=ell-a<ell`, so their displayed linear combination has degree below
`ell`. It must be zero:

```text
V=-m_0Q.                                               (2)
```

Substitute `(2)` into `(MP4)` and use

```text
(P-z_2)(P-z_3)-m_0
 =(P-z_0)(P+z_0-z_2-z_3).                             (3)
```

Cancelling the nonzero polynomial `P-z_0` gives the second identity in
`(MP5)`. Comparing degrees in `(MP4)` gives `deg Q=ell-a=s`. The tail has
`a<ell`, so `Q` is nonconstant. Equations `(2)` and `(MP5)` show that `Q`
divides both `D` and `V`, contrary to `gcd(D,V)=1`. QED.
