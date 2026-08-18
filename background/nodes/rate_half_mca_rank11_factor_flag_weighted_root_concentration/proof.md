# Proof

Use the exact partition from the proved factor-flag router. Every promoted
container has at least `H=38385` common actual zeros. At `T=650`, a
factor-light container has at most `649` factor roots, so its residual
subspace `B_i` has at least

```text
b=H-T+1=37736
```

common-zero evaluation columns.

Put `h=11216` and `g=b-h=26520`. The base-free factor-heavy classes,
residual dimension-two transverse classes, and residual dimension-three
transverse classes cost respectively

```text
floor(1116048/650) R_5                    =  1733735411530980,
floor((1116048)_3/26520^3) R_4           =  4724942273025156,
floor((1116048)_2/26520^2) R_6           = 28498520779560840.
```

Their union cost is `34957198464116976`. Together with the fixed transverse
envelope `209812758437679617`, the paid categories total
`244769956901796593`. An unsafe line has at least `B_*+1` bad slopes, so the
unpaid nontransverse residual classes carry at least

```text
B_*+1-244769956901796593=30210771209598495,
```

proving `(RC1)`.

For each fixed residual class `B_i`, every assigned correction lies in
`PB_i`, of dimension at most four when `dim B_i=2` and at most six when
`dim B_i=3`. The largest class cap is therefore
`R_6=16100859197492`. First-match ownership makes the classes disjoint, so
`(RC1)` forces at least `1877` classes.

Nontransversality supplies, for every such class, a proper flat in
`B_i^perp` containing at least `h+1=11217` labelled evaluation columns.
Choose exactly `S=11217` coordinates by a fixed rule. If `mu_i` is the
class's slope mass and `Z_i` the chosen coordinate set, double counting
weighted incidences gives

```text
sum_x sum_(i:x in Z_i) mu_i
 = sum_i mu_i |Z_i|
 >= S E_flag.
```

The anchor-good universe has size at most `1116048`, so one coordinate has
weighted incidence at least the ceiling in `(RC3)`.

For every class counted at this coordinate, its evaluation column belongs
to a subspace of `B_i^perp`; hence every polynomial in `B_i` vanishes at
`x`. Thus `B_i<=B_x` and every correction in `PB_i` lies in `PB_x`. Since
`B` is base-free, evaluation at `x` is a nonzero linear functional on `B`,
so `dim B_x=4` and `dim(PB_x)<=8`. Finally `x` lies in the anchor-good set,
so equality to the anchor pair is equality to the received pair. This proves
`(RC3)` and `(RC4)`. QED.
