# Proof

Under the hypotheses printed in `statement.md`, fix `d1` and
`m'=K-1+d1`. The identity-prefix map in the cited
proposition partitions the `C(n,m')` eligible level-`m'` supports among
at most `|B|^(d1-1)` prefix values. Therefore its heaviest fiber has at
least

```text
ceil(C(n,m') / |B|^(d1-1)) = ceil(A_B(d1))
```

members. The proposition's support-lift map contributes exactly
`C(m',m)` counted size-`m` objects for each selected level-`m'` member.
The source proof establishes that distinct fiber members give distinct
codewords and that the codeword attached to a valid support is unique
because `m>=K`; hence these contributions are distinct across members.
This multiplier is applied after the fiber has been selected, giving

```text
M_B^disc(d1)=C(m',m) ceil(A_B(d1)).
```

For every real `x`, `ceil(x)<=x+1`; multiplying by the nonnegative
support count gives the soft model

```text
M_B^disc(d1) <= C(m',m)(1+A_B(d1))=M_B^soft(d1).
```

If `0<A_B<1`, its ceiling is one, proving the nonvanishing support-spray
floor. The deployed values follow by exact integer evaluation of the
displayed formula. The verifier uses one million-scale binomial and
exact adjacent-binomial recurrences, checks the eight prefix ceilings,
and rejects the old ceiling-after-multiplication mutation.
