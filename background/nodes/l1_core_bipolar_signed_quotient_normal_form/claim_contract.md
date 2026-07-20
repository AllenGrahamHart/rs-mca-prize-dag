# Claim contract - L1 core bipolar signed-quotient normal form

## Inputs

- a core partition into complete fibers of one monic polynomial `P`;
- one exact defect set `D`;
- dense ties assigned to the sparse side.

## Output

A unique signed quotient presentation

```text
F_D L_H=L_S product_(a in A_+)(P-a),
deg L_H+deg L_S=p_core(D).
```

## Consumer rule

Consumers may replace growing symmetric core polarity by growing total signed
mark degree in this exact identity. They may not infer periodic agreement,
bounded signed-mark multiplicity, or cross-chart ownership.

## Falsifier

Two canonical triples for one `D`, failure of the locator identity, mark sets
with a common root, or total mark degree different from `p_core(D)`.

