# Rank-eleven relative core-interpolant and correction-ray payment

- **status:** PROVED
- **scope:** one full-rank relative high-complexity core `(H_C)` on the
  shortened row `(n',K',m')=(R+K',K',d+K')`
- **range:** `10<=K'<=1048576`, `(R,d)=(1048576,67472)`

Fix the 32 residual explanations of `(H_C)` and let `H(X,Z)` be their unique
coefficientwise slope interpolant of degree at most 31. The residual maximal
supports have empty common intersection.

1. At most

   ```text
   floor(31n'/m') <= 481
   ```

   bad slopes can use the codeword `H(X,gamma)` itself. Outside the 32 core
   slopes, at most `449` additional slopes do so.
2. Fix any nonzero residual codeword direction `P`. The complete set of rich
   correction pairs

   ```text
   h_(gamma,c)=H(X,gamma)+cP(X)
   ```

   has at most

   ```text
   n'(n'-m'+1)+31*C(n',2)
   <= 70227214729216
   ```

   elements. Counting pairs only overestimates distinct slopes.

Consequently, an over-budget `(H_C)` family cannot be explained by the core
interpolant together with one projective correction ray:

```text
481+70227214729216=70227214729697 < B_*.
```

The result is uniform over arbitrary deleted common-core coordinates and
uses no smooth-domain or deployed first-match spread premise.

## Falsifier

An identically zero coordinate error polynomial despite empty maximal core;
more than 31 roots of a nonzero coordinate polynomial; a nonaffine clone
class larger than `K'-1`; a remaining rich point whose support contains no
heterogeneous coordinate pair; a heterogeneous pair supporting more than
31 correction parameters; or a total exceeding the printed uniform bound.
