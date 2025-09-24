Title: Higher Order Mode Tracking
Date: 2025-04-29 18:30
Status: hidden
Slug: monopulse-higher-mode
Save_as: pages/antenna/monopulse/monopulse_higher_mode_tracking.html
Url: pages/antenna/monopulse/monopulse_higher_mode_tracking.html
Comments: False
Template: simple_page
Authors: Yunchi Zhang

[TOC]

# Higher Order Mode (HOM) Tracking System

Modern monopulse systems generate Sum and Difference signals by properly coupling the fundamental
mode and the higher order modes (HOMs) of an overmoded waveguide  that feeds the parabolic antenna.

Within the HOM tracking system, the radiation pattern of the mode $TE_{11}$  (sum pattern) will be
applied for the main signal, while the radiation pattern of one of the modes ($TM_{01}$, $TE_{01}$, $TE_{21}$)
(difference pattern) will be used for the tracking signal. The output of the mode sensor of these
modes will sense any small changes in the satellite pointing angles (azimuth & elevation). The
deviation in amplitude and phase of these modes with respect to those of the $TE_{11}$  (reference
mode) depend on the variations in the satellite pointing angles.

Depending on the polarization of the satellite beacon signal it was necessary to take both modes
$TM_{01}$  and $TE_{01}$  simultaneously in the linear polarization case.  For the circular polarization it
was sufficient to process the signal of a single mode only. Now in the modem systems, the use of
$TE_{21}$  is sufficient for tracking in either linear or circular polarized cases.

![Higher order mode tracking system]({static}/antenna/monopulse/images/higher_mode_tracking_system.png)

*Higher order mode tracking system*

# Field Components and Radiation Pattern

## Electric Field of Modes

![Higher order mode electric field]({static}/antenna/monopulse/images/higher_modes_elctric_field.png)

*Copied from "Controlled Excitation of Waveguide High-Order Modes for a Simple and Accurate
Monopulse Tracking System Test Bench, by Gabriele Ceccato, Juan Luis Cano, Angel Mediavilla and
Luca Perregrini"*

## $TE_{11}$ Mode

$$\begin{cases} E_r=-\frac{jE_0K}{\gamma}J_0(\gamma r)\cos \phi e^{-j\beta Z} \\ \\
E_\phi=\frac{jE_0K}{\gamma}J_0(\gamma r)\sin \phi e^{-j\beta Z} \end{cases} $$

where $\gamma=\frac{2\pi}{\lambda_c}$, $\beta=\frac{2\pi}{\lambda_g} $, $K=\frac{2\pi}{\lambda} $.

The radiation pattern of this mode calculated using the aperture theory is given by:

$$jE_\theta=E_\phi=C\frac{1+\cos\theta}{2}\frac{J_0(Ka\sin\theta)}{(2.405)^2-(Ka\sin\theta)^2}e^{j\phi}\frac{e^{-jKR}}{R}$$

where $a$ is the radius of the circular aperture.

It is clear that the radiation pattern has a rotation symmetry and maximum at $\theta=0$ (Sum pattern).

## $TE_{21}$ Mode

$$\begin{cases} E_r=-\frac{jE_0K}{\gamma}J_1(\gamma r)\cos (2\phi) e^{-j\beta Z} \\ \\
E_\phi=\frac{jE_0K}{\gamma}J_1(\gamma r)\sin (2\phi) e^{-j\beta Z} \end{cases} $$

The far field pattern is:

$$jE_\theta=E_\phi=C\frac{1+\cos\theta}{2}\frac{J_1(Ka\sin\theta)}{(3.832)^2-(Ka\sin\theta)^2}e^{j2\phi}\frac{e^{-jKR}}{R}$$

The far field pattern has a rotational symmetry and zero at $\theta=0$. It is a difference pattern.

## $TM_{01}$ Mode

$$\begin{cases}E_z=E_0J_0(\gamma r)e^{-j\beta Z} \\ \\ E_r=-\frac{j\beta}{\gamma}E_0J_0(\gamma
r)e^{-j\beta Z} \end{cases} $$

The far field pattern is:

$$\begin{cases}E_\theta=A\frac{1+\cos\theta}{2}\frac{J_1(Ka\sin\theta)}{(3.832)^2-(Ka\sin\theta)^2}\frac{e^{-jKR}}{R}
\\ \\ E_\phi=0\end{cases}$$

The far field pattern has a rotational symmetry and zero at $\theta=0$. It is a difference pattern.
$TM_{01}$  radiation field has only one component $E_θ$.

# HOM Excitation and Mode Sensor

## HOM Excitation

In multi-mode monopulse system, when an antenna receives an incident wave, the output level of the
communications signal is maximum when the antenna points directly toward a point signal source. On
the other hand, higher order modes are excited in the waveguide when the boresight axis of the
antenna feed is not in line with the point source (as illustrated in the following figure).

![Higher order mode excitation]({static}/antenna/monopulse/images/hom_excitation.png)

*Higher order mode excitation*

In general, the phase difference between $TE_{11}$  mode and the excited HOM modes jumps between 0 and
180 degress depending on the mode orientations. From a practical point of view, the excited HOM
modes due to the fundamental $TE_{11}^C$  and $TE_{11}^S$ modes are exclusively sensitive to either the
Elevation pointing error ($Δ_{EL}$) or the Azimuth pointing error ($Δ_{AZ}$).

The following table illustrates the details of excitations.

![Higher order mode excitation table]({static}/antenna/monopulse/images/hom_excitation_table.png)

*Copied from "Controlled Excitation of Waveguide High-Order Modes for a Simple and Accurate
Monopulse Tracking System Test Bench, by Gabriele Ceccato, Juan Luis Cano, Angel Mediavilla and
Luca Perregrini"*

## Mode Sensor

The mode sensor detects the signal of the higher order mode that is used to create the difference
pattern which will be applied for the monopulse tracking.  The mode detection is done by resonant
coupling slots cut in a longitudinal or a transversal manner in the waveguide wall, depending on
the mode type. The different configurations are seen in the following figure for coupling different
modes. The coupling slots must be in the direction of the magnetic field lines near the waveguide
walls.

![Higher order mode coupling]({static}/antenna/monopulse/images/hom_coupling.png)

*Copied from "The higher order modes in the feeds of the satellite Monopulse tracking antennas, by
Dr. Lotfy Sakr"*
