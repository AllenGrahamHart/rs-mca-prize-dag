# `A=1` core-one exceptional-only quadratic-moment pin

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality`

Retain the local coordinate and exceptional generator from the dependency.
Because `M_1` is Hankel, write

```text
(M_1)_(i,j)=h^(1)_(i+j),       0<=i,j<=r.             (QMP1)
```

Put

```text
A(X)=Q(gamma_0;X)=sum_(i=0)^(r-1)a_iX^i
```

and, for `s=0,1,2`, define the shifted quadratic convolutions

```text
Theta_s=sum_(i,j=0)^(r-1) a_i a_j h^(1)_(i+j+s).      (QMP2)
```

Then the exceptional crossing gate is exactly

```text
Theta_0=0,       Theta_1=0,       Theta_2!=0.          (QMP3)
```

The residual moment sequence has a finite source representation

```text
h^(1)_k=sum_(x in D_res) omega_x x^k,       0<=k<=2r, (QMP4)
```

where `D_res` is the evaluation domain after contraction of the fixed core
factor. Consequently

```text
Theta_s=sum_(x in D_res) omega_x x^s A(x)^2.          (QMP5)
```

If `R_A` is the squarefree root set of `A` in `D_res`, this may equivalently
be summed over `D_res\R_A`. Thus the squared exceptional locator has zero
weighted residual moments in degrees zero and one and a nonzero moment in
degree two.

The weights `omega_x` are the contracted endpoint-syndrome weights. They are
not asserted to equal the original error values or to be nonzero. The three
scalar conditions are necessary consequences only; they do not reconstruct
the lower Hankel chain, prove splitting, or exclude the corrected square.
