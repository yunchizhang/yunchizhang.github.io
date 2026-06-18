Title: Waveguide Filter in H-Bend
Date: 2026-6-18 11:00
Category: RF Components
Tags: RF, Microwave, System, Waveguide, Passive, Components
Slug: waveguide_filter_h_bend
Authors: Yunchi Zhang
Summary: A waveguide filter built in H-bend.
Keywords: Waveguide Filter

[TOC]

In a full-duplex RF system employing a shared antenna, the diplexer provides frequency separation
between transmit and receive bands. However, the isolation offered by the employed diplexer is
insufficient to adequately suppress transmission leakage to the sensitive receive path. This
leakage causes receiver saturation and intermodulation distortion, degrading system performance.

A waveguide filter designed to fit within an existing H-bend component in the receive path provides
additional rejection at transmit frequencies, complementing the diplexer isolation. By
strategically placing the filter to replace the waveguide H-bend, the design leverages existing
waveguide infrastructure while adding critical stopband attenuation. This document outlines the
design and manufacturing methodology for realizing such a waveguide filter that maintains the
H-bend geometry while meeting the required frequency response specifications.

## Requirements

### Mechanical Dimensions

![Waveguide Bend]({static}/RF_related/images/wg_bend_spec.png)

_Figure 1: H-bend waveguide dimensional specification_

The filter must conform to the following dimensional constraints (see Figure 1):

- Overall H-bend geometry: The filter port interfaces must be aligned with the original H-bend
  ports so that it can replace the H-bend.
- Waveguide port dimensions: Standard Rectangular Waveguide Interface.
- Material: Aluminum
- Finish: White Enamel

### RF Specifications

| Parameter               | Specification | Unit |
| ----------------------- | ------------- | ---- |
| Passband Frequency      | 2.200 - 2.215 | GHz  |
| Passband Insertion Loss | 0.15 max      | dB   |
| Passband VSWR           | 1.20:1 max    | N/A  |
| Stopband Frequency      | 2.025 - 2.040 | GHz  |
| Stopband Rejection      | 50dB min      | dB   |

### Environmental Requirements

- Operating Temperature Range: -20 - 55 °C
- Pressure: 2.0 PSIG

## Design

### Circuit Simulation

A three-pole filter topology was selected based on circuit simulation analysis to meet the
specified RF requirements. The simulation determined that three poles provide the optimal balance
between passband flatness, insertion loss, and stopband rejection while maintaining the mechanical
constraints of the H-bend geometry.

### HFSS Full-Wave Simulation

Standard rectangular waveguide WR430 is required at the filter ports. The filter is designed in
H-Plane with iris coupling between waveguide resonators. The resonator lengths and iris widths are
optimized to achieve the desired filter performance.

The filter design was implemented and optimized using Ansys HFSS (High Frequency Structure
Simulator) to account for the three-dimensional electromagnetic field interactions within the
waveguide structure. The simulation included the complete filter elements to ensure accurate
prediction of the filter response.

#### 3D Model

![Filter 3D Model]({static}/RF_related/images/wg_3pole_filter_hfss_model.png)

_Figure 2: HFSS 3D model of the 3-pole waveguide filter in H-bend configuration_

The 3D model incorporates the filter resonators positioned strategically within the waveguide to
achieve the required frequency response while maintaining the H-bend port interfaces.

#### Simulation Results

![Filter Response]({static}/RF_related/images/wg_3pole_filter_hfss_response.png)

_Figure 3: Simulated 3-pole filter magnitude response_

The HFSS simulation results demonstrate that the three-pole filter design meets the specified requirements.

## Manufacture and Measurement

### Assembly Process

The filter is manufactured as two components: a filter body and a lid. The lid is brazed onto the
filter body to create a hermetic seal, ensuring environmental protection and structural integrity.
Tuning screws are strategically integrated into the filter body to enable precise adjustment of
the resonators and iris couplings, allowing fine-tuning of the filter response during manufacturing
and field commissioning.

### Tuning and Optimization

The tuning screws provide manual control of the resonator frequencies and coupling levels. Through
iterative tuning, the filter response is adjusted to meet the specified passband and stopband
requirements. This tuning capability ensures that manufacturing tolerances do not impact final
filter performance.

### Measurement Results

#### Manufactured Filter

![Manufactured Filter]({static}/RF_related/images/wg_3pole_filter_proto.png)

_Figure 4: Manufactured 3-pole waveguide filter in H-bend configuration_

#### Measurement Data

![Measurement Results]({static}/RF_related/images/wg_3pole_filter_meas.png)

_Figure 5: Network analyzer measurement of the fabricated filter_

The completed filter was measured using network analyzer testing to validate performance against
the RF specifications. The measured results demonstrate that the filter meets all specified
requirements.

The manufactured filter successfully provides the required frequency separation and isolation in
the full-duplex RF system receive path.

## 5-pole Filter Design with Improved Attenuation

While the 3-pole filter design successfully meets the baseline RF requirements, in scenarios where
transmission leakage suppression proves insufficient, a 5-pole filter design offers significantly
enhanced stopband attenuation (>95 dB) to further protect the receive path.

### Design Approach

The 5-pole filter extends the filter topology to five resonators with additional coupling irises,
providing steeper filter skirts and deeper rejection in the stopband. The key innovation in this
design is vertical expansion within the H-bend structure: rather than extending the filter
footprint horizontally beyond the original H-bend envelope, the resonators are strategically
positioned to grow vertically between the fixed waveguide ports. This approach maintains
compatibility with the existing H-bend real estate while accommodating the additional filter
elements.

### HFSS Full-Wave Simulation

The 5-pole filter design was optimized using Ansys HFSS to validate the enhanced performance
while maintaining the constrained geometry. The simulation accounts for the vertical arrangement
of resonators and optimized iris coupling dimensions.

#### 3D Model

![5-pole Filter 3D Model]({static}/RF_related/images/wg_5pole_filter_hfss_model.png)

_Figure 6: HFSS 3D model of the 5-pole waveguide filter with vertical expansion in H-bend configuration_

The 3D model demonstrates how the five resonators are positioned vertically to maximize stopband
attenuation while maintaining the original H-bend port interfaces and fitting within the available
height constraints.

#### Simulation Results

![5-pole Filter Response]({static}/RF_related/images/wg_5pole_filter_hfss_response.png)

_Figure 7: Simulated 5-pole filter magnitude response showing enhanced stopband rejection_

The HFSS simulation results demonstrate that the five-pole filter design achieves greater than
95 dB rejection in the stopband while maintaining acceptable passband performance. The increased
filter order provides the additional attenuation necessary to suppress transmission leakage in
demanding full-duplex RF systems.
