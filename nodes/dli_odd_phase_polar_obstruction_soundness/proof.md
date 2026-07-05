# proof: dli_odd_phase_polar_obstruction_soundness

Fix a smooth square-root component and one actual DLI odd-evaluation phase
`f = P_lambda(sigma(y))`.

The proved node `dli_artin_schreier_conductor_criterion` identifies the
geometrically trivial Artin-Schreier classes with functions of the form

```text
g^p - g + c.
```

Equivalently, after subtracting Artin-Schreier coboundaries, such a class has
a constant representative and hence no positive polar divisor. In local
terms, poles of a raw coboundary `g^p-g` occur with order divisible by `p`;
the reduction process removes those `p`-divisible leading polar terms until a
reduced representative is reached.

Therefore a certificate that the Artin-Schreier-reduced representative of
`f` has a pole of positive order not divisible by `p` proves that the reduced
representative is nonconstant. It cannot be the reduced representative of
`g^p-g+c`, because that class reduces to the constant `c` and has empty polar
divisor.

Applying this local argument to every certified DLI tuple gives
non-Artin-Schreier triviality for every corresponding odd-evaluation phase.
