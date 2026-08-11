# `A=1` core-free cubic gap-one first-jet perfect pairing

- **status:** PROVED
- **closure:** exact local Smith transversality in three packets
- **consumer:** `rate_half_band_crossing_location`

Retain a core-free cubic double-plus-simple `u=1` packet and the notation
`D_0=aP_CE_w` of `(CRF3)`. Fix a supported projective slope `gamma` with

```text
c=c_gamma>0,       E_w(gamma)!=0.                   (FJP1)
```

Choose a local parameter `z` vanishing at `gamma` and write

```text
M_0(z)=M_gamma+z dot M,
Phi_z=Phi_gamma+z dot Phi,
Q_gamma=Q_min R_gamma,       deg R_gamma=c.         (FJP2)
```

Here `Phi_z` is the moment functional represented by the rectangular Hankel
pencil. The specialized apolar kernels are exactly

```text
ker_right M_gamma
 =Q_min F[X]_(<=c),

ker_left M_gamma
 =Q_min F[X]_(<=c-1).                               (FJP3)
```

Define the first-jet pairing

```text
B_gamma(A,B)=dot Phi(Q_min^2 A B),
deg A<=c-1,       deg B<=c.                         (FJP4)
```

Then

```text
rank B_gamma=c,
rad_right(B_gamma)=span{R_gamma}.                   (FJP5)
```

Equivalently, the derivative map induced by `dot M` is a perfect pairing
between the left kernel and

```text
ker_right M_gamma / span{Q_gamma}.                  (FJP6)
```

In particular, when `c=1` and `R_gamma=X-r_gamma` is monic,

```text
dot Phi(Q_min^2(X-r_gamma))=0,
dot Phi(Q_min^2)!=0.                                (FJP7)
```

For the three packets with `w=0`, `(FJP3)--(FJP7)` hold at every supported
rank-loss slope. In the first packet, where `w=1`, they hold at every
supported slope except possibly the single projective slope cut out by
`E_1`; if that line is unsupported, there is no supported exception.

## Scope

The theorem is a first-order apolar constraint, not a packet exclusion. At
the possible `E_1` slope it makes no claim about the larger Smith exponent.
It does not assert that supported slope sets of different heavy rows are
disjoint or that every `c_gamma` equals one.
