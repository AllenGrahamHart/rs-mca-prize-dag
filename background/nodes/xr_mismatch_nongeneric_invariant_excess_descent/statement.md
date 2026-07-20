# Invariant-excess nongeneric mismatch descent

- **status:** PROVED
- **consumer:** `xr_tangent_support_mismatch_bridge`

Consider a chain of live mismatch instances indexed by `j`, with ambient
length `N_j`, RS dimension `K_j`, agreement `A_j`, and common excess

```text
h=A_j-K_j>=1.
```

At a nongeneric full-zero chart, let `d_j` be the external zero count. The
alternative-joint-support equivalence produces the next instance on the old
discrepancy set, with

```text
N_(j+1)<=N_j-A_j,
K_(j+1)=K_j-d_j,
A_(j+1)=A_j-d_j.
```

Then the excess remains `h`, every live transition lowers ambient length by
at least `h+1`, and a chain starting at length `n` has at most

```text
floor(n/(h+1))-1
```

nongeneric transitions. At the six clean-rate candidates this cap is,
respectively,

```text
169, 169, 255, 254, 254, 510,
```

all strictly below the deciding scale `256` or `512`.

This proves termination and depth only. It does not bound the number of
branches or slopes across one level.
