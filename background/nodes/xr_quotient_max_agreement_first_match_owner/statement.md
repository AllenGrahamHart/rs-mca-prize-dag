# XR quotient first match occurs at maximum agreement

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **dependency:** `xr_quotient_boundary_agreement_raise_owner`

Let `C=RS[F,D,k]`, fix `A>=k+1`, and let `C_fib` be a finite family of
declared quotient fiber sizes. For a received line `(u,v)`, put

```text
B_a(u,v)={z in F:there is p in C with agr(u+zv,p)>=a}.
```

Retain `Q_c(>=A)` and `Q_c(A)` from the quotient boundary packets, and define
the maximum-agreement exact quotient image

```text
Q_c^max(A)=Q_c(A) \ B_(A+1)(u,v).                       (QMF1)
```

Then

```text
union_(c in C_fib) Q_c(>=A)
  subseteq union_(c in C_fib) Q_c^max(A) union B_(A+1)(u,v).  (QMF2)
```

If `z in Q_c^max(A)` is witnessed by a codeword `p_z` on an `A`-point
quotient-remainder support `S`, then

```text
{x in D:u(x)+zv(x)=p_z(x)}=S.                           (QMF3)
```

Thus an agreement induction may pay a quotient slope only at its maximum
agreement. At that level its quotient support is a full agreement set, not an
arbitrary subset of a larger witness set. A deterministic order on scales and
witness codewords makes this a disjoint first-match owner.

This theorem removes cross-threshold duplication and witness-subset spray. It
does not bound the number of full-agreement quotient images at one threshold,
aggregate generic charts, pay the raised set, or close XR.
