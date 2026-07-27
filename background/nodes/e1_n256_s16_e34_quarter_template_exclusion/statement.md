# E1 N=256 E=34 quarter-template exclusion

- **status:** PROVED
- **closure:** two independent complete finite censuses

No pair-feasible folded-profile `(3,4,0)` collision at `V=68` lies in the
quarter heavy-position template.

After translation, reflection, and global sign normalization, that template
has

```text
H={0,32,64},       (c_0,c_64)=(2,-2),
96 notin L,        c_32 in {-2,2}.
```

Two independent exact implementations exhaust

```text
binom(124,4) * 2 * 16 = 300,200,032
```

signed vectors. Both give

```text
supports tested                         9,381,251,
vectors with E=34                      1,514,544,
vectors with profile (6,7)             1,181,056,
full-conductor profile-(6,7) vectors   1,031,680,
maximum M_3 on the last class                1188.
```

Since `1188<1947`, the inherited rational cubic-Hermite certificate puts the
collision norm below `2^250`, contradicting pair feasibility. Proper-
conductor candidates are already excluded by the conductor theorem.

This theorem does not exclude the nonquarter diameter, progression, or
generic heavy templates.
