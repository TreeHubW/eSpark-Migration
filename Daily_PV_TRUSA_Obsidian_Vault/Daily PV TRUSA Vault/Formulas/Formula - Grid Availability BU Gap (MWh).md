---
type: formula
output: "[[Grid Availability BU Gap (MWh)]]"
excel_column: AQ
kind: "calculated"
variables: ["[[Grid Availability BU Gap (%)]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, grid-availability]
---

# Grid Availability BU Gap [MWh] (formula)

Produces [[Grid Availability BU Gap (MWh)]]  |  Excel column AQ  |  Group: Grid Availability

## Math

$$
\Delta E_{grid} = \delta_{grid} \cdot E_{exp}^{POA}
$$

## In plain English

Grid availability gap % times the energy potential.

## Inputs

- [[Grid Availability BU Gap (%)]] (ratio)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Grid Availability BU Gap (%)]*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]
> ```
