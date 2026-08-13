# Cycle 198: MCA degree-guarded shifted-lattice witness adapter (2026-08-12)

The failed silent dimension transport from Cycle 196 admits an exact repair
at the lattice-to-witness layer.  For one received-word lattice, the code
shift and effective shift are

```text
s_k(W,N)   = max(deg W, deg N-(k-1)),
s_k+1(W,N) = max(deg W, deg N-k).
```

Every vector, and consequently the two minima, differ by at most one.  For a
monic split complement locator of degree `omega=n-m`, the effective envelope
allows one extra coefficient:

```text
K=k+1 envelope:  deg(N/W)<=k,
actual code:      deg(N/W)<k.
```

Adding the second inequality, equivalently `deg N<=omega+k-1` or the
code-shift cap, gives an exact bijection with degree-`<k` explanations on the
identical size-`m` support.  There is no profile inference in this step.

Same-support pair noncontainment is also executable.  Interpolate `u` and
`v` on the selected support to their unique degree-`<m` polynomials.  The
pair is simultaneously code-explained exactly when both degrees are below
`k`.  A guarded explanation of `u+gamma v` plus failure of this pair test is
therefore an actual support-wise MCA-bad witness.

The theorem closes SEM-QBC soundness at the lattice-to-witness layer and the
algebraic degree guard required by its condition 4.  It does not prove that a
balanced numerical profile is BC-owned, preserve owner chronology across
the shift, exclude Q globally, or cover the frozen BC cell.  Those remain the
semantic frontier.

The primary checker exhausts all `15*7^4=36015` exact-support records in a
`GF(7)` row and confirms exactly `7^3` actual-code records per support.  It
also checks `108` shift-degree pairs and eight mutations.  An independent
checker verifies the official one-coefficient gap and both contained and
noncontained support controls.

```text
start:                   d797d8ffd
result:                  PROVED exact guarded cross-shift witness adapter
DAG delta:               +1 PROVED background node, +1 evidence edge
critical status delta:   none
upstream terminal delta: SEM-QBC conditions 1 and 4 narrowed to owner-level
                         soundness/coverage rather than degree reconstruction
delta-star movement:     none
compute:                 36015 tiny exact toy records; no Modal spend
next route action:       instantiate one typed deployed pole-line certificate,
                         then attack frozen-owner soundness and Q exclusion
```
