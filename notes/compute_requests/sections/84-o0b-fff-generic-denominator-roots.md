## Preregistered O0b `FFF` generic denominator roots

- **decision:** collect every deployed-field root of the 44 generic-basis
  denominators before imposing the FFF necessary subsystem
- **scope:** basis-denominator exceptions only; later generic reductions may
  add further denominator roots
- **source result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **launcher SHA-256:**
  `f6c461bcafcc1f13b3f082d72ac2120f5fa6eb2cd430f07750b304edc01a1cf3`
- **outcome-neutral checker SHA-256:**
  `c99b027800ac50fbc4a5301cdd506d795db5882418ade1428f3a8c38751faaaf`
- **method:** for every denominator compute `gcd(D,t^p-t)` and factor its
  square-free field part; independently repeat on the denominator LCM and
  require equality with the per-denominator root union
- **input ledger:** 44 distinct denominators; degree range 0--42; raw degree
  sum 1,013; field `GF(2130706433)`
- **output ledger:** per-denominator roots and reconstructed linear root
  polynomial; LCM degree/hash; combined root polynomial and exact root list
- **envelope:** one CPU, 1.5 GiB, 180-second container wall; projected cost
  below `$0.03`
- **local safety:** one RAM-guarded Modal client under a 240-second external
  hard stop; no local factorization

The combined root list is exactly the finite set where the current generic
basis may fail to specialize. It has no proof status for `q5,q7,q6`, and it
does not include any denominator introduced by their future reductions.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 240s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_t_denominator_roots_modal.py
```

**Outcome:** first launch `ap-xqXYpg7uKj6R6yoCrP5nRa` was rejected before
factorization because the pinned `fmpz_mod_poly` API has no convenience
`.lcm()` method. No mathematical output was produced. The exact-division
repair completed in Modal app `ap-OWgH6QIeyDAsAMnej0nU6T` in 0.017 seconds.

The raw degree sum 1,013 collapses to an LCM of degree 49. Its deployed-field
root set is exactly

```text
0, 1, 16711679, 666570304, 676802667, 1141382033,
2113994754, 2130706432
```

The per-denominator root union agrees with the independent LCM Frobenius
gcd. The hostile checker reconstructs all 44 linear root polynomials and
rejects all four mutations. Result SHA-256:
`7489a4c860059240395ed0e1b264f5643ba58fe257076781a0bb596e582738b0`.
These eight values are the complete basis-denominator exceptional set;
future reductions may enlarge it.
