# Retained-zero effective-degree descent

- **status:** PROVED
- **consumer:** `petal_k4_primitive_bound`

Let `R` and `T` be disjoint evaluation sets, `|R|=r<=d`, and let `W:T->F`.
The constrained auxiliary list

```text
{G in F[X]_(<=d): G|R=0 and agr_T(G,W)>=a}
```

is in support-preserving bijection with the degree-`<=d-r` list against

```text
W_R(x)=W(x)/L_R(x),   x in T,
```

where `L_R(X)=prod_(z in R)(X-z)`. In particular, exact agreement supports
and their stabilizers are unchanged.

Consequently, if `a^2>(d-r)|T|`, the constrained list, and hence its
stabilizer-primitive part, has size at most

```text
floor(|T|(a-d+r)/(a^2-(d-r)|T|)).
```

For a G1 chart, `a=ell+d-r`, so the only K4 charts not covered by this theorem
satisfy the effective-degree sub-Johnson inequality

```text
(ell+d-r)^2 <= (d-r)mell,    mell=|T|.
```
