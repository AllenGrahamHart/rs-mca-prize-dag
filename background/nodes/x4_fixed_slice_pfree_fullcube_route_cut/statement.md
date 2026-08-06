# Full-prefix to p-free syndrome reduction and full-cube route cut

- **status:** PROVED
- **closure:** proof

In characteristic `p`, put

```text
J={1<=j<=t:p does not divide j},
Psi_J(S)=(sum_(x in S) x^j)_(j in J).
```

Every full depth-`t` elementary locator-prefix fiber on `A`-subsets is
contained in one fixed-weight fiber of `Psi_J`. Since `Psi_J` is linear in the
incidence vector, that fiber is contained in a fiber of the same map on the
full Boolean cube.

This does **not** permit the fixed weight to be discarded at official depth.
For `N=2^41`, the four prize rates, and `B0=F_p(mu_N)`,

```text
t_XR log2|B0| <= N-129.
```

The full-cube map has at most `|B0|^|J|<=|B0|^t_XR` outputs, so one of its
fibers has size at least

```text
2^N/|B0|^t_XR >= 2^129 > N^3=2^123.                 (FC-1)
```

Therefore a direct upper route through the unweighted full-cube maximum is
incapable of proving the official `N^3` maximum-prefix target. A viable
power-sum/F2 bridge must remain Hamming-weight resolved or supply an equally
strong first-match decomposition.
