# L1 Mersenne HNF Frobenius reciprocal gate

- **status:** PROVED
- **dependency:** `l1_mersenne_next_to_maximal_hypergeometric_normal_form`
- **consumer:** `l1_mixed_petal_amplification`

Consider the `ord_0(T)=0` chamber of the dependency. Thus `h=m-1`,
`m in {8,16}`, and

```text
P_s(W)=sum_(r=0)^h binom(s+r-1,r)W^(h-r),
P_s | W^(m(p+1))-1,             s notin F_p.          (FRG1)
```

Define the monic degree-`h` polynomial

```text
Q_s(Z)=Res_W(P_s(W),Z-W^m)=sum_(j=0)^h q_j(s)Z^(h-j),
q_0=1,       C(s)=q_h(s).                              (FRG2)
```

Its coefficients lie in `F_p[s]`, and

```text
C(s)=-binom(s+h-1,h)^m.                               (FRG3)
```

Every survivor satisfies the exact Frobenius reciprocal identity

```text
C(s)Q_(s^p)(Z)=Z^h Q_s(1/Z).                         (FRG4)
```

Equivalently, the pair `(s,t)=(s,s^p)` is an off-diagonal point of the
bounded-degree coefficient system

```text
E_j(s,t)=C(s)q_j(t)-q_(h-j)(s)=0,       0<=j<=h,
t!=s.                                                   (FRG5)
```

The polynomials `q_j` depend only on `m,h`; the official characteristic
enters after this system through reduction modulo `p` and the one equation
`t=s^p`. Therefore a unit certificate for the saturation

```text
<E_0,...,E_h> : (t-s)^infinity                         (FRG6)
```

closes the complete order-zero chamber before any degree-`n` remainder or
inner Belyi lift. If the saturation is nonunit, its exact components are only
necessary candidates: each must still pass `t=s^p`, `P_s|W^n-1`, and the
inner equations.

This gate does not treat `ord_0(T)=1`, assert that the off-diagonal system is
empty, or promote L1.
