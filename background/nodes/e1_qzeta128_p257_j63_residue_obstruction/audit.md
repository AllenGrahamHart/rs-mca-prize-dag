# Audit

- The auxiliary calculation uses one five-million-element prime field; it
  does not enumerate that field or allocate a field-sized table.
- The character is a product over exactly the embeddings
  `s=1,3,...,63`. Its action on all 31 unit generators is checked.
- Roots of unity are killed separately by their order.
- Negative Jacobi exponents are legitimate because every Jacobi factor is
  nonzero at the auxiliary primes.
- The obstruction proves that `alpha` is not a unit times an `ell`th power;
  the Stickelberger relation is what converts this to nonprincipality.
- No GRH assumption, BNF computation, or predicted class coordinate occurs.
