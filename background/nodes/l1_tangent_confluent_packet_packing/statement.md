# L1 tangent confluent-packet packing

- **status:** PROVED
- **role:** replace the raw sum over tangent gcd owners by a collective,
  field-independent exact-shell packing
- **consumer:** `l1_mixed_petal_amplification`

## Setup

Let `H subset F` have `n` distinct points, let `k<=a<=n`, and fix a
received-word interpolant `U`.  For every exact shell codeword `P` with
complete agreement set `S_P`, `|S_P|=a`, write

```text
U-P=L_P Q_P,        D_P=gcd(L_P,Q_P),        r_P=deg D_P.   (HP1)
```

Thus `D_P` is the unique tangent owner.  Its roots carry both value and first
Hasse-derivative agreement with `U`; every root of `L_P` carries value
agreement.

## Collective packing

For every integer `j` with `0<=j<=floor(k/2)`, one has

```text
sum_(P:r_P>=j) binom(r_P,j) binom(a-j,k-2j)
  <= binom(n,j) binom(n-j,k-2j).                       (HP2)
```

Equivalently, if `N_>=r0` is the number of exact shell members with
`r_P>=r0`, then for every `j<=min(r0,floor(k/2))`,

```text
N_>=r0 <= floor(
  binom(n,j) binom(n-j,k-2j)
  / (binom(r0,j) binom(a-j,k-2j)) ).                  (HP3)
```

The minimum of `(HP3)` over legal `j` is an exact integer precharge.  The
case `j=0` is ordinary agreement-packet packing.  If `k>=2`, `j=1` gives the
collective tangent bound

```text
sum_(P:r_P>=1) r_P
  <= n binom(n-1,k-2)/binom(a-1,k-2),                 (HP4)

#tangent members
  <= floor(n binom(n-1,k-2)/binom(a-1,k-2)).          (HP5)
```

No enumeration or summation over the `binom(n,r)` possible owners appears.

## Mixed complement-Hasse packing

Assume also the balanced band `2a<=n+k-1` and put

```text
omega=n-a,        s=n-2a+k>=1.                         (HP6)
```

For every `0<=j<=s`,

```text
sum_(P:r_P>=j) binom(r_P,j) binom(omega,s-j)
  <= binom(n,j) binom(n-j,s-j).                         (HP7)
```

Consequently, for `j<=min(r0,s)`,

```text
N_>=r0 <= floor(
  binom(n,j) binom(n-j,s-j)
  / (binom(r0,j) binom(omega,s-j)) ).                   (HP8)
```

At `j=0`, `(HP8)` is exactly the existing complement-dimension packing
`binom(n,s)/binom(omega,s)`.  Positive `j` replace complement marks by
tangent Hasse marks and can sharpen high-tangency tails without changing the
ambient packet weight `s`.

This optimization is explicit.  If `B_j(r0)` denotes the right side of
`(HP8)` before flooring and `w=a-k=omega-s`, then

```text
B_(j+1)(r0)/B_j(r0)=(w+j+1)/(r0-j).                  (HP9)
```

Hence `j=0` is optimal whenever `r0<=w+1`.  Otherwise an optimum is attained
at

```text
j*=clamp(ceil((r0-w-1)/2),0,min(r0,s)),              (HP10)
```

with the adjacent index tied when the ratio is one.  Thus the mixed family
changes only the genuinely high-tangency tail `r0>w+1`; no scan over `j` is
needed.

## Scope

The packet bounds can remain exponential in the linear band.  The two packet
families must be minimized with the fixed-owner Hasse bound and primitive
shell descent before comparison with a finite reserve.  This theorem does
not prove primitive Pade-section flatness, puncture-stable Q, or a deployed
adjacent-row numerator.
