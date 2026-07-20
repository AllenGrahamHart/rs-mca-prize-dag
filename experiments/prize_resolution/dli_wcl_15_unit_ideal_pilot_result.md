# WCL `(1,5)` unit-ideal route pilot

## Exact coefficient baseline

- **Modal app:** `ap-gWA4UOyBSv4c8C4tqDVd84`
- **resources:** one CPU, 2 GiB, one container, 60-second hard timeout
- **outcome:** expected timeout; no mathematical verdict

The exact `ZZ[c0,c1,b]` quotient representation completed squarings through
exponent `64`. At that checkpoint the five remainder coefficients had

```text
terms:          2847, 2943, 3115, 3212, 2714
total degrees:    60,   61,   61,   61,   59
max coeff bits:   68,   67,   67,   68,   67.
```

The container timed out while forming exponent `128`; it did not reach the
official exponent `256` or start a Groebner basis. This rejects naive exact
coefficient expansion in SymPy as the certificate implementation. It does
not weaken the proved unit-ideal theorem or provide evidence for a survivor.

The selected follow-up is the same quotient computation over one finite
field, followed by a modular Groebner basis. A modular PASS is route evidence
for multi-prime rational reconstruction only, not the required integer
Nullstellensatz certificate.

## Modular coefficient pilot

- **first app:** `ap-2QPkBuKJcQIGnKDEvldeWZ`
- **corrected app:** `ap-4mxCfTnbtIf2yz274On6sh`
- **resources per app:** one CPU, 2 GiB, one container, 60-second hard timeout
- **outcome:** route fence; no mathematical verdict

The first modular app failed immediately on a SymPy nested-domain coercion;
it performed no meaningful computation. The corrected implementation used a
native sparse ring over `GF(65537)` and a manual monic degree-five quotient.
It reproduced every exact term count through exponent `64`, completing that
checkpoint in `8.663s`, but did not finish the exponent-`128` square before
the hard timeout. The largest exponent-`64` coefficient had `3,212` terms.

Reduction modulo a prime removed coefficient growth but did not remove the
sparse multiplication wall. Therefore neither exact nor modular SymPy
expansion is an acceptable implementation for the official remainder. The
next contributor pilot should use FLINT/Singular/Magma quotient arithmetic,
or preserve the ten squarings as a straight-line system inside elimination.
No further Modal retry of this SymPy route is requested.
