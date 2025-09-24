Title: Monopulse Concept
Date: 2025-04-29 18:20
Status: hidden
Slug: monopulse-concept
Save_as: pages/antenna/monopulse/monopulse_concept.html
Url: pages/antenna/monopulse/monopulse_concept.html
Comments: True
Template: simple_page
Authors: Yunchi Zhang

[TOC]

# Basic Concept

Monopulse technology using four feed horns or dipoles are discussed in this page to illustrate the basic
concept.

## Mechanical Design

A paraboloid-reflector antenna fed by a cluster of four feed horns in the focal plane.

![Reflector and feed horns]({static}/antenna/monopulse/images/reflector_horns.png)

*Reflector and feed horns: (a) side view; and (b) axial view of feed horns from reflector*

## Amplitude Comparison Monopulse

The squinted beams received by the feed horns are illustrated below.

![Squinted Beams]({static}/antenna/monopulse/images/squinted_beams.png)

*Four squinted beams in amplitude-comparison monopulse*

![Beam cross sections]({static}/antenna/monopulse/images/cross_section_beams.png)

*Cross section of amplitude-comparison monopulse beams*

### Equation

The Sum and the differences are given by the following equations.

- Sum: $s=\frac{1}{2}(A+B+C+D)$

- Traverse Difference: $d_{tr}=\frac{1}{2}[(C+D)-(A+B)]$

- Elevation Difference: $d_{el}=\frac{1}{2}[(A+C)-(B+D)]$

### Voltage Pattern

The voltage patterns $v_1$  and $v_2$  of the pairs of squinted beams are:

- Traverse:

$$\begin{cases}v_1=\frac{C+D}{\sqrt{2}} \\ \\ v_2=\frac{A+B}{\sqrt{2}} \end{cases}$$

- Elevation:

$$\begin{cases}v_1=\frac{A+C}{\sqrt{2}} \\ \\ v_2=\frac{B+D}{\sqrt{2}} \end{cases}$$

# Comparison Methods

## Amplitude Comparison

A form of monopulse in which the angular deviation of the target from the antenna axis is measured
as the amplitude ratio of the target as received by two antenna patterns. The patterns may be a
pair of beams displaced on opposite sides of the antenna axis or a difference-channel beam having
odd symmetry about the axis and a sum beam having even symmetry. In the latter case the ratio may
have positive and negative values (0° or 180° phase shift, or in some cases +90° and −90°).
Distinguished from phase-comparison monopulse, in which the relative phase of the two patterns
carries the information on target displacement.

## Phase Comparison

A form of monopulse employing receiving beams with different phase centers, as obtained, for
example, from side-by-side antennas or separate portions of an array.

!!!note
    The information on target displacement from the antenna axis appears as a relative phase
    between the signals received at the two phase centers.


# Monopulse Output

## General Principles

All monopulse processors are intended to produce outputs that depend only on ratios, not absolute
values, of signal voltages. Any sensitivity that they have to absolute values is due to design
compromises or equipment imperfections.

![Output diagram]({static}/antenna/monopulse/images/output_diagram.png)

*Monopulse output diagram*

In a general sense, the ratio of two voltages means their complex ratio. The phasor voltages
(complex envelopes) of a monopulse difference $d$ and sum $s$ can be expressed as:

$$d=|d|\exp (j\delta_d)$$

$$s=|s|\exp (j\delta_s)$$

$$\frac{d}{s}=\left|\frac{d}{s} \right|\exp \left[j(\delta_d-\delta_s) \right]=\left|\frac{d}{s}
\right|\exp (j\delta)$$

if $d$ and $s$ are the difference and sums of voltages $v_1$  and $v_2$  from two individual beams
or from two pairs of beams, then

$$\frac{d}{s}=\frac{v_1-v_2}{v_1+v_2} = \frac{1-v_2/v_1}{1+v_2/v_1} $$

## Useful Formula

Define

$$\begin{cases}d=\Re (d) + j\Im (d)=d_I + jd_Q \\ \\ s=\Re (s) + j\Im (s)=s_I + js_Q \end{cases} $$

Then

$$\frac{d}{s}=\frac{ds^*}{ss^*}=\frac{(d_I+jd_Q)(s_I-js_Q)}{(s_I+js_Q)(s_I-js_Q)}=\frac{d_Is_I+d_Qs_Q}{s_I^2+s_Q^2}+j\frac{d_Qs_I-d_Is_Q}{s_I^2+s_Q^2} $$
