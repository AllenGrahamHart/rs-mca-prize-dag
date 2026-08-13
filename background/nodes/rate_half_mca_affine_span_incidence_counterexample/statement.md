# Affine-span MCA incidence counterexample

- **status:** PROVED
- **closure:** exact finite-field counterexample
- **scope:** the affine-span MCA compiler, including its direction-separated
  form, and the two direction-support refinements derived from it

## Statement

Over `F=GF(1009)`, let `D={0,...,99}` and

```text
C=RS[F,D,1],       (n,K,m,w,s)=(100,1,21,20,1).
```

There is one received line `r_gamma=r_0+gamma r_1` and a set of 31
distinct slopes with explanations in the one-dimensional code `C` such
that:

1. every selected explanation has maximal agreement support exactly `21`;
2. every such support is same-support pair-noncontained;
3. the selected explanations have affine span exactly one;
4. `max_(c in C) agr(r_1,c)=20<m`, so the direction-separated hypothesis
   of upstream `thm:affine-span-mca` holds; but
5. the claimed affine-span bound is `23`, while the family has size `31`.

For the minimum direction lift `b=0`, its support has size `e=80`.  On the
same family the claimed direction-support affine-basis bound and common-zero
bound are both `22`, so those refinements fail as well.

## Construction

Partition the domain into

```text
C_0={0,...,19}, E={20,...,49}, T={50,...,70}, W={71,...,99}.
```

Put `(r_0,r_1)=(0,0)` on `C_0`.  On the `i`-th point of `E`, for
`1<=i<=30`, put `(r_0,r_1)=(-i^2,i)`.  Select slopes `i` there with
explanation zero.  On `T`, put `r_0=1` and choose 21 distinct nonzero
direction values avoiding `1+i r_1=0` for every `1<=i<=30`; select slope
zero with explanation one.  On `W`, choose fresh direction values and base
values avoiding all selected agreements.  The deterministic choices are
specified by `source_contract.json` and reconstructed by both verifiers.

## Consequence

Local pair noncontainment does force the incident normals on each witness to
span the parameter space.  It does **not** supply the claimed lower bound on
the number of incident ordered bases: in this example each zero-explanation
witness contains 20 repeated normals in one line and only one transverse
normal.  The missing ingredient is a uniform proper-subspace occupancy
bound, not merely full rank or direction separation.

This counterexample does not refute the ordinary affine-span list theorem,
the codeword-direction gauge equivalence, the directional Johnson bound, or
recursive shortening itself.

## Falsifier

Any failed field operation, a support not exactly 21, a pair-contained
support, affine explanation rank other than one, direction agreement at
least 21, or a recomputed compiler bound at least 31.
