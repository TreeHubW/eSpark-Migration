---
type: formula
output: "[[Expected Irradiation P50 POA (kWh-m2)]]"
excel_column: Y
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]", "[[Date]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, irradiation]
---

# Expected Irradiation P50 POA [kWh/m2] (formula)

Produces [[Expected Irradiation P50 POA (kWh-m2)]]  |  Excel column Y  |  Group: Irradiation

## Math

$$
H_{P50} = \frac{\text{monthly value for (site, month)}}{d_m}, \qquad d_m = \text{days in the month}
$$

## In plain English

Monthly expected P50 POA irradiation looked up by (site, month), divided by days in the month.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)
- [[Date]] (date)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `Expected Irradiation P50 POA [kWh/m2]`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =SUMIFS(Monthly_techData[Expected Irradiation P50 POA [kWh/m2]],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])/DAY(EOMONTH(D5,0))
> ```
