# Degree-guarded shifted-lattice witness adapter

- **status:** PROVED
- **closure:** exact algebraic equivalence
- **scope:** every finite-field Reed-Solomon evaluation domain, with
  `k<m<=n`

## Statement

Let `D` be an `n`-point evaluation domain, put `omega=n-m`, and for a word
`U` define

```text
M_U={(W,N): W(x)U(x)=N(x) for every x in D}.
```

For the code shift `k` and effective shift `k+1`, write

```text
s_k(W,N)   =max(deg W,deg N-(k-1)),
s_k+1(W,N) =max(deg W,deg N-k).
```

Then every nonzero vector satisfies

```text
s_k+1 <= s_k <= s_k+1+1,
```

and the two lattice minima satisfy the same inequalities.

Now let `W` be monic, `D`-split, squarefree, of degree `omega`, with
`W|Lambda_D`, and suppose `W|N`.  The effective envelope
`s_k+1(W,N)<=omega` allows `c=N/W` to have degree at most `k`.  It encodes an
actual degree-`<k` explanation if and only if any, hence all, of

```text
deg c<k,
deg N<=omega+k-1,
s_k(W,N)<=omega
```

hold.  Under this guard, `T=D\Z(W)` has size `m` and `U=c` on `T`.
Conversely every degree-`<k` explanation on an exact size-`m` support gives
one unique guarded pair `(W,N)` in this way.

For a received line `U=u+gamma v`, pair noncontainment on the same support is
also executable: interpolate `u|T` and `v|T` to their unique polynomials of
degree below `m`.  The pair is simultaneously code-explained on `T` if and
only if both interpolants have degree below `k`.  Thus the guarded lattice
data plus failure of that test reconstruct an actual support-wise MCA-bad
witness on the identical line, slope, and support.

## Consequence

This supplies the algebraic and witness-soundness part of a repaired
`K=k+1` adapter, including boundary records.  The extra degree-`k`
coefficient is explicit and must be rejected rather than transported
silently.

## Nonclaims

No numerical profile is identified with a frozen Q or BC owner.  The theorem
does not prove owner preservation, Q exclusion, BC coverage, support
selection from a larger source support, endpoint realization, selector
totality, a slope bound, or a row closure.

## Falsifier

A guarded effective-envelope vector whose quotient has degree `k`, a
degree-`<k` support explanation not represented by the construction, a shift
gap outside `{0,1}`, or disagreement between pair containment and the two
support-interpolant degree tests.
