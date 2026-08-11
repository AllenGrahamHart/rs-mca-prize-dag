# `A=1` core-one quadratic gap-four regular quartic pin

- **status:** PROVED
- **closure:** all unallocated regular-block degree is one quartic
- **consumer:** `rate_half_band_crossing_location`

Retain either root pattern of the core-one scalar quadratic packet at
`u=4`. Let `D_1(U,V)` be the determinant of the residual regular Kronecker
block, normalized as in

```text
adj M_1=D_1qq^T,       deg D_1=e-2.                  (RQP1)
```

## Double-root arm

Let `g_*` be the squarefree form cutting out the `e-6` supported slopes
whose excess factor has the new root `x_*`. Then there are a nonzero
constant `a` and a nonzero binary quartic `E_4` such that

```text
D_1=a g_*E_4.                                        (RQP2)
```

Together with `Q(-;x_*)=c g_*S_B^3`, this gives

```text
det(M_1+tau nu(x_*)nu(x_*)^T)
 =tau a c^2 E_4 g_*^3S_B^6.                         (RQP3)
```

## Two-simple arm

Let `G_1,G_2` be the supported forms from `(TSF2)`. Common roots are counted
with multiplicity in `G_1G_2`. There are a nonzero constant `a` and a
nonzero binary quartic `E_4` such that

```text
D_1=a G_1G_2E_4.                                     (RQP4)
```

Consequently

```text
det(M_1+tau nu(x_1)nu(x_1)^T)
 =tau a c_1^2 E_4 G_1^5G_2S_1^6,

det(M_1+tau nu(x_2)nu(x_2)^T)
 =tau a c_2^2 E_4 G_1G_2^5S_2^6.                   (RQP5)
```

## Scope

The quartic may share roots with every displayed factor and may be
nonreduced. It is not identified with `S_B^2`, `S_1S_2`, or any correction
divisor. The theorem does not exclude either packet.
