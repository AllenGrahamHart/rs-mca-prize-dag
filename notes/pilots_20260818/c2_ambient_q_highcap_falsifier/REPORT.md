# C2 ambient-Q high-cap falsifier: report

## Verdict

The stronger scale-free ambient route is **FALSIFIED**. The complete
registered range contains 189 primes; 56 have nonempty primitive zero fibers
and violate `K_amb<=sqrt(2n)`. The first is

```text
(n,t,q)=(32,2,33409),
Z_0=384, C_1=256, primitive=128,
K_amb=1116161281/33554432=33.264...>8.
```

The preregistered Haar follow-up is **SILENT** against the original
square-root candidate. All 189 rows satisfy `J_prim<=8`; the maximum is

```text
J_prim=2097152/505197=4.151...       at q=37217.
```

At the first ambient firing, `Z_1=1696000` and `B_0=174912`, so

```text
J_prim=33554432/18106125=1.853...<8.
```

The actual Haar denominator, discarded by the ambient floor, is therefore
load-bearing. The target C2'' statement is not falsified.

## Coverage

- Every prime `32768<q<65536`, `q=1 mod 32`: 189/189.
- Four first-pass shards: all PASS, each at most 1.88 seconds.
- Four Haar follow-up shards: all PASS, each at most 3.26 seconds.
- Exact integer gates only; every nonempty primitive count is divisible by
  the rotation orbit size 32.
- Independent Python replay of `q=33409`: PASS.

## Runs

```text
ambient scan: ap-cyl68HXbcxGroGwKLkgEzV
Haar follow-up: ap-f5LlJXuPCIZakI3SGTNs57
```

No transport from `n=32,t=2` to the official row is claimed. The route cut is
logical: a universal scale-free ambient theorem is false.

