# Audit

1. The parameter coordinate is chosen over the algebraic closure only after
   listing every forbidden point. This does not alter absolute
   irreducibility or the bidegrees.
2. `b` and `w` are actual affine degrees; no equality with their upper bounds
   is assumed.
3. The factor `q_inf^(w+b)` in `(LUR3)` is retained. Dropping it would make
   the polynomial resultant identity false when `Q` is not monic in `z`.
4. The repeated-defect case `S|A_0` is included: squarefreeness of `H` makes
   the extra copy divide `B(z;x_0)`.
5. The valuation argument uses local intersection multiplicity and the fact
   that `q_inf(x_0)!=0`; mere set-theoretic common roots would not prove the
   exact split without `(LUR3)`.
6. A synthetic Kummer example satisfies the resultant pattern. The node
   therefore poses the Hankel/separation-rank incompatibility explicitly and
   does not mislabel a general algebraic identity as a contradiction.
7. The lower bounds on `b,w` use the exact local orders, not a genericity
   assumption. A parameter-constant factor has an `m`th-power resultant.
