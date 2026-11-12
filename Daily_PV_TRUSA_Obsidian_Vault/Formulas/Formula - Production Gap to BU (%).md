---
type: formula
output: "[[Production Gap to BU (%)]]"
excel_column: U
kind: "calculated"
variables: ["[[Actual Production (MWh)]]", "[[2026 HQ BU Prod (MWh)]]"]
tags: [formula, production-vs-budget]
---

# Production Gap to BU (%) (formula)

Produces [[Production Gap to BU (%)]]  |  Excel column U  |  Group: Production vs Budget

## Math

[[Production Gap to BU (%)]] =

- −1, if [[Actual Production (MWh)]] = 0
- ([[Actual Production (MWh)]] − [[2026 HQ BU Prod (MWh)]]) ÷ [[2026 HQ BU Prod (MWh)]], otherwise

## In plain English

Gap divided by budget. When actual production is zero it returns -1 (i.e. -100%) instead of calculating.

## Inputs

- [[Actual Production (MWh)]] (MWh)
- [[2026 HQ BU Prod (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IF([Actual Production [MWh]]=0, -1,(([Actual Production [MWh]]-[2026 HQ BU Prod [MWh]])/[2026 HQ BU Prod [MWh]]))
> ```
