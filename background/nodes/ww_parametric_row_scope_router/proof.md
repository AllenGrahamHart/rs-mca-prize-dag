# Proof

The proved `official_row_primes_pinning` packet pins the challenge fragments
"assuming |F| is sufficiently large" and "for every choice of F, L, and k".
It concludes that the specification defines an admissible family rather than
a named list of literal row primes.  It also establishes the certificate
discipline: a certificate is family-uniform or explicitly exhibit-specific.

The proved `descriptor` node gives a total exact map on admissible tuples
`(p,e,s,rho)`.  It computes `q=p^e`, `n=2^s`, `k=rho*n`, checks the official
caps and subgroup divisibility, and emits `B*=floor(q/2^128)`.  All generated
integers have at most 256 bits.  Thus W3 could consume exact row constants
from its input; no prior enumeration of all admissible rows was needed.

W3 is universally quantified.  A uniform theorem discharges that quantifier
directly.  A proved-total generator/checker also discharges it because every
admissible input produces a sound checked certificate.  A finite collection
of exhibit certificates establishes only those instances unless accompanied
by a transfer or totality theorem.  These are elementary consequences of the
quantifier order.

Neither dependency bounds W3's actual non-planted list count.  The conclusion
therefore removed only the false registry/table prerequisite.  That was enough
to expose a decisive admissible scope instance: the exact fiber-layout packet
uses the descriptor at `q=1705*2^120+1`, `n=8192`, `k=2048`, and refutes an
unsafe-cell extension of the envelope. The quantifier theorem proved here
remains valid; its former consumer is now an open but retired `TARGET`.
