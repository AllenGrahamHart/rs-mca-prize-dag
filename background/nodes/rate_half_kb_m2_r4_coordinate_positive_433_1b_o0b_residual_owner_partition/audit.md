# Audit

`verify.py` recomputes the split and repeated row counts, raw-label products,
and totals; checks all seven PROVED parent edges and their count-bearing
closures/statements; and checks the route-consumer edge.  `verify_audit.py`
demotes each closing parent, drops an edge, and mutates the residual census.
