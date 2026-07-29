# Proof

Let `chi:F_257 -> mu_128 union {0}` be the character determined by

```text
chi(0)=0,             chi(3^j)=zeta_128^j.
```

The residue 3 is primitive modulo 257 and `zeta_128 -> 9=3^2` at `q_1`, so
this is the 128th-power residue character attached to `q_1`.

Use the 32 pairs

```text
(a_1,b_1)=(32,32),
(a_i,b_i)=(1,i-1),                 2<=i<=32,
```

and Jacobi sums

```text
j_i=-sum_(x in F_257) chi(x)^a_i chi(1-x)^b_i.       (SR2)
```

For odd `s mod 128`, put

```text
carry_i(s)=((a_i s mod 128)+(b_i s mod 128)
            -((a_i+b_i)s mod 128))/128,
epsilon_i(s)=1-carry_i(s).                           (SR3)
```

All residues in `(SR3)` are least nonnegative residues. The classical
Stickelberger factorization of Jacobi sums gives

```text
(j_i)=product_(s odd mod 128) q_s^epsilon_i(s).      (SR4)
```

The complement in `(SR3)` is important: for example every `j_i` reduces to
zero at `q_1`, where `carry_i(1)=0`.

Now take the integer vector

```text
c=(21121,-24549,-26280,-22490,-16564,-12336,-20492,-20254,
   -28314,-25086,-29901,-20529,-12414,-5602,-8856,-7172,
   2231,7193,0,3708,10233,17881,9371,20529,14851,21121,
   15861,21263,29977,42499,39176,46066).             (SR5)
```

Exact integer arithmetic gives, for every odd `s mod 128`,

```text
sum_i c_i(epsilon_i(s)-epsilon_i(-s))
 =  2 ell,  s=1 or 63,
 = -2 ell,  s=65 or 127,
 =  0,      otherwise.                              (SR6)
```

Define the fractional cyclotomic integer

```text
alpha=product_(i=1)^32 (j_i/bar(j_i))^c_i.           (SR7)
```

Conjugation replaces `s` by `-s` in `(SR4)`. Therefore `(SR6)` applied to
`(SR7)` gives

```text
(alpha)=(q_1 q_63/(q_127 q_65))^(2 ell)=I^(2 ell).
```

This is `(SR1)`. QED.
