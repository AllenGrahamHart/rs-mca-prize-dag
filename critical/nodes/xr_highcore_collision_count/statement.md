# XR high-core collision count

- **status:** see `dag.json` (single source of truth)

At each of the six clean-rate candidates, prove both clauses:

1. **P-A1 (generic high core).** For every globally generic-branch received
   pair `(u,v)`, the number of post-strip live slopes whose selected agreement
   support shares a size-`k` core with another live member is at most

```text
8 n^3.
```

The count is on distinct slopes, not raw supports or the W-collision moment.
2. **P-A2 (nongeneric mismatch total).** For every received pair having a
   joint codeword-pair explanation on an `A`-support, remove only quotient and
   genuinely recovered-line tangent slopes. The total number of all retained
   support-mismatch slopes is at most

```text
16 n^3.
```

P-A2 uses one combined reserve; it does not require separate `8n^3` high/low
bounds. This is exactly the former mismatch-bridge numerical obligation, now
merged into an existing red leaf without changing its constant. Global joint
`A`-proximity is a routing condition, not a payment.

Dihedral-symmetric and extension-type slopes remain inside the applicable
predicate allocation. Genericity-based auxiliary charges below apply to
P-A1. The canonical mismatch descent and support-local LineRay charge attack
P-A2.

The higher-rank uniform-cell compiler now has no collapsed minimum-face
exception. At affine kernel rank `a`, a collapsed rank-two trade on active
union `a+2` would force every active selected error to vanish on that whole
union. Two active errors would then share `(k-a)+(a+2)=k+2` zeros, against
the post-strip cap `k`. Hence, after quotienting the regular Plucker face
syzygies, every surviving rank-two trade has active union at least `a+3`.
On the first residual shell `a+3`, the zero fibers are now proved to be
disjoint pairs, with at most one singleton, paired by one base-field Mobius
involution. Ownership and counting of those quadratic-pullback charts,
higher shells, trade rank at least three, nonuniform cells, and the aggregate
distinct-slope payment remain open.

More generally, a rank-two shell `|X|=a+d+1` now has an exact
degree-versus-arity ledger and an explicit Maxwell deficit. Positivity of
that deficit excludes a rank-two relation supported on every block of its
primitive Maxwell core. At the prize rows this removes primitive full-core
rank two on every shell depth through
`22,428,333;19,217,048;4,478,600`, respectively, at every kernel rank where
the shell exists. On the first residual shell, the remaining rank-three row
space has an exact edge-zero graph normal form and positive full-core deficit,
so the complete primitive first shell is empty at all prize rows. Proper
local circuits and their cross-chart ownership are not paid by these results.
However, every rank-two trade now decomposes into support-minimal circuits on
only four or five blocks. The four-block coefficients form a Mobius/Plucker
Segre circuit and the five-block coefficients form a full projective
five-point circuit. Arbitrary block arity is no longer part of the local
rank-two obligation.

The decomposition ambiguity inside one rank-two trade is also closed. Choose
the lexicographically first basis of its Segre coefficient columns; it has
three or four anchor blocks. Every non-anchor block has one unique
fundamental four/five-block circuit against those anchors, and these circuit
vectors form a basis of the complete row-scaling kernel. What remains is the
first Maxwell-core/trade selection, realized support-embedding count, and
cross-core ownership needed to turn those local stars into the `8n^3`
aggregate.

The three-anchor branch of that star atlas is now fully normalized at the
coefficient level. On every support shell it has

```text
lambda_i=s_i(P+gamma_i Q)/Lambda'_X,
s_i=H(gamma_i)/L'_Gamma(gamma_i),      deg H<t-3,
```

where `P,Q` are independent and `H` avoids every selected slope. This is the
complete full-support dual-`GRS_3` scalar ledger, with explicit barycentric
owner coefficients. Its realized `(X,P,Q,H)` support census is still open;
the four-anchor branch remains separate.

That four-anchor coefficient branch is now exact as well. Relative to its
canonical anchors, every non-anchor is a support-three/four point `beta_e`
on one explicit smooth split quadric

```text
Q_B(beta)=sum_(i<j)(gamma_j-gamma_i)
                    (c_i d_j-d_i c_j) beta_i beta_j=0,
sum_e beta_e=(-1,-1,-1,-1).
```

The point coordinates are exactly its fundamental owner coefficients. Thus
the full rank-two coefficient atlas is complete; realized support embeddings,
first-core selection, and cross-core payment remain open.

Each row now also has an exact dual-codeword support-extension certificate.
If `Z_i=X\S_i` is its active zero fiber and `T_i=A_i\S_i` is the inactive
part of its selected block, then

```text
F_i=R_i Lambda_(Z_i),       P_i=R_i Lambda_(T_i),
|T_i|=h-d-1+|Z_i|,          deg R_i<=d-|Z_i|.
```

The cofactor is unique and the support word is `R_i/Lambda'_(S_i)`. This is
an iff for the two dual-GRS representations. It does not yet prove that the
abstract `T_i` is realized by the received pair as an agreement block.

Actual agreement now imposes a branch-specific received-pair interaction as
well. In the three-anchor basis `(P,Q)`,

```text
((<P,b>,<P,q>),(<Q,b>,<Q,q>))=((0,eta),(-eta,0));
```

in the four-anchor basis `(F,G)`, all four pairings with `b,q` vanish. These
conditions exactly recover the selected trade-row parity equation. The other
`h-1` block checks and their compatible family count remain open.

For a fixed support and slope, those remaining checks are now solved too.
They split into `d-z_i` further support-local checks and
`tau_i=h-d-1+z_i` extension checks. The local checks give one unique
degree-`<a` correction `w_i`; if `E_i` is the external zero set of
`b+gamma_i q+w_i`, then actual selected blocks are exactly

```text
A_i=S_i union T_i,       T_i subset E_i,       |T_i|=tau_i,
```

and their number is `C(|E_i|,tau_i)`. Per-row extension counting is closed;
support-family enumeration, intersection compatibility, and first-core/
cross-core ownership remain open.

Extension-family intersection compatibility is now an exact packing ledger.
Writing `I_i=T_i intersect Z_i` and `O_i=T_i\X`, every pair obeys

```text
|I_i|+|I_j|+|O_i intersect O_j|<=z_i+z_j-d-1,
```

and summing charges inside reuse `t-1` times and each outside point by its
multiplicity pair count. Thus compatibility is no longer open; counting the
coefficient-compatible support families and packing-ledger solutions, plus
first-core/cross-core ownership, remains open.
