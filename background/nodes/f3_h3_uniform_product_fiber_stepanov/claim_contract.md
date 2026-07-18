# Claim contract

- **claim id:** `f3_h3_uniform_product_fiber_stepanov`
- **statement:** `P(tau)<33n^(2/3)` for every nonzero nonidentity target on
  every prime-field C36 row
- **scope:** `n=2^s`, `13<=s<=41`, prime `p=1 mod n`, `p>=n^2`
- **consumers:** `f3_h3_mobius_excess_half`, marginal product-fiber evidence;
  `f3_h3_double_accident_derivative_ideal`, solely to optimize `B_n`
- **status:** `PROVED`
- **dependencies:** none beyond the fully reproduced auxiliary-polynomial
  argument and elementary algebra in `proof.md`
- **falsifier:** one in-scope row and target with `P(tau)>=33n^(2/3)`
- **replay:** `python3 background/nodes/f3_h3_uniform_product_fiber_stepanov/verify.py`
- **upstream mapping:** residual balanced-core ray compiler / exact
  shift-pair control

The claim does not bound `R(tau)`, any joint moment, or C36'.
Its one required consumer does not claim otherwise: it uses only the literal
pointwise cap to reduce a separator exponent in an independently proved
ideal construction.
