# Audit

`verify.py` checks the exact three-parent proof composition, parent statuses,
required edges, count-bearing parent closures, aggregate statement census,
and route-consumer edge.  `verify_audit.py` mutates each dependency and the
printed closure counts to ensure the aggregate cannot remain green after a
missing packet or transport premise.
