---
type: formula
output: "[[Model Irradiation GHI (kWh-m2)]]"
excel_column: AC
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]", "[[Date]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, irradiation]
---

# Model Irradiation GHI [kWh/m2] (formula)

Produces [[Model Irradiation GHI (kWh-m2)]]  |  Excel column AC  |  Group: Irradiation

## Math

[[Model Irradiation GHI (kWh-m2)]] = monthly value for ([[Site Name]], [[Month]]) ÷ days in that month

## In plain English

Monthly expected GHI looked up by (site, month), divided by days in the month.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)
- [[Date]] (date)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `Expected Irradiation GHI [kWh/m2]`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =SUMIFS(Monthly_techData[Expected Irradiation GHI [kWh/m2]],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])/DAY(EOMONTH(D5,0))
> ```
