---
type: formula
output: "[[Grid Availability Loss (MWh)]]"
excel_column: AS
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, grid-availability]
---

# Grid Availability Loss [MWh] (formula)

Produces [[Grid Availability Loss (MWh)]]  |  Excel column AS  |  Group: Grid Availability

## Math

[[Grid Availability Loss (MWh)]] = −(average of the site's curtailed energy on the matching [[Date]])

## In plain English

Averages the site's Economic Curtailed Energy for the Date and flips the sign. IFERROR returns '!' on failure. See [[Site Data Source Map]].

## Inputs

- [[Site Name]] (text)
- [[Date]] (date)

## Data sources

- [[Site Data Source Map]]

> [!warning] The sign flip means a curtailment of 5 MWh shows as -5.

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =-IFERROR(IF([Site Name]="Oberon 1A",AVERAGEIFS(Oberon[Economic Curtailed Energy (MWh)],Oberon[Date],[Date]),IF([Site Name]="Rayos del Sol",AVERAGEIFS(Rayos[Economic Curtailed Energy (MWh)],Rayos[Date],[Date]),IF([Site Name]="Ellis",AVERAGEIFS(Ellis[Economic Curtailed Energy (MWh)],Ellis[Date],[Date]),IF([Site Name]="Myrtle",AVERAGEIFS(Myrtle[Economic Curtailed Energy (MWh)],Myrtle[Date],[Date]),IF([Site Name]="Danish",AVERAGEIFS(Danish[Economic Curtailed Energy (MWh)],Danish[Date],[Date]),IF([Site Name]="Skysol",AVERAGEIFS(Skysol[Economic Curtailed Energy (MWh)],Skysol[Date],[Date]),IF([Site Name]="Hill",AVERAGEIFS(Hill1Data!N:N,Hill1Data!A:A,[Date]),IF([Site Name]="Big Sky",AVERAGEIFS(BigSkyData!N:N,BigSkyData!B:B,[Date]),IF([Site Name]="Cottonwood",AVERAGEIFS(CottonwoodData!N:N,CottonwoodData!A:A,[Date]),IF([Site Name]="Clinton",AVERAGEIFS(ClintonData!N:N,ClintonData!B:B,[Date]),IF([Site Name]="Brazoria",AVERAGEIFS(BrazoriaData!N:N,BrazoriaData!B:B,[Date]),IF([Site Name]="Montpelier",AVERAGEIFS(MontpelierData!N:N,MontpelierData!B:B,[Date]),IF([Site Name]="Hill 2",AVERAGEIFS(Hill2Data!N:N,Hill2Data!B:B,[Date]),"!"))))))))))))),"!")
> ```
