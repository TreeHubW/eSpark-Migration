---
type: formula
output: "[[2026 techBU Prod (MWh)]]"
excel_column: P
kind: "lookup"
variables: ["[[Site Name]]", "[[Month]]", "[[Date]]"]
sources: ["[[Monthly_techData]]"]
tags: [formula, production-vs-budget]
---

# 2026 techBU Prod [MWh] (formula)

Produces [[2026 techBU Prod (MWh)]]  |  Excel column P  |  Group: Production vs Budget

## Math

$$
E_{BU}^{tech} = \frac{\text{monthly value for (site, month)}}{d_m}, \qquad d_m = \text{days in the month}
$$

## In plain English

Monthly '2026 techBU Prod' looked up by (site, month), divided by the number of days in that month.

## Inputs

- [[Site Name]] (text)
- [[Month]] (text, 2 digits)
- [[Date]] (date)

## Data sources

- [[Monthly_techData]]
- Monthly column used: `2026 techBU Prod [MWh]`

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =SUMIFS(Monthly_techData[2026 techBU Prod [MWh]],Monthly_techData[Site Name],[Site Name],Monthly_techData[Month],[Month])/DAY(EOMONTH(D5,0))
> ```
