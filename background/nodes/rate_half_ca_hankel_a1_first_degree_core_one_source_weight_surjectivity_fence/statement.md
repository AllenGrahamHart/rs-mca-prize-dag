# `A=1` first-degree core-one source-weight surjectivity fence

- **status:** PROVED
- **closure:** contracted RS sources impose no standalone Hankel restriction
- **consumer:** `rate_half_band_crossing_location`

Let `s_0 in D` be the fixed core root in a core-one `A=1` profile, let
`v_x in F^x` be the RS dual column multipliers, and put

```text
D_res=D\{s_0},       d=rho-1.                        (SWS1)
```

If an endpoint word has source values `a_x`, its syndrome moments are

```text
y_k=sum_(x in D)a_xv_xx^k.                           (SWS2)
```

Contracting by the fixed factor `X-s_0` gives residual moments

```text
h_k=y_(k+1)-s_0y_k
   =sum_(x in D_res)omega_xx^k,
omega_x=(x-s_0)v_xa_x.                               (SWS3)
```

The coordinate map

```text
(a_x)_(x in D_res) |-> (omega_x)_(x in D_res)        (SWS4)
```

is a diagonal linear isomorphism. Hence every residual source-weight vector
occurs for an RS word.

At the official first-degree core-one row,

```text
|D_res|=N-1=4rho-1,
2d+1=2rho-1.                                         (SWS5)
```

The truncated moment map

```text
F^(D_res) -> F^(2d+1),
omega |-> (sum_x omega_xx^k)_(0<=k<=2d)              (SWS6)
```

is surjective. Therefore every symmetric Hankel matrix of size `(d+1)` and
every pair of such endpoint Hankel matrices has a contracted RS source
representation on `D_res`.

## Route fence

The source expansion in the marked-source theorem cannot by itself force
termwise noncancellation, a valuation bound, or failure of the factor
`D_1g_*^2S_B^6`. Any valid exclusion must additionally use at least one
non-source condition, such as column-farness, the simultaneous supported
split-locator incidence, the primitive minimal-index profile, or the Forney
contact identities.

This theorem does not say that an arbitrary represented Hankel pair is
column-far or realizes the retained packet.
