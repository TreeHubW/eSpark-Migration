---
type: formula
output: "[[Residual BU Gap (MWh)]]"
excel_column: BB
kind: "calculated"
variables: ["[[Production Gap to BU (MWh)]]", "[[HQ vs Tech BU Gap (MWh)]]", "[[Irradiation Gap (MWh)]]", "[[Availability BU Gap (MWh)]]", "[[Grid Availability BU Gap (MWh)]]", "[[Plant Performance (PR) gap (MWh)]]"]
tags: [formula, residual-gap]
---

# Residual BU Gap [MWh] (formula)

Produces [[Residual BU Gap (MWh)]]  |  Excel column BB  |  Group: Residual Gap

## Math

[[Residual BU Gap (MWh)]] = [[Production Gap to BU (MWh)]] − ([[HQ vs Tech BU Gap (MWh)]] + [[Irradiation Gap (MWh)]] + [[Availability BU Gap (MWh)]] + [[Grid Availability BU Gap (MWh)]] + [[Plant Performance (PR) gap (MWh)]])

## In plain English

Total production gap minus the sum of the five explained components. See [[Gap Bridge]].

## Inputs

- [[Production Gap to BU (MWh)]] (MWh)
- [[HQ vs Tech BU Gap (MWh)]] (MWh)
- [[Irradiation Gap (MWh)]] (MWh)
- [[Availability BU Gap (MWh)]] (MWh)
- [[Grid Availability BU Gap (MWh)]] (MWh)
- [[Plant Performance (PR) gap (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Production Gap to BU [MWh]]-([HQ vs Tech BU Gap [MWh]]+([Irradiation Gap [MWh]])+[Availability BU Gap [MWh]]+[Grid Availability BU Gap [MWh]]+[Plant Performance (PR) gap [MWh]])
> ```
