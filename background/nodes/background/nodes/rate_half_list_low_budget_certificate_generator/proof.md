# Proof

The generator first passes the exact five-field row input to the proved
canonical descriptor. It then checks `rho=1/2`, `4|n`, `k=n/2`, and
`B* in {1,2}`. Hence every accepted row lies in the scope of the proved
low-budget list theorems, subject to the descriptor's printed external
primality/domain preconditions.

For `LIST`, the proved ordinary theorem supplies

```text
L_1(3n/4)<=B*<L_1(3n/4-1).
```

For `INTERLEAVED_LIST`, the proved all-arity theorem supplies the same pair for
every positive common-support arity. The generator therefore constructs two
claim-ID-bearing packets: a lower count `B*+1` at `3n/4-1` and an upper count
`B*` at `3n/4`. It marks the object, field-scope, denominator, and endpoint
axes proved under that theorem packet and public official-row contract.

The proved compiler canonically recomputes the embedded descriptor, derives
`q,n,k,B*`, classifies the consecutive cells as unsafe and safe, and emits the
unique adjacent crossing. Its endpoint conversion gives

```text
n-3n/4=n/4,
n-(3n/4-1)=n/4+1,
```

with the latter boundary not attained by the largest safe closed radius. The
generator independently compares the compiler result with these exact values
and refuses an internal mismatch.

Every unsupported object, malformed row, non-rate-half row, non-quarter
length, or budget outside `{1,2}` raises an error before a theorem packet is
created. Thus the map has exactly the claimed fail-closed behavior. QED.
