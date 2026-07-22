# L1 boundary-Q planted-root descent

- **status:** PROVED
- **role:** remove every domain root of the boundary minimal vector before Q
- **consumer:** `l1_mixed_petal_amplification`

## Statement

Use the boundary profile and basis

```text
g_1=(W_1,N_1),       g_2=(W_2,N_2),
d_1=w+1,             d_2=omega,
det(g_1,g_2)=gamma Omega.
```

Let an affine-cell exact member be the codeword `P`, agreement locator `L`,
and complement locator `W=Omega/L`.  Then, up to the nonzero scalar introduced
by projective normalization,

```text
W_1 P-N_1=c_P L.                                      (PR1)
```

Put

```text
D=gcd(W_1,Omega),       S=roots_H(D),       r=deg D.  (PR2)
```

Then `D|N_1`, every exact member agrees with `U` on all of `S`, and `D|L`.
Writing

```text
W_1=D Wbar_1,       N_1=D Nbar_1,       L=D Lbar,
H'=H\S,             Omega'=Omega/D,
```

gives the root-free projective cell

```text
Wbar_1 P-Nbar_1=c_P Lbar,       gcd(Wbar_1,Omega')=1. (PR3)
```

The exact affine boundary cell is in bijection with the degree-below-`k`
polynomials `P` which:

1. satisfy the `r` planted conditions `P|S=U|S`; and
2. make the left side of `(PR3)` a nonzero scalar multiple of a monic
   degree-`m-r` divisor of `Omega'`.

If `r>=k`, the cell has at most one member.  If `r<k`, let `P_S` be the
degree-below-`r` interpolant of `U|S` (zero when `r=0`).  Every candidate is
uniquely

```text
P=P_S+D R,       deg R<k-r,                              (PR4)
```

and `(PR3)` becomes

```text
W_1 R+(Wbar_1 P_S-Nbar_1)=c_P Lbar.                     (PR5)
```

Thus descent preserves the surplus

```text
(m-r)-(k-r)=w,                                          (PR6)
```

and leaves one root-free rational-Q atom on `H'`, with no sum over planted
owners.

## Scope

No row-sharp bound for `(PR5)`, quotient coalescing, smooth-domain inheritance,
or transport to the fixed-column locator-Q atom is proved.  When `W_1=1`,
`D=1` and this reduces to the standard polynomial-led boundary cell.
