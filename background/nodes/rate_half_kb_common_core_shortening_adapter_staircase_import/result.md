# Result

- Typed reversible shortening adapter for common-core MCA records:
  `(n,k,m) -> (n-c,k-c,m-c)`, slopes/badness/invariants preserved,
  PROVED (with the `c < k` non-affine clause cited from source).
- Exact KoalaBear walls: degree-18 interface dies at `c = 4131`;
  fixed-core cells fit only `s <= 2`; direction-separated boundary
  between `J_13` and `J_14`; Jo transfer blocked by a 3765-bit exact
  multiplier that telescopes.
- Route cut RECORD: no chronology-correct whole-line selector exists in
  the active v4 source; zero ledger movement.
- Replays: `verify.py` (walls, exact integers) PASS;
  `verify_audit.py` (from-scratch F_17 adapter replay + second-method
  walls) PASS.
