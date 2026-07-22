# Claim contract - broad-checkpoint Frobenius periodicity exclusion

- **claim:** every official `m>=3` checkpoint row with remainder greater than
  16 has no pair of complete `p`-point Frobenius-pencil fibers, hence no
  minimum-width first-checkpoint collision.
- **scope:** the seven exact atlas rows printed in `broad_orbit_closure.tsv`,
  tail width `t=p`, and all first-checkpoint depths.
- **proved dependencies:** first-checkpoint split-pencil reduction and the
  official checkpoint characteristic atlas.
- **falsifier:** a table mismatch, a missing frequency not divisible by its
  printed gcd, a valid pair whose signed support is not prime-field valued,
  or an odd-size sign support in an even-period coefficient word.
- **nonclaim:** no exclusion on the nine `n=m(p+1)` rows, no higher-width
  bound, and no full L1 payment.
- **compute policy:** no contributor or Modal run remains on the seven closed
  rows. Any minimum-width request must name one of the nine residual rows.
