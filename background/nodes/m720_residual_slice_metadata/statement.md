# m720_residual_slice_metadata

- **status:** PROVED
- **closure:** verifier

## Statement

Under the Modal count-ceiling window rule, every `h=7..20` residual cell beyond
the WSL-safe complete zero cells is either a `W<n` window slice or one of
exactly two over-ceiling complete-window cells:

```text
n=32, h=16, q_exp=2
n=32, h=16, q_exp=3
```

## Falsifier

A residual configured cell that is complete, under the count ceiling, and not
already in the WSL-safe complete-cell list.
