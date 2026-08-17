# Rank-eleven rich-flat self-iteration budget wall

- **status:** PROVED method wall
- **row:** KoalaBear MCA, post-near affine error rank eleven
- **source terminal:** upstream PR `#1173`, imported by
  `rate_half_mca_rank11_anticode_branch_payments_import`

At cutoff `tau=1547`, put

```text
A=1114501,  c0=2A-n=131850,
L_low=B_*-2w-H(tau)-(n-A)=206105684094104220.
```

For a `q`-dimensional affine container and ordered-basis gap `Delta`, the
self-similar route charges

```text
floor(m_fall_(10-q)/Delta^(10-q)) R_q,
```

where `R_1=8147918` is the proved rank-one ray cap and, for `q>=2`,

```text
R_q=(n-A) floor(C(n-K+q,q)/C(A-K+q,q)).
```

The exact shared one-rung scan gives `Delta=89398`, hence `h=42452`, as
the largest payable threshold. This independently reproduces PR `#1173`.

Serially iterating the same mechanism cannot pay even one survivor branch:

```text
start q=1: min = 2539543014780268202 at (Delta_1,Delta_2)=(64305,67546),
           excess over L_low = 2333437330686163982;

start q=2: min = 3232479920013973566 at (Delta_2,Delta_3)=(66671,65180),
           excess over L_low = 3026374235919869346.
```

These minima grant the branch the entire low-record budget and ignore its
sibling branch. Therefore ordinary self-iteration fails by more than an
order of magnitude.

## Nonclaim

This does not refute factor synchronization, cross-bucket incidence
coupling, a Wronskian/subspace-design inequality, or chronology-safe owner
routing. One of those genuinely new resources is required.
