# Proof

Fix a rank-ten eleven-set `T` and let `C` be its unique circuit support,
with `c=|C|`.  A nine-subset of `T` is obtained by omitting one of the 55
pairs.  It retains the circuit and has rank eight exactly when the omitted
pair is disjoint from `C`.  There are `C(11-c,2)` such pairs.  Every other
nine-subset has rank nine, proving

```text
q_c=55-C(11-c,2).                                  (1)
```

Let `I_c` count low incidences of support `c=2,3,4,5`, and let `H` count
all incidences of support at least six.  Counting their marked rank-nine
shadows inside the one global capacity `G` gives

```text
45H + sum_(c=2)^5 q_c I_c <=G.                     (2)
```

Add `sum (45-q_c)I_c` to both sides of (2).  Then

```text
45(H+sum I_c)
 <=G+sum_(c=2)^5 (45-q_c)I_c.                      (3)
```

For one structural branch, each record contributes at most `L_c` to class
`c`.  Hence `I_c<=R L_c`, and (3) gives `(JL)` after division by 45 and an
integer floor.

If records may occupy different branches, apply (3) record by record to
the premium term.  Every record contributes at most

```text
max_a sum_(c=2)^5 (45-q_c)L_c^(a).
```

Multiplication by `R` proves the branch form.  This is one joint ledger:
the sparse incidences still consume their `q_c` ordinary marks and receive
only the remaining premium.  QED.
