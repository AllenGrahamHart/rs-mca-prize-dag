# Proof

The source census leaves four ordinary `xi=0` points and two ordinary
`xi=2` points in each source-sign row.  At an ordinary point let

```text
m = B(-t^2)/A(-t^2),
S = (-t^2) beta(-t^2)^2/A(-t^2)^2.
```

For `xi=0`, impose `de=m` and `(d+e)^2=S`.  For `xi=2`, impose `de=-m`
and `(d-e)^2=S`.  For each target lane and matching `0,1,2`, adjoin the
three paired-resultant equations and invert the full target guard.  This is

```text
16 positive source points * 4 lanes * 3 matchings = 192 systems,
 8 negative source points * 4 lanes * 3 matchings =  96 systems.
```

Singular obtains the unit ideal in all 288 systems.  Independently,
substituting `e=de/d` reduces each system to two variables; SymPy again
obtains 288 unit ideals.  The two `A=B=0` points per source-sign row are on
the proved all-role section-base stratum and therefore contribute no target.

Finally, the universal involutions send the six direct labels onto

```text
{(0,0),(1,0)},
{(0,1),(0,2),(1,1),(1,2)},
{(2,0)},
{(2,1),(2,2)}.
```

These are four active orbits and nine labels. QED.
