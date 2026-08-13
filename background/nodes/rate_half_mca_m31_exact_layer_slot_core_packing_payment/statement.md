# Mersenne exact-layer slot-core packing payment

- **status:** PROVED
- **scope:** Mersenne-31 full-lift supports `130226<=e<=130236`
- **adjacent route wall:** `e=130237`

Let a line slot selected by the recursive bank belong to exact layer `h`
and contain `lambda>=2` members.  If its inside common core has size `u`,
then

```text
u>=ceil((lambda*h-e)/(lambda-1)).
```

Use this layer-aware lower bound in the preceding high-core/capped-core
dichotomy.  For each printed support, choose the tabled legal cutoff.  Three
selected lines then violate pairwise inside-core packing.  At `e=130237`,
the only useful legal bank forces threshold two at its first layer; the
layer-aware core lower bound is only 807 and the current packing route does
not close.
