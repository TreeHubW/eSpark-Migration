---
type: formula
output: "[[MWp]]"
excel_column: L
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, capacity]
---

# MWp (formula)

Produces [[MWp]]  |  Excel column L  |  Group: Capacity

## Math

$$
P_{p} = \text{MWp for (site, month), from the monthly table}
$$

## In plain English

SUMIFS on Site Name and Month over the monthly table's MWp column.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `MWp`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =SUMIFS(Monthly_techData[MWp],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])
> ```
