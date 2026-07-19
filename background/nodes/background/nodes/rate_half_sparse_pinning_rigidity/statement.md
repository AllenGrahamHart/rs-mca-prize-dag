# Rate-half sparse pinning and budget rigidity

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Let `C=RS[F,D,k]`, `|D|=n`, put `m=n-k`, and fix agreement

```text
a=k+tau,       1<=tau<=m-1,       r=n-a=m-tau.
```

Let `(epsilon_1,epsilon_2)` be a sparse pair with support union `E`,
`e=|E|<=r`. Call `j in E` active when `epsilon_2(j)!=0`, and let `A` be the
number of active coordinates. A slope `gamma` is tangent when
`epsilon_1(j)+gamma epsilon_2(j)=0` at some `j in E`.

Then:

1. there are at most `e` tangent slopes, and if `e<=tau`, every MCA-bad
   slope is tangent;
2. every non-tangent MCA-bad slope has a maximal failing witness given by a
   nonzero code polynomial `z` and an active matched coordinate `j`, with

   ```text
   gamma=(z(j)-epsilon_1(j))/epsilon_2(j);                (PR1)
   ```

3. writing `w_out=wt(z|_(D\E))`, the ambiguity polynomial has at least
   `a-e` roots in `D\E` and the exact normal form

   ```text
   z=h product_(x in Z)(X-x),
   Z subset D\E,       |Z|>=a-e,
   deg h<=e-tau-1;                                      (PR2)
   ```

4. if `T` active coordinates are matched and `u` inactive support
   coordinates are unmatched, then

   ```text
   (A-T)+u+w_out<=r,
   T>=A-e+tau+1+u>=A-e+tau+1.                           (PR3)
   ```

For fixed `z`, formula `(PR1)` gives at most `A<=e` slopes. Thus the sparse
mutual upper problem is reduced to counting ambiguity polynomials obeying the
single coupled budget `(PR2)--(PR3)`; separate ambient value-set bounds are
not sufficient.

At the official rate-half row, every candidate has `r<=2^40-1`. Hence for
`q>=2^168` the entire tangent contribution is already below the prize budget:

```text
#tangent<=r<=2^40-1<=floor(q/2^128).                     (PR4)
```

Only the non-tangent coupled system remains in that high-field slice.

## EXPLICIT SPARSE-SAFE CURVE (wave-10 audited, 2026-07-18; pin deltas appended)


- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Let `C=RS[F,D,k]`, `|D|=n`, put `m=n-k`, and fix agreement

```text
a=k+tau,       1<=tau<=m-1,       r=n-a=m-tau.
```

Let `(epsilon_1,epsilon_2)` be a sparse pair with support union `E`,
`e=|E|<=r`. Call `j in E` active when `epsilon_2(j)!=0`, and let `A` be the
number of active coordinates. A slope `gamma` is tangent when
`epsilon_1(j)+gamma epsilon_2(j)=0` at some `j in E`.

Then:

1. there are at most `e` tangent slopes, and if `e<=tau`, every MCA-bad
   slope is tangent;
2. every non-tangent MCA-bad slope has a maximal failing witness given by a
   nonzero code polynomial `z` and an active matched coordinate `j`, with

   ```text
   gamma=(z(j)-epsilon_1(j))/epsilon_2(j);                (PR1)
   ```

3. writing `w_out=wt(z|_(D\E))`, the ambiguity polynomial has at least
   `a-e` roots in `D\E` and the exact normal form

   ```text
   z=h product_(x in Z)(X-x),
   Z subset D\E,       |Z|>=a-e,
   deg h<=e-tau-1;                                      (PR2)
   ```

4. if `T` active coordinates are matched and `u` inactive support
   coordinates are unmatched, then

   ```text
   (A-T)+u+w_out<=r,
   T>=A-e+tau+1+u>=A-e+tau+1.                           (PR3)
   ```

For fixed `z`, formula `(PR1)` gives at most `A<=e` slopes. Thus the sparse
mutual upper problem is reduced to counting ambiguity polynomials obeying the
single coupled budget `(PR2)--(PR3)`; separate ambient value-set bounds are
not sufficient.

There is an exact terminal wedge. If `r<=tau`, then every sparse support has
`e<=r<=tau`, so clause 1 leaves only tangent slopes and

```text
S_sparse(a)<=r.                                           (PR4)
```

For `B*=floor(q/2^128)`, put

```text
r_sp=min(floor((n-k)/2),B*),       a_sp=n-r_sp.
```

Then `r_sp<=tau_sp=(n-k)-r_sp` and

```text
S_sparse(a_sp)<=r_sp<=B*.                                (PR5)
```

At the official rate-half row, every candidate has `r<=2^40-1`. Hence for
`q>=2^168` the entire tangent contribution is already below the prize budget:

```text
#tangent<=r<=2^40-1<=floor(q/2^128).                     (PR6)
```

Only the non-tangent coupled system remains in that high-field slice. At the
specific half-distance agreement `a=3n/4`, `(PR5)` applies already for
`q>=2^167`.
