# Product engineering portfolio

Hassan Kazmi · Electrical engineering at Toronto Metropolitan University

Open a project repository for its source, run commands, and test scope. The links below go directly to editable designs, parts lists, code, and exports. Engineering notes explain the implementation and its failure conditions.

## Hardware and robotics

### Shaggy

Pico 2 stem player with Hall-sensor controls, SD libraries, flash caching, and CircuitPython firmware.

- [Firmware](https://github.com/hxssank/shaggy/tree/main/firmware), [audio/install tools](https://github.com/hxssank/shaggy/tree/main/tools), and [host tests](https://github.com/hxssank/shaggy/tree/main/tests).
- [KiCad schematic and PCB](https://github.com/hxssank/shaggy/tree/main/hardware/pcb), [BOM](https://github.com/hxssank/shaggy/blob/main/hardware/pcb/bom.csv), and [cable pinout](https://github.com/hxssank/shaggy/blob/main/hardware/pcb/cable-pinout.csv).
- [Board STEP](https://github.com/hxssank/shaggy/blob/main/hardware/pcb/shaggy-carrier.step), [schematic PDF](https://github.com/hxssank/shaggy/blob/main/hardware/pcb/reports/schematic.pdf), and [prototype Gerbers/drills](https://github.com/hxssank/shaggy/tree/main/hardware/pcb/fabrication-prototype).
- [Timing and cache recovery](https://github.com/hxssank/shaggy/blob/main/ENGINEERING.md).

Host tests use fake hardware. They do not measure playback timing or audio quality. Fabrication files need review before ordering; audio libraries are excluded.

### Spark

Compact power-bank design study with parametric enclosure models and a routed bench boost converter.

- [CAD generators](https://github.com/hxssank/spark/tree/main/mechanical), [Prototype A STEP](https://github.com/hxssank/spark/tree/main/mechanical/exports), [print STLs](https://github.com/hxssank/spark/tree/main/mechanical/print_parts), and [compact packing models](https://github.com/hxssank/spark/tree/main/mechanical/compact-exports).
- [KiCad board and schematic](https://github.com/hxssank/spark/tree/main/electronics/boost-prototype), [bench BOM](https://github.com/hxssank/spark/blob/main/electronics/boost-prototype/BOM.csv), and [parts/sourcing tables](https://github.com/hxssank/spark/tree/main/sourcing).
- [Schematic PDF](https://github.com/hxssank/spark/blob/main/electronics/boost-prototype/reports/schematic.pdf), [Gerbers/drills and review status](https://github.com/hxssank/spark/tree/main/electronics/boost-prototype/manufacturing-review), and [assembly UI source](https://github.com/hxssank/spark/tree/main/review).
- [Current, heat, and usable-energy calculations](https://github.com/hxssank/spark/blob/main/ENGINEERING.md).

25 W is a compact-design target. The bench PCB does not implement the complete charger, USB-PD system, cell protection, or temperature cutoff. Compact packing models and Prototype A parts represent different designs.

### Pager

Pocket Linux computer concept with a thumb keyboard, trackball, and a 96 x 166 x 17.4 mm packaging target.

- [CAD generator and layout constraints](https://github.com/hxssank/pager/tree/main/mechanical).
- [Assembly STEP](https://github.com/hxssank/pager/blob/main/mechanical/slim-packaging-target.step), [grip-dummy STEP](https://github.com/hxssank/pager/blob/main/mechanical/slim-grip-dummy-96x166x17.4.step), and [grip-dummy STL](https://github.com/hxssank/pager/blob/main/mechanical/slim-grip-dummy-96x166x17.4.stl).
- [Parts list](https://github.com/hxssank/pager/blob/main/parts-list.csv), [geometry tests](https://github.com/hxssank/pager/blob/main/mechanical/test_slim.py), and [thickness budget](https://github.com/hxssank/pager/blob/main/ENGINEERING.md).

The models reserve component space. The parts list is a selection worksheet, not an order-ready BOM. No custom PCB, firmware image, or finished enclosure is available.

### Alfred

Robotics development on ToddlerBot, with attributed runtime validation, communication, motor handling, and recording changes.

- [Standalone repository and reconstruction commands](https://github.com/hxssank/alfred).
- [Patch against the pinned upstream revision](https://github.com/hxssank/alfred/tree/main/patches), [upstream provenance](https://github.com/hxssank/alfred/blob/main/upstream.json), and [licence](https://github.com/hxssank/alfred/blob/main/LICENSE).
- [Model exporter](https://github.com/hxssank/alfred/blob/main/scripts/export_model.py), [export tests](https://github.com/hxssank/alfred/blob/main/tests/test_model_export.py), and [runtime contracts](https://github.com/hxssank/alfred/blob/main/ENGINEERING.md).

ToddlerBot provides the base robot and models. There is no original Alfred PCB/CAD package, trained Alfred policy, or validated household robot.

## Software

| Project | Source to inspect | Scope |
| --- | --- | --- |
| [Mazal](https://github.com/hxssank/mazal) | [SQLite persistence](https://github.com/hxssank/mazal/blob/main/server/persistence.ts), [Python engine](https://github.com/hxssank/mazal/tree/main/backend/mazal_engine), [Swift shell](https://github.com/hxssank/mazal/tree/main/macos), [import design](https://github.com/hxssank/mazal/blob/main/ENGINEERING.md) | Local finance app. Forecasts depend on entered records; the README reports release-check status. |
| [Cant Pin Me](https://github.com/hxssank/cant-pin-me) | [Workout model](https://github.com/hxssank/cant-pin-me/blob/main/dist/model.js), [movement code](https://github.com/hxssank/cant-pin-me/blob/main/dist/exercise-motion.js), [tests](https://github.com/hxssank/cant-pin-me/tree/main/tests) | 60-exercise workout planner. Movement demos have no clinical or biomechanical validation. |
| [Drip](https://github.com/hxssank/drip) | [State model](https://github.com/hxssank/drip/blob/main/dist/model.js), [photo storage](https://github.com/hxssank/drip/blob/main/dist/photos.js), [closet layout](https://github.com/hxssank/drip/blob/main/dist/closet.js) | Browser wardrobe app with synthetic public data and local photo storage. |
| [Mazal Academy](https://github.com/hxssank/mazal-academy) | [Calculation models](https://github.com/hxssank/mazal-academy/blob/main/shared/learning.ts), [progress transactions](https://github.com/hxssank/mazal-academy/blob/main/src/academy/progress-storage.ts) | Simplified finance lessons and labs. Browser progress has no account or cloud sync. |

## Circuit studies

[Electrical engineering coursework](https://github.com/hxssank/electrical-engineering-coursework) contains notes across 25 subjects, Python models for loaded resistor dividers and ideal RC response, and tests for numerical results and limiting cases. [Worked derivations](https://github.com/hxssank/electrical-engineering-coursework/blob/main/ENGINEERING.md) connect the equations to the implementation. These are study models, not measured circuit results.

[Profile](https://github.com/hxssank) · Personal records, private infrastructure, and confidential work are excluded from this portfolio.
