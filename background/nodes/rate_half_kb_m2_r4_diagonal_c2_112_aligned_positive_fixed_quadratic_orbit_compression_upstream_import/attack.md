# Attack

For each of the six orbit representatives:

1. Use rows `(0,1)`, the unique pair that is quadratic in `w`; an exact
   twelve-case sweep rejects every pair involving the two quartic rows.
2. Factor only the terminal `U,V,Z` cores after removing declared units.
3. On `V!=0`, substitute `w=-U/V` into the remaining two q-slice rows and
   use a regular chain or block elimination in the three base variables.
4. On `V=0`, impose `U=0` and split every actual leading-coefficient degree
   drop before localization.
5. Terminate each component in exact emptiness, a named same-record owner,
   or an explicit primitive route.

Do not rerun a monolithic four-variable basis or use generic saturation.
