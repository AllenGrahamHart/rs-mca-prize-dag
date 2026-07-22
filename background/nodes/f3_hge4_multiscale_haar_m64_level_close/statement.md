# HGE4 multiscale Haar norm product and the `m=64` level close

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_exact_ratio_tower_orbit_compiler`,
  `f3_hge4_ambient_norm_level_contraction`

Use an official ambient row

```text
n=2^s, 13<=s<=41,       m=2^r|n,
p prime, p=1 mod n,     p>=n^2,
4<=h<m/4.                                             (MHN1)
```

For the signed support difference `f` of a hypothetical primitive exact-level
pair, put

```text
M=m/2,       q_t=f_t+f_(t+M),
D=sum_(t<M)(f_t-f_(t+M))^2,       L=sum_(t<M)q_t^2,
H=floor((h-1)/2),       ell=1+floor(log_2 H).        (MHN2)
```

For `0<=a<ell`, define

```text
N_a=M/2^a,
Q_a(u)=sum_(0<=t<M, t=u mod N_a) q_t,
Delta_a=sum_(u<N_a/2)(Q_a(u)-Q_a(u+N_a/2))^2,
r_a=#{b<=H/2^a:b odd}.                               (MHN3)
```

These energies share one exact Haar budget:

```text
D+L=4h,       sum_(a<ell) Delta_a/2^(a+1)<=L.        (MHN4)
```

Moreover `Delta_a=0` exactly when the signed support polynomial
`F(X)=sum_t f_tX^t` is divisible by `Phi_(N_a)(X)`. Let

```text
S={a:Delta_a>0},       Z={0,...,ell-1}\S,
R_S=floor(h/2)+sum_(a in S)r_a,
T_2(S)=sum_(O in {m} union {N_j:j in S})
           sum_(a in Z) min(O,N_a)/2.               (MHN5)
```

Then the product of the nonzero cyclotomic norms satisfies

```text
2^T_2(S) p^R_S divides
 |Norm_m(F(zeta_m))| product_(a in S)|Norm_(N_a)(F(zeta_(N_a)))|,

 |Norm_m(F(zeta_m))| product_(a in S)|Norm_(N_a)(F(zeta_(N_a)))|
 <=D^(m/4) product_(a in S) Delta_a^(N_a/4).         (MHN6)
```

Thus all moment norms consume the single budget `(MHN4)`, rather than one
copy of `L` per scale. This is the multiscale Haar norm router.

For an immediately checkable uniform exclusion gate, put

```text
A=m/4,       B_a=N_a/4,       W_S=A+sum_(a in S)B_a,
U_S=2^(sum_(a in S)(a+1)B_a) (4h)^W_S
      A^A product_(a in S)B_a^B_a / W_S^W_S.        (MHN7)
```

If

```text
2^T_2(S) n^(2R_S)>=U_S                              (MHN8)
```

for every subset `S`, no primitive pair exists at that width. The comparison
in `(MHN8)` is a rational integer comparison after multiplication by
`W_S^W_S`; it does not require materializing cyclotomic integers.

At `m=64`, the one width not closed directly by `(MHN8)` has a sharper finite
endpoint inequality. For `h=4`, let `Delta_0` have the meaning above and let
`nu` be nine or the first nonzero Taylor-coefficient index of `F(X) mod 2`,
whichever is smaller. Equivalently, `nu` is the multiplicity of `X-1`
truncated at nine. Whenever
`D Delta_0!=0`,

```text
D^16 Delta_0^8 / 2^(2nu) <=10^24/4 <2^78.          (MHN9)
```

The first inequality is an exhaustive 16-quarter-orbit support lemma with
only 28,171 aggregate states. It is replayed by `verify.py`.

Consequently, for every official ambient row,

```text
E_h^prim(64,p)=0       for every 4<=h<=32,
sum_(h=4)^32 E_h^prim(64,p)=0.                     (MHN10)
```

The exact level `m=64` is therefore fully paid at zero cost. Together with
the already empty lower levels, any surviving HGE4 exact-level contribution
starts at `m=128`. This theorem does not pay any level `m>=128` or prove the
full HGE4 aggregate.
