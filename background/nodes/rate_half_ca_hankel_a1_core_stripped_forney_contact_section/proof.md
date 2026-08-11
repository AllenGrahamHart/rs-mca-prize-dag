# Proof

The core-stratified ledger supplies the contracted residual pencil. It has
generic rank `d`, `d+1` columns, and `rho` rows; its regular Kronecker size is
`Delta`. Its primitive right-kernel generator is `Qbar`.

Maximality of the stripped core rules out an `X`-only factor, while
parameter primitivity rules out a parameter-only factor. Moreover, at least

```text
T-Delta
 >=rho+2-(rho-s-(s+1)e)
 =(s+1)e+s+2>e                                      (1)
```

supported fibres specialize `Qbar` to a squarefree split polynomial. The
same leading-coefficient argument as in the core-free case excludes a
repeated mixed factor. Thus `C` is reduced and every component is mixed.

Use all contracted moments and write

```text
Y(z;u)=sum_(i=0)^(d+rho-1)x_i(z)u^i.                 (2)
```

The `rho` recurrence rows cancel the coefficients of `qbar^vee Y` in
degrees `d,...,d+rho-1`. Hence

```text
qbar^vee Y=N_F+u^(d+rho)R                            (3)
```

for a polynomial `R`. If `N_F` vanished, its low coefficients would kill
`x_0,...,x_(d-1)`, and the recurrence rows would then kill the remaining
`rho` moments. That would make the contracted pencil zero, contrary to
generic rank `d`. Thus `N_F` is nonzero.

On `C`, equation `(3)` gives contact order `d+rho` at domain infinity. The
numerator has bidegree at most `(d-1,e+1)`, so it defines a nonzero section
of

```text
O_C(d-1-(d+rho),e+1)=O_C(-rho-1,e+1).                (4)
```

Finally, using `d=rho-s`,

```text
(-rho-1)e+(e+1)d=d-(s+1)e=Delta.                    (5)
```

This proves `(A1S2)`. QED.
