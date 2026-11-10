---
type: formula
output: "[[Production Gap to BU (MWh)]]"
excel_column: T
kind: "calculated"
variables: ["[[Actual Production (MWh)]]", "[[2026 HQ BU Prod (MWh)]]"]
tags: [formula, production-vs-budget]
---

# Production Gap to BU [MWh] (formula)

Produces [[Production Gap to BU (MWh)]]  |  Excel column T  |  Group: Production vs Budget

## Math

$$
\Delta E_{BU} = E_{act} - E_{BU}^{HQ}
$$

## In plain English

Actual production minus HQ budget production.

## Inputs

- [[Actual Production (MWh)]] (MWh)
- [[2026 HQ BU Prod (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Actual Production [MWh]]-[2026 HQ BU Prod [MWh]]
> ```
