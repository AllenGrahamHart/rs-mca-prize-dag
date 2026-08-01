# KoalaBear m2 r4 positive three-loop outside-edge eliminant compiler

- **status:** PROVED
- **scope:** each of the 56 outside edge records in the eight positive
  three-loop Vieta lanes
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_three_loop_signed_outside_vieta_atlas`
  and `rate_half_kb_m2_r4_coordinate_positive_three_loop_common_kernel_compiler`
- **consumer:** `rate_half_band_closure`

For one outside target record `(p,s^2)`, write

```text
P(w)=Aw^2+Bw+C=E(w)-pD(w),
Q(w)=q_4w^4+q_3w^3+q_2w^2+q_1w+q_0
    =beta^2w(w-1)^2-s^2D(w)^2.                   (KBP3E-1)
```

The coefficients are explicit:

```text
A=-(a_infinity^2+p)d_2,
B=(a_0^2-a_1^2)d_0-a_1^2d_1
  +(a_infinity^2-a_1^2)d_2-pd_1,
C=-(a_0^2+p)d_0,                                 (KBP3E-2)

(q_0,...,q_4)=
(-s^2d_0^2,
 beta^2-2s^2d_0d_1,
 -2beta^2-s^2(d_1^2+2d_0d_2),
 beta^2-2s^2d_1d_2,
 -s^2d_2^2).                                     (KBP3E-3)
```

On the generic branch `A!=0`, define

```text
R_1=q_4(-B^3+2ABC)+q_3A(B^2-AC)-q_2A^2B+q_1A^3,
R_0=q_4(-B^2C+AC^2)+q_3ABC-q_2A^2C+q_0A^3.
```

Then

```text
A^3 Res_w(P,Q)=A R_0^2-B R_0R_1+C R_1^2.         (KBP3E-4)
```

The resultant has 22 terms and total coefficient degree six.

The degree-drop branch is genuine and is not discarded.  Since `d_2!=0`,
`A=0` exactly when `p=-a_infinity^2`.  If `B!=0`, the unique finite product
root is `w=-C/B`, and the exact cleared sum cut is

```text
L=q_4C^4-q_3C^3B+q_2C^2B^2-q_1CB^3+q_0B^4=0.   (KBP3E-5)
```

If also `B=0`, then `C!=0` by distinct loop target pairs and leading
support, so no outside edge exists.  On either surviving branch, the root
must still pass the common-label, leading-support, pairwise-label, and
target-collision saturations from the signed atlas.

This compiler eliminates one quotient variable but does not make a bare
resultant sufficient, prove an eight-lane deletion, close positive parity,
or prove either Prize result.

## Falsifier

Failure of `(KBP3E-2)--(KBP3E-5)`, a valid `A=0` edge omitted by the linear
branch, or a claimed generic survivor whose guarded root does not satisfy
the original product and squared-sum equations.
