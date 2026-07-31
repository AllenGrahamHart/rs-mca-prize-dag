# KoalaBear m2 r4 coordinate negative two-loop 433 constrained product-q classifier

- **status:** PROVED
- **scope:** the constrained cells `X2,N1,L1` from `(KB43P-6)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld` and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_product_minor_cell_cut`
- **consumer:** `rate_half_band_closure`

In all three cells put `b=-c^3` and define

```text
P_8(M)=M^4+8M^3-2M^2+8M+1.                      (KB43C-1)
```

After saturating by label, signed-pair, and product-value distinctness, all
remaining common-`K` product minors and the second squared q weld are
equivalent to the following exact rows:

```text
X2:
 P_8(M)=0,
 (c^2+1)(M+1)^2-c(M-1)^2=0;                      (KB43C-2)

N1:
 P_8(M)=0,
 (c^2+1)(M+1)^2+c(M-1)^2=0;                      (KB43C-3)

L1:
 M^2+1=0,
 2c^4+3c^2+2=0,
 3L=4c^3+2c-M.                                   (KB43C-4)
```

The `BC` label is respectively `-M,-M,-M`; the `A`-loop label is
`-M^2,-1,L`.  Each row has at most eight geometric candidates before
Galois identification and guard replay, hence these three cells contribute
at most 24 common-`K` candidates.

The rows are genuinely nonempty with every distinctness guard.  Exact
examples occur in

```text
X2 over F_11: (M,c,L,b)=(7,7,6,9),
N1 over F_11: (M,c,L,b)=(7,3,10,6),
L1 over F_113: (M,c,L,b)=(15,23,74,37).           (KB43C-5)
```

For every squared-weld survivor, reversing the `BC` orbit if necessary
realizes the unsquared second weld; the first weld already fixes the
relative `AB+/-` orientation.  Thus these are actual common-`K` Vieta
interfaces, not complete source-facet or component realizations.

This theorem does not classify `M1,M2,M3`, impose the other seven fibers or
paired-product involution, delete the skeleton/orientation, move an
owner/payment, close a row, or prove either Prize result.

## Falsifier

An actual constrained-cell packet outside `(KB43C-2)--(KB43C-4)`, a printed
row failing one product minor or squared weld, or failure of a certificate
in `(KB43C-5)`.
