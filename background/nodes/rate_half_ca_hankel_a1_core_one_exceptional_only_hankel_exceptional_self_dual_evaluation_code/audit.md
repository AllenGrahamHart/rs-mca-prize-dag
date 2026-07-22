# Audit

1. The evaluation kernel has dimension two because the degree box is
   `2e+1`, not `2e`; both `A` and `XA` must be retained.
2. The coefficient plane loses only `q_0` under evaluation, while the
   rank-one flag loses both `q_0` and `v`.
3. Nonzero source weights make the diagonal evaluation form nondegenerate.
4. Complementary minor signs depend on column orders, but squaring removes
   those signs; the remaining `(-1)^e` comes from the determinant of `(5)`.
5. Self-duality is a necessary structure theorem, not a claim that every
   self-dual code comes from a valid endpoint packet.
