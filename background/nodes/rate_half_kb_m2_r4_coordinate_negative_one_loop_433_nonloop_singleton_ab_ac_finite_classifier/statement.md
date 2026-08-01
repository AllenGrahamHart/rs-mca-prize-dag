# KoalaBear m2 r4 coordinate negative one-loop 433 AB/AC finite classifier

- **status:** PROVED
- **scope:** common matching cells `3,6` of the negative one-loop `(4,3,3)`
  skeleton, in all eight cell/root-sign rows over the deployed field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Let `p=2130706433` and `i=16711679`, so `i^2=-1`.  Use

```text
products=(-1,b,c,bc,-bc),       sums=(0,1+b,1+c,b+c,b-c).       (KB433AB-1)
```

Cell `3` has singleton `AB` and antipodal pairs `L:AC`, `BC+:BC-`.
For root signs `(epsilon_1,epsilon_2)`, normalize its roots to

```text
(1,t,epsilon_1*i,r,epsilon_2*i*r).                              (KB433AB-2)
```

After explicit guard removal, exact product and q elimination leaves the
following complete packet table:

```text
(epsilon_1,epsilon_2)       r           t
(+,+)                    669515297   639982870
(+,-)                   1125500162  1732861855
(-,+)                   1461191136  1490723563
(-,-)                   1005206271   397844578

b=1375161449  -> c=1621120540
b= 477266026  -> c=1039843884.                                  (KB433AB-3)
```

Thus cell `3` has exactly eight guarded common packets.  Target exchange
`b<->c`, with `epsilon_2<->-epsilon_2`, transports them bijectively to
exactly eight cell-`6` packets, where `AC` is the singleton.  Cells `3,6`
therefore have exactly sixteen common packets in total.

This theorem classifies only the common one-loop equations.  It does not
assert that any listed packet admits the required outside records, delete
either cell, treat another matching orbit, close the coordinate
orientation, close a Prize row, or prove either Prize result.

## Falsifier

A guarded common solution outside `(KB433AB-3)`, a listed packet that fails
an original product minor or q weld, or a failure of the target-exchange
transport.
