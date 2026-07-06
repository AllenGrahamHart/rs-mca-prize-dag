# zone_b conditional proof
## Predicate node
- `e1_fullness`
## Claim
The zone-(b) value-set determination: |{e_1(B)}| is (1-o(1))-full relative to
the signed-core quotient at the open cells N' in {128, 256}.
## Proof
The value set factors exactly through the signed-core quotient: full antipodal
pairs contribute zero (proved, the Brief-F/H zero-sum lemma), so e_1 depends
only on the signed core; the quotient count is ((3^{N'/2}+1)/2-type) exact.
Non-quotient collisions are norm-gated (collision_norm_criterion, PROVED);
e1_fullness bounds their density for admissible primes. Data: the exact cells
match the quotient prediction (equality at N'=16 p=60161; 99.6% at N'=32),
prize-shape scans show zero collision mass. Modulo e1_fullness the
determination lands on the collision-free branch, feeding prob:perfiber at
sigma=1 = mca_unsafe's last input.
