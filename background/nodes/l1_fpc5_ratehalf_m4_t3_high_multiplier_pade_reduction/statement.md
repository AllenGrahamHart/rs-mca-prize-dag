# Rate-half FPC5 `M=4,t=3` high-multiplier Pade reduction

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`
- **upstream interface:** split-pencil/rational-approximation census

Fix one guarded LS6 atom and write

```text
M=L_2L_3,       deg M=2ell,
j=2ell-a,       s=ell-a,
E=Etilde,       e=deg E,       c=lc(E).
```

Assume the high-multiplier range

```text
e>s.                                                   (HP1)
```

For every candidate, the equation

```text
D E=M Q+V,       deg V<=s                              (HP2)
```

has

```text
deg Q=e-a,       lc(Q)=c.                              (HP3)
```

Divide, for each such `Q`,

```text
M Q=E T_Q+R_Q,       deg R_Q<e.                        (HP4)
```

Then the complete monic unguarded high-multiplier slice is exactly

```text
{T_Q : deg Q=e-a, lc(Q)=c, deg R_Q<=s},               (HP5)
```

with

```text
D=T_Q,       V=-R_Q.                                   (HP6)
```

Since every core divisor is coprime to the petal locator `M`, the guarded
atom is exactly the subfamily of `(HP5)` satisfying

```text
T_Q|L_C,       gcd(T_Q,Q)=1.                           (HP7)
```

Thus the LS6 gcd guard is a primitive numerator-denominator guard in the
high-multiplier quotient coordinates.

Let `F` be the canonical inverse multiplier,

```text
E F==1 mod M,       deg F<2ell.                        (HP8)
```

Every candidate also satisfies

```text
D=rem_M(FV).                                           (HP9)
```

On the live branch `a<=ell/2`, nonemptiness forces the dual degree gate

```text
deg F>=ell+a.                                          (HP10)
```

The official FPC5 tail has the stronger `a<ell/4`, so `(HP10)` applies to
every official cell.

## Scope

This is an exact two-sided Pade/rational-approximation reduction. It does not
bound the number of `Q` satisfying the high-coefficient conditions in
`(HP5)`, prove that `T_Q` splits, or pay primitive, periodic, or dihedral
solutions. It replaces the generic high-multiplier BC label by a smaller
guarded quotient problem.
