# Audit - PMA three-petal projective Johnson bound

## Hypothesis ledger

| hypothesis | use | failure mode |
|---|---|---|
| reduced three-petal mu-basis | gives coefficient degrees summing to `e-1` | ambient coefficient degree gives the wrong overlap cap |
| determinant nonzero on the core | makes `(F_p(x),F_q(x))` a nonzero row | a base point makes the projective target undefined |
| primitive `(u,v)` | prevents simultaneous coefficient zeros and makes zero cross-product imply projective equality | multiplying one pair by a polynomial defeats the intersection argument |
| monic split degree-`d` core divisor | gives a `d`-subset of the fixed core and removes scalar duplication | nonsplit or lower-degree members are different objects |
| strict `J>0` | permits division in the packing inequality | equality gives no finite bound |
| exact official source equations | proves the rate-quarter positivity and rate-half tail formula | rounded rates require a separate calculation |

## What closes

The theorem pays the complete `M=4,t=3` branch at rate `1/4`, not merely its
small-background part. It also pays every rate-half cell with `b<=6` and all
rate-half cells satisfying the exact positive-denominator test.

## What remains

- rate-half `M=4,t=3` cells in (PJ8) with nonpositive `J`;
- `M=4,t=2` at rates `1/2` and `1/4`;
- larger `M` full-petal cells;
- mixed and diffuse partial petals.

No claim is made that every coordinate in (PJ8) is realizable. It is a
necessary tail, not a counterexample family.

## Adversarial controls

The verifier checks the exact packing bound against maximum compatible
small set systems, exhausts official rate-quarter and rate-half arithmetic,
and verifies a finite-field projective interpolation fixture. It must reject:

1. replacing the overlap cap `e-1` by an off-by-one smaller value;
2. dropping coefficient-pair primitivity;
3. treating `J=0` as a positive-denominator case;
4. extending the uniform rate-half background claim from `b<=6` to `b<=7`;
5. deleting the rate-half top-tail coordinate `a`.
