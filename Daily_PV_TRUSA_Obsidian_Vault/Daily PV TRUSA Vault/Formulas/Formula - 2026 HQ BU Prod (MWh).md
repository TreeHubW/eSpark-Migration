---
type: formula
output: "[[2026 HQ BU Prod (MWh)]]"
excel_column: O
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]", "[[Date]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, production-vs-budget]
---

# 2026 HQ BU Prod [MWh] (formula)

Produces [[2026 HQ BU Prod (MWh)]]  |  Excel column O  |  Group: Production vs Budget

## Math

$$
E_{BU}^{HQ} = \frac{\text{monthly value for (site, month)}}{d_m}, \qquad d_m = \text{days in the month}
$$

## In plain English

Monthly '2026 HQ BU Prod' looked up by (site, month), divided by the number of days in that month.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)
- [[Date]] (date)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `2026 HQ BU Prod [MWh]`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =SUMIFS(Monthly_techData[2026 HQ BU Prod [MWh]],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])/DAY(EOMONTH(D5,0))
> ```
