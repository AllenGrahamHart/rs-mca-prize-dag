# Source evidence

The interfaces are imported from the local PROVED nodes

- `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`;
- `rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler`; and
- `rate_half_kb_m2_r4_coordinate_colored_quotient_resultant_compiler`.

The witness itself is new and self-contained in `certificate.json`. The
primary verifier reconstructs every star, matrix row, polynomial product,
division, and support test from that raw certificate. The audit uses a
separate determinant-and-evaluation replay.

The upstream coordinate K-fiber verifier at commit
`780520c4399815451f30a28ec22bdff075629242` contains only coefficient-generated
sample ranks over `F_101`; it does not contain this edge-realized packet or a
finite admissible packet census.
