# Proof

Use the cyclic starts `Z/bZ`, where `b=3e+3`. A start `j` carries
`w_j=3-sigma_j` distinct light points, with `w_j` equal to two or three.
The light part of block `E_t` consists of the starts in

```text
W_t={t-e+1,...,t}.                                   (1)
```

A block is deficient exactly when `W_t` contains three of the seven marked
starts. There are `e-6` deficient blocks. When `e>=14`, more than seven
blocks are deficient, whereas at most seven indices `t` have `t+1` marked.
Choose a deficient `t` for which `t+1` is unmarked.

The adjacent start union

```text
I=W_t union W_(t+1)={t-e+1,...,t+1}                  (2)
```

still contains three marks. Hence its light weight is

```text
sum_(j in I)w_j=3(e+1)-3=3e.                        (3)
```

Because `E_t` is deficient, the full pair already contains the padded heavy
point `x_*`, as well as the common core point.

Consider a third block `E_k`. If `W_k` meets `I`, at least two of its light
points are already in the pair. Every block has at most `3e-2` light points,
so

```text
|E_t union E_(t+1) union E_k|
 <=1+3e+(3e-4)+1=6e-2=2rho.                         (4)
```

It is not an expander. If `W_k` is disjoint from `I`, all its light points
are new. Every block has at least `3e-3` light points, and the core and
heavy point are already present, so

```text
|E_t union E_(t+1) union E_k|
 >=1+3e+(3e-3)+1=6e-1=2rho+1.                       (5)
```

It is an expander. The complement of the length-`e+1` interval `I` is a
cyclic interval of length `2e+2`. It contains exactly

```text
(2e+2)-e+1=e+3                                      (6)
```

length-`e` block windows. This proves `(CDS1)`.

Finally `r_t=1`, while `r_(t+1)>=0`. Since `rho=3e-1`, the necessary count
from the two-slope spread is at least `ceil((3e+6)/2)`, strictly larger than
`e+3`. The cyclic design violates that necessary condition. QED.
