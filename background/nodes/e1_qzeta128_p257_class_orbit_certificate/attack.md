# Attack

Use two independent exact class-group implementations on
`K=Q[x]/(x^64+1)`.

Primary route:

1. compute and unconditionally certify the class group invariant factors;
2. factor 257 and choose the degree-one prime specified in the transcript;
3. compute its class coordinate and the induced actions of `x->x^-1` and
   `x->x^3`;
4. emit the 64 coordinates and prove they are distinct.

Independent route:

- repeat in a different CAS/algorithm, or
- check an exported relation matrix plus exact principal-ideal witnesses and
  its Smith form without invoking the primary class-group routine.

The job must checkpoint before certification, preserve useful partial output,
and distinguish `PASS`, `FAIL`, and `INCOMPLETE`. No local WSL class-group
computation is authorized.
