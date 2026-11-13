---
type: formula
output: "[[Expected Grid Availability]]"
excel_column: AO
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, grid-availability]
---

# Expected Grid Availability (formula)

Produces [[Expected Grid Availability]]  |  Excel column AO  |  Group: Grid Availability

## Math

[[Expected Grid Availability]] = average of the monthly table value for ([[Site Name]], [[Month]])

## In plain English

AVERAGEIFS on Site Name and Month over the monthly table.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `Expected Grid Availability`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =AVERAGEIFS(Monthly_techData[Expected Grid Availability],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])
> ```
