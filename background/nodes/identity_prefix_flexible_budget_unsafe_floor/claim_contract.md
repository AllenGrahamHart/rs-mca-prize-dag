# Claim contract

## Inputs

- finite fields `B <= F`, `q=|F|`, and `D subset B` of size `n`;
- `C=RS[F,D,k]`, integer agreement `m in [k+1,n]`;
- target exponent `t` and `B*=floor(q/2^t)`;
- exact proofs of the two displayed strict integer inequalities.

## Output

One ambient-field simple-pole line with at least `B*+1` distinct support-wise
MCA-bad slopes at agreement `m`.

## Guards

- `w=m-k-1`, because the prefix list lives in the dimension-`k+1` code;
- the first inequality is strict;
- the collision budget uses `binom(B*+1,2)k`, not `B*^2 k/2`;
- the denominator and counted slopes both use the ambient field `F`;
- endpoint conversion is `delta=1-m/n` in the closed-ball convention.

Failure of a guard or sufficient inequality invalidates the certificate but
does not prove the row safe.
