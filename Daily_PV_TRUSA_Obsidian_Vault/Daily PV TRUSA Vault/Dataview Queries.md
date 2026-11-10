---
type: utility
---

# Dataview Queries

These need the free **Dataview** community plugin (Settings > Community plugins). They update automatically as you edit notes.

## Glossary of all variables

```dataview
TABLE column, symbol, units, kind, group
FROM "Variables"
SORT file.name ASC
```

## Variables by group

```dataview
TABLE WITHOUT ID group AS Group, length(rows) AS Count, rows.file.link AS Variables
FROM "Variables"
GROUP BY group
```

## All formulas that use a given variable (change the name)

```dataview
LIST
FROM "Formulas"
WHERE contains(variables, [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]])
```

## Formulas with the most inputs

```dataview
TABLE length(variables) AS Inputs, output
FROM "Formulas"
SORT length(variables) DESC
LIMIT 10
```

## Variables with no formula (inputs / not populated)

```dataview
LIST
FROM "Variables"
WHERE kind = "input" OR kind = "not populated"
```
