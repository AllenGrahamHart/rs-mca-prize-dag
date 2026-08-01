# KoalaBear m2 r4 coordinate negative one-loop 442 outside binary-sextic eigenvalue compiler

- **status:** PROVED
- **scope:** every one-loop `(4,4,2)` residual binary sextic in the live
  rank-six common orbit
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_invariance_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler`
- **consumer:** `rate_half_band_closure`

Write

```text
M=[[Alpha,Beta],[Gamma,-Alpha]],
Delta=Alpha^2+Beta*Gamma != 0,
H(X,Z)=sum_(j=0)^6 h_j X^(6-j) Z^j,   h_0=1.
```

The residual paired-product gate is equivalent to the exact eigenvalue
identity

```text
H(Alpha X+Beta Z,Gamma X-Alpha Z)=Delta^3 H(X,Z). (KB41EV-1)
```

In particular, the unspecified proportionality scalar in the binary-sextic
invariance compiler is always `Delta^3`; the negative eigenvalue is excluded
by fixed-point freedom.

For `0<=ell<=6`, let

```text
T_ell = sum_(j=0)^6 h_j
        sum_(p=max(0,ell-j))^min(ell,6-j)
        binom(6-j,p) binom(j,ell-p)
        Alpha^(6-j-p) Beta^p
        Gamma^(j-ell+p) (-Alpha)^(ell-p).       (KB41EV-2)
```

Then `(KB41EV-1)` is exactly the seven division-free coefficient equations

```text
T_ell-Delta^3 h_ell=0,  0<=ell<=6.             (KB41EV-3)
```

As a linear system in `(h_0,...,h_6)`, `(KB41EV-3)` has rank three over
every deployed field.  Thus each of the eighty invariant-form cells needs
only three independent scalar conditions, rather than fifteen residual
matching tests or an unknown proportionality scalar.

This theorem does not evaluate any of the eighty cells, impose outside sums
or full interpolation, close the coordinate orientation or a row, or prove
either Prize result.

## Falsifier

A guarded fixed-point-free residual sextic satisfying invariance only with
eigenvalue `-Delta^3`, a failure of `(KB41EV-2)`, or a deployed specialization
where the coefficient system has rank other than three.
