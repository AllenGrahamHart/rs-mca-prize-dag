# Audit

Run `verify.py` and `verify_audit.py`. The first pins the adapter, primary
packet, unchanged compiler, tower, kernel, independent root packet, direct
replay, and orbit router. It checks this node's exact row cover and terminal
ledger while selecting only pairing 3 from the shared audit.

The second parses all executable sources, checks the independent root method,
checks the pairing-3 root replay and its empty `q` intersection, and rejects a hostile mutation of the pairing-3
ledger.
