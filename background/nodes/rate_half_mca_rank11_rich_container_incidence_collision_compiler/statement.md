# Rank-eleven rich-container incidence collision compiler

- **status:** PROVED
- **input:** 508 distinct dimension-two/three containers, each with at least
  42453 common actual zero coordinates in a universe of size 1048576

Choose any 508 containers and write `J_i` for one 42453-element subset of
the actual zero set of container `W_i`. Then:

1. some coordinate belongs to at least 21 of the `J_i`;
2. some pair satisfies `|J_i intersect J_j|>=1640`, so
   `W_i+W_j` has dimension at most 6 and vanishes on at least 1640 common
   actual coordinates;
3. some triple has intersection at least 61, so its span has dimension at
   most 9 and vanishes on at least 61 common actual coordinates.

At least 254 selected containers have one common dimension `r in {2,3}`.
Inside that typed subfamily:

```text
one coordinate lies in at least 11 containers;
one pair has common zero set at least 1562 and span dimension at most 2r;
one triple has common zero set at least 52 and span dimension at most 3r.
```

## Nonclaim

No two locators are asserted equal. The common zero sets in the pair and
triple conclusions are intersections of actual labelled coordinate sets,
not synchronized global cores for the complete 508-container family.
