# Cycle 514: population-endpoint plane-line design

## Result: PROVED saturated endpoint router

At `q=3170`, the residual interval is `4960<=K'<=4982` and at least
985,788 coordinates have the maximum 218 owners. The local plane-218
endpoint theorem bounds one plane's recurrence by `K'-2044`, forcing

```text
339..358 distinct 218-point planes.
```

A balanced point-plane moment then gives

```text
at least 22752 plane pairs with intersection size 15,
at least 217 distinct saturated 15-point lines.
```

The line-cap equality count gives each such line an original common core of
size at least 1,045,967, so its residual recurrence is at least
`K'-2609>=2351`.

## Burn-down

```text
starting local pin:       e682ff9bc
canonical prize pin:      0dd5b3244
upstream PR #1170 pin:    6186c7b1
DAG delta:                +1 PROVED endpoint-design node, +3 edges
critical status delta:    none
compute spend:            none
closed interface:         abstract near-saturation at q=3170
next action:              couple recurrent saturated lines across endpoint planes
```

## Nonclaims

- the `q=3170` endpoint is not excluded;
- no dense owner or residual row is paid;
- dimension four, rank eleven, and MCA remain open.
