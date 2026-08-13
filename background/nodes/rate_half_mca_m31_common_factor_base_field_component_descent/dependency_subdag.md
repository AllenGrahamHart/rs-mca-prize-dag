# Dependency sub-DAG

```text
weighted-degree bound: 2<=d<=43
                 |
                 +--> char(F)>d --> separable component descent
                 |                       |
factor mass t_d -+--> non-F(X) loss <=d^2
                                         |
                                         +--> >=5079 base-field sections
                                                     |
                                                     +--> >=126263 points
```

This is the requested base-field normalization step.  It replaces an
arbitrary geometric factor union by a union of `F(X)`-defined components,
without assuming that union is irreducible.
