---
type: formula
output: "[[HQ vs Tech BU Gap (MWh)]]"
excel_column: X
kind: "calculated"
variables: ["[[2026 techBU Prod (MWh)]]", "[[2026 HQ BU Prod (MWh)]]"]
tags: [formula, production-vs-budget]
---

# HQ vs Tech BU Gap [MWh] (formula)

Produces [[HQ vs Tech BU Gap (MWh)]]  |  Excel column X  |  Group: Production vs Budget

## Math

[[HQ vs Tech BU Gap (MWh)]] = [[2026 techBU Prod (MWh)]] − [[2026 HQ BU Prod (MWh)]]

## In plain English

Tech BU budget minus HQ BU budget.

## Inputs

- [[2026 techBU Prod (MWh)]] (MWh)
- [[2026 HQ BU Prod (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[2026 techBU Prod [MWh]]-[2026 HQ BU Prod [MWh]]
> ```
