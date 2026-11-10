---
type: source
tags: [source]
---

# Site Data Source Map

Several daily variables are read from each site's own data sheet through a long nested IF on Site Name. This table shows, for each site, which sheet column or table column each variable comes from. It is generated directly from the formulas.

| Site | [[Actual Production (MWh)]] | [[Actual Irradiation GPOA (kWh-m2)]] | [[Actual Irradiation GHI (kWh-m2)]] | [[Actual Plant Availability]] | [[Grid Availability Loss (MWh)]] | [[Substation AVL (%)]] | [[Inverter AVL (%)]] | [[Combiner AVL (%)]] | [[Tracker AVL(%)]] |
|---|---|---|---|---|---|---|---|---|---|
| Oberon 1A | `OberonData!B:B` | `Oberon[Irradiance]` | `Oberon[GHI (kW/m2/day)]` | `Oberon[Availability (%)]` | `Oberon[Economic Curtailed Energy (MWh)]` | `Oberon[Substation AVL (%)]` | `Oberon[Inverter AVL (%)]` | `Oberon[Combiner AVL (%)]` | `Oberon[Tracker AVL(%)]` |
| Rayos del Sol | `RayosData!B:B` | `RayosData!C:C` | `RayosData!D:D` | `RayosData!N:N` | `Rayos[Economic Curtailed Energy (MWh)]` | `Rayos[Substation AVL (%)]` | `Rayos[Inverter AVL (%)]` | `Rayos[Combiner AVL (%)]` | `Rayos[Tracker AVL(%)]` |
| Ellis | `EllisData!B:B` | `EllisData!C:C` | `EllisData!D:D` | `EllisData!N:N` | `Ellis[Economic Curtailed Energy (MWh)]` | `Ellis[Substation AVL (%)]` | `Ellis[Inverter AVL (%)]` | `Ellis[Combiner AVL (%)]` | `Ellis[Tracker AVL(%)]` |
| Myrtle | `Myrtle[Myrtle Production (MWh)]` | `Myrtle[Irradiation (kW/m2/day)]` | `Myrtle[GHI (kW/m2/day)]` | `Myrtle[Availability (%)]` | `Myrtle[Economic Curtailed Energy (MWh)]` | `Myrtle[Substation AVL (%)]` | `Myrtle[Inverter AVL (%)]` | `Myrtle[Combiner AVL (%)]` | `Myrtle[Tracker AVL(%)]` |
| Danish | `Danish[Danish Production (MWh)]` | `Danish[Irradiation (kW/m2/day)]` | `Danish[GHI (kW/m2/day)]` | `DanishData!Q:Q` | `Danish[Economic Curtailed Energy (MWh)]` | `Danish[Substation AVL (%)]` | `Danish[Inverter AVL (%)]` | `Danish[Combiner AVL (%)]` | `Danish[Tracker AVL(%)]` |
| Skysol | `Skysol[Production (MWh)]` | `Skysol[Irradiation (kW/m2/day)]` | `Skysol[GHI (kW/m2/day)]` | `SkysolData!Q:Q` | `Skysol[Economic Curtailed Energy (MWh)]` | `Skysol[Substation AVL (%)]` | `Skysol[Inverter AVL (%)]` | `Skysol[Combiner AVL (%)]` | `Skysol[Tracker AVL(%)]` |
| Cottonwood | `CottonwoodData!E:E` | `CottonwoodData!F:F` | `CottonwoodData!G:G` | `CottonwoodData!Q:Q` | `CottonwoodData!N:N` | `CottonwoodData!I:I` | `CottonwoodData!J:J` | `CottonwoodData!K:K` | `CottonwoodData!L:L` |
| Big Sky | `BigSkyData!E:E` | `BigSkyData!F:F` | `BigSkyData!G:G` | `BigSkyData!Q:Q` | `BigSkyData!N:N` | `BigSkyData!I:I` | `BigSkyData!J:J` | `BigSkyData!K:K` | `BigSkyData!L:L` |
| Montpelier | `MontpelierData!E:E` | `MontpelierData!F:F` | `MontpelierData!G:G` | `MontpelierData!Q:Q` | `MontpelierData!N:N` | `MontpelierData!I:I` | `MontpelierData!J:J` | `MontpelierData!K:K` | `MontpelierData!L:L` |
| Clinton | `ClintonData!E:E` | `ClintonData!F:F` | `ClintonData!G:G` | `ClintonData!Q:Q` | `ClintonData!N:N` | `ClintonData!I:I` | `ClintonData!J:J` | `ClintonData!K:K` | `ClintonData!L:L` |
| Hill | `Hill1Data!E:E` | `Hill1Data!F:F` | `Hill1Data!G:G` | `Hill1Data!Q:Q` | `Hill1Data!N:N` | `Hill1Data!I:I` | `Hill1Data!J:J` | `Hill1Data!K:K` | `Hill1Data!L:L` |
| Brazoria | `BrazoriaData!E:E` | `BrazoriaData!F:F` | `BrazoriaData!G:G` | `BrazoriaData!Q:Q` | `BrazoriaData!N:N` | `BrazoriaData!I:I` | `BrazoriaData!J:J` | `BrazoriaData!K:K` | `BrazoriaData!L:L` |
| Hill 2 | `Hill2Data!E:E` | `Hill2Data!F:F` | `Hill2Data!G:G` | `Hill2Data!Q:Q` | `Hill2Data!N:N` | `Hill2Data!I:I` | `Hill2Data!J:J` | `Hill2Data!K:K` | `Hill2Data!L:L` |

A site name that is not in the nested IF returns `!`.
