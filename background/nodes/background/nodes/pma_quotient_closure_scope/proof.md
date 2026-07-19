# Proof - PMA quotient-closure scope and route cut

## 1. Folded source lists are exact-periodic

Let `kappa in K_d`. Since `kappa^d=1`,

```text
U(kappa x)=V((kappa x)^d)=V(x^d)=U(x),
P(kappa x)=W((kappa x)^d)=W(x^d)=P(x).
```

Thus `P(x)=U(x)` if and only if `P(kappa x)=U(kappa x)`. Therefore
`K_d A_P=A_P`. The list threshold makes `A_P` nonempty, so its exact
stabilizer contains `K_d` and has order at least `d>1`. The exact-periodic
owner partitions by the full stabilizer order, so it charges `P` at that
unique exact scale, including the possible full-domain scale.

The hypothesis on `U` is necessary. If only `P` factors through `x^d`, an
arbitrary `U` can make `A_P` any prescribed subset by assigning `U=P` there
and different values elsewhere. Such an agreement set can have trivial
stabilizer.

## 2. Boundary stripping

Fix `d|n`, put `B=partial_d E_P`, and write `beta=|B|`. The full core is a
union of `K_d`-cosets, so its locator is a polynomial in `T^d`. Hence

```text
M_E(T)=B_E(T) M_tilde(T^d),
B_E(T)=product_(b in B)(T-b)=sum_(u=0)^beta b_u T^u.
```

Write the primitive syndrome moments of the error vector as

```text
s_r=sum_(x in E_P) w_x x^r,       w_x != 0.
```

Define the filtered moments

```text
t_r=sum_(u=0)^beta b_u s_(r+u).
```

Expanding and interchanging sums gives

```text
t_r=sum_(x in E_P) w_x B_E(x)x^r
   =sum_(x in E_d^full) w_x B_E(x)x^r.
```

The boundary terms vanish. On the full core, `B_E(x)` is nonzero because the
core and boundary are disjoint, so all transformed amplitudes remain
primitive. Thus the filtered syndrome has the exactly `K_d`-periodic support
`E_d^full` of size `j-beta`.

For fixed `B`, the map `E_P -> E_d^full` is injective because
`E_P=E_d^full union B`. Its image is contained in the periodic
multisequence shell counted by `P_(d,j-beta)(T_B s)`. Summing over all
`beta`-subsets `B` proves `(LDEF)`. A deterministic order on the finite
triples `(d,beta,B)` makes the union disjoint without changing this upper
bound.

If the original syndrome length is `D`, then the filtered length is
`D-beta`, while the periodic core has size `j-beta`. Therefore

```text
(D-beta)-(j-beta)=D-j,
```

so the reserve is preserved exactly.

## 3. The raw official-row route does not fit

At `sigma=1`, the first error shell has

```text
j=n-k-1.
```

For `d=2`, a one-point boundary leaves periodic core size
`j-1=n-k-2`. With `N=n/2` and `h=k/2+1`,

```text
(j-1)/2=N-h.
```

The word-free periodic candidate universe therefore has size

```text
binom(N,(j-1)/2)=binom(N,h).
```

There are `n` singleton boundaries. Pascal's ratio gives

```text
binom(N,h)=N/(N-h) binom(N-1,h)
          =N/(N-h) Q_2(k+2).
```

Since `0<h<N`, the ratio `N/(N-h)` is greater than one. Hence

```text
Raw_(2,1)>n Q_2(k+2)>=2^13 Q_2(k+2)>719 Q_2(k+2).
```

So the proved structural reduction, followed only by the word-free quotient
candidate count, cannot supply the finite profile charge. Setting `QCLOSE`
empty introduces no gap: `QOWN_per` and its exact-stabilizer-one complement
are exhaustive. Removing any separately proved source owner from that
complement and applying the B11 five-cell router to the remainder is still
exhaustive. The unresolved direct cell is therefore exactly the post-owner
`GROW union RES` class, with every unowned low-defect survivor retained.
