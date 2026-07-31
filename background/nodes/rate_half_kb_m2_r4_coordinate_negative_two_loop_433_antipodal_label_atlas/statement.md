# KoalaBear m2 r4 coordinate negative two-loop 433 antipodal-label atlas

- **status:** PROVED
- **scope:** every negative-parity coordinate packet in the two-loop
  `(4,3,3)` skeleton `(1,0,1;2,0,1)`
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature` and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Name the loop edge types `A,A` and `C,C`.  Let their common-`K` labels be
`k_A,k_C`; let `k_+,k_-` carry the two signed `AB` product types, and let
`k_BC` carry the remaining `BC` type.  Every actual packet satisfies

```text
k_C^2=k_+ k_-.                                    (KB43-1)
```

Normalize by `k_+` and put

```text
X=1,   M=k_C/k_+,   N=k_-/k_+=M^2,
L=k_A/k_+,          Z=k_BC/k_+.                   (KB43-2)
```

The five distinct labels contain exactly two antipodal pairs and one
singleton.  Of the fifteen singleton/perfect-matching cells, exactly nine
remain:

```text
cell  singleton  pairs   forced relations
X1    X          ML|NZ   L=-M,   Z=-M^2
X2    X          MZ|NL   Z=-M,   L=-M^2

M1    M          XN|LZ   M^2=-1, Z=-L
M2    M          XL|NZ   L=-1,   Z=-M^2
M3    M          XZ|NL   Z=-1,   L=-M^2

N1    N          XL|MZ   L=-1,   Z=-M
N2    N          XZ|ML   Z=-1,   L=-M

L1    L          XN|MZ   M^2=-1, Z=-M
Z1    Z          XN|ML   M^2=-1, L=-M.            (KB43-3)
```

Every row is subject to pairwise distinctness of `X,M,N,L,Z`.  Cells
`M1,L1,Z1` retain the displayed free singleton parameter; each other cell
retains `M` as its sole `K` parameter.  The other six matching cells force
`M=-1` and `N=X`, or another printed-label collision.

In particular the banked `F_29` set `K={1,-1,4,-4,9}` admits no role
assignment satisfying `(KB43-1)`, independently of the `J` labels and edge
orientations.

This theorem does not impose the full product map or the second q weld,
delete any of the nine cells, handle the other three negative skeletons or
positive parity, close the coordinate orientation, move an owner/payment,
close a row, or prove either Prize result.  Those conclusions remain open.

## Falsifier

An actual packet in this skeleton violating `(KB43-1)`, or a tenth
five-distinct antipodal matching outside `(KB43-3)`.
