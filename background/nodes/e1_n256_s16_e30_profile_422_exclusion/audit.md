# Audit

1. The production relaxation enumerates normalized vertex triples and expands
   cyclic convolutions directly. The audit enumerates positive circular gaps
   and uses a signed-triple kernel.
2. Both relaxation engines agree on every shard, including all 29,541,960
   assignments, the three exceptions, and maximum 1146.
3. The production actual-vector engine folds 21 unordered chords. Its audit
   multiplies by the negacyclic reverse and checks anti-palindromicity.
4. Both actual engines agree on all six survivors after 59,543,808 vectors per
   engine, including the conductor split `2+0+0`.
5. FLINT and PARI/GP independently compute both primitive norms.
6. The verifier replays every surviving vector, the profile, conductor split,
   `F_2(x)=F_1(-x)`, packet hashes, DAG edges, and exact integer margin.

Modal applications:

```text
production relaxation final: ap-tvZbcv7UZUzrmCYpkGAOTG
independent relaxation audit: ap-dJMmIFzqO9ccMXj6V7w4EQ
actual-vector final:          ap-6dp2yFFRypuGUw2Xs9tKcD
exact primitive norms:        ap-z7K1Nn5YhdCDPYES6pvGLd
```

The earlier actual-vector launch `ap-IQ6rztTj4LeLC4wg1DSGgC` failed while
compiling a misspelled audit variable and ran no numerical tasks. It is not
evidence.
