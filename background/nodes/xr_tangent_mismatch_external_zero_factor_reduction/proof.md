# Proof

Outside `T`, both error vectors vanish. On `W=S\T`, the witness equation

```text
p_z=u+zv
```

therefore gives `q_z=0`. Since the points of `D` are distinct, the locator
`P_W` divides the polynomial `q_z`. The latter is nonzero and has degree
below `K`, so `d=|W|<=K-1` and `g_z=q_z/P_W` has degree below `K-d`.

The locator has no zero on `T`, so the scaled words `b_0,b_1` are well
defined there. For `x in S intersect T`, divide

```text
q_z(x)=e_0(x)+z e_1(x)
```

by `P_W(x)` to obtain `g_z(x)=b_0(x)+z b_1(x)`. The agreement set has size

```text
|S intersect T|=A-d.
```

The degree bound makes the punctured code dimension `K-d`; it is legitimate
because `A-d=(K-d)+h<=|T|`. Finally,

```text
|T|-(A-d)
 = [|T|-(K-d)]-[(A-d)-(K-d)]
 = R-h.
```

This proves every assertion. Canonical selection and aggregation over the
external-zero charts remain the critical target.
