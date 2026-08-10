# Audit

`verify.py` checks artifact custody, exact case coverage, normalized
coefficient arrays, the `92/100` numerator and `104/112` denominator degree
profiles, the common four-guard atlas, and the required DAG edges.
`verify_audit.py` mutates case coverage, degrees, guard identity, and source
custody to ensure those controls fail closed.
