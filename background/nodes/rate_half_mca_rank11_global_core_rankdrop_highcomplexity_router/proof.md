# Proof

Let `C_*` be the nonempty complete-family core emitted by the whole-line
router and let `L_C` be its monic locator. The common-core adapter chooses
actual size-`m` witnesses through `C_*`, subtracts the received-column
interpolants `A_C,B_C`, divides by `L_C`, and deletes `C_*`. It preserves
slopes, badness, pair noncontainment, and maximal supports.

## The dense pair and deviations descend

Fix the dense pair `p_0=(a_0,b_0)`. Two distinct slopes owned by this pair
have maximal-support intersection

```text
H_0={x:r_0(x)=a_0(x), r_1(x)=b_0(x)}.
```

Since `C_*` lies in every maximal support, `C_* subset H_0`. Hence
`a_0-A_C` and `b_0-B_C` vanish on `C_*` and are divisible by `L_C`. Define

```text
a_0'=(a_0-A_C)/L_C,       b_0'=(b_0-B_C)/L_C.
```

For every record,

```text
d_gamma'=h_gamma'-a_0'-gamma b_0'
        =(h_gamma-a_0-gamma b_0)/L_C.
```

Multiplication by the nonzero polynomial `L_C` is injective, so exact
division preserves the deviation-space dimension. Write that dimension as
`r`. The residual polynomials have degree below `K'`, whence `r<=K'`; the
off-pair-line record gives `r>=1`.

The adapter maps every maximal support to `S_hat_gamma minus C_*`. By the
definition of the complete intersection, these residual maximal supports
have empty common intersection.

## Every rank drop is paid

For an explanation span of dimension `r`, support-local transversality with
automatic margin one gives

```text
max {
  n'_fall_(r+1)/(m' (d+1)_rise_(r-1)),
  (n'-K'+r)_fall_(r+1)/(d+1)_rise_r
}.
```

The second endpoint is independent of `K'`. For the first endpoint, the
successive ratio from `K'` to `K'+1` changes side of one at most once,
because its cross-multiplied difference is

```text
r K' + (r+1)d - R + r.
```

Therefore its maximum on `r<=K'<=K` occurs at an endpoint. Exact endpoint
evaluation for `1<=r<=8` is largest at `r=8,K'=K`, where it is
`110390969172173096`. Adding the disjoint near charge `134944` gives
`110390969172308040 < B_*`.

For `r=9`, apply the proved margin/interleaving theorem at `T=667`. Its
ordinary-list cap and low-margin term depend only on `R,d,r,T`, not on
`K'`. Every support-local high-margin factor has the same one-turn
successive-ratio property, and `floor(n'/T)` is increasing. Thus it suffices
to inspect `K'=9` and `K'=K`. The deployed endpoint is larger and equals

```text
high = 5143522968716559,
low  = 56727790457914040,
near = 134944,
total= 61871313426765543 < B_*.
```

This proves the first two branches uniformly for arbitrary `C_*`.

## The full-rank residual anchor star

Assume `r=10`; then `K'>=10`. Choose eighteen residual records owned by
`p_0'`, ten actual records whose deviations form a basis of `V'`, and three
distinct fillers. As in the deployed anchor theorem, the intersection of
the first twenty-eight maximal supports is

```text
H_0' intersection Z(V').
```

This is the complete residual common support and is empty. Fillers cannot
create a common coordinate. The resulting deck `A_*'` has 31 fixed records.

For any record `z` outside the deck, `A_*' union {z}` contains eighteen
slopes on the descended pair line and a nonzero basis deviation. Its
coefficientwise slope interpolant has degree at most 31, vanishes relative
to the pair line at eighteen slopes, and is not identically zero. Its degree
therefore lies in `18..31`.

Apply the proved support-collapsed extraction theorem on the shortened row.
There is no further common support. If one tuple has

```text
chi' >= 3m'-K'+3,
```

retain it as `(H_C)`. Lifting restores `C_*` to all 32 supports, adding
exactly `2c` to two-cover complexity, so

```text
chi=chi'+2c,
chi >= 3(m-c)-(K-c)+3+2c = 3m-K+3 = 2299571.
```

Otherwise every star tuple has a pure-locator or scalar-locator rational
certificate. The adapter lift keeps the denominator, affine locator
scalars, and exact original locators. A pure locator is `(E)`. If a
nonzero denominator vanishes on `D minus C_*` or on `C_*`, the lifted
certificate is a named denominator-root exception `(E)`.

It remains to consider certificates whose denominators are root-free on
all of `D`. On the residual row, any two target tuples share the identical
31 anchor triples and have empty anchor intersection. Collision rigidity
makes their certificates projectively identical or emits its quantified
collision/near-sunflower exception. The latter lifts by adjoining `C_*`:
both the 31-overlap core threshold and its noncollision deficit increase by
exactly `c`, so it is the original-row `(E)` threshold. Outside `(E)`, one
residual certificate covers every star tuple and lifts to one coherent
original-row rational atom `(A)`.

The anchors themselves occur in any one target tuple, and an over-budget
post-near family has more than 31 records. Hence the star covers the complete
residual family. This proves the stated exhaustive route.
