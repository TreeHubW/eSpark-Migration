---
type: formula
output: "[[Week PH]]"
excel_column: H
kind: "calculated"
variables: ["[[Date]]"]
tags: [formula, identity-calendar]
---

# Week PH (formula)

Produces [[Week PH]]  |  Excel column H  |  Group: Identity & Calendar

## In plain English

WEEKNUM(Date, 1): week number with Sunday as the first day of the week. The workbook does not say what 'PH' stands for.

## Inputs

- [[Date]] (date)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =TEXT(WEEKNUM([Date],1),"00")
> ```
