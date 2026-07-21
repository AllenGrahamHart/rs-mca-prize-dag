# Frontier

## Current addendum (2026-07-21)

The covering-free all-zero charge supersedes the historical catch-#158
qualification below. Together with the post-strip affine-pencil and RS
common-root basis charges, it pays selector ranks through `4,4,4` at RowC
and `16,16,14` at the prize rows. The first open selector ranks are therefore
`5,5,5` and `17,17,15`, respectively.

The arbitrary-rank uniform-cell compiler now also excludes its collapsed
minimum-face branch. A rank-two trade on union `a+2` is either a regular
Plucker face syzygy, which is quotiented, or would give two selected errors
with `k+2` common zeros against the post-strip cap `k`. Thus the residual
uniform-cell frontier consists of larger-union rank-two trades
`|X|>=a+3` and trade-rank-at-least-three cores. The first residual shell
`|X|=a+3` is a single quadratic-pullback class: its two-point zero fibers are
cycles of one base-field Mobius involution, with at most one singleton.
Owning and counting those charts, higher shells, nonuniform `u>=1` cells,
and the cross-core aggregate remain open.

Every rank-two shell `|X|=a+d+1` also obeys the parity-sensitive zero-mass
and row-arity ladder `(SR2)--(SR4)` and the explicit Maxwell deficit router
`(SR5)`. The exact prize core-size caps `384,448,960` make that deficit
positive for every primitive rank-two shell through depths
`22,428,333;19,217,048;4,478,600`. On shell `d=2`, rank three is the only
other possible primitive rank; its edge-zero graph deficit is also positive.
Thus the primitive first shell is empty at every prize rank. The paid object
is full-core primitivity, not proper local-circuit ownership.

Proper rank-two trades have also been compressed exactly: every such trade
is a sum of row-scaling circuits on four or five blocks. Four-block circuits
are the Mobius/Plucker rank-three sections of the coefficient Segre quadric;
five-block circuits have coefficient rank four with every four independent.
The remaining rank-two task is support-embedding and first-match ownership of
these two constant-arity classes, not an arbitrary-size circuit census.

Within one fixed rank-two trade, first-match ownership is now exact. Its
lexicographically first coefficient basis has three or four anchors, and
every non-anchor has a unique fundamental circuit against those anchors;
the owner vectors form a basis of the whole scaling kernel. Thus the open
phrase above is now specifically first Maxwell-core/trade selection,
realized support embedding, and cross-core deduplication. It is not
intratrade circuit decomposition.

The three-anchor (`q=3`) coefficient branch is also exact on every shell.
After one basis change its rows are `s_i(P+gamma_i Q)`, and the complete
scalar vector is the full-support dual-`GRS_3` word
`s_i=H(gamma_i)/L'_Gamma(gamma_i)` with `deg H<t-3`. Four-block owner weights
are the corresponding barycentric ratios. The remaining `q=3` problem is
therefore a realized support census for `(X,P,Q,H)`, not an unspecified
Mobius relation. The four-anchor (`q=4`) support branch remains open.

At coefficient level the four-anchor branch is now closed too. In canonical
anchor coordinates, every non-anchor is a support-three/four point on the
explicit pullback of the Segre determinant quadric, and all non-anchor points
have affine centroid `(-1,-1,-1,-1)`. Support three and four are exactly the
four- and five-block owners. Consequently no rank-two coefficient geometry
remains unclassified: the open `q=4` phrase above is now the realized support
census for these quadric-centroid configurations.

The dual-codeword part of support realization has a complete common-cofactor
certificate. For each row, its active zero fiber `Z_i`, inactive block
extension `T_i`, and unique cofactor `R_i` satisfy
`F_i=R_i Lambda_Zi`, `P_i=R_i Lambda_Ti`, with forced
`|T_i|=h-d-1+|Z_i|`. Conversely these data reconstruct the same dual word on
the two domains. The remaining realization problem is therefore the
received-pair agreement condition and compatible family/first-core count,
not compatibility of the two dual-GRS numerator descriptions.

One received-pair agreement equation per row is now paid globally. Pairing a
rank-two polynomial plane with the received directions gives an alternating
matrix in the three-anchor branch and the zero matrix in the four-anchor
branch. The former has an exact `eta=0` / perfect-pairing split. These are
necessary for actual blocks and sufficient for the selected trade-row parity
equations. The support census must now impose only the other `h-1` block
checks, compatible extensions, and first-core/cross-core ownership.

Per fixed support/slope, the other `h-1` checks are now completely routed.
Polynomial division by the extension locator gives `d-z_i` remaining local
checks and `tau_i` extension checks. Unique support interpolation produces a
residual external zero set `E_i`; every actual block is exactly a
`tau_i`-subset of `E_i`, so its extension count is
`C(|E_i|,tau_i)`. The open support census is now family-level: enumerate the
coefficient-compatible supports, enforce pairwise block/core compatibility,
and assign first-core/cross-core owners.

The pairwise compatibility test in that sentence is now closed. Splitting
each extension into active-zero reuse `I_i` and outside part `O_i` gives the
exact slack `z_i+z_j-d-1`; the summed ledger charges
`(t-1)sum|I_i|+sum_x C(m_x,2)`. For fixed supports and external zero sets,
compatible families are precisely the finite set packings satisfying these
inequalities. What remains is a bound on the number of coefficient-compatible
supports and packing solutions, together with first-core/cross-core
ownership.

## Paid

- post-strip cross-slope cores are at most `k`;
- fixed-core pencil populations obey the moving-root/sunflower bound;
- the exact W-collision pair moment and codeword-pair regrouping are proved;
- every generic fixed union chart `|U|=R+d` obeys the field-independent GRK
  ray bound. Exact candidate arithmetic pays `d<=3` at all RowC rates and
  `d<=11,10,9` at the prize rates `1/4,1/8,1/16` respectively.
- the canonical component-union atlas partitions the high-core slope set,
  chooses one witness ray per slope, and applies GRK once per disjoint slope
  component. This resolves deduplication across collision cores and union
  charts exactly.
- the all-LineRay affine-core theorem pays the slope target whenever any
  one-per-slope selector has affine error rank `sigma<=3`, directly by
  `C(sigma+r,sigma)<=8n^3`. It separately counts the complete pair family at
  its full affine rank. Exact arithmetic rejects `sigma=4` at all six rows.
- the collision-line basis ledger proves `sum_ell b_ell<=C(n,s-1)` and the
  exact line cap `floor((n-k)/(A-k))`. A line with only `b` bases puts the
  whole selector in a chart of excess at most `b+s-2`; a minimum-basis line
  also self-localizes the basis injection to that chart. Uniform core matroids
  are paid through ranks `13,9,7,60,40,30` on the six rows.
- the affine-core cogirth ray bound proves
  `#slopes C(h+s-1,s-1)<=C(N,s-1)(N-s+1)`. It pays full-domain ranks through
  `4,4,3,11,11,10` and, on the self-localized line charts, closes selector rank
  four on all six high-core rows.
- every high-direction-distance fixed chart obeys the field-independent DDR
  bound `<=|U|^2`; the exact complementary branch has a sparse lift of the
  received direction. For an MDS chart direction at the prize rows, DDR pays
  residual excess through `d=45,210,182`, `38,693,399`, and `8,985,287` at
  rates `1/4`, `1/8`, and `1/16`. At RowC scale the MDS-direction excess
  threshold is zero.

## Open

Prove the aggregate distinct-slope count `<=8n^3` by controlling the explicit
canonical ledger

```text
sum_C floor(C(R+d_C,d_C) R / C(d_C+h,d_C)).
```

Every selector of the open family must have affine error rank at least
`5,5,5` at RowC and `17,17,15` at the prize rates `1/4,1/8,1/16`,
respectively. The former catch-#158 rank-four branch is paid.
Within the component route, the open quantities are the number of collision
components and their union excesses `d_C`; chart deduplication itself is paid.
The P9 profile records giant connected toy components with `d_C=k`, canonical
selector rank `k+1`, and no selector of rank at most three after the tangent
deletion. Thus neither a general small-excess claim nor a universal low-
transversal-rank claim is supported. In the uniform split-pencil route,
minimum-face collapsed trades are now excluded; larger-union rank-two and
trade-rank-at-least-three cores remain. The `a+3` rank-two shell is reduced
to quadratic-involution chart ownership. Higher shells now have exact
zero-fiber arity and primitive-deficit tests, but remain unclassified where
the deficit is nonpositive. At prize scale, primitive rank two is absent
through the printed multi-million shell band and the primitive first shell
is empty; only proper local circuits survive there. Their rank-two part has
constant block arity four/five, but its embedding count is not paid. The
canonical fundamental-circuit star also pays ownership inside each fixed
trade, but not first-core selection or cross-core ownership. The collision
moment still cannot replace the distinct-slope target. On the DDR
complement, use the sparse-direction normal form rather than treating low
direction distance as an unnamed exception.
