# Budget-three antipodal pure ramification passport

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_pure_euler_ramification_router`,
  `rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity`

Retain the pure-quartic packet `(PER1)--(PER5)` with `r>=2`, and put

```text
N=4r=d-4,       Phi=TU^3,       Phi+d=e_4V^3C,
Phi'=U^2V^2L,       deg L=1,                             (PRP1)
```

and let `ell` be the root of `L`. If `Lambda` is the linear factor in the
second-derivative Wronskian from pure-quartic degree rigidity, then

```text
A'B''-A''B'=Y^(d-2)U^2V^2 Lambda,
A=DU^4,       B=e_4DV^4,
Lambda=dL.                                               (PRP2)
```

Thus the two formerly separate linear residuals are the same residual.
Moreover, over an algebraic closure,

```text
Z(gcd(T,U))=Z(U) intersect (Z(D) union {0}),
Z(gcd(C,V))=Z(V) intersect (Z(D) union {0}).             (PRP3)
```

Either gcd is one or linear. If nontrivial, its root is `ell` and both
same-side factors have simple roots there.

The rational map

```text
R=Phi/(Phi+d)=TU^3/(e_4V^3C)                            (PRP4)
```

is a tame degree-`N` cover. Above `1` it has the single point `Y=infinity`
with ramification index `N`. Every survivor lies in exactly one of the
following five cases. Exponential notation records a ramification partition,
so `3^r 1^r` means `r` parts of size three and `r` parts of size one.

1. **Generic almost-Belyi case.** `ell` is outside `Z(UV)` and
   `c=Phi(ell)` is neither `0` nor `-d`. The four branch values and profiles
   are

   ```text
   0:       3^r 1^r,
   infinity:3^(r-1) 1^(r+3),
   1:       N,
   lambda=c/(c+d): 2 1^(N-2).                         (PRP5)
   ```

2. **U--T collision.** `ell` is a common simple root of `U,T`. Equivalently,
   it is the unique root of `U` in `Z(D) union {0}`. There are only three
   branch values, and the profile above zero is

   ```text
   4 3^(r-1) 1^(r-1).                                 (PRP6)
   ```

3. **double-T case.** `ell` lies outside `Z(UV)` and `Phi(ell)=0`. It is an
   exact double root of `T`, and the profile above zero is

   ```text
   3^r 2 1^(r-2).                                     (PRP7)
   ```

4. **V--C collision.** `ell` is a common simple root of `V,C`. Equivalently,
   it is the unique root of `V` in `Z(D) union {0}`. The profile above
   infinity is

   ```text
   4 3^(r-2) 1^(r+2).                                 (PRP8)
   ```

5. **double-C case.** `ell` lies outside `Z(UV)` and `Phi(ell)=-d`. It is an
   exact double root of `C`, and the profile above infinity is

   ```text
   3^(r-1) 2 1^(r+1).                                 (PRP9)
   ```

In cases 2--5 the unchanged opposite profile is the one in `(PRP5)`, and
the map is branched only above `0,infinity,1`. The five cases are mutually
exclusive and exhaustive. Their ramification defects all sum to `2N-2`.

This replaces an unstructured low-critical-value search by four exact Belyi
passports and one exact almost-Belyi passport. It does not classify covers
with these passports or enforce the harmonic deleted-root/Fermat matching;
those remain the pure-boundary obstruction.
