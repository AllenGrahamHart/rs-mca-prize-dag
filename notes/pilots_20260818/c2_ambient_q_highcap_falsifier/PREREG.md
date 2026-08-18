# C2 ambient-Q high-cap falsifier: preregistration

## Candidate under attack

The proved fixed-weight ambient-Q bridge makes

```text
K_amb(n,t,q) = q^t (Z_0-C_1)/2^n <= sqrt(2n)             (AQSQRT)
```

a sufficient strengthening of the C2'' square-root route. This is not a DAG
premise. The purpose of this pilot is to try to kill it before using it.

Primitive supports on a cyclic `2`-group occur in rotation orbits of size
`n`. For `(n,t)=(32,2)`, if

```text
q^2/2^32 > sqrt(64)/32 = 1/4,
```

then one primitive orbit already violates `(AQSQRT)`. Thus the complete
high-cap analogue is

```text
32768 < q < 65536,       q prime,       q=1 mod 32.       (HC)
```

## Exact experiment

Exhaust every prime in `(HC)`. For each field, choose a primitive order-32
root `zeta` and compute

```text
Z_0 = #{S subset Z/32 : sum_(i in S) zeta^i =
                         sum_(i in S) zeta^(2i) = 0},
C_1 = #{T subset Z/16 : sum_(i in T) zeta^(2i) = 0}.
```

Use two independent 16-coordinate subset-sum histograms for `Z_0`; enumerate
the owner census separately. All comparisons are integer-only.

## Registered verdicts

- **FALSIFIED:** some row has `Z_0-C_1>0`, equivalently `(AQSQRT)` fires in
  this complete high-cap regime.
- **SURVIVED:** every prime in `(HC)` has `Z_0=C_1`. This is evidence for an
  emptiness branch only; it proves no transport to `n=2^41,t=2^33`.
- **INCOMPLETE:** any prime in `(HC)` is omitted or any shard times out before
  returning its complete interval. Partial rows remain recorded.

The original Haar-normalized `J_prim<=sqrt(2n)` is not under attack here. A
failure of `(AQSQRT)` does not falsify C2'' because its true denominator can
be larger than `q^-t`.

