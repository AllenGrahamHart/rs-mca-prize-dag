# HGE4 linear-boundary orbit bound

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_boundary_defect_trace_pin`

Let `m=3h+1` be dyadic with `h>1`, and work in characteristic zero or
characteristic greater than `4h`. For a non-full ordered shift pair at exact
ratio level `m`, normalize its scaling orbit by `P(0)=1` and put

```text
x=Q(0) in mu_m\{1},
d=x-1,
a=(1+x)/(x(x-1)^2).
```

Define

```text
C_0=1,
C_j=product_(r=0)^(j-1)(3r+1)/j!.
```

Then the normalized locator is forced coefficient by coefficient:

```text
P(X)=sum_(j=0)^(h-1) C_j a^j X^(h-j)+1.             (LBO1)
```

The value `x=-1` is impossible when `h>1`. Consequently normalized ordered
scaling orbits inject into `mu_m\{1,-1}`, and

```text
E_h^prim(m,p)<=m-2.                                 (LBO2)
```

Every survivor also passes the one-variable endpoint equation

```text
h! x^h(x-1)^(2h)
 =2 product_(r=0)^(h-1)(3r+1) (1+x)^(h-1).          (LBO3)
```

Thus the entire `e=1` exact-level width is analytically paid. Equation
`(LBO3)` is a stricter candidate screen, not a converse to the split-root
conditions.
