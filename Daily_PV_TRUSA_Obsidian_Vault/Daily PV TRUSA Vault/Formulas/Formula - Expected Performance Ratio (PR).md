---
type: formula
output: "[[Expected Performance Ratio (PR)]]"
excel_column: AX
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, expected-energy-performance-ratio]
---

# Expected Performance Ratio (PR) (formula)

Produces [[Expected Performance Ratio (PR)]]  |  Excel column AX  |  Group: Expected Energy & Performance Ratio

## Math

$$
PR_{exp} = \text{average of Expected Performance Ratio (PR) for (site, month), from the monthly table}
$$

## In plain English

AVERAGEIFS on Site Name and Month over the monthly table.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `Expected Performance Ratio (PR)`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =AVERAGEIFS(Monthly_techData[Expected Performance Ratio (PR)],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])
> ```
