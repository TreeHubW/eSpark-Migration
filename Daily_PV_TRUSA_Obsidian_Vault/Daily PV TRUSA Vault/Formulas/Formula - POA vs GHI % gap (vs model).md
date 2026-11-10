---
type: formula
output: "[[POA vs GHI % gap (vs model)]]"
excel_column: AF
kind: "calculated"
variables: ["[[Irradiation Gap (%)]]", "[[GHI Gap (%)]]"]
tags: [formula, irradiation]
---

# POA vs GHI % gap (vs model) (formula)

Produces [[POA vs GHI % gap (vs model)]]  |  Excel column AF  |  Group: Irradiation

## Math

$$
\delta_{POA-GHI} = \delta_{irr} - \delta_{GHI}
$$

## In plain English

POA gap % minus GHI gap %.

## Inputs

- [[Irradiation Gap (%)]] (ratio)
- [[GHI Gap (%)]] (ratio)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Irradiation Gap (%)]-[GHI Gap (%)]
> ```
