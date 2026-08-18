# Claim contract

## Declared method

- one factor-root cutoff `T`;
- one residual transversality threshold `h`;
- one larger emitted-flat threshold `S`;
- ordered-basis class counts charged independently by `R_4` and `R_6`.

## Result

The method cannot pay any output threshold `S>=18167`; its exact maximum is
the already-proved `S=18166`.

## Falsifier

A legal `T,h,S` with `S>=18167` whose declared complete charge is within the
residual allowance, or an intermediate ordered-basis denominator larger than
the printed global maxima.
