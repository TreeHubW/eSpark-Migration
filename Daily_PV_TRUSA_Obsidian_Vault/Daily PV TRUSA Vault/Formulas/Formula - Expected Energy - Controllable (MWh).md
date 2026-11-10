---
type: formula
output: "[[Expected Energy - Controllable (MWh)]]"
excel_column: AT
kind: "calculated"
variables: ["[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]", "[[Grid Availability Loss (MWh)]]"]
tags: [formula, expected-energy-performance-ratio]
---

# Expected Energy - Controllable (MWh) (formula)

Produces [[Expected Energy - Controllable (MWh)]]  |  Excel column AT  |  Group: Expected Energy & Performance Ratio

## Math

$$
E_{ctrl} = E_{exp}^{POA} + L_{grid}
$$

## In plain English

Expected energy at actual irradiation plus grid loss (a negative number).

## Inputs

- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)
- [[Grid Availability Loss (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]+[Grid Availability Loss [MWh]]
> ```
