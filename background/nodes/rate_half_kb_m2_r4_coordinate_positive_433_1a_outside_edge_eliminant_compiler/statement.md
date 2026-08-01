# KoalaBear m2 r4 positive 433-1a outside-edge eliminant compiler

- **status:** PROVED
- **scope:** each of the seven outside edge records in every principal
  `433-1a -> O0b` ledger case
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`
- **consumer:** `rate_half_band_closure`

Use the unique common coefficient kernel

```text
A_2(w)=d_0+d_1w+d_2w^2,
A_0(w)=e_0+e_1w+e_2w^2,
B_1(w)=beta_0+beta_1w.
```

For one outside target record with product `p` and squared sum `s^2`, put

```text
P(w)=Aw^2+Bw+C=A_0(w)-pA_2(w),
Q(w)=q_4w^4+q_3w^3+q_2w^2+q_1w+q_0
    =wB_1(w)^2-s^2A_2(w)^2,                      (KBPQE-1)

A=e_2-pd_2,       B=e_1-pd_1,       C=e_0-pd_0, (KBPQE-2)

(q_0,...,q_4)=
(-s^2d_0^2,
 beta_0^2-2s^2d_0d_1,
 2beta_0beta_1-s^2(d_1^2+2d_0d_2),
 beta_1^2-2s^2d_1d_2,
 -s^2d_2^2).                                      (KBPQE-3)
```

On the generic branch `A!=0`, define

```text
R_1=q_4(-B^3+2ABC)+q_3A(B^2-AC)-q_2A^2B+q_1A^3,
R_0=q_4(-B^2C+AC^2)+q_3ABC-q_2A^2C+q_0A^3.
```

Then the exact scalar cut is

```text
A^3 Res_w(P,Q)=A R_0^2-B R_0R_1+C R_1^2=0.      (KBPQE-4)
```

The abstract resultant has 22 terms and total coefficient degree six.
The degree-drop branch is retained.  If `A=0,B!=0`, the unique product
root is `w=-C/B` and the exact cleared sum cut is

```text
L=q_4C^4-q_3C^3B+q_2C^2B^2-q_1CB^3+q_0B^4=0.   (KBPQE-5)
```

If `A=B=0`, then `C!=0`: otherwise `A_0=pA_2` identically, forcing all
five supported common products to equal `p`, contrary to the distinct
common products `b` and `-b`.  Thus this branch has no product root.

Every actual packet must pass `(KBPQE-4)` or `(KBPQE-5)` for all seven
records, with roots outside the common labels and denominator locus.  These
seven scalar cuts are a necessary relaxation of the paired-source ledger;
they do not enforce that roots are distinct or occur in three deck pairs.

This theorem does not make a bare resultant sufficient, prove simultaneous
seven-edge incompatibility, delete either alignment branch, close positive
coordinate parity, K3, a Prize row, or either Prize result.

## Falsifier

Failure of `(KBPQE-2)--(KBPQE-5)`, a valid degree-drop edge omitted by the
compiler, an actual packet whose outside record fails its scalar cut, or an
`A=B=C=0` branch compatible with the guarded common products.
