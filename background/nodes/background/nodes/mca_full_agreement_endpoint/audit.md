# Audit

The upper proof is in the quotient `F^D/C`, so it counts slopes rather than
codewords or witnesses. The case where the entire quotient line is zero is
handled separately: it yields no failed witness because the received pair is
already in `C^2`.

The verifier exhausts all received pairs and slopes for a proper binary
linear code, checks the exact numerator at every agreement, and verifies the
explicit lower construction and field-cutoff arithmetic.
