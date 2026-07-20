# Audit

1. The signed-factor field bound is denominator-only and applies to the
   `c=1` role patterns; the matched source equations are not imported.
2. The surviving field line is `q_field=p^2`, `p=1 mod 2^40`. The stronger
   congruence `p=1 mod 2^41` is not assumed.
3. The top source lift `r` is allowed to be Frobenius anti-invariant. Only
   `t=r^4` and the matched unordered outer trace must descend.
4. The scalar identity is `S^2=(y+2)T`; omitting `+2` is a detected mutation.
5. The correct square-class endpoint is `T/q_out=W^4`. Testing `T=W^4`
   would falsely reject exact-order outer ratios in the nonsplit prime-field
   congruence shard.
6. The trace depth is 39 because the outer ratio lies in `mu_(2^39)`.
7. The constant gate follows from `S(0)=2H` and `T(0)=-1/t`; it is
   `4tH^2+y+2=0`.
8. The gcd gate is necessary, not sufficient, and does not justify a dense
   official-degree computation.

