# Frontier

Any successor sparse-first generator must consume all three certified
integer filters before exact ring arithmetic:

```text
max |xi_t|<=3,       sum |xi_t|<=60,       sum xi_t^2<=101.
```

It must then apply the cofactor-specific coefficient boxes to both `u` and
`u^(-1)` and retain only exact profile-`(3,6,S=18)` products. A generic
coordinate or ellipsoid enumeration remains rejected.
