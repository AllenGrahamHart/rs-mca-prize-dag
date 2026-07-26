# Status ruling

`TARGET`. The historical Modal/fpylll run is useful numerical evidence, but
it is not the complete machine-checkable certificate required by this node.

The only banked executable is `notes/modal_e1_cert.py`. It reports rounded
norms and a truncated vector head, but banks no exact run output, lattice
basis, primitive root, complete shortest vector, enumeration transcript, or
independently checkable lower-bound certificate. More importantly, the script
catches every exception from `SVP.shortest_vector` and does not record whether
that call completed. Its fallback BKZ vector is an upper bound on the lattice
minimum, not a proof that no shorter vector exists. The floating GSO summary
is neither used as an exact certificate nor independently audited.

Thus the printed observation `31.67 > 16` does not prove that every nonzero
lattice vector has norm greater than the box radius. The node may return to
`PROVED` only after banking the exact named field/root and lattice, a complete
no-vector proof certificate or deterministic exhaustive proof log, an
independent exact checker, and hostile mutation tests.
