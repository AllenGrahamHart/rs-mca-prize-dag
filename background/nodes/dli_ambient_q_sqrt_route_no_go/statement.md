# DLI ambient-Q square-root route no-go

The stronger ambient route

```text
K_amb(n,t,q)
 = q^t P(Prim intersect Phi^(-1)(0))
 = q^t (Z_0-C_1)/2^n
 <= sqrt(2n)                                                (AQSQRT)
```

is false even for a one-sided nested DLI prefix with first-owner deletion.
At

```text
(n,t,q,zeta)=(32,2,33409,7473),
```

`q` is prime, `zeta` has exact order 32, and exact subset-sum censuses give

```text
Z_0=384,       C_1=256,       Z_0-C_1=128,
Z_1=1696000,  B_0=174912.
```

Therefore

```text
K_amb = 1116161281/33554432 = 33.264... > sqrt(64)=8,       (NQ1)
J_prim = 33554432/18106125 = 1.853... < 8.                 (NQ2)
```

Thus the ambient replacement loses a factor essential to the true Haar
target. It does not falsify `J_prim<=sqrt(2n)` or C2''.

As supporting exhaustive evidence, all 189 primes

```text
32768<q<65536,       q=1 mod 32
```

were scanned exactly. Ambient `(AQSQRT)` fails at 56 rows, while the true Haar
ratio fails at none; its maximum is

```text
2097152/505197 = 4.151... < 8       at q=37217.
```

The complete scan is evidence; the explicit `q=33409` certificate alone
proves the no-go.

