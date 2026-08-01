# Proof

The common product matrix has rows

```text
[-p_j,-p_j lambda_j,-p_j lambda_j^2,
  1,lambda_j,lambda_j^2].                         (1)
```

Its rank is five by the common-kernel theorem.  The six signed
maximal cofactors therefore span its one-dimensional kernel.  Writing that
kernel vector as the coefficients of `A_2,A_0` makes (1) exactly
`A_0(lambda_j)=p_j A_2(lambda_j)`, proving `(KBPQI-2)` on the common
labels.  Common-kernel uniqueness fixes `B_1` at the same scale.  The
complete-fiber Vieta theorem applies this coefficient vector at all twelve
labels and supplies `A_2(kappa)!=0` there.

The source-facet theorem makes the six-set `I` deck invariant.  Since its
intersection with `L` is the five-set `(KBPQI-1)`, the sixth member is the
mate `xi=-M`.  Evaluating the complete product equation there gives
`(KBPQI-3)`.

Suppose an actual residual source deck pair is `{kappa,-kappa}` and its
two products are `y,z`.  Then

```text
P_y(kappa)=0,       Q_z(kappa)=0.
```

The two quadratics have a common root, so their resultant vanishes.  The
Sylvester determinant for quadratics expands to `(KBPQI-4)`.  This
argument remains valid when either polynomial drops degree; no division by
a leading coefficient is used.

The signed-edge atlas gives exactly `(KBPQI-5)`.  The source-facet location
census puts one of its five internal records at `eta`.  The seven outside
source labels consist of `xi` and three further deck pairs.  Select the
record at `xi`; the six records left over must therefore split into three
perfect matchings, each satisfying `(KBPQI-4)`.  There are five possible
internal `eta` records, seven possible `xi` records, and fifteen perfect
matchings of six objects, proving `(KBPQI-6)`.  The aligned case permits
the `eta` and `xi` choices to name the same internal record; in the
near-aligned case they name distinct source records.

Finally choose a source square root `z_xi` above `xi` and let `s_x` be the
target-root sum at its star.  The invariant sum record is
`q_xi=z_xi s_x`, so `q_xi^2=xi s_x^2`.  The positive Vieta sum equation is

```text
xi B_1(xi)+q_xi A_2(xi)=0.
```

Squaring and dividing by the nonzero source label `xi` gives exactly
`(KBPQI-7)`.  This equation is independent of the choice of source square
root and target-edge orientation.

Apply the same argument at `kappa` and `-kappa` for each of the three
residual source deck pairs.  Their product equations are precisely
`P_y(kappa)=Q_z(kappa)=0`; their squared sum equations are the last two
rows of `(KBPQI-8)`.  Source-label distinctness makes the three deck pairs
distinct and disjoint from the common set. QED.
