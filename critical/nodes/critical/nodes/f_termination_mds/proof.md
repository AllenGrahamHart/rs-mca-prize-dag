# f_termination_mds proof

For coordinate-prefix and fiber flats in this node, the evaluation code is a
shortened Reed-Solomon/MDS code. Shortening an MDS code is again MDS on the
remaining coordinate set.

The dual of an MDS code is MDS, so its minimum distance is the Singleton
dual distance. In the parameter range of the node, that distance is above the
sparse-support threshold used by the descent machinery. Therefore there are
no low-weight sparse dual supports to generate nontrivial closed sets.

The support lattice is consequently trivial: it contains only the initial
state. The descent tree has size `1`, and the spread moment count applies
directly.
