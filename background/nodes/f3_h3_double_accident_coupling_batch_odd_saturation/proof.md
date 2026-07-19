# Proof

Write `a=2^r b` with `b` odd. The root `zeta_n^a` is primitive of order
`n/2^r`, and

```text
Norm_(Q(zeta_n)/Q)(1-zeta_n^a)=2^(2^r).            (1)
```

Indeed, the norm in its primitive cyclotomic subfield is
`Phi_(n/2^r)(1)=2`, and the extension to `Q(zeta_n)` has degree `2^r`.
Since `Norm(pi)=2`, division by `pi` proves `(CBS2)`. In particular no prime
ideal above an odd rational prime contains `c_a`, so `c_a` is a unit after
inverting two.

Expand the left side of `(CBS4)`:

```text
c_(u_0)(beta_E c_(u_1)-c_(v_1))
 -c_(u_1)(beta_E c_(u_0)-c_(v_0))
=-c_(v_1)c_(u_0)+c_(v_0)c_(u_1)
=-theta_01.
```

Thus `theta_01` belongs to `(lambda_0,lambda_1)` already over `O`, giving one
inclusion in `(CBS5)`. Conversely, `(CBS4)` gives

```text
lambda_1=c_(u_0)^(-1)(c_(u_1)lambda_0-theta_01)
```

in `O[1/2]`. This gives the reverse inclusion and proves `(CBS5)`.

Localization equality at every prime ideal above an odd rational prime means
that the corresponding prime-ideal valuations of the two integral ideals are
equal. Taking ideal norms therefore gives equality of their odd parts.

Apply `(CBS5)` separately to each pair `(Q_0,Q_i)`. Every `theta_(0,i)` lies
in the localized coupling batch, and every `lambda_i` lies in the localized
anchor ideal. Adding the common ideal `J` proves `(CBS7)`. The final C36'
interpretation follows by taking `J=(alpha_F,alpha_G)` and invoking the proved
nonzero-coupling count. QED.
