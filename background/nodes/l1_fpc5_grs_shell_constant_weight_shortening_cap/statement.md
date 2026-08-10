# Constant-weight shortening cap for FPC5 GRS shells

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix one nonempty FPC5 GRS syndrome shell on a core of size `N`, with monic
squarefree locator degree `d`. Define

```text
H=t ell,       sigma=H-d                 when u<0,
H=d+ell,       sigma=ell                 in one fixed-u-set chart when u>=0,
w=min(d,N-d).                                             (CW1)
```

For an integer `0<=j<=w`, put

```text
x_j=w-j,
Delta_j=x_j^2-(N-j)(x_j-sigma).                          (CW2)
```

Call `j` admissible when either `x_j<sigma`, in which case set `P_j=1`, or
when `Delta_j>0`, in which case set

```text
P_j=floor((N-j)sigma/Delta_j).                           (CW3)
```

Then the number of members in the fixed shell is at most

```text
A_j=floor(binom(N,j) P_j/binom(w,j)).                    (CW4)
```

Consequently it is at most the minimum of `(CW4)` over admissible `j` and
the trivial support count `binom(N,w)`. For the complete fixed
source/touched/degree cell this gives

```text
|F_(M,t,d)| <= A_j                         when u<0,
|F_(M,t,d)| <= binom(b,u) A_j              when 0<=u<=b.  (CW5)
```

The second line is the exact required-background incidence union. No field
size, split-pencil classification, or maximum-to-mean hypothesis enters the
cap.

## Scope

The theorem is a fixed source, touched-set, and defect-degree cap. The factor
`binom(b,u)` is retained. Source layouts, touched subsets, defect degrees,
and source scales require a separate valid aggregation theorem. If the first
admissible shortening depth grows with `N`, `(CW4)` may remain exponential;
the theorem does not assert a uniform polynomial bound on every FPC5 cell.
