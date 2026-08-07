# Rate-half FPC5 inverse source-ratio degree gate

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`
- **upstream interface:** split-pencil / short-syzygy census

Fix any live guarded LS6 atom, in either multiplier range. Write

```text
M=L_2L_3,       s=ell-a,       j=2ell-a,
V=rem_M(D E),   deg V<=s,       gcd(D,V)=1,
F=E^(-1) mod M, deg F<2ell.
```

The official branch has `a<ell/4`; the proof only needs `a<=ell/2`.
Nonemptiness forces

```text
deg F>=ell+a.                                         (RG1)
```

The source CRT residues determine `F` exactly. If the normalized source
labels are `(0,1,lambda)`, then

```text
F==L_1                 mod L_2,
F==lambda^(-1)L_1      mod L_3.                      (RG2)
```

Put

```text
U=rem_(L_3)(L_1 L_2^(-1)).                           (RG3)
```

Then

```text
F=L_1+L_2 A,
A=rem_(L_3)((lambda^(-1)-1)L_1L_2^(-1))
  =(lambda^(-1)-1)U.                                 (RG4)
```

Because `lambda notin {0,1}`, the scalar in `(RG4)` is nonzero. Therefore
`(RG1)` is equivalent to the source-only gate

```text
deg U>=a.                                             (RG5)
```

Equivalently, a violating source has the exact short syzygy

```text
L_1=U L_2+R L_3,       deg U<a,       deg R<a.        (RG6)
```

Such a source supports no guarded LS6 candidate. In particular, if
`L_i=P-z_i` lie in one common degree-`ell` pencil, then `U` is constant and
every tail cell with `a>=1` is empty.

## Scope

This is a source exclusion, not a split-divisor count. It does not show that
the surviving ratio degree is generic, classify the degree-`>=a` syzygies,
or pay any candidate that passes the gate.
