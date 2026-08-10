# Proof

Fix a minimizing pair `(g,h)` from `(FRC1)` and a supported slope `gamma`
different from both. Since `a*` is the minimum union of any two distinct
locator sets,

```text
|S_gamma union S_g|>=a*,       |S_gamma union S_h|>=a*.
```

Inclusion-exclusion therefore gives

```text
|S_gamma intersect S_g|<=u_gamma+u_g-a*,
|S_gamma intersect S_h|<=u_gamma+u_h-a*.              (1)
```

Because `W*=S_g union S_h`, subadditivity and `(1)` imply

```text
|S_gamma intersect W*|
 <=|S_gamma intersect S_g|+|S_gamma intersect S_h|
 <=2u_gamma+u_g+u_h-2a*.                              (2)
```

Substituting `u_delta=rho-o_delta` into `(2)` proves `(FRC2)`. Subtracting
`(2)` from `|S_gamma|=u_gamma` proves

```text
|S_gamma \ W*|>=2a*-u_gamma-u_g-u_h,
```

and the same substitution proves `(FRC3)`.

Finally, insert `rho=4m-1`, `a*=7m-1`, and zero defects:

```text
4rho-2a*=2m-2,       2a*-3rho=2m+1.
```

This is `(FRC4)`. QED.
