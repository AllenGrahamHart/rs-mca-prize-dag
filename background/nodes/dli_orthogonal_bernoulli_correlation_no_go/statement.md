# DLI orthogonal Bernoulli-correlation no-go

- **status:** PROVED
- **closure:** exact tensor counterexample
- **consumer:** `dli_c2pp_joint_reserve`

Coordinate independence, balanced coefficients, and orthogonality of the
constraint row spaces do not imply a polynomial-loss product bound for null
events on a Bernoulli cube.

For `r>=1`, split `4r` independent uniform bits into blocks
`(X_(s,1),...,X_(s,4))`. Define

```text
U_s = X_(s,1)+X_(s,2)-X_(s,3)-X_(s,4),
V_s = X_(s,1)-X_(s,2)+X_(s,3)-X_(s,4),
A_r = {U_s=0 for every s},
B_r = {V_s=0 for every s}.
```

Every coefficient row is balanced, the `U` row space is orthogonal to the
`V` row space, and

```text
P(A_r)=P(B_r)=(6/16)^r,
P(A_r intersect B_r)=(4/16)^r.
```

Consequently

```text
P(A_r intersect B_r)/(P(A_r)P(B_r))=(16/9)^r.             (NG)
```

The ratio already exceeds `sqrt(2n)` at `r=3`, `n=12`, and eventually
exceeds every fixed power of `n=4r`.

This does not falsify the DLI square-root candidate. That candidate also has
cyclic root-of-unity coefficients, a nested dyadic allocation of frequencies,
and antipodal first-owner deletion. It proves that at least one such extra
feature must do load-bearing work; a generic discrete Brascamp-Lieb, entropy,
or orthogonal-subspace assertion with only the properties above cannot close
the node.
