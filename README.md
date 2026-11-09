# Product engineering portfolio

Hassan Kazmi · Electrical engineering at Toronto Metropolitan University

I want to build and launch products across robotics, electronics, embedded systems, CAD, and software. This portfolio connects each project to source code, design decisions, and the evidence available today.

## Start with these projects

- **[Shaggy](https://github.com/hxssank/shaggy)** connects physical controls to an embedded audio system. Review bank validation, SD-to-flash caching, playback state, and installation recovery.
- **[Spark](https://github.com/hxssank/spark)** connects enclosure dimensions to PCB and component placement. Review the difference between a routed bench converter and a complete battery product.
- **[Mazal](https://github.com/hxssank/mazal)** connects a desktop interface to financial records, document provenance, and calculation services. Review the import and persistence rules before the interface code.
- **[Alfred](https://github.com/hxssank/recruiter-portfolio/tree/main/projects/alfred)** makes the contribution to an existing robotics platform explicit. Review the patch against its pinned ToddlerBot base and the regression tests alongside it.

## Hardware and robotics

| Project | Product problem | Implementation to review | Current boundary |
| --- | --- | --- | --- |
| [Shaggy](https://github.com/hxssank/shaggy) | Make an audio-stem player respond to physical controls and recover from media failures | [Firmware](https://github.com/hxssank/shaggy/tree/main/firmware), [host tools](https://github.com/hxssank/shaggy/tree/main/tools), [carrier board](https://github.com/hxssank/shaggy/tree/main/hardware) | Host tests use fake hardware; they do not measure playback timing or audio quality |
| [Spark](https://github.com/hxssank/spark) | Fit power electronics, a battery reservation, and an enclosure into a compact package | [Bench PCB](https://github.com/hxssank/spark/tree/main/electronics/boost-prototype), [CAD generators](https://github.com/hxssank/spark/tree/main/mechanical), [review UI](https://github.com/hxssank/spark/tree/main/review) | A 25 W design target; charging, USB-PD, protection, temperature, and physical fit are unfinished |
| [Alfred](https://github.com/hxssank/recruiter-portfolio/tree/main/projects/alfred) | Validate commands, communication, and recordings in a humanoid research stack | [Runtime patch](https://github.com/hxssank/recruiter-portfolio/tree/main/projects/alfred/patches), [model exporter](https://github.com/hxssank/recruiter-portfolio/tree/main/projects/alfred/scripts) | ToddlerBot provides the upstream platform; no trained Alfred policy or hardware qualification |
| [Pager](https://github.com/hxssank/pager) | Package a pocket Linux computer with a thumb keyboard and trackball | [Layout constraints](https://github.com/hxssank/pager/blob/main/mechanical/slim-layout.json), [CAD generator](https://github.com/hxssank/pager/blob/main/mechanical/build_slim.py) | The 96 x 166 x 17.4 mm envelope is a packaging target, not a completed device |

## Software and interfaces

| Project | Product problem | Implementation to review | Current boundary |
| --- | --- | --- | --- |
| [Mazal](https://github.com/hxssank/mazal) | Keep financial records, source documents, and forecasts connected | [SQLite persistence](https://github.com/hxssank/mazal/blob/main/server/persistence.ts), [calculation engine](https://github.com/hxssank/mazal/tree/main/backend/mazal_engine), [desktop shell](https://github.com/hxssank/mazal/tree/main/macos) | Local personal application; forecasts depend on entered records and assumptions |
| [Cant Pin Me](https://github.com/hxssank/cant-pin-me) | Turn routine planning and completed sets into a usable training history | [Workout model](https://github.com/hxssank/cant-pin-me/blob/main/dist/model.js), [movement code](https://github.com/hxssank/cant-pin-me/blob/main/dist/exercise-motion.js), [tests](https://github.com/hxssank/cant-pin-me/tree/main/tests) | Movement illustrations have no clinical or biomechanical validation |
| [Drip](https://github.com/hxssank/drip) | Connect outfit choices, wear, laundry, photos, and closet locations | [State model](https://github.com/hxssank/drip/blob/main/dist/model.js), [photo storage](https://github.com/hxssank/drip/blob/main/dist/photos.js), [closet logic](https://github.com/hxssank/drip/blob/main/dist/closet.js) | Synthetic public demo; fixed mannequin geometry and browser-local storage |
| [Mazal Academy](https://github.com/hxssank/mazal-academy) | Make financial concepts interactive and preserve learning progress | [Calculation models](https://github.com/hxssank/mazal-academy/blob/main/shared/learning.ts), [progress storage](https://github.com/hxssank/mazal-academy/blob/main/src/academy/progress-storage.ts) | Simplified teaching models; no account service or cloud progress sync |

## Evidence and review expectations

Each project README provides run commands, source links, validation scope, and unfinished work. A passing calculation or geometry test does not establish that a physical product works. Renders identify themselves as CAD concepts, and software previews use empty or synthetic data.

The public projects are reviewed source snapshots. Personal records, private infrastructure configuration, audio libraries, and work-confidential material are excluded. Third-party libraries, anatomy assets, and ToddlerBot retain their attribution; their contribution is distinguished from mine.

## Engineering foundations

[Electrical engineering coursework](https://github.com/hxssank/electrical-engineering-coursework) contains notes across 25 subjects and original Python examples for resistor-divider loading and ideal RC response. Its 38 tests cover expected values, invalid physical inputs, and limiting cases. These are study examples, not measured circuit results or a claim of degree completion.

[Back to my profile](https://github.com/hxssank)
