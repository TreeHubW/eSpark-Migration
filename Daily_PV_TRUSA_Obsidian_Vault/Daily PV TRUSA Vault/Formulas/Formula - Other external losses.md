---
type: formula
output: "[[Other external losses]]"
excel_column: AW
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, expected-energy-performance-ratio]
---

# Other external losses (formula)

Produces [[Other external losses]]  |  Excel column AW  |  Group: Expected Energy & Performance Ratio

## Math

$$
L_{ext} = \text{average of Other external losses for (site, month), from the monthly table}
$$

## In plain English

AVERAGEIFS on Site Name and Month over the monthly table.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `Other external losses`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =AVERAGEIFS(Monthly_techData[Other external losses],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])
> ```
