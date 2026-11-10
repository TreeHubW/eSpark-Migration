---
type: formula
output: "[[Inverter AVL (%)]]"
excel_column: BG
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, availability-loss-breakdown]
---

# Inverter AVL (%) (formula)

Produces [[Inverter AVL (%)]]  |  Excel column BG  |  Group: Availability & Loss Breakdown

## Math

$$
A_{inv} = \text{value from the site's own data sheet on the matching Date}
$$

## In plain English

Nested IF on Site Name, AVERAGEIFS on Date, wrapped in IFERROR. See [[Site Data Source Map]].

## Inputs

- [[Site Name]] (text)
- [[Date]] (date)

## Data sources

- [[Site Data Source Map]]

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IFERROR(IF([Site Name]="Oberon 1A",AVERAGEIFS(Oberon[Inverter AVL (%)],Oberon[Date],[Date]),IF([Site Name]="Rayos del Sol",AVERAGEIFS(Rayos[Inverter AVL (%)],Rayos[Date],[Date]),IF([Site Name]="Ellis",AVERAGEIFS(Ellis[Inverter AVL (%)],Ellis[Date],[Date]),IF([Site Name]="Myrtle",AVERAGEIFS(Myrtle[Inverter AVL (%)],Myrtle[Date],[Date]),IF([Site Name]="Danish",AVERAGEIFS(Danish[Inverter AVL (%)],Danish[Date],[Date]),IF([Site Name]="Skysol",AVERAGEIFS(Skysol[Inverter AVL (%)],Skysol[Date],[Date]),IF([Site Name]="Hill",AVERAGEIFS(Hill1Data!J:J,Hill1Data!A:A,[Date]),IF([Site Name]="Big Sky",AVERAGEIFS(BigSkyData!J:J,BigSkyData!B:B,[Date]),IF([Site Name]="Cottonwood",AVERAGEIFS(CottonwoodData!J:J,CottonwoodData!A:A,[Date]),IF([Site Name]="Clinton",AVERAGEIFS(ClintonData!J:J,ClintonData!B:B,[Date]),IF([Site Name]="Brazoria",AVERAGEIFS(BrazoriaData!J:J,BrazoriaData!B:B,[Date]),IF([Site Name]="Montpelier",AVERAGEIFS(MontpelierData!J:J,MontpelierData!B:B,[Date]),IF([Site Name]="Hill 2",AVERAGEIFS(Hill2Data!J:J,Hill2Data!B:B,[Date]),"!"))))))))))))),"!")
> ```
