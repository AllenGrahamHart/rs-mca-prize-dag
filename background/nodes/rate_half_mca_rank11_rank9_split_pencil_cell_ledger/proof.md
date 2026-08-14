# Proof

Evaluation on the ten coordinates `B` has rank nine and kernel `F*u`.
Choose one codeword pair `(A_*,B_*)` agreeing with the received pair on `B`;
the component-star route supplies many such owners, so this set is nonempty.
Every other agreeing pair differs from it by

```text
(alpha*u,beta*u),       (alpha,beta) in F^2.
```

This is the affine owner plane `Pi_B`.

For a record of slope `gamma`, ownership means

```text
A+gamma B=h_gamma.
```

Inside `Pi_B` this is one nonempty affine line with direction
`(-gamma*u,u)`. Distinct slopes give nonproportional directions, so two
record lines meet in exactly one point. That point is one affine pair which
owns both records. Grouping record pairs by their unique intersection point
proves (1).

## Common root core and disjoint petals

At a coordinate `x in Z(u)`, all points of `Pi_B` have the same pair value.
Put `x in J_B` when this value equals the received pair. Then either every
owner point agrees at `x` or none does.

If `x notin Z(u)`, the map

```text
(alpha,beta) -> (A_*(x)+alpha u(x),B_*(x)+beta u(x))
```

is a bijection from the parameter plane to `F^2`. Exactly one owner point
can agree with the received pair at `x`. It follows that

```text
C_p=J_B disjoint_union P_p
```

and that all `P_p` are pairwise disjoint. Since `B subset J_B`,
`|J_B|>=10`, and

```text
sum_p |P_p|<=n'-|J_B|<=2097152-10.                  (4)
```

## Extension and owner charges

Every record assigned to the cell has at least 45153 full-rank component
extensions of `B`. Such an extension coordinate is outside `Z(u)` and its
component owner is the unique point on the record line whose petal contains
that coordinate. Summing extension incidences first over records and then
over owner points gives (2).

For a fixed owner point `p`, let `c_p=|C_p|`. The exception sets outside
`C_p` of distinct slopes owned by `p` are disjoint: at a coordinate outside
the core, equality of the received and owner affine lines determines at most
one slope. Since every record has agreement at least `m'`,

```text
t_p(m'-c_p)<=n'-c_p.
```

Support-wise pair noncontainment gives `c_p<m'`. The quotient is largest at
`c_p=m'-1`, so

```text
t_p<=n'-m'+1=(1048576-67472)+1=981105.               (5)
```

Combining (2), (4), and (5) yields

```text
45153*g
 <=981105*(2097152-10),
g<=45567659.
```

The proof is local to one fixed `B`; no count of rank-nine cells is made.
