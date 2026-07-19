# Proof

For a pair `ij`, `(SP1)` factors the nonzero difference as

```text
f_j-f_i=J A_k A_l e_ij q_ij.
```

The factor preceding `q_ij` is monic and has degree
`|S_i intersect S_j|`. Since `q_ij` is nonzero,

```text
deg b_ij=p_ij+deg q_ij.
```

If `delta_ij=0`, the factor preceding `q_ij` already has degree `2d-1`.
Thus `q_ij` is constant and the coefficient of `X^(2d-1)` in the difference
is nonzero, so `c_i!=c_j`. If `delta_ij=1`, that factor has degree `2d-2`.
The quotient is constant exactly when `deg(f_j-f_i)=2d-2`, equivalently
`c_i=c_j`; otherwise it is linear and `c_i!=c_j`. This proves `(SF1)`.

The degree-chamber table now follows by inserting the six printed `p` and
`delta` rows from the normal form. There is only one compatibility removal.
In the pendant type, if both deficit quotients `q_13,q_23` were constant,
then `(SF1)` would give

```text
c_1=c_3=c_2.
```

But edge `12` is tight, so `(SF1)` also gives `c_1!=c_2`, a contradiction.
The remaining one-bit choices give respectively `3,4,2,1,2,1` chambers,
for a total of thirteen.

Now take a triangle `ijk` all of whose slacks vanish. Its three quotients are
nonzero constants. Equation `(SP2)` becomes

```text
q_ij(A_k e_ij)+q_jk(A_i e_jk)=q_ik(A_j e_ik).      (1)
```

The three root sets are

```text
T_k union E_ij,  T_i union E_jk,  T_j union E_ik.
```

They are pairwise disjoint incidence blocks. When their degrees agree, the
three monic polynomials in `(1)` are therefore distinct pairwise-coprime
members of one constant two-dimensional pencil. Substitution of the exact
`deg A_i` and `p_ij` rows gives the split-fiber table:

```text
pendant:              012 at d-1;
4-cycle:              no deficit-free triangle;
K_4-e:                012,013 at d-1;
K_4:                  all four triangles at d-1;
path + singleton:     012 at d, 013 at d-1;
triangle + singleton: 012 at d, the other three at d-1.
```

Finally let `P,Q` be a coprime basis of any such constant pencil. At a point
`x in D`, two distinct projective members cannot both vanish: two independent
constant linear combinations vanishing would force `P(x)=Q(x)=0`, contrary
to coprimality. Every completely `D`-split degree-`h` member consumes `h`
distinct points, and different members consume disjoint points. There are
only `4d` points, proving `(SF3)`. For `h=d` the cap is four. For `h=d-1`,
`floor(4d/(d-1))=4` when `d>=6`. QED.
