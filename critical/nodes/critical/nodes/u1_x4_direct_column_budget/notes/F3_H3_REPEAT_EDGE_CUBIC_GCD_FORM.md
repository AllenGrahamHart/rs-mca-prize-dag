# F3 h=3 repeat edge cubic gcd form

Status: PROVED ALGEBRAIC NORMAL FORM PLUS FINITE GUARDRAILS.

This packet gives an alternative algebraic interface for the singleton-hitting
target: active coordinate edges are root sets of explicit cubics, and singleton
hitting is common-root positivity for those cubics.

## Cubic Form

For an active edge `E={u,v,w}`, let

```text
lambda = u+v+w-2,
m = uvw.
```

The repeat-boundary equation gives

```text
uv+uw+vw = 1+2lambda.
```

Therefore `E` is the root set of

```text
P_E(T) = T^3 - (lambda+2)T^2 + (2lambda+1)T - m.
```

Conversely, this cubic has the three distinct roots `u,v,w`.

For a row with active edge family `E_i`, singleton hitting is equivalent to

```text
gcd_i P_{E_i}(T) has positive degree.
```

If the gcd is constant, the active edge family has no common coordinate and
there is a star obstruction.

## Finite Guardrails

The verifier checks that each active edge cubic has exactly its edge as
subgroup roots, and that common subgroup roots agree with the coordinate
intersection:

```text
p=337   n=16  active_edges=1 common_roots=191,297,336
p=2017  n=32  active_edges=1 common_roots=459,1790,2016
p=4801  n=64  active_edges=1 common_roots=355,1644,3602
p=7937  n=64  active_edges=2 common_roots=2595
p=65537 n=256 active_edges=8 common_roots=2
p=91393 n=256 active_edges=2 common_roots=91160
```

The non-boundary contrast row has no common root:

```text
p=97 n=32 active_edges=15 common_roots=-
```

## Role in h=3

The star theorem can be attacked as a common-root theorem for the active edge
cubics:

```text
H3-CUBIC-COMMON-ROOT:
  in the boundary-style regime, the active cubics P_E have nonconstant gcd.
```

This is equivalent to `tau_coord<=1`, hence to the `90n^2` repeat-residue
payment.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_edge_cubic_gcd_form.py
```

Expected digest:

```text
H3_REPEAT_EDGE_CUBIC_GCD_FORM_PASS
```
