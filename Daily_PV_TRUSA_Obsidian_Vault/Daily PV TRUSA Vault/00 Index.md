---
type: index
---

# Daily PV TRUSA: Formula Documentation

Documents the **Daily PV TRUSA** sheet (table `Daily_techData`). Each row is one site on one day. The sheet compares actual solar production to budget and breaks the difference into causes.

## How to read this vault

- **Variables/** has one note per column: symbol, units, definition.
- **Formulas/** has one note per calculated column: the math, a plain-English version, its inputs (linked), and the original Excel formula.
- **Sources/** documents where lookups come from: [[Monthly_techData]] and the [[Site Data Source Map]].
- [[Flow Diagrams]] has the dependency charts.
- [[Dataview Queries]] has live tables (needs the Dataview plugin).

## Where the data comes from

1. **Keys you type:** Site Name and Date.
2. **Monthly lookups** from [[Monthly_techData]]: capacity, budget, expected irradiation, expected availability and PR. Budget and irradiation are divided by days in the month.
3. **Daily pulls** from each site's data sheet: production, irradiation, availability, curtailment.
4. **Calculations** turn those into gaps in MWh

## Tips

- Open the **Graph view** (Ctrl/Cmd + G). Variables are blue, formulas orange, sources purple.
- On any variable note, open **Backlinks** to see every formula that uses it.
- Click a variable then use the **Local graph** to see just its neighborhood.

## All variables

| Group | Col | Variable | Units | Kind | Formula |
|---|---|---|---|---|---|
| Identity & Calendar | C | [[Site Name]] | text | input | - |
| Identity & Calendar | D | [[Date]] | date | input | - |
| Identity & Calendar | E | [[Day]] | text, 2 digits | calculated | [[Formula - Day]] |
| Identity & Calendar | F | [[Month]] | text, 2 digits | calculated | [[Formula - Month]] |
| Identity & Calendar | G | [[Week]] | text, 2 digits | calculated | [[Formula - Week]] |
| Identity & Calendar | H | [[Week PH]] | text, 2 digits | calculated | [[Formula - Week PH]] |
| Identity & Calendar | I | [[Portfolio]] | text | input | - |
| Identity & Calendar | J | [[COD]] | date | not populated | - |
| Capacity | K | [[MWac]] | MW | lookup | [[Formula - MWac]] |
| Capacity | L | [[MWp]] | MWp | lookup | [[Formula - MWp]] |
| Capacity | M | [[Actual MWp]] | MWp | lookup | [[Formula - Actual MWp]] |
| Capacity | N | [[Total Shares]] | shares | not populated | - |
| Production vs Budget | O | [[2026 HQ BU Prod (MWh)]] | MWh | lookup | [[Formula - 2026 HQ BU Prod (MWh)]] |
| Production vs Budget | P | [[2026 techBU Prod (MWh)]] | MWh | lookup | [[Formula - 2026 techBU Prod (MWh)]] |
| Production vs Budget | Q | [[Actual Production (MWh)]] | MWh | site-data pull | [[Formula - Actual Production (MWh)]] |
| Production vs Budget | R | [[Production anticipated COD (MWh)]] | MWh | not populated | - |
| Production vs Budget | S | [[Production Delayed COD( MWh)]] | MWh | not populated | - |
| Production vs Budget | T | [[Production Gap to BU (MWh)]] | MWh | calculated | [[Formula - Production Gap to BU (MWh)]] |
| Production vs Budget | U | [[Production Gap to BU (%)]] | ratio | calculated | [[Formula - Production Gap to BU (%)]] |
| Production vs Budget | V | [[Prod Gap Comment]] | text | input | - |
| Production vs Budget | W | [[Expected Prod - BU Assumptions (MWh)]] | MWh | calculated | [[Formula - Expected Prod - BU Assumptions (MWh)]] |
| Production vs Budget | X | [[HQ vs Tech BU Gap (MWh)]] | MWh | calculated | [[Formula - HQ vs Tech BU Gap (MWh)]] |
| Irradiation | Y | [[Expected Irradiation P50 POA (kWh-m2)]] | kWh/m2 per day | lookup | [[Formula - Expected Irradiation P50 POA (kWh-m2)]] |
| Irradiation | Z | [[Actual Irradiation GPOA (kWh-m2)]] | kWh/m2 per day | site-data pull | [[Formula - Actual Irradiation GPOA (kWh-m2)]] |
| Irradiation | AA | [[Irradiation Gap (MWh)]] | MWh | calculated | [[Formula - Irradiation Gap (MWh)]] |
| Irradiation | AB | [[Irradiation Gap (%)]] | ratio | calculated | [[Formula - Irradiation Gap (%)]] |
| Irradiation | AC | [[Model Irradiation GHI (kWh-m2)]] | kWh/m2 per day | lookup | [[Formula - Model Irradiation GHI (kWh-m2)]] |
| Irradiation | AD | [[Actual Irradiation GHI (kWh-m2)]] | kWh/m2 per day | site-data pull | [[Formula - Actual Irradiation GHI (kWh-m2)]] |
| Irradiation | AE | [[GHI Gap (%)]] | ratio | calculated | [[Formula - GHI Gap (%)]] |
| Irradiation | AF | [[POA vs GHI % gap (vs model)]] | ratio | calculated | [[Formula - POA vs GHI % gap (vs model)]] |
| Temperature | AG | [[Module temp coef (%-°C)]] | %/°C | not populated | - |
| Temperature | AI | [[Actual avg module temp (°C)]] | °C | not populated | - |
| Temperature | AJ | [[Temp gap (MWh)]] | MWh | not populated | - |
| Plant Availability | AK | [[Expected Plant Availability]] | ratio | lookup | [[Formula - Expected Plant Availability]] |
| Plant Availability | AL | [[Actual Plant Availability]] | ratio | site-data pull | [[Formula - Actual Plant Availability]] |
| Plant Availability | AM | [[Availability BU Gap (MWh)]] | MWh | calculated | [[Formula - Availability BU Gap (MWh)]] |
| Plant Availability | AN | [[Availability BU Gap (%)]] | ratio | calculated | [[Formula - Availability BU Gap (%)]] |
| Grid Availability | AO | [[Expected Grid Availability]] | ratio | lookup | [[Formula - Expected Grid Availability]] |
| Grid Availability | AP | [[Actual Grid Availability]] | ratio | calculated | [[Formula - Actual Grid Availability]] |
| Grid Availability | AQ | [[Grid Availability BU Gap (MWh)]] | MWh | calculated | [[Formula - Grid Availability BU Gap (MWh)]] |
| Grid Availability | AR | [[Grid Availability BU Gap (%)]] | ratio | calculated | [[Formula - Grid Availability BU Gap (%)]] |
| Grid Availability | AS | [[Grid Availability Loss (MWh)]] | MWh | site-data pull | [[Formula - Grid Availability Loss (MWh)]] |
| Expected Energy & Performance Ratio | AT | [[Expected Energy - Controllable (MWh)]] | MWh | calculated | [[Formula - Expected Energy - Controllable (MWh)]] |
| Expected Energy & Performance Ratio | AU | [[Production @100% avail]] | MWh | calculated | [[Formula - Production @100% avail]] |
| Expected Energy & Performance Ratio | AV | [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] | MWh | calculated | [[Formula - Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] |
| Expected Energy & Performance Ratio | AW | [[Other external losses]] | ratio | lookup | [[Formula - Other external losses]] |
| Expected Energy & Performance Ratio | AX | [[Expected Performance Ratio (PR)]] | ratio | lookup | [[Formula - Expected Performance Ratio (PR)]] |
| Expected Energy & Performance Ratio | AY | [[Plant Performance (PR) Act]] | ratio | calculated | [[Formula - Plant Performance (PR) Act]] |
| Expected Energy & Performance Ratio | AZ | [[Plant Performance (PR) gap (MWh)]] | MWh | calculated | [[Formula - Plant Performance (PR) gap (MWh)]] |
| Expected Energy & Performance Ratio | BA | [[Plant Performance (PR) gap %]] | ratio | calculated | [[Formula - Plant Performance (PR) gap %]] |
| Residual Gap | BB | [[Residual BU Gap (MWh)]] | MWh | calculated | [[Formula - Residual BU Gap (MWh)]] |
| Residual Gap | BC | [[Residual gap %]] | ratio | calculated | [[Formula - Residual gap %]] |
| Availability & Loss Breakdown | BF | [[Substation AVL (%)]] | ratio | site-data pull | [[Formula - Substation AVL (%)]] |
| Availability & Loss Breakdown | BG | [[Inverter AVL (%)]] | ratio | site-data pull | [[Formula - Inverter AVL (%)]] |
| Availability & Loss Breakdown | BH | [[Combiner AVL (%)]] | ratio | site-data pull | [[Formula - Combiner AVL (%)]] |
| Availability & Loss Breakdown | BI | [[Tracker AVL(%)]] | ratio | site-data pull | [[Formula - Tracker AVL(%)]] |
| Availability & Loss Breakdown | BJ | [[Plant Availability Loss (MWh)]] | MWh | calculated | [[Formula - Plant Availability Loss (MWh)]] |
| Availability & Loss Breakdown | BK | [[BoS Loss (MWh)]] | MWh | calculated | [[Formula - BoS Loss (MWh)]] |
| Availability & Loss Breakdown | BL | [[Inverter Loss (MWh)]] | MWh | calculated | [[Formula - Inverter Loss (MWh)]] |
| Availability & Loss Breakdown | BM | [[DC Loss (MWh)]] | MWh | calculated | [[Formula - DC Loss (MWh)]] |
| Availability & Loss Breakdown | BN | [[Tracker Loss (MWh)]] | MWh | calculated | [[Formula - Tracker Loss (MWh)]] |
| Availability & Loss Breakdown | BO | [[Residual Loss (MWh)]] | MWh | calculated | [[Formula - Residual Loss (MWh)]] |
| Comments & QA | BD | [[PR Gap Comments]] | text | input | - |
| Comments & QA | BE | [[Residual Gap Comments]] | text | input | - |
| Comments & QA | BP | [[Loss Comments]] | ratio | calculated | [[Formula - Loss Comments]] |
| Comments & QA | BQ | [[Data QA]] | TRUE/FALSE | calculated | [[Formula - Data QA]] |

Columns B (`#`, a row counter) and AH (`Column1`, a placeholder) were not documented.
