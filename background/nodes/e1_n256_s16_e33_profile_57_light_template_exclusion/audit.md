# Audit

- Production app `ap-GpozWWr9n5UCGVYAn4Ydl8` completed all 100 light-orbit
  tasks in 238.629139 aggregate worker-seconds.
- Independent ordered-negacyclic app `ap-Q31nLvELxLsAfXipcD01L5` completed
  the same 100 tasks in 382.736139 aggregate worker-seconds.
- Both launchers checkpoint after every returned template, preserve explicit
  errors, and set `complete=true` only for the exact set `0,...,99`.
- The checker independently derives 7,200 normalized diameter-Sidon supports
  and 100 affine-unit orbits.
- The two implementations agree on every template's light representative,
  coverage, profile count, full-conductor count, and both maxima.
- Every production maximizing witness is independently reconstructed from its
  positions and coefficients, including profile, conductor, and `M_3`.
- Hostile controls reject one missing orbit, the false full-conductor maximum
  1415, and any attempt to pass the proper-conductor maximizer through the
  full-conductor gate.
