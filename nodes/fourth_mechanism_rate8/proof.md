# proof: fourth_mechanism_rate8 (Pro Brief C; verified 11/11 exact)

Route (a) delivers 0.0625 grid steps — 8.8x the required 0.00707.

THE SHARPENED CAP at rho = 1/8 (n = 2^41, k = 2^38, q < 2^256): via the
PROVED quotient-remainder floor (cs25_cap_v12.tex,
cor:extension-pole-quotient-remainder-floor) at the finer quotient scale
c = 2^28 (N = 8192), full-fiber s = 0, d = 17, m = 1041:
- charged prefix coefficients w_c(0, 17c-1) = 16 (verified);
- L >= C(8192,1041)/|B|^16 > 2^398 (exact big-int; Pro's bound 2^380 was
  conservative);
- the trigger threshold (q-n)/k < 2^218 is cleared by 180 bits;
- hence eps_mca > 1/(2k) >> 2^-128 for all delta in
  [7/8 - 17/8192, 7/8): the unsafe boundary moves from 7152/8192 to
  7151/8192 — one part in 8192 = 1/16 grid step.
Ordinary RS, no interleaving; nonconstructive in the same prefix-
pigeonhole sense as the printed cap. The printed reserve 2^-9 came from
the declared N_rho = 1024; the machinery supports N = 8192 here with slack.
