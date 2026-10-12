# Final technical validation — WeAct Black Pill STM32F411CEU6 V3.x

Date: 2026-10-12. Configuration revision: 1.1.

## Scope and source baseline

This review covers the complete WeAct MiniF4 module fitted with the STM32F411CEU6, not the bare UFQFPN48 MCU. The official source baseline is WeActStudio/WeActStudio.MiniSTM32F4x1 commit `05380f5c41f38eea8966a81c5acdeb7512cd909f`.

Local copies of the official schematic, mechanical drawing, pinout image, STEP, and release notes are retained under `validation/official_sources/` and `3dmodels/` for audit purposes, but are ignored by Git because the upstream repository does not declare a general redistribution license. The public CSV traceability matrix identifies every library pad against connector P1, P2, or P3 on page 1 of the official schematic.

## Mechanical geometry and coordinate transformation

The official STEP was evaluated with OpenCascade/CadQuery. The axes of cylindrical surfaces in the PCB solid were extracted. Forty-four holes with radius 0.45 mm correspond to the 44 electrical contacts. Other holes belong to the USB-C connector and are not carrier-board contacts.

Native STEP coordinates are:

- header rows: Y = 2.794 mm and Y = 18.009 mm;
- header X coordinates: X = 1.397 + n × 2.54 mm, where n = 0…19;
- SWD row: X = 45.872 mm and Y = 6.629 + n × 2.54 mm, where n = 0…3.

The STEP-to-KiCad transformation is:

```text
X_KiCad = X_STEP - 19.558
Y_KiCad = -Y_STEP + 9.1948
rotation = (0°, 0°, 0°)
scale = (1, 1, 1)
model offset = (-19.558, -9.1948, 0) mm
```

The Y-axis inversion converts the CAD coordinate convention to KiCad's footprint coordinate convention; it is not a mirror operation.

All 44 pad centers match the STEP hole centers within the 0.001 mm acceptance threshold. Maximum observed center error is 0.000566 mm. Row spacing is 15.2146 mm in the footprint and 15.215 mm in the STEP; the official drawing rounds it to 15.22 mm. This sub-micrometre difference is source-rounding, not a manufacturing discrepancy. Pitch is 2.54 mm in both sources.

The footprint outline is 52.8066 × 20.7786 mm, the STEP outline is 52.806999 × 20.778999 mm, and the official nominal dimensions are 52.81 × 20.78 mm. These rounded representations must not be described as mathematically identical.

In top view, USB-C is on the left; pad 1/PB12 is at the lower left; pad 40/5V is at the upper left; and SWD is on the right, with pad 41 at the bottom and pad 44 at the top. The simultaneous agreement of all 44 holes, the USB-C position, and schematic numbering excludes both mirroring and a 180° rotation.

## Electrical pin mapping

The library contains 44 unique pin and pad numbers, 1 through 44. No numbering changes were made during final validation.

Critical mappings:

| Pad | Signal |
|---:|---|
| 1 | PB12 |
| 20 | 3V3 |
| 21 | VBAT |
| 40 | 5V |
| 41 | 3V3 |
| 42 | SWDIO / PA13 |
| 43 | SWCLK / PA14 |
| 44 | GND |

See `validation/pinout_and_geometry.csv` for the complete 44-contact mapping and geometric comparison.

Special labels match the official schematic: PA11/USB_DM (named USB_DN by WeAct), PA12/USB_DP, PA4/FLASH_CS, PA5/FLASH_SCK, PA6/FLASH_MISO, PA7/FLASH_MOSI, PA0/USER_KEY through 330 Ω, PC13/LED, and PB2/BOOT1. NRST is exposed. BOOT0 exists only as an onboard pushbutton, so the library does not invent an external BOOT0 pad.

WeAct states that V3.1 retains V3.0 board size and pin definitions. The V3.1 STEP validates interface geometry for both versions; it does not certify V3.0 component placement or cosmetic details. No compatibility claim is made for clones or other revisions.

## Footprint conventions and fabrication checks

Pad 1 is the only rectangular pad. Pads 40 and 41 are circular while retaining their documented sizes and drills. A triangle and `1` label on both `F.SilkS` and `F.Fab` point only to pad 1. Rectangular features visible in the official STEP belong to the source board and do not define the carrier-footprint Pin 1 convention.

All 44 pads are plated through-hole with copper and solder mask on both sides. Standard pads use a 0.90 mm drill and 1.70 mm copper diameter. Pad 41 uses a 0.90 mm drill and 1.50 mm copper diameter. Corresponding annular rings are 0.40 mm and 0.30 mm. Minimum copper-to-copper gap is 0.84 mm.

No local clearance override is imposed; fabrication constraints are controlled by the consuming project. The closed rectangular courtyard has a nominal 0.25 mm margin around the module. `F.Fab` preserves the physical outline and USB-C orientation. Reference text is horizontal on `F.SilkS`; value text is horizontal on `F.Fab` outside the body. No paste-layer apertures are assigned to through-hole contacts.

## Electrical pin types and ERC limitations

GPIO and SWDIO are `bidirectional`; SWCLK and NRST are `input`; GND and VBAT are `power_in`. The 5V and 3V3 rails are `passive` because they are exposed common rails connected to USB power and the onboard regulator. Marking them unconditionally as `power_out` would cause false conflicts when the module is powered from a header.

This is an intentional ERC limitation: the symbol does not prove a valid power topology and cannot prevent opposing supplies or backfeeding. Every carrier design must review power direction explicitly.

SWCLK models its intended SWD role and does not express PA14 as a general-purpose GPIO. `FLASH_*` describes onboard connections/reservations and does not guarantee that a flash device is populated. PC14/PC15 share the installed LSE crystal, PA11/PA12 share USB, PC13 shares the LED, and PA0 shares the user button. These loads remain present when the pins are used for alternate functions.

The minimal validation schematic intentionally marks every contact as no-connect. Clean ERC/DRC results prove library structure and mapping consistency; they do not represent a functional flight-computer design.

## Mechanical integration TBD

Final Z height, selected headers or sockets, clearance above the carrier PCB, and the USB-cable envelope remain system-integration TBDs. The official STEP contains no installed headers. Z = 0 preserves the official model datum but is not a ready-to-manufacture carrier-board mounting definition: the module PCB solid occupies approximately Z = -1.491…0 mm and includes bottom-side components.

Do not use this datum for carrier collision verification until the actual mating hardware and stand-off height are defined.

## Configuration closure

Technical status: **WeAct Black Pill STM32F411CEU6 V3.x KiCad Library — VALIDATED**, revision 1.1, developed by ASTRA TEAM.

KiCad 10.0.7 results:

- ERC violations: 0
- DRC violations: 0
- unconnected items: 0
- schematic/PCB parity issues: 0
- numbering changes: 0

No exclusions were used to conceal corrected discrepancies. `ignored_checks` in KiCad's JSON reports are categories disabled by the default rule set; for example, the footprint's existing courtyard was independently inspected even though `missing_courtyard` is disabled by default.

Fresh top and isometric 3D screenshots show the official STEP with USB-C on the left and all 44 holes aligned. Numerical extraction provides the geometric evidence because screenshots cannot demonstrate sub-micrometre agreement. The layer-render SVG provides an unobstructed inspection of the carrier-footprint Pin 1 mark.
