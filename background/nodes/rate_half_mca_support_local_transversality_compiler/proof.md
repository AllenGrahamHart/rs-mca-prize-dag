# Proof

Encode the affine explanation family by parameter points in `F^(s+1)`.
At coordinate `x`, agreement is an affine hyperplane with normal

```text
v_x=(r_1(x),-c_1(x),...,-c_s(x)).
```

Local pair noncontainment gives full incident rank. For a proper
`r`-dimensional normal span with `r<s`, the MDS common-zero argument leaves
at least `w+s-r` incident normals outside the span. These stages contribute
`(w+1)_rise_(s-1)`.

At the final `r=s` stage, let `(delta,mu)` span the annihilator. If
`delta=0`, the RS root bound leaves at least `w+1>=theta` choices. If
`delta!=0`, normalize it to one and put `b=sum_i mu_i c_i in C'`; the
definition of `theta` leaves at least `theta` choices on the actual selected
support. This is the final factor missing from the refuted global
direction-separation compiler.

Let `z` be the number of zero normals and `g<=z` the number incident with
every parameter point. Common-zero dimension gives `z<=K-s`. Every point
therefore owns at least

```text
(m-g) theta (w+1)_rise_(s-1)
```

ordered full-rank tuples, while a tuple determines at most one point. Hence

```text
|Z| <= (n-z)_fall_(s+1) /
       ((m-g) theta (w+1)_rise_(s-1)).                 (1)
```

For fixed `z`, the worst case is `g=z`. The successive ratio in `z` has
sign `n-(s+1)m+sz`, so it changes at most once from decreasing to increasing.
The maximum is therefore at `z=0` or `z=K-s`; substituting those endpoints
gives `(ST1)`. If `theta=0`, then `r_1=b` on one selected support and the
corresponding base word supplies a containing codeword pair, contradiction.
Thus `theta>=1`.

The shortened-row margins are exact integer evaluations of `(ST1)` and are
replayed independently by both node verifiers.
