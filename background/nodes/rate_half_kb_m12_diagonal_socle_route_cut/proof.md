# Proof

## 1. The derived block kernel is subdirect

Let `B_0,...,B_4` be the blocks of the composition and let `G_0` be the
degree-five outer monodromy. For each `i`, the block stabilizer induced on
`B_i` is the terminal primitive inner monodromy `H_i`. Conjugation by `G`
identifies the five abstract groups. The complete degree-12 primitive
catalogue with subdegrees `1,11` is

```text
H_i       |H_i|       simple socle S_i
M11         7920      M11
M12        95040      M12
PSL2(11)     660      PSL2(11)
PGL2(11)    1320      PSL2(11)
A12        12!/2      A12
S12        12!        A12.                         (1)
```

Put `P_i=N^(B_i)`. It is normal in `H_i`. It is nontrivial: otherwise the
action of `H_i` would factor through the outer point stabilizer, whose order
is at most `24`, whereas every group in `(1)` has order at least `660`.
Since `H_i` is almost simple, `P_i` contains `S_i`.

Now put `D=[N,N]`. Projection commutes with taking the derived subgroup, and
for every possible `P_i` one has

```text
[P_i,P_i]=S_i.
```

Therefore `D <= product_i S_i` and every coordinate projection of `D` is
onto. Thus `D` is a subdirect product of five isomorphic nonabelian simple
groups.

## 2. Scott strips collapse to two cases

Scott's subdirect-product lemma writes `D` as a direct product of full
diagonal strips whose supports partition the five coordinates. The subgroup
`D` is characteristic in `N` and hence normal in `G`, so the outer action
`G_0` preserves this support partition. A transitive group of prime degree
five is primitive. Hence the partition is either the singleton partition or
the one-part partition. Equivalently,

```text
D=S_0 x ... x S_4,                                 (2)
```

or `D` is one full diagonal strip, with arbitrary automorphism twists
between coordinates.

Fix a sheet `alpha in B_0`. The actual quartic component supplies a
`G_alpha`-suborbit `Delta` of size four. By the proved same-inner-fiber
exclusion, `Delta` meets a block other than `B_0`. If `(2)` held, then
`D_alpha` would contain the full transitive factor `S_j` on every other
block `B_j`; the orbit of any point there would have size twelve. This
contradicts `|Delta|=4`. Therefore `D` is full diagonal.

## 3. Cross-actions of the diagonal socle

Identify the diagonal `D` with its simple factor `S=S_0`. Its action on
each block is a faithful degree-12 action, possibly twisted by an
automorphism of `S`. Put `A=D_alpha`, an index-12 point stabilizer.

For `M11`, `PSL2(11)`, and `A12`, the degree-12 action is unique up to the
available automorphisms; its rank is two. The same is true for either fixed
degree-12 action of `M12`. Thus in an equivalent block action the `A`-orbits
have lengths `1,11`, with exactly one fixed point.

The exceptional possibility is the other degree-12 action of `M12`, obtained
by its outer automorphism. Aligning the standard generators in the ATLAS
`12a` and `12b` representations gives a synchronized group of order `95040`.
The stabilizer of one `12a` point has order `7920` and is transitive on all
twelve `12b` points. Hence the cross-action orbit length is `12`, not a new
small orbit.

Because `D_alpha` is normal in `G_alpha`, every `D_alpha`-orbit through a
point of `Delta` lies in `Delta`. The orbit lengths above show that each
block met by `Delta` contributes exactly its unique fixed point, and an
opposite `M12` action block cannot be met at all. Therefore

```text
|Delta| >= number of projected blocks,
|Delta| <= number of projected blocks,
```

so the two quantities are equal to four. The block projection of the actual
component has outer subdegree `r`; the previous route cut leaves only
`r=2,4`. Hence `r=4`, proving `(KBD-1)` and deleting the Dickson branch.

For `r=4`, the outer stabilizer orbit is all four blocks other than `B_0`.
Thus, when `S=M12`, every one of those actions is equivalent to the action
on `B_0`; all five action classes agree. QED.
