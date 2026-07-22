# Proof

## 1. Fixed multipartial source

For every `f`-subset `E` of the unmarked labels, write

```text
V_E(T)=product_(b in E)(T-b)
      =T^f+v_1(E)T^(f-1)+...+v_f(E).
```

Bucket the sets `E` by `(v_1,...,v_t)`. There are at most `|B|^t`
buckets, so one bucket `eta` has the size in `(MP2)`. Let `L_P` be the
partial-template locator and define

```text
U=L_P(phi^f+sum_(i=1)^t eta_i phi^(f-i)),
L_E=L_P V_E(phi).
```

Because `phi` is monic and its selected fibers are complete, `L_E` is the
monic locator of exactly `P` together with the full fibers indexed by `E`.
The first `t` quotient coefficients cancel in `U-L_E`, so for `t<f`

```text
deg(U-L_E)<=r+c(f-t-1)<K.
```

Thus `U-L_E` is a codeword and its exact agreement set with `U` is the root
set of `L_E`. Distinct sets `E` give distinct monic locators and hence
distinct codewords. If `t=f`, the full coefficient vector determines `E`,
so each nonempty bucket supplies its one member.

Finally `U` is monic of degree `A>=K`. Subtracting a degree-below-`K`
polynomial leaves a nonzero monic degree-`A` polynomial, which has at most
`A` roots. Therefore no codeword has more than `A` agreements and the
complete ball is boundary-only.

## 2. Extension-field pin

Under the upstream printed complete-fold contract, view the base-field center
over the target extension. If a target-field codeword has `A` agreements, its difference
from the center is monic of degree `A` with those `A` distinct base-field
roots. It equals their monic locator, which is base-field-valued. The
codeword is therefore base-field-valued as well. The exact integer
substitution in `(MP3)` is replayed by `verify.py`.

## 3. Multiprefix obstruction

The verifier works over `F_17^*` with

```text
S_1={1,2,3,4,9,13,14,15,16},
S_2={1,5,6,7,9,10,11,12,16},
g(X)=X^3+8X^2+16X+9.
```

It checks one received word whose exact agreement sets with the codewords
`0` and `g` are `S_1` and `S_2`. Their common agreement set is
`{1,9,16}`: `{1,16}` is one complete quadratic fiber and `{9}` is the same
partial remainder. Their error sets intersect exactly in `{8}`, the same
partial error remainder. Direct locator multiplication gives `(MP4)`.

For every exact agreement set `S`, divisibility gives `(MP5)` with the
nonvanishing condition exactly excluding additional agreements. Translating
the received word and all explanations by one codeword leaves `Y-P`
unchanged, so it leaves `(L_S,H)` unchanged. The unequal prefixes therefore
survive every common translation. Summing disjoint target fibers gives
`sum_z N_Y(z)`; a maximum-fiber estimate alone does not bound that sum
without an attained-target payment. QED.
