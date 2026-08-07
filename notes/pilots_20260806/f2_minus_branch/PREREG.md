# F2 omitted minus-branch adversarial audit - preregistration

- **date:** 2026-08-06
- **claim under attack:** the all-official-row scope of
  `f2_admissible_direct_sum_grs_reduction`
- **candidate witness:** `p=2^61-1`, `q=p^2`, `n=2^41`

In one fresh Modal worker, verify all of the following exactly:

1. Lucas--Lehmer returns zero for M61, certifying that `p` is prime.
2. `q<2^256`, `n|(q-1)`, and `ord_n(p)=2=[F_q:F_p]`.
3. `v_2(p-1)=1`, so the parent's formula gives `2^40`, not the actual
   order two.
4. `gcd(n,p-1)=2`; after choosing one representative per antipodal pair,
   every `F_p`-proportionality class is a singleton.  The full window has
   `C=2^40`, contradicting `C<=4`.
5. The current manifest still records the attacked node as PROVED with
   all-official scope; this is a regression detector, not evidence for it.

Use one CPU, 1 GiB RAM, a 120-second function cap, a 90-second subprocess
cap, and zero retries.  Only a zero return code and the printed PASS marker
authorize graph surgery.  The first correction must preserve the true
`p=1 mod 4` theorem, record this omitted branch explicitly, and avoid any
consumer promotion.

## Result

Modal app `ap-gD4VmoDpSyQJ2F6a5xsRnQ` returned PASS. Lucas--Lehmer
certified M61; the 122-bit admissible quadratic row has actual order two,
old-formula order `2^40`, and `2^40` singleton antipodal classes. The
captured result has SHA-256
`d7c9d525886cf5877a06e1d7b07dc1e84209c1fc5115013842455d2f4e69b1fa`.
