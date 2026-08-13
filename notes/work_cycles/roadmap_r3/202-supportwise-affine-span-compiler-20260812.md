# Cycle 202: support-wise affine-span compiler (2026-08-12)

Cycle 201 left a direction-list residual because the imported affine-span
theorem assumes that the shortened direction has agreement below `m` with
every codeword. That global assumption is stronger than the support-wise MCA
application needs.

Fix one selected slope `gamma`, its exact size-`m` agreement support
`S_gamma`, and an affine explanation space of dimension `s`. A failure of
full rank among the incident normals gives a nonzero relation

```text
delta r_1 - sum_i mu_i c_i = 0 on S_gamma.
```

If `delta=0`, basis independence produces a nonzero degree-`<K` codeword
with `m=K+w>K` roots. If `delta!=0`, the direction agrees with a codeword
`b` on `S_gamma`; subtracting `gamma b` from the slope explanation makes the
base word a codeword on that same support. Both cases contradict either the
Reed-Solomon root bound or exact same-support pair noncontainment. Hence the
incident normals have full rank without direction separation, and the
upstream affine-span incidence count applies unchanged.

For the complete shortened code (`K=s`, `n=R+s`, `m=d+s`) the resulting
bound is

```text
J_s=floor(product_(i=0..s) (R+i)/(d+i)).
```

The exact deployed transitions are

```text
KoalaBear:   J_13=47876303026096432 <= B*=274980728111395087
             < J_14=743896698428332665
Mersenne-31: J_5=14115447 <= B*=16777215 < J_6=219426634.
```

Thus the direction-list residual disappears at every numerically paid depth.
After whole-line global-core cancellation, the first remaining dimension
residual is `s>=14` for KoalaBear and `s>=6` for Mersenne-31.

The hostile `GF(11)` control shortens `(10,5,7)` to `(9,4,6)`. Its direction
has agreement six with a degree-`<4` codeword, so the old hypothesis fails,
but all seven selected incident-normal matrices have rank five and
`7<=J_4=21`. The primary checker verifies this control and both official
integer transitions. The independent audit exhausts all
`7*11^5=1,127,357` normal-relation candidates and all `11^4` shortened
direction codewords.

```text
start:                   be4efd23a
result:                  PROVED support-wise affine-span compiler
DAG delta:               +1 PROVED background node, +2 edges
critical status delta:   none
upstream terminal delta: direction-separation branch removed; only the
                         large shortened dimensions s>=14 / s>=6 remain
delta-star movement:     none
compute:                 tiny exact GF(11) replay; no Modal spend
next route action:       attack the large-shortened-dimension residual
```
