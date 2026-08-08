# Audit

Run `verify.py` and `verify_audit.py`. The independent audit checks the AST
adapter boundary, reconstructs every finite-field norm and inverse root set,
checks complete candidate-root coverage and each leading-boundary transport,
then rebuilds the source kernel and proves all 80 final `q`-polynomial gcds
are constant.
