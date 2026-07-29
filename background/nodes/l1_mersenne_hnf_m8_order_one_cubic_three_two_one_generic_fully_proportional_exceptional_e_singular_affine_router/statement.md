# L1 Mersenne HNF m=8 order-one cubic three-two-one exceptional-E singular-affine router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the `a_2!=0`, `S_1=S_0=0` chart (FEQ7) of the fully
  proportional official `h=7` cubic `3+2+1` residue

Put `z=b^2` and define

```text
A(z)=1575-247z,
C(z)=-800z^2+8929z-11025,
N(z)=40z^2+51z-2835,                               (FSA1)

E_0=42A(z)b+(z+27)C(z),
E_1=15A(z)(8z-21)
    +b(-52800z^2+710097z-1497825).                 (FSA2)
```

Then the singular coefficients satisfy

```text
S_0=360bE_0,             S_1=126E_1.               (FSA3)
```

On `z=b^2`, put

```text
R=163b(z+27)-N(z).
```

There is an exact identity

```text
(z+27)E_1-66bE_0=-3A(z)R.                         (FSA4)
```

The inherited chart has `b*A(z)!=0`. Hence `S_1=S_0=0` forces `R=0`.
Moreover `z+27` is a unit on every official solution: if `z=-27`, then
`N(z)=24948`, whose residues at the four official primes are
`(375,24948,24948,24948)`.

Define two quartics

```text
H(z)=N(z)^2-163^2 z(z+27)^2,
K(z)=42A(z)N(z)+163(z+27)^2C(z).                   (FSA5)
```

Then the complete singular coefficient-proportionality locus is equivalent
to

```text
H(z)=K(z)=0,
b=N(z)/(163(z+27)),
z=b^2.                                             (FSA6)
```

Both `H` and `K` have degree four in every official characteristic, with
leading coefficients `1600` and `-130400`. After reconstructing `b`, retain

```text
F_b(z,q)=X_*(b,q)=0.                               (FSA7)
```

Equation (FEQ3) then recovers `E_G=0`. The selected role packet, `P_4`, the
`J_*` split, every structural equation, saturation, and arithmetic-lift
filter remain mandatory. This is an exact two-quartic router, not a gcd,
root, ambient-quadratic-field, or emptiness verdict.
