# `A=1` collision shape-A global subgroup genus floor

- **status:** PROVED
- **closure:** the shape-A normalization has genus at least
  `131176846286340314460`
- **scope:** the official prime-field shape-A collision branch
- **consumer:** `rate_half_band_crossing_location`

Retain shape A and put

```text
N=2^41,             H=mu_N,
e=(2^39+1)/3,       m=e-2,
n=(3e-7)/2,         R=(9e-7)/2,
P_char>2^167.                                      (SGF1)
```

Let `C` be the normalization of the absolutely irreducible curve
`G(t,X)=0`. The coordinate functions have degrees

```text
deg_C(t)=n,       deg_C(X)=m.                      (SGF2)
```

The classified-row splitting gives at least

```text
P=Rm=151115727450087753427630                      (SGF3)
```

distinct points of `C` with both coordinates in `H`. The functions `t`
and `X` are multiplicatively independent modulo constants. If `S` is the
union of their zero and pole supports and

```text
chi_C=|S|+2g(C)-2,
```

then

```text
chi_C >= ceil(P^3/(54N^2mn))
      =262353693488940318721.                      (SGF4)
```

Since `|S|<=2(m+n)`, this forces

```text
g(C)>=131176846286340314460.                       (SGF5)
```

## Scope

This is a lower bound, not a shape-A exclusion. The full bidegree genus
ceiling is `(m-1)(n-1)=50371909149143533442400`, so the theorem leaves a
factor smaller than `385` between the forced genus and that ceiling. A
closure through this route now requires a source/Pade genus upper bound
strictly below `(SGF5)`, or a stronger subgroup-point theorem. Reusing the
generic bidegree genus ceiling does not close the branch.
