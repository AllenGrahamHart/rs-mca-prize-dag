# Cycle 333: MCA rank-11 rank-eight nine-shadow deficit (2026-08-14)

Two PROVED nodes sharpen the full nine-shadow containment resource on its
corank-two stratum.

Fix a rank-eight nine-subset `U` of an exact support `S`, and write

```text
C=cl_S(U),  c=|C|<=K'-2,  X=S\C,  q=|X|>=67474.
```

The contraction by `U` has rank two.  Every parallel class in `X` has size
at most `K'-1-c`, because adjoining one such class to `C` gives a rank-nine
flat.  Consequently each point of `X` has at least

```text
q-(K'-1-c)=m'-K'+1=67473
```

partners outside its parallel class.  After dividing the ordered count by
two, at least

```text
L_2=C(67474,2)=2276336601
```

support pairs raise the rank from eight to ten.  Thus a rank-eight
nine-subset extends to a kernel eleven-set in at most

```text
C(m'-9,2)-L_2
```

ways.  The full-containment resource from Cycle 332 therefore strengthens to

```text
[52+3E_0/E_1] I_1 + [55+6L_2/E_2] I_2
  + 55 sum_(d>=3) I_d <= E_0 C(m',9),

E_0=C(m'-9,2), E_1=C(K'-10,2), E_2=C(K'-11,2).
```

The exact two-resource LP now closes every row through `K'=17608`.  At that
endpoint the demand-capacity gap is

```text
126547040539829546354916747965612889135249249684319416999204.
```

At `K'=17609`, capacity exceeds demand by

```text
165662859003771823867021831078593815988062146919602894849014,
```

so the method stops honestly.  The endpoint and wall share the same active
pattern: coranks one and three are at their individual caps, coranks two and
four are resource-tight, coranks five through nine vanish, and both shared
resources bind.  The independent audit reconstructs all fifteen exact active
intervals rather than reusing the primary dual-vertex enumeration.

Focused verification on Modal:

```text
RATE_HALF_MCA_RANK11_KERNEL_RANK8_NINESHADOW_EXTENSION_DEFICIT_PASS
  checks=82977 pair_floor=2276336601 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_RANK8_NINESHADOW_EXTENSION_DEFICIT_AUDIT_PASS
  rows=98635 pair_floor=2276336601
RATE_HALF_MCA_RANK11_KERNEL_RANK8_NINESHADOW_CAPACITY_CUT_PASS
  checked=17599 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_RANK8_NINESHADOW_CAPACITY_CUT_AUDIT_PASS
  checked=17599 patterns=15 wall=17609
```

The four Modal jobs peaked at 55--57 MB each.

```text
DAG delta:             +2 PROVED rank-eight nine-shadow nodes,
                       +3 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=10..17608
remaining intervals:  K'=10..17608 rank eight only;
                       K'=17609..22525 rank eight plus kernel;
                       K'=22526..37995 dense-owner chronology plus kernel;
                       K'=37996..1048576 kernel only
delta-star movement:   none
compute:               exact 17,599-row primal/dual replay on Modal
next route action:     improve the coupled corank-two/corank-four wall;
                       standalone rank-six pair extensions cannot help,
                       because two additions reach rank at most eight
```
