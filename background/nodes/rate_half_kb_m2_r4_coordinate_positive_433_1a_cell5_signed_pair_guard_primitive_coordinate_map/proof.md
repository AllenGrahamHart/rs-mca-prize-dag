# Proof

The primitive residue ledger supplies the monogenic etale algebra

```text
A_g ~= K[s]/(chi(s)),  s |-> ell=x1+2*x0+3*b,
```

of dimension 24 over `K=F_2130706433(t)`.  In the certified stable basis,
let `L` be multiplication by `ell` and let `e_1` be the cyclic first
basis vector.  Thus

```text
V = [e_1, L e_1, ..., L^23 e_1]
```

is invertible over `K`.

## Exact coordinate solves

The same exact quotient normal-form implementation independently computed
the stable-basis columns for multiplication of `e_1` by `x1`, `x0`,
and `b`.  For each `u` in that set, Nemo solved

```text
V c_u = u e_1
```

over `K` and checked the equality before exporting `c_u`.  Define
`p_u(s)=sum_(j=0)^23 c_u[j]s^j`.  Multiplication operators in the
commutative algebra commute with `L`, so equality on the cyclic vector
implies

```text
u L^j e_1 = L^j u e_1 = p_u(L)L^j e_1
```

for every `0<=j<24`.  These vectors span `A_g`; therefore
`u=p_u(s)` in `A_g), proving (KBCM-1).

The exact map packet has SHA-256

```text
001c959648176669651c87a913f2c830ad425a4f1e240041cc4edeb63d69a009.
```

It contains all 72 coefficients.  Their maximum numerator or denominator
degree in `t` is 1046.  The independently generated coordinate-column
packet has SHA-256

```text
f5bfdb6cb515b6bbe54fa1abd19d1517759b0a584f501aa308e76f68e1ff1e25.
```

## Independent checks

A standard-library checker cross-multiplies the three rational coefficients
in every `s` degree.  Polynomial products are exact NTT convolutions in
`F_2130706433[t]`; the modulus satisfies
`2130706433-1=127*2^24`.  It verifies (KBCM-2) coefficientwise, rather than
by sampling.

Independently, at the regular fiber `t=2`, it evaluates the full
24-by-24 multiplication matrix, evaluates every exported map coefficient,
forms `p_u(L)e_1`, and obtains exactly the separately generated column
`u e_1` for all three variables.  Hostile tests reject a dropped
coefficient, a changed coefficient, altered operator provenance, and a
changed source column.  The exact primary solve and these independent
checks prove (KBCM-1)--(KBCM-2).  QED.
