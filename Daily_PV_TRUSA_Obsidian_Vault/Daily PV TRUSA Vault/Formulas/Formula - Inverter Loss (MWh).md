---
type: formula
output: "[[Inverter Loss (MWh)]]"
excel_column: BL
kind: "calculated"
variables: ["[[Inverter AVL (%)]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, availability-loss-breakdown]
---

# Inverter Loss (MWh) (formula)

Produces [[Inverter Loss (MWh)]]  |  Excel column BL  |  Group: Availability & Loss Breakdown

## Math

$$
L_{inv} = \left(A_{inv} - 1\right) \cdot E_{exp}^{POA}
$$

## In plain English

Availability minus one (a negative number when availability is below 100%) times the energy baseline.

## Inputs

- [[Inverter AVL (%)]] (ratio)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =([Inverter AVL (%)]-1)*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]
> ```
