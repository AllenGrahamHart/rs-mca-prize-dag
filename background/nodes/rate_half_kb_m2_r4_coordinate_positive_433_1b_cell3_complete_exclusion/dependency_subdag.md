# Dependency Sub-DAG

```text
rank-drop common exception classifier [PROVED] ------------------+
parallel-DE first-pair aggregate + pairings 3..14 [PROVED] ------+
six xi3 matching blocks [PROVED] --------------------------------+
xi4 -> xi3 outside-role transport [PROVED] ----------------------+
xi5 finite-source exclusion + xi6 endpoint exclusion [PROVED] ---+
                                                                  |
                                                                  v
                                      role cell 3 complete [PROVED]
                                                                  |
                                                                  v ev
                                               rate-half band [OPEN]
```

All inbound edges are `req`.  The edge to the rate-half consumer is `ev`:
this theorem closes one role cell, not the full positive route.
