# Result

The near-third scalar prefilter is now one modular gcd:

```text
G_(m,p)=gcd(Q_M, (-(X+2)/8)^((p-1)/m)-1),
N_trace=deg G_(m,p).
```

Here `deg Q_M<=m/2-1`, and the large exponent is evaluated modulo `Q_M` by
repeated squaring. The gcd can be factored to recover every trace ID. Exact
nonempty controls prevent this filter from being mistaken for an emptiness
theorem. The open HGE4 work is now visibly the trace-to-pencil fiber count,
not scalar candidate generation.
