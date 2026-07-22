# XR mismatch terminal-tangent agreement raise

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **dependencies:** `xr_mismatch_accumulated_locator_flag_normal_form`,
  `xr_true_tangent_coordinate_injection`

For a received pair `(u,v)` and agreement threshold `a`, write

```text
B_a(u,v)={z in F:there is p in C with agr(u+zv,p)>=a}.  (TAR1)
```

Let `(c_0,c_1)` be any codeword pair jointly agreeing with `(u,v)` on at
least `A` coordinates. Suppose a retained support-wise bad slope `z` has a
witness whose explaining codeword is exactly

```text
p_z=c_0+z c_1.                                         (TAR2)
```

Then

```text
z in B_(A+1)(u,v).                                     (TAR3)
```

Consequently, in any deterministic canonical mismatch forest, if `Z_tan`
is the union of slopes whose first terminal event is a genuine tangent to a
lifted explanation, then

```text
Z_tan subseteq B_(A+1)(u,v),
|Z_tan|<=|B_(A+1)(u,v)|.                               (TAR4)
```

This is stronger than summing `(n-A)` over terminal explanation pairs: the
union is charged once to one stricter-agreement slope set on the original
received pair. Repeating this routing can raise agreement at most `n-A`
times before the bad set is empty.

The theorem does not bound `B_(A+1)`, preserve a quotient/profile label after
raising agreement, aggregate generic terminal charts, or close the mismatch
bridge.
