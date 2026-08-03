# Claim Contract

- Claim ID: `KBP1B3-XI3P12-RL-1`.
- Inputs: the proved global quadratic quotient, compact kernel, and product
  rank compiler for positive deployed 433-1b role cell 3.
- Guarded scope: `xi=3`, `pairing in {1,2}`, all four source signs and all
  four target lanes.
- Internal cover: three exhaustive `q=de` branches. Pairing 1 checks all four
  target lanes per branch row; pairing 2 fixes `sigma_c` and checks both
  `sigma_o` lanes.
- Certificate: formal same-product factorization, an even quartic in
  `z=1/d`, a quadratic paired cut, exact linear-remainder resultant, direct
  six-by-six/tower norm equality, exhaustive exceptional-root lift, and
  final-pair replay.
- Conclusion: all 32 raw cases are empty.
- Exclusions: pairings 3 through 14, missing indices 4 through 6, full cell 3,
  K3, LIST, MCA, and either Prize problem.
