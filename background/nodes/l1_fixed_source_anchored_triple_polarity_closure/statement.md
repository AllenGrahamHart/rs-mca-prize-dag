# L1 fixed-source anchored triple-polarity closure

- **status:** PROVED
- **role:** aggregate bounded-polarity anchored quotient recharts, including
  partial source cores
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Setup

Fix one maximal sunflower source with `M_src` petals of size `ell`. Consider
canonical genuine common-pencil source charts whose monic degree-`ell`
quotient polynomial carries at least one fixed-source petal as a complete
level fiber. Identify additive shifts of the quotient polynomial.

For one anchored partition, let

```text
T_1,...,T_L,       |T_j|=ell,       L<=n/ell          (AT1)
```

be all its complete fibers in the domain, and put

```text
R=H\disjoint_union_j T_j.                              (AT2)
```

A canonical internal source chart has an arbitrary `(k-1)`-point core `C`
and full-fiber source petals chosen among the `T_j` disjoint from `C`. For an
exact core defect `D subset C` and exact supports `S_i` on those petals,
define

```text
p_layout=|C intersect R|
         +sum_j min(|C intersect T_j|,ell-|C intersect T_j|),

p_defect=|D intersect R|
         +sum_j min(|D intersect T_j|,
                     |C intersect T_j|-|D intersect T_j|),

p_petal=sum_i min(|S_i|,ell-|S_i|).                   (AT3)
```

The residual terms in `(AT3)` are necessary because a non-intrinsic
polynomial need not partition the whole domain into complete fibers.

## Theorem

Assume fixed caps and the L1 cutoff

```text
p_layout<=R_0,       p_defect<=B_0,       p_petal<=P_0,
ell>=c_0 n/log_2 n,       ell>2P_0,       q<=n^gamma. (AT4)
```

Across every anchored partition, every compatible canonical source chart,
and every common-pencil degree strip, the total number of contributors is at
most

```text
M_src (R_0+1)(B_0+1)(P_0+1)
  16^(n/ell) n^(R_0+B_0+P_0) q^(2P_0).              (AT5)
```

Consequently `(AT5)` is at most

```text
(log_2 n/c_0)(R_0+1)(B_0+1)(P_0+1)
n^(4/c_0+R_0+B_0+P_0+2 gamma P_0),                  (AT6)
```

and is polynomial. In particular, the existing CRT and thin-edge bounds pay
all numerator/Forney multiplicity in this scope; no separate Forney-key
first-match factor remains.

## Scope

The theorem requires the internal degree-`ell` partition to carry one whole
petal of the fixed first source. It does not supply that anchor, handle a
smaller-fiber refinement in which a source petal is a union of fibers, or
treat arbitrary petal locators. A super-polynomial anchored common-pencil
family must therefore have growing layout, core-defect, or petal polarity.
