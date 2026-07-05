# proof: dli_deligne_weyl_transfer

Fix a central profile, a nonzero frequency, and a harmonic `m` in the range
used by `dli_et_peak_mass_reduction`. The predicate
`dli_odd_phase_noncollapse_conductor` supplies the geometric input: on each
square-root component, the phase defining

```text
exp(2 pi i m P_lambda(sigma(y)))
```

is represented by a geometrically nontrivial trace sheaf of bounded conductor,
and the conductor bounds have harmonic total `o(t)` over all DLI factors and
harmonics.

For a geometrically nontrivial trace sheaf on a curve over `F_q`, the
Weil/Deligne Riemann-hypothesis estimate gives square-root cancellation:

```text
|sum_y trace(Frob_y)| <= C(conductor) q^{1/2}
```

after summing over the rational points of the relevant component, with the
usual bounded contribution from the missing singular points. Dividing by the
component size gives a normalized Weyl-sum bound of size
`O(C(conductor) q^{-1/2})`, plus the same lower-order endpoint terms.

Summing these bounds over the finite set of components and over the harmonic
ranges produces exactly the harmonic error budget assumed in the predicate.
By that predicate, the total is `o(t)`. These are the finite-frequency Weyl
bounds needed by `dli_et_peak_mass_reduction`, so the DLI odd-evaluation
exponential-sum bound follows from the noncollapse/conductor input.

This node proves only the standard transfer from geometric nontriviality and
conductor control to Weyl cancellation. It does not prove that the actual
odd-evaluation phases have those properties; that is the target
`dli_odd_phase_noncollapse_conductor`.
