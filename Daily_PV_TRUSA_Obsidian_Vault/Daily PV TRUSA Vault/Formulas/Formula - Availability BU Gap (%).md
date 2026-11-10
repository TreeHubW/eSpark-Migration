---
type: formula
output: "[[Availability BU Gap (%)]]"
excel_column: AN
kind: "calculated"
variables: ["[[Actual Plant Availability]]", "[[Expected Plant Availability]]"]
tags: [formula, plant-availability]
---

# Availability BU Gap (%) (formula)

Produces [[Availability BU Gap (%)]]  |  Excel column AN  |  Group: Plant Availability

## Math

$$
\delta_{avail} = \frac{A_{plant}^{act} - A_{plant}^{exp}}{A_{plant}^{exp}}
$$

## In plain English

(Actual - expected) / expected plant availability.

## Inputs

- [[Actual Plant Availability]] (ratio)
- [[Expected Plant Availability]] (ratio)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =([Actual Plant Availability]-[Expected Plant Availability])/[Expected Plant Availability]
> ```
