# Source evidence

The two surviving types are pinned through draft upstream PR `#1132`,
first-layer commit `e368e5c8fc101ae0040b47265c2cd167e70dadd2`. The
normal-form compiler is exported in the second layer at current PR head
`f7a42415bdb24c7e626b76394558bad100c5a874`, with theorem blob
`5a36de4a27d80d5a885aa0751db9fc37d9744aab`, certificate blob
`8e0ecd7f5b008900ada67dbf80848e8dbbff8416`, and payload SHA-256
`7eb4f4053f90cb4ca0d0f3379fa3f8f33522ae0ec9b3dc67f5c7e602150d22f0`.
The five `r=4` profiles are proved by the local dependency
`rate_half_kb_m12_r4_low_genus_branch_profile_reduction`.

The Dickson quotient argument and the five derivative-integration normal
forms are new local deductions. Both verifiers use exact rational or
quadratic-field arithmetic only; no external computation is imported.
