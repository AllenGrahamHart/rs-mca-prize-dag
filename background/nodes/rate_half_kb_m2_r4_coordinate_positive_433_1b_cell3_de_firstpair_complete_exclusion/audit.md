# Audit

- Pairings one and two reuse only the proved target-free first pair; all
  remaining equations are solved anew.
- For `xi=2`, `de=-m` and the quartic uses `(d^2-de)^2`; both signs are pinned
  in source and verifier.
- The negative-`DE` rows die before target-lane equations because the `d`
  quartic has no field root.  The positive rows die by degree-zero `f` gcds.
- The `xi=1` transport is checked for pairing indices one and two, not inferred
  from the earlier pairing-zero claim alone.
- The theorem's 144 cases consist of 48 parent, 64 newly computed, and 32
  newly transported raw atlas cases; finite subrows are not recounted as raw
  cases.
- The timed-out `xi=3` pilots produce no theorem evidence.
