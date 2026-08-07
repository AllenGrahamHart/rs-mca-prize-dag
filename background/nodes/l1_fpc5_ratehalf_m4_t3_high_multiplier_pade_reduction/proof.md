# Proof: high-multiplier Pade reduction

## 1. Quotient coordinates

For a monic LS6 candidate, leading degrees in

```text
D E=M Q+V
```

give

```text
deg Q=(2ell-a)+e-2ell=e-a,
lc(Q)=lc(E)=c.                                         (1)
```

Use `(HP4)` and subtract it from `(HP2)`:

```text
E(D-T_Q)=R_Q+V.                                        (2)
```

Both terms on the right have degree below `e`: `deg R_Q<e` by division and
`deg V<=s<e` by `(HP1)`. Since the right side is divisible by the degree-`e`
polynomial `E`, it must vanish. Hence

```text
D=T_Q,       V=-R_Q.                                   (3)
```

Conversely, any `Q` in `(HP5)` defines `(D,V)` by `(3)` and satisfies the
LS6 degree equation. Formula `(1)` makes `T_Q` monic of degree `j`. This
proves the bijection `(HP5)`--`(HP6)`.

## 2. Exactness guard

Every LS6 locator `D` divides the core locator `L_C`, while `M` is the
product of two disjoint petal locators. Thus `gcd(D,M)=1`. Reducing `(HP2)`
modulo `D` gives

```text
V==-M Q mod D.
```

Therefore

```text
gcd(D,V)=gcd(D,MQ)=gcd(D,Q),                           (4)
```

where the last equality uses `gcd(D,M)=1`. Combining `(3)` and `(4)` proves
`(HP7)`.

## 3. Inverse coordinates and the dual degree gate

Multiply `DE==V mod M` by the canonical inverse `F`. Since `deg D=j<2ell`,
the canonical representative is

```text
D=rem_M(FV),                                           (5)
```

proving `(HP9)`.

Put `f=deg F` and suppose, for contradiction, that `f<ell+a`. For every
`V` of degree at most `s=ell-a`,

```text
deg(FV)<=f+s<2ell,
```

so no reduction modulo `M` occurs in `(5)` and `D=FV`. On the live branch
`a<=ell/2`, one has `ell+a<=j`. Since `deg D=j` and `f<ell+a<=j`, the
polynomial `V` is nonconstant. It then divides both `D` and `V`, contrary to
the LS6 guard `gcd(D,V)=1`. Hence `f>=ell+a`, which is `(HP10)`.

For official cells,

```text
a<=floor((b-3)/4)<ell/4
```

because `b<ell`, so the live-branch hypothesis is automatic. QED.
