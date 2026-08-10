### 2026-08-10 rate-half unique-decoding transfer scope

The Round-31 supply audit left the ABF/BCIKS CA/MCA conversion as a candidate
bridge from ordinary LIST supply to the live far-CA crossing. Its exact scope
has now been specialized and fenced.

For agreement `a` and radius `r=n-a`, the imported MCA-from-CA theorem and
the BCIKS correlated-agreement input require

```text
2r<=n-k.
```

On the official rate-half row this is exactly `a>=3n/4`. The live crossing
interval is `k+2^34<=a<3n/4`; at its nearest interior integer the gate already
fails by two. Thus the named unique-decoding bridge supplies only the existing
half-distance endpoint and no point of the live interior.

The crossing target remains open. Its selected safe-side problem is now
unambiguously a beyond-half-distance theorem: either bound `B_ca^far` in the
window `[2^39.9773,2^128)` at `a=k+2^34`, or prove another endpoint together
with a matching predecessor witness. Ordinary LIST supply and
unique-decoding CA/MCA transfer cannot be composed to do this.
