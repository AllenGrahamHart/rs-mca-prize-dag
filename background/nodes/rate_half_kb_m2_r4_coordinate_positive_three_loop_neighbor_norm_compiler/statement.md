# KoalaBear m2 r4 positive three-loop neighbor-norm compiler

- **status:** PROVED
- **scope:** all eight signed positive coordinate three-loop lanes
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_three_loop_common_placement_atlas`,
  and `rate_half_kb_m2_r4_coordinate_positive_three_loop_signed_outside_vieta_atlas`
- **consumer:** `rate_half_band_closure`

Write the positive source form as

```text
H(T,X)=D(W)T^2+E(W)+XT B(W),       W=X^2,          (KBP3N-1)
```

where `D=A_2`, `E=A_0`, and `B=B_1=beta(W-1)` in the three-loop
normalization.  For a target square `U`, define

```text
N_num(U)=Res_W(E, U D^2-W B^2),
N_den(U)=Res_W(D, E^2-U W B^2),
mathcal_N(U)=N_num(U)/N_den(U).                     (KBP3N-2)
```

Both resultants have degree at most two in `U`.  Let `r` be any of the six
nonzero signed-pair representatives and let `t_1,...,t_4` be its four
target neighbors, with source-fiber and edge multiplicities retained.  The
complete-fiber leading-support guard gives `N_den(r^2)!=0`, and

```text
product_(j=1)^4 t_j=mathcal_N(r^2).                (KBP3N-3)
```

For the four common placements, target-edge incidence gives the exact
tables below; `sigma in {+1,-1}` is the outside cycle sign.

```text
442 root low:
 N(1)=-b^2, N(b^2)=-b^2, N(c^2)=c^2ef,
 N(d^2)=e^2f^2,
 N(e^2)=-sigma c d^2f, N(f^2)=-sigma c d^2e.

442 root high:
 N(1)=-c^2, N(b^2)=b^2ef, N(c^2)=-c^2,
 N(d^2)=e^2f^2,
 N(e^2)=-sigma b d^2f, N(f^2)=-sigma b d^2e.

433 root low:
 N(1)=bc, N(b^2)=b^2e, N(c^2)=c^2f,
 N(d^2)=e^2f^2,
 N(e^2)=-sigma b d^2f, N(f^2)=-sigma c d^2e.

433 root high:
 N(1)=ce, N(b^2)=b^2cf, N(c^2)=bc^2,
 N(d^2)=e^2f^2,
 N(e^2)=-sigma d^2f, N(f^2)=-sigma b d^2e.       (KBP3N-4)
```

Here `N(U)` abbreviates `mathcal_N(U)`.  Consequently, the common kernel
already determines both colored labels in either 433 placement:

```text
433 root low:   e=N(b^2)/b^2,       f=N(c^2)/c^2;
433 root high:  e=N(1)/c,           f=N(b^2)/(b^2c). (KBP3N-5)
```

After (KBP3N-5), a 433 lane has the three necessary equations in the sole
remaining outside target `d`:

```text
N(d^2)=e^2f^2,
N(e^2)=-sigma a d^2f,
N(f^2)=-sigma a' d^2e,                              (KBP3N-6)
```

with `(a,a')=(b,c)` in root-low and `(1,b)` in root-high.  In 442 the
common kernel determines the colored product

```text
ef=N(c^2)/c^2       (root low),
ef=N(b^2)/b^2       (root high),                    (KBP3N-7)
```

followed by the last three rows of its table in (KBP3N-4).

These norm equations are necessary aggregate consequences of the complete
Vieta system.  They do not reconstruct the seven distinct outside quotient
labels, enforce their saturation, prove any lane empty, delete positive
parity or an orientation, close K3, or prove either Prize result.

## Falsifier

An actual complete three-loop packet with `N_den(r^2)=0`, failure of
`(KBP3N-3)`, a fifth placement table, or an edge multiset whose four-neighbor
products differ from `(KBP3N-4)`.
