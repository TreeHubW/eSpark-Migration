---
type: formula
output: "[[MWac]]"
excel_column: K
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, capacity]
---

# MWac (formula)

Produces [[MWac]]  |  Excel column K  |  Group: Capacity

## Math

[[MWac]] = MWac for ([[Site Name]], [[Month]]), from the monthly table

## In plain English

SUMIFS on Site Name and Month over the monthly table's MWac column.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `MWac`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =SUMIFS(Monthly_techData[MWac],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])
> ```
