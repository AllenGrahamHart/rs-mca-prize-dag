# L1 boundary shifted-lattice affine Q cell

- **status:** PROVED
- **role:** separate the boundary Q profile from the interior balanced split-pencil census
- **consumer:** `l1_mixed_petal_amplification`

## Boundary profile

Use the band shifted-lattice notation with `w=m-k`, `omega=n-m`, and a
shifted weak-Popov basis

```text
g_1=(W_1,N_1),       g_2=(W_2,N_2).
```

Assume the boundary profile

```text
d_1=w+1,       d_2=omega.                            (BQ1)
```

Every degree-`omega` census element has unique coordinates

```text
(W,N)=A g_1+B g_2,
deg A<=omega-w-1,       B in F.                      (BQ2)
```

After monic normalization, exact-shell members split disjointly into:

1. **the point at infinity `B=0`:** all valid supports on this ray are
   explained by one fixed codeword `P_0=N_1/W_1`; the complete-agreement
   guard retains at most one member, and retains it only when
   `agr(U,P_0)=m`;
2. **the affine Q cell `B!=0`:** projectively normalize `B=1`.  Members are
   the guarded split points of

   ```text
   (W,N)=g_2+A g_1,       deg A<=omega-w-1,           (BQ3)
   ```

   with `W` a scalar multiple of a monic degree-`omega` divisor of `Omega`
   and the usual complement guard `gcd(Q,Omega/L)=gcd(Q,W)=1`.

The affine parameter `A` is unique for every valid support.  Thus the
boundary costs one possible exact codeword plus one received-word-dependent
affine divisor fiber.  It does not belong to the interior BC census.

## Locator-Q specialization

If `W_1=1`, then `(BQ3)` is

```text
W=W_2+A,       deg A<=omega-w-1.                     (BQ4)
```

Hence the top `w+1` coefficients of the monic degree-`omega` divisor `W`
are prescribed.  This is exactly upstream's boundary locator-Q atom.  For
nonconstant `W_1`, `(BQ3)` is the corresponding quotient/residue affine Q
cell; no transport to the fixed-column atom is asserted.

## Scope

No row-sharp Q bound, quotient-pullback priority map, base-field
normalization, or finite reserve inequality is proved.  Interior profiles
`d_1>=w+2` remain in the balanced BC census.
