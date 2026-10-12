# KiCad Library for WeAct Studio Black Pill STM32F411CEU6 V3.0 / V3.1

KiCad symbol, through-hole footprint, official 3D model, and a small validation project for the complete **WeAct Studio MiniF4 / Black Pill STM32F411CEU6 module**.

This library was built by **ASTRA TEAM** for an STM32F411-based CanSat flight computer. It represents the development board as a COTS module; it is not a symbol for the bare STM32F411 MCU.

![WeAct Black Pill STM32F411CEU6 in KiCad 3D Viewer](validation/BlackPill_validation_3D_iso.png)

## Download

**[Download the complete library as a ZIP](https://github.com/edulandoni/WeAct-BlackPill-STM32F411CEU6-KiCad-Library/archive/refs/heads/main.zip)**

The ZIP contains everything required, including the STEP model. Extract it to a permanent folder before adding the libraries to KiCad.

## What is included

| Item | Path |
|---|---|
| Symbol library | `WeAct_BlackPill_STM32F411CEU6.kicad_sym` |
| Footprint library | `WeAct_BlackPill_STM32F411CEU6.pretty/` |
| Official WeAct V3.1 STEP model | `3dmodels/WeAct_MiniF4x1Cx_V31.step` |
| Minimal KiCad test project | `validation/BlackPill_validation.kicad_pro` |
| Pin and geometry audit | `validation/pinout_and_geometry.csv` |
| ERC and DRC reports | `validation/erc.json`, `validation/drc.json` |

## Installation

1. Extract the downloaded ZIP.
2. In KiCad, open **Preferences → Manage Symbol Libraries**, select **Add existing library to table**, and choose `WeAct_BlackPill_STM32F411CEU6.kicad_sym`.
3. Use the nickname `WeAct_BlackPill_STM32F411CEU6`.
4. Open **Preferences → Manage Footprint Libraries**, select **Add existing library to table**, and choose the `WeAct_BlackPill_STM32F411CEU6.pretty` folder.
5. Use the same nickname: `WeAct_BlackPill_STM32F411CEU6`.
6. Open **Preferences → Configure Paths** and add:

   ```text
   Name:  WEACT_BLACKPILL_KICAD_LIB
   Path:  absolute path to the extracted library folder
   ```

The footprint resolves its model from:

```text
${WEACT_BLACKPILL_KICAD_LIB}/3dmodels/WeAct_MiniF4x1Cx_V31.step
```

To check the installation, open `validation/BlackPill_validation.kicad_pro`, open the PCB, and press `Alt+3`. The USB-C connector should be on the left in the 3D Viewer.

## Validation

Baseline: **revision 1.1, 2026-10-12, KiCad 10.0.7**.

| Check | Result |
|---|---:|
| Symbol pins checked against WeAct P1/P2/P3 | 44 / 44 |
| Pad numbers present and unique | 1–44 |
| Header pitch | 2.54 mm |
| Footprint row spacing | 15.2146 mm |
| Maximum pad-to-STEP hole-center error | 0.000566 mm |
| Acceptance threshold | 0.001 mm |
| Nominal board outline | 52.81 × 20.78 mm |
| ERC violations | 0 |
| DRC violations | 0 |
| Unconnected items | 0 |
| Schematic/PCB parity issues | 0 |

The source baseline is WeActStudio/WeActStudio.MiniSTM32F4x1 commit [`05380f5`](https://github.com/WeActStudio/WeActStudio.MiniSTM32F4x1/tree/05380f5c41f38eea8966a81c5acdeb7512cd909f). The full review is in [docs/VALIDATION.md](docs/VALIDATION.md); the complete pin mapping is in [validation/pinout_and_geometry.csv](validation/pinout_and_geometry.csv).

Pin 1 is PB12. It is the only rectangular pad and has explicit markers on both `F.SilkS` and `F.Fab`. Pads 41–44 are the SWD header: 3V3, SWDIO, SWCLK, and GND.

## Hardware coverage

The library targets original WeAct Studio MiniF4 / Black Pill boards fitted with the STM32F411CEU6:

- V3.1 is checked directly against the official schematic, mechanical drawing, and STEP model.
- V3.0 uses the same documented external dimensions and pin definitions.
- Clones and other revisions are outside the validated configuration.

The V3.1 STEP does not contain installed headers. Header height, socket selection, carrier-PCB clearance, and USB-cable clearance must therefore be checked in the final assembly. Pins shared with USB, onboard flash, LED, user button, BOOT1, and the LSE crystal retain those onboard loads.

## Source and licensing

The STEP file is the unmodified model published by WeAct Studio. WeAct Studio confirmed to ASTRA TEAM by email that it may be redistributed. The pinned source, file hash, and attribution are recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

ASTRA TEAM's KiCad files, validation material, and documentation are released under the [MIT License](LICENSE). The WeAct model remains attributed to WeAct Studio and is not covered by that MIT grant.

If a future board revision changes the pinout or geometry, open an issue with a link to the official source. Pad or pin numbers should never be changed without updating the traceability matrix and rerunning the checks.
