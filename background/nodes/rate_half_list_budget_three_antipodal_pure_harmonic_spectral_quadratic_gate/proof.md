# Proof

Let the roots of the two quadratic factors in `(HSQ2)` be `x,y` and `z,t`.
Choose lifts

```text
a^2=x,       b^2=y,       c^2=z,       e^2=t
```

and put `alpha=ab`, `beta=ce`. Thus

```text
alpha^2=q,       beta^2=u,
(a+b)^2=S+2alpha,       (c+e)^2=T+2beta.                (1)
```

The harmonic pairing equation for this split is

```text
h=2(alpha+beta)-(a+b)(c+e)=0.                           (2)
```

Fixing the signs of `alpha,beta`, the two remaining sign classes change the
sign of `(a+b)(c+e)`. Their product in `(2)` is

```text
F=4(alpha+beta)^2-(S+2alpha)(T+2beta)
 =4q+4u-ST-2Talpha-2Sbeta+4alpha beta.                  (3)
```

Taking the norm in `beta^2=u` first and reducing `alpha^2=q` gives

```text
N_beta(F)=C_0+C_1alpha,                                 (4)
```

where `C_0,C_1` are exactly the expressions in `(HSQ3)`. The remaining norm
in `alpha^2=q` is

```text
N_alpha N_beta(F)=C_0^2-qC_1^2=P(D_1,D_2).              (5)
```

Equations `(3)--(5)` multiply `(2)` over all eight lift-sign classes modulo
simultaneous negation. Therefore `(HSQ3)` is exactly the pairing factor of
the binary-quartic harmonic support norm. It vanishes if and only if one sign
class realizes this harmonic pairing. The three quadratic splittings are the
three pair partitions of four roots, so testing all three is equivalent to
the complete harmonic support norm.

The spectral reconstruction theorem proves that `(HSQ1)` and its two
fourth-power tests reconstruct the unique normalized pure norm packet.
`X^4+e_4` has a harmonic root set whenever it splits with `e_4!=0` in the
official characteristic. Equality of the unordered harmonic cross-ratio
orbits is exactly the Mobius matching required by the pure harmonic-Fermat
router. Hence adjoining `(HSQ4)` is necessary and sufficient for the
harmonic-matched packet. QED.
