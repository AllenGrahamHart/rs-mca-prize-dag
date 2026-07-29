# Attack

1. Falsify first: seek six diagonal Galois orbits of actual profile-(0,18)
   polynomials with the same exact norm `514p`, where `p` is an
   official-admissible prime. Six modular/autocorrelation candidates defeat
   only an intermediate filter; they do not kill the stated threshold.
2. Screen the 12 surviving signed magnitude profiles by the fixed-root trace equation
   `18+sum_d A_d(s^d+s^-d)=0 mod 257` and local multiplicity two.
   The Hermite moment exclusion has already removed `(9;1,2,0)` and
   `(11;7,1,0)`, and the cubic relation exclusion has removed `(10;6,1,0)`;
   do not enumerate them.
   The explicit `{1,...,11,15}` energy-twelve target survives root, parity,
   positivity, and cubic-moment screens, so this stage cannot close the route.
   The proved singleton-completion no-go shows that `F(s)=0` plus local
   multiplicity one, without the low-energy gate, admits all 128 ideals.
3. Impose coefficient realization for 18 distinct signed singleton terms;
   do not confuse an autocorrelation target with a realizable polynomial.
4. Canonicalize by inversion and diagonal Galois action while retaining the
   relative row-root/257-root class.
5. Compute exact norms only for surviving realizable types. Group by the
   exact quotient `p=Norm/514`; count diagonal Galois orbits, not raw
   autocorrelation targets or roots of the squared-magnitude polynomial.

Any substantial computation belongs on Modal after budget authorization.
It must stream partial results and retain exact witnesses within the recorded
cost cap.

The staged launcher is
`experiments/prize_resolution/e1_profile018_m514_low_energy_root_search_modal.py`.
It is not an occupancy verifier: a hit proves only that the first joint
realization/root/energy gate is nonempty.
