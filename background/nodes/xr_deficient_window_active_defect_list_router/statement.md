# XR deficient-window active-defect list router

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count`
- **scope:** official prize rows, high-band deficient primitive Pade family

Use the primitive normal form

```text
(f_tau,g_tau)=(f_*+Q tau,g_*-P tau),    deg tau<k-ell,
gcd(P,Q)=1,    ell=max(deg P,deg Q).
```

For the base errors `E_*=u-f_*`, `E_*'=v-g_*`, define the invariant
primitive residual and its active defect support by

```text
rho(x)=P(x)E_*(x)+Q(x)E_*'(x),
D={x in H:rho(x)!=0},       e=|D|.                         (AD1)
```

Then:

1. `rho` is independent of the chosen family member, `D subset G_d`, and

   ```text
   e<=|G_d|<=d-ell-1.                                       (AD2)
   ```

   No point of `D` belongs to the full joint core of any member.

2. There is a fixed word `w:H\D->F` such that, for every parameter `tau`,

   ```text
   E_tau=Q(w-tau),       E_tau'=-P(w-tau)       on H\D.     (AD3)
   ```

   Hence the parameter family injects into the exact ordinary RS list

   ```text
   {tau in F[X]_{<k-ell}:
       |{x in H\D:tau(x)=w(x)}|=k+d}.                       (AD4)
   ```

3. For a projective slope `lambda=[alpha:beta]`, put

   ```text
   L_lambda=alpha Q-beta P.
   ```

   This is a nonzero polynomial of degree at most `ell`, and on `H\D`

   ```text
   alpha E_tau+beta E_tau'=L_lambda(w-tau).                 (AD5)
   ```

   If a selected ray of `tau` has all its off-core points in `D`, every
   `H\D` root of `L_lambda` is already in the joint core. Its off-core
   block is exactly

   ```text
   B_lambda(tau)={x in D:
       alpha E_tau(x)+beta E_tau'(x)=0},
   |B_lambda(tau)|=h-d.                                     (AD6)
   ```

   Blocks for distinct selected slopes of one pair are disjoint.

4. Partition `N_d=N_d^out+N_d^D`, where `N_d^D` counts pairs for which
   every selected off-core point lies in `D`. Then

   ```text
   N_d^out<=n-e,       N_d^D>0 => e>=2(h-d),
   L_(f_tau,g_tau)<=floor(e/(h-d)) for every D-local pair.   (AD7)
   ```

Thus the unpaid deficient family is an exact punctured ordinary RS list
with at least two disjoint active-defect blocks, not a general affine
parameter family.

This does not bound `N_d^D`. Przemek's rational-owner localization is only
an analogy: it localizes whole agreement supports inside an owner domain,
whereas here the full joint core lies in `H\D` and only selected off-core
blocks lie in `D`.

## Falsifier

Dependence of `rho` on `tau`; a joint-core point in `D`; failure of `(AD3)`
or `(AD5)`; an `H\D` root of `L_lambda` outside the core of a `D`-local
selected ray; intersecting blocks for two selected slopes; or more than
`n-e` pairs exposing a selected off-core point outside `D`.
