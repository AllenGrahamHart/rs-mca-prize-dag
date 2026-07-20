# HGE4 boundary-defect trace pin

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_complement_separator_defect_normal_form`

Use the separator-defect notation, and write the top of the monic locator as

```text
P=X^h+aX^(h-1)+bX^(h-2)+...,
Q=P+d,
G=B-A.
```

Assume `h>e=m-3h`, as holds at every official `e=1,2` boundary width.
Then the two boundary systems have no independent coefficients in `G`:

```text
e=1, m=3h+1:
G=d^2 (a-(h/m)X),                                  (BTP1)

e=2, m=3h+2:
G=d^2 ((b-2a^2)+((m-1)/m)aX-(h/m)X^2).             (BTP2)
```

If `p_0=P(0)` and `q_0=Q(0)=p_0+d`, evaluation of the differential normal
form at zero gives the scalar gates

```text
p_0+q_0=d^2 a p_0q_0                 in the e=1 case, (BTP3)
p_0+q_0=d^2 (b-2a^2) p_0q_0          in the e=2 case. (BTP4)
```

Both constants lie in `mu_m`. In the dyadic `e=1` case,
`gcd(h,m)=1`; scaling the root sets uniquely normalizes `p_0=1`. With
`x=q_0 in mu_m\{1}`, one then has

```text
d=x-1,       a=(1+x)/(x(x-1)^2).                    (BTP5)
```

These are necessary trace and constant-term pins. They do not exclude either
boundary system or count its split subgroup-root solutions.
