---
type: formula
output: "[[BoS Loss (MWh)]]"
excel_column: BK
kind: "calculated"
variables: ["[[Substation AVL (%)]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, availability-loss-breakdown]
---

# BoS Loss (MWh) (formula)

Produces [[BoS Loss (MWh)]]  |  Excel column BK  |  Group: Availability & Loss Breakdown

## Math

$$
L_{BoS} = \left(A_{sub} - 1\right) \cdot E_{exp}^{POA}
$$

## In plain English

Availability minus one (a negative number when availability is below 100%) times the energy baseline.

## Inputs

- [[Substation AVL (%)]] (ratio)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =([Substation AVL (%)]-1)*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]
> ```
