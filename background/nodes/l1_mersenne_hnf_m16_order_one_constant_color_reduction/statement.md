# L1 Mersenne HNF m=16 order-one constant-color reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the official `(m,h,p)=(16,15,8191)` next-to-maximal row

Put `d=c-1`, `r=rho*c`, and suppose all fourteen reduced roots have one
color `epsilon`. Define

```text
zeta=d^(p+1) in mu_16,       alpha=epsilon*zeta.     (CCR1)
```

The first two colored reciprocal coefficient equations force

```text
r=1-alpha,                                           (CCR2)
182alpha*d=(alpha+1)zeta+28alpha^2                  (CCR3)
```

outside the separately impossible values `alpha=+1,-1`.

Consequently `d in F_(p^2)`, `zeta in {+1,-1}`, and the trace
`s=alpha+alpha^(-1)` satisfies

```text
zeta=+1:       28s^2+29s+370=0 mod 8191;
zeta=-1:       28s^2+27s-1202=0 mod 8191.            (CCR4)
```

All possible traces of a sixteenth root are the roots of

```text
T_16(S)=S(S^2-4)(S^2-2)(S^4-4S^2+2).               (CCR5)
```

Thus two unit gcds

```text
gcd(T_16,28S^2+29S+370),
gcd(T_16,28S^2+27S-1202)        over F_8191          (CCR6)
```

close the complete constant-color chamber. Their verdict is not asserted
here. Degrees four through thirteen, actual cyclotomic divisibility, and
inner lifts also remain open.
