# proof: cap_envelope_parameter_sweep (verifier replayed ALL PASS)

The quotient-remainder floor is SCALE-FREE: every hypothesis of
cor:extension-pole-quotient-remainder-floor (via lem:quotient-remainder-prefix)
is on (c, m, s, A0) alone — c|n, K<n, m<=N, A0>k, and (s>0 only) mc+s<=n; the
box side-condition is vacuous at full-fiber s=0. N_rho = 1024 was a declared
convenience. Exact big-int sweep results (net gain vs required):

- rate 1/4:  (c,d) = (2^25, 209):  net 81/128  = 0.6328 vs 0.367 required (+0.266)
- rate 1/8:  (c,d) = (2^21, 2251): net 203/2048 = 0.0991 vs 0.023 (+0.076; beats the d=17 template)
- rate 1/16: (c,d) = (2^28, 11):   net 3/8     = 0.3750 vs 0.304 (+0.071)

All conventions conservative (box charged at 2^256; a proper subfield would be
2^128, making these lower bounds). Binding constraint everywhere: the benign
entropy-vs-box tradeoff, matching the window-cleanup figures.
