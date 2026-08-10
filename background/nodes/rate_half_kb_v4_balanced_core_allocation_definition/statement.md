# Balanced-core allocation definition

- **status:** TARGET
- **joint unpaid reserve:** `274980728110413983`

The active partition gives

```text
U_paid + U_Q + U_BC + U_new <= B*,
U_paid = 981104,
B* = 274980728111395087.
```

Define a K3/balanced-core allowance only after proving exact compatible caps
for `U_Q` and `U_new`, or after supplying an equivalent certified three-way
allocation whose three atoms are each proved within their shares. In the
direct subtraction form,

```text
U_K3_allocation = B* - U_paid - U_Q - U_new.
```

The joint reserve `B*-U_paid` cannot be substituted for this value unless
`U_Q=U_new=0` is proved.

## Falsifier

An unproved sibling value, a negative allowance, a partition mismatch, or
use of a jointly owned reserve as a K3-only allocation.
