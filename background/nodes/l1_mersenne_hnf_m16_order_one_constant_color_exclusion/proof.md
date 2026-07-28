# Proof - L1 Mersenne HNF m=16 order-one constant-color exclusion

Put

```text
Q_+(S)=28S^2+29S+370,
Q_-(S)=28S^2+27S-1202,
P_4(S)=S^4-4S^2+2.                                  (1)
```

The factors `S`, `S^2-4`, and `S^2-2` are excluded directly. For `Q_+`,
the values at `S=0,+2,-2` are `370,540,424`. On `S^2=2`, a common root
would force

```text
426^2-2*29^2=179794=7783 mod 8191,                  (2)
```

which is nonzero. For `Q_-`, the three values are
`-1202,-1036,-1144`; on `S^2=2`, a common root would force

```text
1146^2-2*27^2=1311858=1298 mod 8191,                (3)
```

again nonzero.

It remains to exclude the primitive trace factor `P_4`. For a quadratic

```text
Q(S)=aS^2+bS+c,
```

put

```text
L=-b(b^2-2ac-4a^2),
M=-cb^2+ac^2+4a^2c+2a^3.                            (4)
```

Reduction of `P_4` modulo `Q` gives

```text
P_4(S)=(LS+M)/a^3 mod Q.                            (5)
```

When `L!=0`, a common root would consequently force

```text
aM^2-bML+cL^2=0.                                    (6)
```

For `(a,b,c)=(28,29,370)`, equations (4) and (6) give

```text
(L,M,aM^2-bML+cL^2)=(3964,47,4509) mod 8191.        (7)
```

For `(a,b,c)=(28,27,-1202)`, they give

```text
(L,M,aM^2-bML+cL^2)=(439,321,4947) mod 8191.        (8)
```

The last entries are nonzero, so neither quadratic meets `P_4`. Equations
(2), (3), (7), and (8) prove both unit gcds in (CCE15). The dependency then
excludes every possible sixteenth-root trace in the constant-color chamber.
QED.
