# Proof

The source census leaves no ordinary `xi=0` point and two ordinary `xi=2`
points in each source-sign row.  Thus `xi=0` is empty before introducing any
target variables.  At an ordinary `xi=2` point let

```text
m = B(-t^2)/A(-t^2),
S = (-t^2) beta(-t^2)^2/A(-t^2)^2.
```

Impose `de=-m` and `(d-e)^2=S`.  For each target lane and matching `0,1,2`,
adjoin the three paired-resultant equations and invert the full target guard.
This is

```text
8 negative source points * 4 lanes * 3 matchings = 96 systems.
```

Singular obtains the unit ideal in all 96 systems.  Independently,
substituting `e=de/d` reduces each system to two variables; SymPy again
obtains 96 unit ideals.  Both ledgers have no unresolved system or witness.

Finally, the universal involutions send the six direct labels onto

```text
{(0,0),(1,0)},
{(0,1),(0,2),(1,1),(1,2)},
{(2,0)},
{(2,1),(2,2)}.
```

These are four active orbits and nine labels. QED.
