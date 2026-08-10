# Proof

Fix an admissible received line. The active BC compiler proves that selected
certificates and `Z_BC` are in bijection. Each certificate stores its affine
slope, explaining data, and an exact agreement support of size
`m=1116048`. Membership in the first-match cell also records that the slope
is bad and belongs to this same received line.

If the cell has at most 31 slopes, the first branch is immediate. Otherwise,
choose any 32-element slope subset. Bijection gives exactly one certificate
for each slope, so the explanations are distinct in slope and no raw witness
multiplicity enters.

For each explanation, its maximal agreement set is uniquely the full set of
coordinates where the stored explaining polynomial agrees with the received
word at that slope. It contains the certificate's exact `m`-support. Thus
maximalizing and then selecting that stored sub-support is exactly the
normalization required by the harvested partial relative theorem.

Apply that theorem. It changes neither the received line nor the slope set;
it classifies their support/codeword data. Hence the original owner and slope
labels persist into the affine, rational, near-sunflower, or primitive-spread
alternative. No endpoint record is constructed. QED.
