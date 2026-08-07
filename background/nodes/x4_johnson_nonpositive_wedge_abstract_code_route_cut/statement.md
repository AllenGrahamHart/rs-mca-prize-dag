# Johnson-nonpositive wedge abstract-code route cut

- **status:** PROVED
- **closure:** route cut

At the official rate-half base tuple, put

```text
N=2^41,       A=N/2+t_XR,       e=N/8,       d=e-t_XR-1.
```

There exists an abstract family of more than `16N^3` pairs

```text
(P_i,Q_i),    P_i subset D\S0,  Q_i subset S0,
|P_i|=|Q_i|=e,
```

whose changed sets `W_i=P_i union Q_i` satisfy

```text
|W_i intersect W_j|<=e+d       for i!=j.              (AC-1)
```

The parameters also satisfy the exact side-width pin `e=t_XR+d+1` and lie in
the Johnson-nonpositive wedge `4e^2<=N(e+d)`.

Thus `(AC-1)`, the side-width pin, and official row arithmetic alone cannot
prove a polynomial bound on the remaining wedge.  A valid continuation must
use locator divisibility/coefficient equations, coefficient primitivity, or
the declared first-owner predicates.

The constructed pairs are abstract blocks.  They are not asserted to satisfy
`deg(L_P-L_Q)=d`, so this is not a counterexample to X4/SP or either Prize
problem.

## Falsifier

Failure of the official upper bound on `t_XR`, failure of the binary-code
construction or its intersection identity, a family size at most `16N^3`,
or an assertion that the abstract blocks are actual locator incidences.
