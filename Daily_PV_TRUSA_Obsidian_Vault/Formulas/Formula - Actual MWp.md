---
type: formula
output: "[[Actual MWp]]"
excel_column: M
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, capacity]
---

# Actual MWp (formula)

Produces [[Actual MWp]]  |  Excel column M  |  Group: Capacity

## Math

[[Actual MWp]] = Actual MWp for ([[Site Name]], [[Month]]), from the monthly table

## In plain English

SUMIFS on Site Name and Month over the monthly table's Actual MWp column.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `Actual MWp`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =SUMIFS(Monthly_techData[Actual MWp],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])
> ```
