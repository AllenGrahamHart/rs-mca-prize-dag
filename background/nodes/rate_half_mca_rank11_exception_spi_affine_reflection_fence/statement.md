# Affine reflections survive the twenty-fiber SPI interface

- **status:** PROVED
- **closure:** exact additive-energy averaging on the official base field
- **consumer:** `rate_half_band_crossing_location` (evidence)
- **dependency:**
  `rate_half_mca_rank11_heavy_ruling_exception_split_pencil_normal_form`

Let

```text
p=2130706433,       H=mu_N subset F_p^*,       N=2^21.
```

For `c in F_p`, put

```text
R_c=#{x in H:c-x in H}.
```

There is a nonzero `c` with `R_c>=2065`. After deleting the possible fixed
point `x=c/2`, the involution `x -> c-x` therefore has at least `1032`
two-element orbits in `H`. Every orbit `{x,c-x}` gives one member of the
quadratic pencil

```text
u(X)=X^2-cX,       v(X)=1,
u(X)+gamma_x v(X)=(X-x)(X-(c-x)),
gamma_x=x(c-x).                                      (AR1)
```

Different orbits give distinct slopes and pairwise-disjoint split squarefree
degree-two domain locators. The pencil has coprime generators, degree two,
and constant locator scalar one. It therefore satisfies the bounded
exception-SPI interface with more than twenty fibers.

Because `c!=0`, translation reflection does not preserve all of `H`; it is
not a global multiplicative cyclic or dihedral quotient of the domain. Thus
the bare twenty-fiber interface cannot be closed by classifying only global
domain symmetries. Partial affine-reflection fibers or additional
heavy-ruling semantics must also be controlled.

This is an official-field algebraic route fence, not an actual unsafe MCA
line or prize counterexample.

## Falsifier

Failure of the additive-energy identity, a nonzero-reflection average below
the printed value, fewer than `1032` nonfixed orbits, repeated slopes from
different orbits, a nonsplit or repeated locator, or a claim that the
nonzero translation globally stabilizes `H`.
