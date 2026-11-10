---
type: formula
output: "[[Grid Availability BU Gap (%)]]"
excel_column: AR
kind: "calculated"
variables: ["[[Actual Grid Availability]]", "[[Expected Grid Availability]]"]
tags: [formula, grid-availability]
---

# Grid Availability BU Gap (%) (formula)

Produces [[Grid Availability BU Gap (%)]]  |  Excel column AR  |  Group: Grid Availability

## Math

$$
\delta_{grid} = \frac{A_{grid}^{act} - A_{grid}^{exp}}{A_{grid}^{exp}}
$$

## In plain English

(Actual - expected) / expected grid availability.

## Inputs

- [[Actual Grid Availability]] (ratio)
- [[Expected Grid Availability]] (ratio)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =([Actual Grid Availability]-[Expected Grid Availability])/[Expected Grid Availability]
> ```
