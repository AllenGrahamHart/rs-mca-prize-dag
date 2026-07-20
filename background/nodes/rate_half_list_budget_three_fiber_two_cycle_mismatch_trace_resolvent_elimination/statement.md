# Budget-three fiber-two mismatch trace-resolvent elimination

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_fiber_two_cycle_mismatch_invariant_coupling_router`

Retain the notation of the mismatch invariant router. Write

```text
D_*(Y)=Y^4-e_1Y^3+e_2Y^2-e_3Y+e_4
      =product_(A in Omega)(Y-A),
O(W)=W^4+alpha W^2+beta W+gamma,
I=alpha^2+12gamma,
J=72alpha gamma-27beta^2-2alpha^3.                 (MTR1)
```

The roots in `Omega` are distinct nonzero squares, and `O` is separable.
Both mismatch packets admit radical-free constant-degree eliminations.

For `c=2`, define the pair-trace resolvent

```text
R_D(Z)=product_({A,B} subset Omega)(ZAB-(A+B)^2)
      =sum_(j=0)^6 r_j Z^j.                         (MTR2)
```

Its coefficients depend only on `D_*` and are

```text
r_6=e_4^3,
r_5=-e_4^2(e_1e_3+8e_4),
r_4=e_4(e_1^2e_2e_4+6e_1e_3e_4-2e_2^2e_4
            +e_2e_3^2+24e_4^2),
r_3=-e_1^4e_4^2-e_1^2e_2e_4^2-e_1e_2^2e_3e_4
    -16e_1e_3e_4^2+8e_2^2e_4^2-e_2e_3^2e_4
    -e_3^4-32e_4^3,
r_2=3e_1^4e_4^2+e_1^3e_2e_3e_4-4e_1^2e_2e_4^2
    -e_1^2e_3^2e_4-2e_1e_2^2e_3e_4+e_1e_2e_3^3
    +24e_1e_3e_4^2+e_2^4e_4-8e_2^2e_4^2
    -4e_2e_3^2e_4+3e_3^4+16e_4^3,
r_1=-3e_1^4e_4^2+e_1^3e_2e_3e_4-e_1^3e_3^3
    -e_1^2e_2^3e_4+4e_1^2e_2e_4^2+2e_1^2e_3^2e_4
    +4e_1e_2^2e_3e_4+e_1e_2e_3^3-16e_1e_3e_4^2
    -e_2^3e_3^2+4e_2e_3^2e_4-3e_3^4,
r_0=(e_1^2e_4-e_1e_2e_3+e_3^2)^2.                (MTR3)
```

Put

```text
K_O(Z)=4I^3 Z(Z-36)^2-J^2(Z+12)^3.                 (MTR4)
```

Then the `c=2` completion-root coupling holds if and only if

```text
Res_Z(R_D,K_O)=0.                                   (MTR5)
```

The leading coefficient of `K_O` is `4I^3-J^2`, which is nonzero because
`O` is separable. Hence `K_O` has exact degree three. A nonconstant gcd
`gcd(R_D,K_O)` prints all passing pair-trace classes and has degree at most
three. Factoring `D_*` and matching one of its six pairs to a printed trace
recovers the original candidate and then its PGL map.

For `c=1`, choose `A in Omega` and an unordered pair
`{B,D} subset Omega\{A}`; the unused root is the residual exceptional
square `C`. There are exactly `4*binom(3,2)=12` such choices. Define

```text
P=BD,                         S=B+D,
X=A^2+P+3AS,                 Y=A^2+P-9AS,
E_0=A(Y-16P),                F_0=16A^2-Y,
J_even=4(E_0^2+P F_0^2),     J_odd=8E_0F_0,
I_even=X^3+192A^2XP,         I_odd=-24AX^2-512A^3P,
K_0=I^3J_even-J^2I_even,     K_1=I^3J_odd-J^2I_odd,
N_(A;B,D)=K_0^2-PK_1^2.                              (MTR6)
```

Then the `c=1` completion-root coupling holds if and only if at least one
of the twelve radical-free tests satisfies

```text
N_(A;B,D)=0.                                         (MTR7)
```

Thus the former `24+6` lift/root tests become twelve quadratic norms and
one degree-`6`/degree-`3` resultant. These expressions use only the roots
or coefficients of `D_*` and the canonical outer coefficients. They are
ready for substitution into the doubled-order gap and canonical-span
equations. The theorem does not make the resulting official-order
elimination small, prove either mismatch census empty, or authorize a
computation.

