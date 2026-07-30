# Proof - M31 adjacent quotient-rotation product spectrum

The parameter identities in (MQR1), (MQR2), and (MQR5) are immediate. The
general quotient-rotation theorem applies because `c|n/2`, `N=32`, `d=1`,
`m=17`, and `0<s<c`. Its high-prefix proof has two disjoint coefficient
blocks when `d=1`: the fixed monic block and `a_0(A)L_0`, where `L_0` is the
fixed partial-root locator and

```text
a_0(A)=(-1)^17 product(A).
```

The leading coefficient of `L_0` is one, so distinct products give distinct
high prefixes, while equal products give the same high prefix. It remains to
count 17-subsets of the 31 nonidentity elements of `C_32` by product.

Let `zeta` generate `C_32`. Fourier inversion gives

```text
C_r=(1/32) sum_(t=0)^31 zeta^(-rt)
       [y^17] product_(j=1)^31 (1+y zeta^(tj)).       (MQR8)
```

For `t=0`, the coefficient is `binom(31,17)=265182525`. If `t` has even
order `o` and `g=32/o`, then

```text
product_(j=1)^31(1+y zeta^(tj))=(1-y^o)^g/(1+y).
```

The coefficient of `y^17` is

```text
a_o=-sum_(ell=0)^floor(17/o) (-1)^ell binom(g,ell),
```

and the five possible values are

| `o` | 2 | 4 | 8 | 16 | 32 |
|---:|---:|---:|---:|---:|---:|
| `a_o` | -6435 | -35 | -3 | 1 | -1 |

Grouping `t` by order turns (MQR8) into

```text
C_r=(1/32)(265182525
           -6435 c_2(r)-35 c_4(r)-3 c_8(r)
           +c_16(r)-c_32(r)),                        (MQR9)
```

where `c_q` is the Ramanujan sum. For `q=2^j`,

```text
c_q(r)= q/2   if q|r,
        -q/2  if q/2|r but q does not divide r,
         0    otherwise.
```

Substitution gives exactly the four rows in (MQR3). Their weighted sum is

```text
16*8287155+8*8286755+5*8286751+3*8286750
=265182525,
```

and the maximum is (MQR4). The quotient-rotation theorem now supplies the
received word and distinct exact-agreement codewords, proving (MQR6).
Finally, direct subtraction gives (MQR7). QED.
