# M31 source-head infinity-owner route cut

- **status:** PROVED
- **closure:** proof
- **requires:** `l1_m31_top_pair_source_head_saturation_router`
- **role:** prevent an invalid transport of source-head colors into the
  full-projective-line deletion ledger

Inside the normalized-label class, the source head

```text
gamma(f)=[X^(d-1)]f
```

is the evaluation-at-infinity functional on the degree-below-`d` polynomial
space. Adjoining the point at infinity to an extended Reed--Solomon domain
therefore realizes `gamma` as one additional projective evaluation line.

The existing full-projective-line deletion recurrence, however, pays
agreement incidences with one fixed received label. At infinity it can pay
only the single fiber

```text
{f:gamma(f)=u_infinity}.
```

It supplies no sum over all source-head values and no owner for the colored
core cells attached to different values. Re-running the recurrence with a
different `u_infinity` changes the received word; those separate bounds may
not be added as one first-match ledger.

Moreover the already-proved local inequalities alone admit arbitrarily large
abstract neighbor ledgers: give every neighbor a distinct head and `4980`
private cores. Then every head fiber and every `(core,head)` cell has load
one, and every fixed core has load one, regardless of the number of
neighbors. Thus the caps `458812`, `240`, and `15`, even with the
`71,643,276` colored-core floor, do not imply the local cap `215792` without
a new cross-head/core owner or source incidence theorem.

## Scope

This is an interface route cut, not a source counterexample. It does not rule
out an extended-domain theorem that couples infinity to finite agreement
coordinates, nor a Pad\'e theorem that bounds the head/core spectrum.
