# `A=1` collision shape-A componentwise degree floor

- **status:** PROVED
- **closure:** every off-diagonal image component has bidegree at least
  `39,768,216`
- **scope:** the official prime-field shape-A collision branch
- **consumer:** `rate_half_band_crossing_location`

Retain shape A and put

```text
e=(2^39+1)/3,       m=e-2,       n=(3e-7)/2=2^38-3,
N=2^41,             H=mu_N,      P_char>2^167.       (CDF1)
```

Let `C` be the normalization of `G(t,X)=0`, viewed as a connected
degree-`n` cover of the parameter line. Let `W` be any geometric
irreducible component of the off-diagonal fiber product, let `h` be its
degree over either copy of `C`, and let `Z` be its image in the `(X,Y)`
plane. If `q` is the generic degree of `W -> Z`, then:

1. `W` and `Z` are defined over the base field;
2. `Z` has bidegree `(D,D)`, where

```text
D=mh/q;                                                (CDF2)
```

3. `Z` contains at least

```text
ceil((e+7)nh/q)=ceil((e+7)nD/m)                       (CDF3)
```

distinct points of `H^2`;
4. `Z` is not a translated one-dimensional subtorus.

Consequently

```text
D>=D_0,
D_0=ceil((e+7)^3 n^3/(108 N^2 m^3))
   =39768216.                                         (CDF4)
```

In particular, every component image contains at least

```text
ceil((e+7)nD_0/m)=10931403977394458172                (CDF5)
```

official subgroup points, and its generic forgotten-parameter
multiplicity satisfies

```text
q<4608h.                                              (CDF6)
```

## Scope

This excludes the complete low-degree component route, not shape A. High
degree non-toral components remain possible. The argument uses the
prime-field characteristic floor `P_char>2^167`; no extension-field
transport is claimed.
