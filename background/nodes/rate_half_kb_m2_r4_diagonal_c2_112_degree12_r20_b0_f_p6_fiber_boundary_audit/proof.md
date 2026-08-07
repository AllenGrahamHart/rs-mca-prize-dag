# Proof

For a fixed cell and `s=j`, specialize the three exact pseudo-remainder core
equations in `F_p0[x,pvar]` and compute their Groebner basis. Every one of the
64 specialized ideals is proper and zero-dimensional.

Repeated squaring modulo that basis computes reduced representatives of
`x^(p0^6)-x` and `pvar^(p0^6)-pvar` without constructing polynomials of
degree `p0^6`. Adjoining these representatives cuts out exactly the
`F_(p0^6)`-rational points of the specialized algebra. The resulting ideal
remains proper in every case.

Sequentially multiply and reduce the required factors in the fixed source
order. The first seven partial products are nonzero in all 64 field
quotients, while the eighth is zero. Source-order reconstruction identifies
the eighth factor as the transported named unit `1+s+pvar`. Thus every
`F_(p0^6)` point in every listed fiber lies on an excluded boundary, so no
listed fiber has an admissible point. QED.
