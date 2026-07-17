# DLI ell-two weight-six split-16 counterfixture

- **status:** PROVED
- **role:** route cut for the open `(ell,w)=(2,6)` WCL slot

## Statement

Let `q=65537`, let `g=3`, and put

```text
omega=g^64 in GF(q).
```

Then `omega` has exact order `1024`. The set

```text
E={0,180,211,585,852,903} subset Z/1024Z
```

is reduced and antipodal-free, and its associated roots satisfy

```text
sum_(e in E) omega^e=0,
sum_(e in E) omega^(3e)=0.                          (S16)
```

Thus the simultaneous odd-moment equations for the `(2,6)` router have a
genuine guarded solution over a field with

```text
v_2(q-1)=16.
```

Consequently exact order-1024 splitting, or any blanket split threshold at
most `2^16`, does not imply emptiness of the weight-six slot. An official-row
exclusion must use the additional ambient requirement `v_2(q-1)>=41` or an
equivalent stronger arithmetic input.

## Scope

This is not an official WCL counterexample: `16<41`. It does not change the
five-slot frontier or prove that an official counterexample exists. It
refutes only the stronger split-only route.
