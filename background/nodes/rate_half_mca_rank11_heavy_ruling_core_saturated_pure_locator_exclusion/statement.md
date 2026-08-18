# Core-saturated heavy-ruling pure-locator exclusion

- **status:** PROVED
- **scope:** the selected pair types in the heavy-ruling degree-24 packet
  after deterministic pair ownership has been fixed

Reselect each record's exact size-`m` agreement support to contain its
assigned pair core

```text
H_p={x:r_0(x)=a_p(x), r_1(x)=b_p(x)}.
```

This is possible because support-wise pair noncontainment gives `|H_p|<m`,
every selected explanation has at least `m` agreements, and `H_p` is part
of its agreement set. Two distinct owned slopes are retained from every
represented pair type. Their exact supports intersect exactly in `H_p`.
Consequently the complete packet intersection is the recovered heavy-core
intersection `J`, so

```text
C=J,       c=|C|<K-2.
```

After cancellation, every represented residual pair core has size at least
`m'-11`. Two distinct residual pair types have core intersection at most
`K'-1`; hence their core union has size at least

```text
2(m'-11)-(K'-1)=m'+67451>m'.                         (PLX)
```

The pure-locator output of the exact partial-relative router is impossible.
Thus this packet has one of only two interfaces:

1. a nontrivial scalar-locator rational certificate, retaining denominator
   roots and with denominator degree at most `67472`; or
2. original two-cover complexity `chi>=2299571`.

Neither remaining interface is paid here.
