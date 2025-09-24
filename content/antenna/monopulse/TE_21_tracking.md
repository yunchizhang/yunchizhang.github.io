Title: TE21 Monopulse Tracking
Date: 2025-04-29 18:40
Status: hidden
Slug: monopulse-te21-tracking
Save_as: pages/antenna/monopulse/monopulse_te21_tracking.html
Url: pages/antenna/monopulse/monopulse_te21_tracking.html
Comments: False
Template: simple_page
Authors: Yunchi Zhang

[TOC]

# $TE_{21}$ Tracking

Higher order mode $TE_{21}$  coupling can be used for monopulse tracking solutions. The $TE_{11}$ mode
propagates through the main circular waveguide, while $TE_{21}$  mode gets coupled, through a properly
designed slots or holes array, into the rectangular waveguide branch, thus feeding the branching
network to which it is connected.

## Block Diagram

$\Sigma$ in the following diagram represents signal combiner, usually Magic-T is employed. $TE_{11}^C$
represents vertical polarization, while $TE_{11}^S$ represents horizontal polarization.

![TE21 mode plots]({static}/antenna/monopulse/images/te21_mode_field_plots.png)

![TE21 tracking system]({static}/antenna/monopulse/images/te21_tracking_system.png)

*Linear/circular polarization $TE_{21}$ tracking coupler architecture (copied from "ALPERTON TE21
  Tracking Solutions")*

## Tracking Scenarios

Tracking system outputs at Port1 and Port2 depend on the source signal polarizations. The following
subsections illustrate the outputs for different source polarizations.

### Single Linear Polarization

Define the linear incident electric field is $E_0$ and making an angle $\psi$ with respect to $x$-axis,
then the field components that will excite the mode sensor are:

$$\begin{cases}E_x=E_0\cos\psi~(horizontal~polarized~component) \\ \\E_y=E_0\sin\psi~(vertical~polarized~component) \end{cases}$$

The output from the mode sensor of $TE_{21}^C$ ($TE_{21}$ mode #1 in the diagram) exposed to the $E_x$ and
$E_y$ components is given by

$$E_{21}^1=\Delta_{EL}E_y-\Delta_{AZ}E_x=E_0\left(\Delta_{EL}\sin\psi-\Delta_{AZ}\cos\psi \right) $$

The output from the mode sensor of $TE_{21}^S$ ($TE_{21}$ mode #2 in the diagram) exposed to the $E_x$ and
$E_y$ components is given by

$$E_{21}^2=\Delta_{AZ}E_y+\Delta_{EL}E_x=E_0\left(\Delta_{AZ}\sin\psi+\Delta_{EL}\cos\psi \right)
$$

TBA

### Dual Linear Polarization

TBA

### Circular Polarization

TBA

### Dual LHCP and RHCP

TBA

## Handware Sample

![TE21 tracking system hardware sample]({static}/antenna/monopulse/images/te21_tracking_hardware.png)

*Manufactured Ku-band linear/circular pol. TE21 tracking coupler*
