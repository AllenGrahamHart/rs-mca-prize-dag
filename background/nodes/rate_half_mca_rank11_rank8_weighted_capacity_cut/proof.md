# Proof

Write

```text
n'=1048576+K',   m'=67472+K',   D=n'-m'=981104.
```

The weighted component concentrator gives

```text
W_B >=ceil(L(K')),
L(K')=(55*495405467*N_min*C(m',11))
      /(10^9*C(n',9)),
N_min=274980728111260126.                           (1)
```

If this fixed target has evaluation rank eight, the owner-pair cap gives

```text
W_B <=U(K')=(D+1)*C(n'-9,2).                        (2)
```

Exact integer evaluation at `K'=37996` gives

```text
ceil(L)=579191514708840299,
U      =579155144020629315,
ceil(L)-U=36370688210984.                           (3)
```

Because `U` is an integer, (3) also implies `L>U`. To propagate the strict
gap, use

```text
C(n',9)C(n'-9,2)=55C(n',11).
```

After cancellation,

```text
L(K')/U(K')
 =constant*C(m',11)/C(n',11)
 =constant*product_(i=0)^10 (m'-i)/(n'-i).          (4)
```

Every factor in (4) strictly increases with `K'` because `n'-m'=D>0`.
Thus `L(K')>U(K')` for every `K'>=37996`, contradicting (1)-(2).

At `K'=37995`, exact evaluation instead gives

```text
ceil(L)=579135903691691071,
U      =579154077989218305,
U-ceil(L)=18174297527234.
```

Monotonicity of (4) makes this the honest first crossing of this method.
