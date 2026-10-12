# Official STEP model

The WeAct Studio STEP file is intentionally not committed because the official repository does not declare a repository-wide redistribution license.

Download the pinned official file from:

<https://raw.githubusercontent.com/WeActStudio/WeActStudio.MiniSTM32F4x1/05380f5c41f38eea8966a81c5acdeb7512cd909f/Hardware/MiniF4x1Cx_V31_3D.step>

Save it in this directory as:

```text
WeAct_MiniF4x1Cx_V31.step
```

Expected SHA-256:

```text
e713074f681a8ee3d1c54ae5419c8165c01b16e5abb54afae9252521651cb594
```

PowerShell example:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/WeActStudio/WeActStudio.MiniSTM32F4x1/05380f5c41f38eea8966a81c5acdeb7512cd909f/Hardware/MiniF4x1Cx_V31_3D.step" -OutFile "WeAct_MiniF4x1Cx_V31.step"
Get-FileHash -Algorithm SHA256 "WeAct_MiniF4x1Cx_V31.step"
```

For normal library use, define the KiCad path variable `WEACT_BLACKPILL_KICAD_LIB` as the repository root. The validation project uses a project-relative model path.
