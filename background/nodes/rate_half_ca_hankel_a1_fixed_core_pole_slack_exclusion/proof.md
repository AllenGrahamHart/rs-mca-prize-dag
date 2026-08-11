# Proof

Work on the residual curve `C:Qbar=0` of bidegree `(d,e)`. Its residual
domain locator has degree `N-s`. The standard fibrewise multiplication
argument gives a pole-cancellation ideal of colength

```text
p<=O<=Delta.                                           (1)
```

Since `3(floor(p/3)+1)>p`, a nonzero form `F` of bidegree
`(2,floor(p/3))` clears the poles. On a component where the core-stripped
contact section is nonzero, a domain degree at most two would give contact
degree at most

```text
2(e+1)-(rho+1)<0,                                     (2)
```

because every fixed-core range has `e<=rho/2-1`. Thus `F` does not contain
that component, and the regular section `FG/H` is nonzero there.

Three contact copies produce a nonzero section of

```text
O_C(d-1,floor(p/3)-e+ell+3-beta).                     (3)
```

Indeed, the first coordinate is

```text
(N-s)+2-3(rho+1)=rho-s-1=d-1.
```

If `(A1X2)` holds, the second coordinate is negative. Subtracting the curve
equation leaves first degree `-1`, so the restriction sequence and Kunneth
give zero sections, a contradiction. This proves `(A1X2)` and `(A1X3)`.

For `s=1,e=m+1`, one has

```text
Delta=2m-3,       beta=1,       0<=ell<=3.            (4)
```

Using `p<=Delta`, the left side of `(A1X2)` is at most
`floor((2m-3)/3)+5`, which is less than `m+1` on the official row. Hence
the first degree is excluded.

It remains to prove the full `s=2` assertion. If `Delta>0`, then

```text
rho=3e+Delta+2,       beta=1,
ell<=T_max-rho-2=e-Delta-3.                           (5)
```

Therefore

```text
floor(p/3)+ell+2
 <=floor(Delta/3)+e-Delta-1<e.                        (6)
```

If `Delta=0`, then `3e=d`, `beta=2`, `p=0`, and

```text
ell<=T_max-rho-2=e-2,
floor(p/3)+ell+1<e.                                   (7)
```

Thus `(A1X2)` holds in every `s=2` profile. QED.
