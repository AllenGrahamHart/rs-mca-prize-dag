# Compiler to the weighted leaf

For every integer `m>=0`,

```text
(m-35)_+ <= m(m-1)/138.
```

For `m<=35` this is immediate. For `m>=36`, it is equivalent to

```text
m(m-1)-138(m-35)=(m-69)(m-70)>=0,
```

which holds for integer `m` (including the two equality cases). Therefore

```text
X_35 <= M_21/138 <= 69n^2/138=n^2/2.
```
