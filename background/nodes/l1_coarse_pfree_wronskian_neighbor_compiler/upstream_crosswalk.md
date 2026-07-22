# Upstream crosswalk - coarse Wronskian neighbor compiler

In upstream `(Q)` terminology this is a collision-gap `Gamma_j` compiler.
The first nontrivial collision width has a constant Wronskian in even depth
and a linear Wronskian in odd depth; each additional exchanged root pair
raises the certificate degree by exactly two. For fixed exchanged subset the
certificate has multiplicity one.

The formal constant/linear boundary is not automatically admissible. The
tame-tail upgrade deletes it whenever its width is below `p`; at official
checkpoint depth the first surviving width is at least `p>n/24`.

This can be vendored as a characteristic-safe collision-gap rung independent
of Myerson flatness. It does not prove the summit: the choice of exchanged
subset remains exponential at linear width. A successor exchange-compression
argument should count how many anchor subsets can support the same low-degree
certificate/owner, rather than re-enumerating target values.
