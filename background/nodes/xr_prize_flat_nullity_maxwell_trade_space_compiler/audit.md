# Audit

- The selected exact-size block contains both a `W` basis and a witness that
  the extension direction is not locally in `W`; arbitrary truncation would
  not preserve those properties.
- The domain, block size, and cap are respectively
  `R+a+u`, `a+h+u+v`, and `a+u+v`.
- The dense-core coefficient is `h`, while each parity block has `h+u+v`
  rows. Their exact difference gives `(u+v)(t-2)`.
- No MDS dual-distance claim is made for `u>0`. Rank-one trades are routed by
  a matroid circuit, not by the `u=0` locator polynomial.
- The circuit owner is necessary and canonical, but no count or sufficiency
  claim is made for the local-tangent condition alone.
- No Modal or large local computation is used.
