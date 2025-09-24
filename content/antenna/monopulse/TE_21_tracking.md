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

Outputs at Port1 and Port2 of the 3dB hybrid are given by

$$\begin{cases}E_1=\frac{1}{\sqrt{2}}\left(E_{21}^1-jE_{21}^2
\right)=\frac{E_0}{\sqrt{2}}\left(\Delta_{EL}-j\Delta_{AZ} \right)e^{j\left(\psi-\frac{\pi}{2}
\right)} \\ \\ E_2=\frac{1}{\sqrt{2}}\left(-jE_{21}^1+E_{21}^2
\right)=\frac{E_0}{\sqrt{2}}\left(\Delta_{EL}+j\Delta_{AZ} \right)e^{-j\psi} \end{cases} $$

Signal from either port can be employed for tracking purpose. 3dB power loss is introduced due to
the hybrid combiner. The introduced phase due to polarization orientation needs to be compensated
in the sum channel by a phase shifter.

#### Vectical Polarization Only ($TE_{11}^C$, $\psi=\frac{\pi}{2}$)

$$\begin{cases}E_1=\frac{E_0}{\sqrt{2}}\left(\Delta_{EL}-j\Delta_{AZ} \right) \\ \\
E_2=\frac{E_0}{\sqrt{2}}\left(\Delta_{EL}+j\Delta_{AZ} \right)e^{-j\frac{\pi}{2}} \end{cases} $$

#### Horizontal Polarization Only ($TE_{11}^S$, $\psi=0$)

$$\begin{cases}E_1=\frac{E_0}{\sqrt{2}}\left(\Delta_{EL}-j\Delta_{AZ} \right)e^{-j\frac{\pi}{2}} \\ \\
E_2=\frac{E_0}{\sqrt{2}}\left(\Delta_{EL}+j\Delta_{AZ} \right) \end{cases} $$

### Dual Linear Polarization

Simultaneous dual linear polarization signals are supported if the tracking signal on one
polarization has different frequency than signal on the other polarization. However, if signals on
both polarizations have overlapped frequency, signal on different polarization than tracking signal
will behave like noise for tracking receiver (based on the above study).

### Circular Polarization

The field component of LHCP can be decomposed as combination of vertical and horizontal field
components with delayed 90 degree phase at horizontal field:

$$E_{LHCP}=\frac{E_0}{\sqrt{2}}\left(e_V+je_H \right) $$

The field component of RHCP can be decomposed as combination of vertical and horizontal field
components with advanced 90degree phase at horizontal field:

$$E_{RHCP}=\frac{E_0}{\sqrt{2}}\left(e_V-je_H \right) $$

#### LHCP Outputs

$$\begin{cases}E_1=-j\frac{E_0}{2}\left(\Delta_{AZ}+j\Delta_{EL}
\right)-j\frac{E_0}{2}\left(\Delta_{AZ}+j\Delta_{EL} \right)=E_0\left(\Delta_{EL}-j\Delta_{AZ}
\right) \\ \\ E_2=\frac{E_0}{2}\left(\Delta_{AZ}-j\Delta_{EL}
\right)-\frac{E_0}{2}\left(\Delta_{AZ}-j\Delta_{EL} \right)=0 \end{cases}$$

#### RHCP Outputs

$$\begin{cases}E_1=-j\frac{E_0}{2}\left(\Delta_{AZ}+j\Delta_{EL}
\right)+j\frac{E_0}{2}\left(\Delta_{AZ}+j\Delta_{EL} \right)=0 \\ \\ E_2=\frac{E_0}{2}\left(\Delta_{AZ}-j\Delta_{EL}
\right)+\frac{E_0}{2}\left(\Delta_{AZ}-j\Delta_{EL} \right)=E_0\left(\Delta_{EL}+j\Delta_{AZ}
\right)e^{-j\frac{\pi}{2}} \end{cases}$$

### Dual LHCP and RHCP

Simultaneous dual circular polarization signals are supported since either Port 1 or Port 2 can be
selected for the tracking signal polarization.

## Handware Sample

![TE21 tracking system hardware sample]({static}/antenna/monopulse/images/te21_tracking_hardware.png)

*Manufactured Ku-band linear/circular pol. TE21 tracking coupler*
