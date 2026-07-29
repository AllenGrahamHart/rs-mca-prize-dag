# Attack

1. Prove or falsify `e1_qzeta128_p257_class_orbit_certificate`. The published
   class coordinates imply a two-ideal bound, but the class-group calculation
   must be replayed unconditionally before promotion.
2. The former falsifier was six diagonal Galois orbits of actual
   profile-(0,18) polynomials with one exact norm `514p`. The class-descent
   route predicts that even three are impossible. Retain any exact collision
   witness as a direct audit of the published class ledger.
3. Historical fallback: screen the 10 surviving signed magnitude profiles by the fixed-root trace equation
   `18+sum_d A_d(s^d+s^-d)=0 mod 257` and local multiplicity two.
   The Hermite moment exclusion has already removed `(9;1,2,0)` and
   `(11;7,1,0)`, and the cubic relation exclusions have removed
   `(10;6,1,0)`, `(11;11,0,0)`, and `(12;12,0,0)`; do not enumerate them.
   The explicit `{1,...,11,15}` energy-twelve target survives root, parity,
   positivity, and cubic-moment screens, but its entire profile is now below
   the exact norm floor.
   The proved singleton-completion no-go shows that `F(s)=0` plus local
   multiplicity one, without the low-energy gate, admits all 128 ideals.
4. Impose coefficient realization for 18 distinct signed singleton terms;
   do not confuse an autocorrelation target with a realizable polynomial.
5. Canonicalize by inversion and diagonal Galois action while retaining the
   relative row-root/257-root class.
6. Compute exact norms only for surviving realizable types. Group by the
   exact quotient `p=Norm/514`; count diagonal Galois orbits, not raw
   autocorrelation targets or roots of the squared-magnitude polynomial.

Any substantial computation belongs on Modal after budget authorization.
It must stream partial results and retain exact witnesses within the recorded
cost cap.

The staged launcher
`experiments/prize_resolution/e1_profile018_m514_low_energy_root_search_modal.py`.
is superseded on the live route. It is not an occupancy verifier: a hit proves
only that the first joint realization/root/energy gate is nonempty.
