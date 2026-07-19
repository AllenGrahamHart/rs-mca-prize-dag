# PMA three-petal mu-basis reduction

- **status:** PROVED
- **role:** exact arbitrary-locator normal form for the remaining full-petal
  three-touch branch
- **consumer:** `petal_mixed_amplification`, hence `imgfib`

## Statement

Let `K` be a field. Let `L_1,L_2,L_3 in K[X]` be pairwise coprime monic
polynomials of the same degree `ell>=1`, and let `c_1,c_2,c_3 in K` be
distinct. Put

```text
d=ell+s,       0<=s<ell.
```

Define `V_s` to be the vector space of pairs `(F,W)` with
`deg F,deg W<=d` such that

```text
L_i | W-c_iF       for i=1,2,3.
```

Let

```text
Syz(L)_<=s
 = {(B_1,B_2,B_3): deg B_i<=s and sum_i L_iB_i=0}.
```

Then the following hold.

### 1. Exact syzygy dictionary

Writing

```text
A_i=(W-c_iF)/L_i,
alpha=(c_2-c_3,c_3-c_1,c_1-c_2),
```

the map

```text
(F,W) -> (alpha_1A_1,alpha_2A_2,alpha_3A_3)
```

is a linear bijection from `V_s` to `Syz(L)_<=s`. In particular, every
three-petal contributor obeys

```text
(c_2-c_3)L_1A_1
+(c_3-c_1)L_2A_2
+(c_1-c_2)L_3A_3=0.                    (TP)
```

### 2. Mu-basis and exact filtration

There is an integer `mu`, with

```text
0<=mu<=floor(ell/2),
```

and a basis `p,q` of the full polynomial syzygy module such that

```text
deg_vec(p)=mu,       deg_vec(q)=ell-mu,
```

their leading coefficient vectors are independent, and

```text
deg_vec(up+vq)
 = max(deg(u)+mu,deg(v)+ell-mu)         (PB)
```

for every nonzero pair `(u,v)`. Consequently

```text
dim_K V_s
 = [s-mu+1]_+ + [s-(ell-mu)+1]_+,      (HF)
[x]_+=max(x,0).
```

The integer `mu` is independent of the chosen reduced basis.

### 3. Saturated exact-defect balance

Suppose `V_s` contains a pair with

```text
deg F=d,       gcd(F,W)=1.              (SAT)
```

Then

```text
mu=s       or       mu>=ell-s.          (BAL)
```

Equivalently,

```text
s<ell/2   ==>   mu=s and dim_K V_s=1,
s>=ell/2  ==>   mu>=ell-s and dim_K V_s=2s-ell+2.
```

Thus, with

```text
e=max(0,2s-ell+1)=max(0,2d+1-3ell),
```

the below-half strip has one projective candidate. In the upper-half strip,
every candidate has the unique form

```text
B=up+vq,
deg u<=s-mu,
deg v<=s-ell+mu,
```

and the two coefficient-degree allowances sum to

```text
(s-mu)+(s-ell+mu)=e-1.                 (BUDGET)
```

For a saturated pair, the three nonzero products

```text
G_i=L_iA_i=W-c_iF
```

are pairwise coprime.

### 4. Determinant normalization

Let `(F_p,W_p)` and `(F_q,W_q)` be the contributor pairs corresponding to
the reduced basis vectors `p,q`. Then for some `kappa in K^*`,

```text
F_pW_q-F_qW_p=kappa L_1L_2L_3.         (DET)
```

Every pair in `V_s` is uniquely

```text
(F,W)=u(F_p,W_p)+v(F_q,W_q).
```

If `gcd(F,L_1L_2L_3)=1`, then

```text
gcd(F,W)=1       iff       gcd(u,v)=1.  (PRIM)
```

For PMA, `F` is a split locator on the core while the `L_i` vanish on
disjoint petals, so the displayed coprimality with the petal product is
automatic.

## PMA consequence

For a carried full-petal source, the petal locators are monic, squarefree,
and pairwise coprime. Hence every exact saturated `t=3` contributor in the
strict strip `ell<d<2ell` is governed by the normal form above. In the
remaining `M=4,t=3` branch, there are only four touched-petal triples, and
the unresolved freedom is exactly the split-monic `F` locus inside the
two-generator coefficient family with budget `e-1`. Equivalently, it is the
primitive coefficient-pair locus for which

```text
uF_p+vF_q
```

is a monic degree-`d` divisor of the core locator.

This is a strict reduction, not a count. It does not bound the split locus by
a fixed polynomial when `e` grows, does not produce a common-pencil rechart,
and does not close `petal_mixed_amplification`.
