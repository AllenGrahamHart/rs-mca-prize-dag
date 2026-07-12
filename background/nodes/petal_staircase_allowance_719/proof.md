# Proof

Using

```text
C(n+6,6) = (n+1)(n+2)(n+3)(n+4)(n+5)(n+6)/720,
```

the strict upper inequality

```text
n^6 < 720 C(n+6,6)
```

is immediate because every factor `n+i` exceeds `n`.

For each of the four official maximal rows, direct exact integer multiplication
gives

```text
719 (n+1)(n+2)(n+3)(n+4)(n+5)(n+6) <= 720 n^6.
```

The verifier performs these four integer comparisons without floating-point
arithmetic, checks the quotient is exactly 719, and rejects the mutation that
replaces 719 by 720. This proves the claimed finite-row allowance.

