# Proof

Let `Omega` be the 60 sheets, partitioned into the five original blocks
`B_0,...,B_4` of size twelve. By the diagonal-socle dependency, the derived
block kernel is a full diagonal copy `D` of one nonabelian simple group `S`,
and all five degree-12 `S`-actions are equivalent. The last assertion
includes the exceptional `M12` case: an opposite action block would have a
12-point cross-orbit and cannot occur in the actual four-block transversal.

Choose `D`-equivariant bijections

```text
B_i -> X,       |X|=12,
```

so that, in the resulting coordinates `Omega=X times {0,...,4}`, every
`s in S` acts as

```text
(x,i) -> (s*x,i).                                  (1)
```

## Trivial centralizer

The action of `S` on `X` is faithful and two-transitive, with point-
stabilizer orbits `1,11`. Let `c` centralize `S` and fix `alpha in X`. By
transitivity, `c` then fixes every point, so `c=1`. If instead
`c(alpha)=beta!=alpha`, every element of `S_alpha` fixes `beta`, because

```text
s*beta=s*c(alpha)=c*s(alpha)=c(alpha)=beta.
```

This contradicts transitivity of `S_alpha` on `X-{alpha}`. Hence

```text
C_Sym(X)(S)=1.                                     (2)
```

## The secondary block system

Take `g` in the full monodromy group `G`, and let `pi` be its permutation of
the five original blocks. Normality of `D` gives one automorphism
`phi_g in Aut(S)` such that

```text
g s g^(-1)=phi_g(s)       for all s in S.           (3)
```

Write the restriction from `B_i` to `B_(pi(i))`, in the chosen `X`
coordinates, as `n_i`. Equation `(3)` gives

```text
n_i s n_i^(-1)=phi_g(s)       for every i.          (4)
```

For any `i,j`, the permutation `n_j^(-1)n_i` centralizes `S`; by `(2)` it is
the identity. Thus all `n_i` equal one permutation `n_g`, and

```text
g(x,i)=(n_g(x),pi(i)).                              (5)
```

Consequently `G` preserves the twelve subsets

```text
C_x={(x,0),...,(x,4)},       x in X.               (6)
```

They form a nontrivial block system with block size five. By the standard
monodromy/intermediate-field correspondence and Luroth's theorem, `(6)`
gives a geometric functional decomposition of the same rational endpoint
map with inner degree five.

The degree-60 divisor adapter applies to every geometric decomposition of
this endpoint map. Its inner-degree-five profile, together with the deployed
field arithmetic, is ruled out by
`rate_half_kb_degree5_decomposition_exclusion`: two rational total
ramification points force fifth-power fibers, while fifth power is injective
on `F_(2130706433^6)` and cannot contain five distinct rational active
points. This contradicts the decomposition forced by `(6)`, proving
`(KBS-1)`. QED.
