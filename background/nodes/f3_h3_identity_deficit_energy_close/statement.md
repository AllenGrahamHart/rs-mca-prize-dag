# C36' identity-deficit energy close

- **status:** see `dag.json` (single source of truth)
- **consumers:** `f3_h3_mobius_excess_half`, `f3_h3_three_to_one_c36`
- **dependencies:** `f3_h2_stepanov_inhouse`,
  `f3_h3_quotient_block_identity`
- **audit:** `audit.md`
- **claim contract:** `claim_contract.md`
- **dependency sub-DAG:** `dependency_subdag.md`

Let `H<=F_p^*` have official order `n`, put `A=(1-H)\{0}`, and define

```text
P(t)=#{(a,b) in A^2:ab=t},
R(t)=#{(c,d) in A^2:d/c=t},
E_x(A)=sum_t P(t)^2,
N_3to1(A)=sum_t P(t)R(t).
```

Product and quotient fibers have exactly the same `L2` energy, and their
correlation has the identity

```text
sum_t R(t)^2=E_x(A),
N_3to1(A)=E_x(A)-(1/2)sum_t(P(t)-R(t))^2.          (ID1)
```

The identity coordinate satisfies

```text
R(1)=n-1,       P(1)<4n^(2/3).                    (ID2)
```

Consequently the clean energy estimate

```text
4E_x(A)<=145(n-1)^2                              (ID3)
```

implies the original C36' bound

```text
N_3to1(A)<36n^2-16n^(4/3)-n/2                   (ID4)
```

on every official order `n=2^s`, `13<=s<=41`.

This is a strictly weaker energy target than the previously recorded
`E_x(A)<=35n^2`: for every official `n`,

```text
(145/4)(n-1)^2>35n^2.
```

The abstract profiles that violate the cutoff-18 premise at energy
`36(n-1)^2` do not refute this direct route: they do not simultaneously carry
the source identity-coordinate separation inside the correlation count.
This theorem does not prove `(ID3)` and does not promote C36'.
