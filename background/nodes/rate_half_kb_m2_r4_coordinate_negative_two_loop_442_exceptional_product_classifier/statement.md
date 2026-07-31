# KoalaBear m2 r4 coordinate negative two-loop 442 exceptional-product classifier

- **status:** PROVED
- **scope:** every negative-parity coordinate packet in the `(4,4,2)`
  two-loop skeleton after the antipodal-label classifier
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_antipodal_label_classifier`
- **consumer:** `rate_half_band_closure`

Scale the three signed `J`-pair representatives so that `A=1`, write

```text
b=B/A,       c=C/A,
```

and normalize the cross-edge signs to

```text
p_AB=b,       p_AC=c,       p_BC=tau*b*c,
tau in {+1,-1}.                                  (KB4P-1)
```

The loop products are `p_A=-1`, `p_B=-b^2`.  Distinct signed pairs give

```text
b*c*(b^2-1)*(c^2-1)*(b^2-c^2)!=0.                (KB4P-2)
```

On the three label loci from `(KB44-3)`, the five common-`K` product rows
have rank at most three only on the following exact six rows:

```text
H6: l^2-l+1=0
 tau=-1: 4b^2+b+4=0,       3c+2b-2=0;
 tau=+1: 4b^2+7b+4=0,      c-2b-2=0.             (KB4P-3)

H8-L: l^4+1=0
 tau=-1: b^2-b*l^3+b*l-b+1=0,
         c=(b-2)(l^3-l+1);
 tau=+1: b^2-2b*l^3+2b*l-b+1=0,
         c=-b*l^3+b*l+b+2.                       (KB4P-4)

H8-M: l^4+1=0
 tau=-1: b^2-b*l^3+b*l-b+1=0,
         c=(2b-1)(l^3-l+1);
 tau=+1: b^2-2b*l^3+2b*l-b+1=0,
         c=2b-l^3+l+1.                           (KB4P-5)
```

Here `H8-L` means the `A`-loop label is the singleton; `H8-M` means the
`B`-loop label is the singleton.  Conversely, each printed row makes all
five `4 x 4` product minors vanish.  The injectivity and support guards must
still be checked at each root.  Thus there are at most twelve normalized
geometric common-`K` product packets before Galois identification.

The six rows are nonempty over the geometric closure.  Therefore the
common-`K` product gate does not delete the `(4,4,2)` two-loop skeleton; its
signed q weld, one `eta` and six `L^c` records (the other seven fibers), paired-product involution,
source-facet completion, and deployed-field descent remain open.

This theorem does not close a skeleton or orientation, move an owner or
payment, close a row, or prove either Prize result.

## Falsifier

An actual in-scope product packet outside `(KB4P-3)--(KB4P-5)`, or a printed
row on which one of the five maximal product minors is nonzero.
