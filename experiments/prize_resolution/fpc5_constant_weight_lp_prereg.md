# FPC5 constant-weight LP screen: preregistration

## Question

Can the ordinary Delsarte linear-programming bound for the Johnson scheme
improve the new support-shortening cap enough to approach the first blocked
rate-`1/16` scale?

The representative dominant shell is

```text
length N=511,
support weight w=255,
minimum binary distance 224 (Johnson distance sigma=112).
```

The proved shortening cap is

```text
1751945892004456252745 < 2^71.
```

The most restrictive dominant cell needs a per-chart cap near
`1.9*10^15`, about 20 bits smaller, before outer background and touched-set
multiplicities can fit the strict prize budget.

## Method

Solve the standard Johnson-scheme inner-distribution LP numerically. Variables
`A_i` are indexed by Johnson distance `i>=112`, with `A_0=1`,
`A_i>=0`, and the Delsarte inequalities

```text
1+sum_i A_i Q_k(i)>=0,       1<=k<=255.
```

The normalized dual-Hahn values are computed exactly as

```text
Q_k(i)=E_i(k)/[binom(w,i)binom(N-w,i)],
E_i(k)=sum_(j=0)^i (-1)^(i-j)
       binom(w-j,w-i) binom(w-k,j)
       binom(N-w+j-k,j).
```

SciPy/HiGHS receives floating projections of these exact rational
coefficients. The output is a route screen only, not a proof certificate.

## Decision rule

- **PAYMENT SIGNAL:** numerical optimum at most `2*10^15`.
- **USEFUL SIGNAL:** optimum below `2^60`; seek an exact rational dual.
- **WEAK/NO SIGNAL:** optimum at least `2^66`; arbitrary support LP saves too
  little, so return to the primitive/background guard or split-divisor
  structure.
- A failed, timed-out, or numerically unstable solve changes no DAG status.

## Resource contract

One Modal container, two CPUs, 1 GiB RAM, 60-second function timeout. The
worker checks a 50-second internal deadline and returns partial matrix status
instead of intentionally starting a larger run. No local heavy computation.
