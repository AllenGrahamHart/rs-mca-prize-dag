# Audit

- The binary Hasse-derivative enumeration covers all `120+1820+8008=9948`
  nonzero parity supports modulo 16.
- Successful Modal replay: app `ap-NgXdlPnSNBEljttQ9JDVKa`, peak child RSS
  56 MB. The calculation used the generic content-shipped script runner.
- Targeted proof-verifier replay: app `ap-LJBYsuhoIlh39oqfpo1sLm`, PASS in
  0.091 seconds. Repository gates also passed on Modal: prize DAG
  `ap-AmxyUvMc69xYPgDwdeFawu`, critical harness
  `ap-ZqqFG6yW0eN4StmoTATA5G`, crosswalk
  `ap-uceSHUrzexzJaf3DLj6HeX`, and joint protocol
  `ap-tegzWx1Og20IYD5jFN1hm7`.
- The replay found low multiplicities
  `{1,2,3,4,5,6,8,9,10}` after the cofactor bound. In particular,
  multiplicity seven is impossible.
- The verifier independently recomputes the residue table, cofactor list,
  endpoint logarithmic certificate, and every Taylor onset/previous-row pair.
- The `V=2` argument reuses only the profile-independent Lucas-resultant
  calculation after deriving the required one-lag shape and valuation-lag
  identity anew.
- No support-9 vector census or cyclotomic norm batch was run.
