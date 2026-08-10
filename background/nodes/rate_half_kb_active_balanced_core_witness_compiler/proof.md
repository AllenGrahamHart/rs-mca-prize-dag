# Proof

## 1. Concrete source relation

Fix one admissible received line and finite slope `z`. The active MCA source
package associates to its received word the shifted interpolation lattice

```text
M_U={(W,N): W(x)U(x)=N(x) for every x in D}.
```

At the deployed row the active locator parameters are

```text
n=2097152,  k=1048576,  K=k+1=1048577,
m=1116048,  omega=n-m=981104,  w=m-K=67471.
```

The proved lattice census identifies an agreement support with a monic
degree-`omega` split locator `W|Lambda_D` and matching numerator/explaining
data in `M_U`. The balanced branch is the source profile with minimal shifted
degree `d1>=w+1`; earlier tangent and Q membership is retained as explicit
first-match exclusion data. These conditions, with the fields and guards in
`certificate_schema.json`, define `ValidBC(line,z,c)`.

We now resolve the previously symbolic predicate name by definition:

```text
bcCertified(line,z)  iff  there exists c, ValidBC(line,z,c).
```

This is not an added truth hypothesis. It is the concrete semantics of the
predicate slot already used by the active first-owner partition.

## 2. Exact projection

The active cell is

```text
Z_BC={z: bad(z), not tangent(z), not qCertified(z), bcCertified(line,z)}.
```

Substituting the displayed definition of `bcCertified` gives exactly the
slope projection of valid certificates carrying those same earlier-owner
exclusions. Both containments are substitution; no owner or support is
inferred from an endpoint object.

## 3. Canonical selection and fibers

All data are finite. The challenge field, evaluation domain, coefficient
vectors under the printed degree caps, supports, and owner tags are finite
sets. Fix their public basis/coordinate orders and the lexicographic product
order printed in the schema. Every nonempty certificate fiber therefore has
a unique least member.

For each `z in Z_BC`, select that least certificate. Existence follows from
the predicate definition and uniqueness from total-order minimality. The
certificate stores `z`, so selected certificates for distinct slopes are
distinct. Projection back to `z` is inverse to selection. Hence the selected
certificate-to-slope map is a bijection and all selector fibers equal one.

Nothing here realizes an endpoint record or bounds `|Z_BC|`. QED.
