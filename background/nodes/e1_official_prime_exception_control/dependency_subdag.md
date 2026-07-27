# dependency sub-DAG: e1_official_prime_exception_control

Edges are directed from dependency to consumer.

```text
official_row_primes_pinning [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_clean_anchor_exact_collision_allowance [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_pair_feasible_ambient_generation [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_pair_feasible_ambient_generation [PROVED]
    --requirement--> e1_pair_feasible_prime_field_reduction [PROVED]

e1_pair_feasible_prime_field_reduction [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_prime_field_l2_norm_collision_radius [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_high_variance_collision_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_sparse_l1_variance_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e38_quotient_schur_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e37_quotient_schur_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e36_quotient_schur_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e35_quotient_schur_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e34_endpoint_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e33_endpoint_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e32_profile_parity_diameter_reduction [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e32_profile_08_light_template_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e32_four_odd_light_template_reduction [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_proper_conductor_collision_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_2adic_cofactor_collision_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_signed_chord_collision_gate [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_local_norm_cofactor_collapse [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n512_four_singleton_collision_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n512_trinomial_interval_norm_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e30_profile_parity_light_reduction [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e30_three_profile_quotient_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e30_two_odd_profile_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_s16_e30_profile_422_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_official_prime_exception_control [TARGET]
    -> e1_fullness [CONDITIONAL]
```

The exact compiler fixes the finite allowance but supplies no collision bound.
The two field reductions prove that the live branch is ambient-generating and
prime-field. Exact folded-norm arguments remove swap distances through four at
`N=256` and through two at `N=512`. The square-mass-16 logarithmic and
endpoint refinements reduce one `N=256,s=5` profile to positive even variance
at most 60. At `V=64`, exact cubic and parity arithmetic leaves
only `(4,7)`, `(0,8)`, and `(3,5,1)`; the exact light-template census removes
`(0,8)`, and the two four-odd branches share a proved 148-template
repeated-wedge router. Two independent joint censuses remove `(3,5,1)` with
`M_3=1392<1517`; two independent exact-resultant ledgers and the proper-
conductor theorem remove `(4,7)`. The endpoint synthesis closes `V=64`, and
the corresponding eight-template chain closes `V=62`. At `V=60`, exact
profile/parity and quotient reductions plus a complete two-odd census first
leave three six-odd profiles. The proved profile-`(4,2,2)` exclusion uses a
complete odd-difference relaxation and exact exceptional norms. The proved
profile-`(5,4,1)` exclusion adds two independent 2,924,654,040-assignment
relaxations, two independent exceptional actual-vector engines, and exact
FLINT/PARI norms. The proved profile-`(6,6)` exclusion adds independent
44,779,702,968-assignment relaxations, independent 23,638,891,776-vector
exceptional censuses, and exact norms for the 1,232 primitive exceptions. The
E30 endpoint synthesis is therefore proved, and the live positive even
frontier is `V<=58`. The proved E29 profile/parity/light reduction then leaves
eight profiles on exactly 111 affine one-diameter light templates. The proved
joint exclusion uses two independent 2,203,120,896-vector censuses, the exact
`M_3=872` cutoff, the proper-conductor theorem, and independent FLINT/PARI
norms for 820 primitive exceptions. The E29 endpoint synthesis closes `V=58`
and advances the live positive even frontier to `V<=56`. The proved E28
reduction then reuses the four-odd atlas and leaves eight profiles on 154
templates. Its joint exclusion combines two independent 3,056,582,144-vector
censuses, conductor, and exact FLINT/PARI norms for 4,372 primitive exceptions.
The E28 endpoint synthesis closes `V=56` and advances the frontier to `V<=54`.
The proved E27 reduction leaves six profiles on eight three-odd affine
templates. Its joint exclusion combines two independent 158,783,488-vector
censuses, conductor, and exact FLINT/PARI norms for 404 primitive exceptions.
The E27 endpoint synthesis closes `V=54` and advances the frontier to `V<=52`.
The proper-conductor theorem also removes all proper-subfield lifts from both
first-band profiles. The 2-adic cofactor theorem supplies independent
singleton-exponent screens in both profiles. Full-conductor vectors passing
those screens remain. In `(3,4,0)`, every remaining support has a signed
equal-chord relation and therefore lies on a three-term or parallelogram
template. Local reciprocity leaves only five power-of-two cofactors in that
profile and 419 explicit cofactors in `(4,2,0)`. Their odd norm parts
are not yet paid.
The official quantifier pin and named-exhibit certificate subgraph remain in
`background/nodes/` and have `ev`, not `req`, edges into this target. The
unresolved target is a logical leaf, with its route-uniform scope printed
directly.
The evidence nodes do not belong to the mathematical critical orbit without a
theorem transporting their content into a closed route-wide result.
