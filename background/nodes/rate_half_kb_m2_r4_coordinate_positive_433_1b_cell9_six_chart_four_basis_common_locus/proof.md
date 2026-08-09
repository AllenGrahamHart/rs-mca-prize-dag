# Proof

Let `K0,...,K6` be the proved lex basis of a source-sign common curve.  `K0`
is quadratic in `t`.  Both `K1,K2` are quadratic in `b`, and each of
`K3,K4,K5` is linear in `c`.  Choose one relation of each latter type and
invert its leading coefficient, giving six charts.

For every source-sign row and chart, Singular reduces all seven `Ki` to zero
modulo the three selected relations.  The localized source and tower ideals
both have dimension one.  Adjoining both `b` leading coefficients to the
source ideal gives the unit ideal; the same holds after adjoining all three
`c` leading coefficients.  Hence the six charts cover the whole guarded
curve.  Successive quadratic reduction leaves `1,t,b,tb`. QED.
