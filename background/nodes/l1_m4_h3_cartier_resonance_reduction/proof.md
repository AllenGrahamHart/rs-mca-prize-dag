# Proof - L1 m=4, h=3 Cartier resonance reduction

Put

```text
L=n-3nu,       A=U^3D.
```

The Wronskian identity from the dependency is

```text
XA'-LA=U^2H.                                           (1)
```

For any nonnegative integer `s`, the product rule gives

```text
(X^sA)'=X^(s-1)(sA+XA')
        =X^(s-1)U^2(H+(s+L)UD).                       (2)
```

Since `L=4p+4-3nu`, the five choices in `(CRR2)` satisfy `s+L=0` in the
field. This proves `(CRR3)`.

Let `h=deg H`. The right side of `(CRR3)` is nonzero and monic up to the
nonzero leading coefficient of `H`; its degree is

```text
s-1+2(p-nu)+h.                                        (3)
```

At the previous maximum `h=4-nu`, expression (3) equals `3p-1` for
`nu=0,1` and `2p-1` for `nu=2,3,4`. But for every polynomial
`F=sum f_k X^k` in characteristic `p`, the coefficient of `X^(jp-1)` in

```text
F'=sum k f_k X^(k-1)
```

is `jp f_(jp)=0`. The nonzero leading coefficient on the right of `(CRR3)`
is impossible. Hence `h<=3-nu` for `nu<=3`. When `nu=4`, this would say
`h<=-1`, contradicting `H!=0`. This proves `(CRR4)`.

Finally, every remaining `jp-1` slot on the right side of `(CRR3)` must also
vanish. Removing the shift `s-1` gives the source degrees

```text
nu=0: (p-1)-(p-5)=4,       (2p-1)-(p-5)=p+4;
nu=1: (p-1)-(p-2)=1,       (2p-1)-(p-2)=p+1;
nu=2: (p-1)-1=p-2;
nu=3: (p-1)-4=p-5.
```

All later resonance slots lie above the improved degree in each case. This
proves `(CRR5)`.
