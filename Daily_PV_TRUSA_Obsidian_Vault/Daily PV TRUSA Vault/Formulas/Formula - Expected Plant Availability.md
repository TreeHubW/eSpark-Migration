---
type: formula
output: "[[Expected Plant Availability]]"
excel_column: AK
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, plant-availability]
---

# Expected Plant Availability (formula)

Produces [[Expected Plant Availability]]  |  Excel column AK  |  Group: Plant Availability

## Math

$$
A_{plant}^{exp} = \text{average of Expected Plant Availability for (site, month), from the monthly table}
$$

## In plain English

AVERAGEIFS on Site Name and Month over the monthly table.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `Expected Plant Availability`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =AVERAGEIFS(Monthly_techData[Expected Plant Availability],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])
> ```
