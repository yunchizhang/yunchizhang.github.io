Title: Polarization Match: Special Cases
series: Polarizations
series_index: 3
Date: 2026-2-27 14:43
Category: Antenna
Tags: Antenna, Polarization
Slug: antenna_polarization_3
Authors: Yunchi Zhang
Summary: Wave polarization match factor of special cases.
Keywords: Antenna Polarization

[TOC]


Special cases of polarization match in a transmit-receive system are studied herein.

## Polarization-Matched Antennas

If we have two polarization-matched antennas in a transmit-receive system, the polarization match
factor is equal to 1. Thus

$$\begin{equation} \rho=\frac{(1+p_1p_2)(1+p_1^*p_2^*)}{(1+p_1p_1^*)(1+p_2p_2^*)}=1
\end{equation}$$

It gives:

$$\begin{equation}(p_1-p_2^*)(p_2-p_1^*)=0 \end{equation}$$

which means

$$\begin{equation}p_1=p_2^* \end{equation}$$

and

$$\begin{equation}q_1=q_2^* \end{equation}$$

Therefore,

$$\begin{equation}\begin{cases}AR_1=AR_2 \\ \\ \tau_1=-\tau_2 \end{cases}\end{equation}$$

$\tau_1$ and $\tau_2$ are defined in different coordinate systems. $\tau_1=-\tau_2$ means the
semi-major axes of the two polarizations are coincide. For polarization-match antennas,
the rotation senses of the two polarization ellipses are identical when described in the
appropriate coordinate systems.  If we think of both antennas transmitting a right elliptic wave,
for example, the two waves will appear to rotate in opposite directions at a point in space at
which they "meet."

## Cross-Polarized Antennas

Two antennas in a transmit-receive configuration that are so polarized that no signal is received
are said to be cross-polarized. Thus, $\rho=0$. Then,

$$\begin{equation}p_1=-\frac{1}{p_2} \end{equation}$$

and

$$\begin{equation}q_1=-\frac{1}{q_2} \end{equation}$$

Therefore,

$$\begin{equation}\begin{cases}AR_1=AR_2 \\ \\ \tau_1+\tau_2=\pm\frac{\pi}{2}
\end{cases}\end{equation}$$

For cross-polarized antennas, the major axis of one polarization ellipse coincides
with the minor axis of the other. The rotation senses of the two polarization ellipses are
different when described in the appropriate coordinate systems.

## Ideal Linear Polarization to Elliptical Polarization

The polarization match factor between an ideal linear polarization and an elliptical polarization
is:

$$\begin{equation}\rho=\frac{1}{2}+\frac{(AR^2-1)\cos2\beta}{2(AR^2+1)} \end{equation}$$

where $AR$ is the axial ratio of the elliptical polarization, $\beta$ is the angle between the
linear polarization and semi-major axis of the elliptical polarization.

For linear polarization to circular polarization case, $AR=1$, then $\rho=\frac{1}{2}$ which is the
well known 3dB power mismatch loss.

## Practical Linear to Practical Circular

In practical linear polarization antenna, there is always power leakage from colinear polarization
to cross polarization. The power leakage is represented by cross polarization discrimination (XPD).
The linear antenna field can be written as:

$$\begin{equation}\mathbf{E_{LP}}=E_{0,LP}\left(\hat{x}+\frac{1}{\sqrt{XPD_{LP}}}e^{j\phi}\hat{y}
\right)=\frac{E_{0,LP}}{\sqrt{1+\gamma_{LP}^2}}\left(\hat{x}+\gamma_{LP}e^{j\phi}\hat{y} \right)
\end{equation}$$

where $XPD_{LP}=\frac{|E_x|^2}{|E_y|^2}$, $\gamma_{LP}=\frac{1}{\sqrt{XPD_{LP}}}$, $\phi$ is the
phase difference between $E_x$ and $E_y$, $E_x$ is considered as colinear direction. In practice,
the linear polarization cross-pol phase is unknown and probably random.

The practical linear polarization with limited XPD is actually an elliptical polarization whose
semi-major axis direction depends on $XPD_{LP}$ and $\phi$ and is not necessarily aligned with the
colinear direction.

The practical circular polarization field is give as:

$$\begin{equation}\mathbf{E_{CP}}=\frac{E_{0,CP}}{\sqrt{\gamma_{CP}^2+1}}\left[\left(\cos\beta-js\gamma_{CP}\sin\beta
\right)\hat{x}+\left(\sin\beta+js\gamma_{CP}\cos\beta\right)\hat{y}\right] \end{equation}$$

where $\gamma_{CP}=\frac{1}{AP_{CP}}$, $AP_{CP}$ is the axial ratio, $\beta$ is the angle between
colinear direction of the linear polarization and semi-major axis of the circular polarization, and
$s=\pm 1$ to indicate the rotation sense.

The polarization match factor can be derived as:

$$\begin{equation}\begin{split}\rho(\phi)=\frac{|\mathbf{E_{LP}^*}\cdot\mathbf{E_{CP}}|^2}{|\mathbf{E_{LP}^*}|^2|\mathbf{E_{CP}}|^2}&=\frac{1}{(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)}\left|(\cos\beta-js\gamma_{CP}\sin\beta)+\gamma_{LP}e^{-j\phi}(\sin\beta+js\gamma_{CP}\cos\beta)\right|^2
\\ \\
&=\frac{\cos^2\beta+\gamma_{CP}^2\sin^2\beta+\gamma_{LP}^2\left(\sin^2\beta+\gamma_{CP}^2\cos^2\beta\right)+2\gamma_{LP}\left[\left(1-\gamma_{CP}^2\right)\sin\beta\cos\beta\cos\phi+s\gamma_{CP}\sin\phi\right]}{(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)}
\\ \\ &=
\frac{1}{2}+\frac{(1-\gamma_{LP}^2)(1-\gamma_{CP}^2)\cos2\beta}{2(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)}+\frac{\gamma_{LP}\sqrt{4\gamma_{CP}^2+(1-\gamma_{CP}^2)^2\sin^2
2\beta}\cos(\phi-\phi_0)}{(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)}\end{split}\end{equation}$$

where $\tan\phi_0=\frac{2s\gamma_{CP}}{(1-\gamma_{CP}^2)\sin2\beta}=\frac{s\tan 2\delta}{\sin 2\beta}$, $\gamma_{CP}=\tan\delta$.

In practical antenna, cross-pol phase $\phi$ is typically unknown and often varies with frequency or
mechanical alignment. The extrema can be calculated:

$$\begin{equation}\begin{cases}\rho_{max}=\bar{\rho}+ \frac{\gamma_{LP}\sqrt{4\gamma_{CP}^2+(1-\gamma_{CP}^2)^2\sin^2
2\beta}}{(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)}, &if\space \phi=\phi_0 \\ \\ \rho_{min}=\bar{\rho}- \frac{\gamma_{LP}\sqrt{4\gamma_{CP}^2+(1-\gamma_{CP}^2)^2\sin^2
2\beta}}{(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)}, &if\space \phi=\pi+\phi_0 \end{cases} \end{equation}$$

where $\bar{\rho}$ is the average term:

$$\begin{equation}\rho=\bar{\rho}=\frac{1}{2}+\frac{(1-\gamma_{LP}^2)(1-\gamma_{CP}^2)\cos2\beta}{2(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)},
\space if \space \phi=\pm\frac{\pi}{2}+\phi_0\end{equation}$$

If $\phi$ is assumed to be random with a uniform distribution in $[0,2\pi]$, then

$$\begin{equation}\begin{cases}\left<\cos\phi \right>=0 \\ \\ \left<\sin\phi \right>=0 \\ \\
\left<e^{-j\phi} \right>=0 \end{cases}\end{equation}$$

The cross terms vanish. Thus, the averaged polarization match factor is:

$$\begin{equation}\left<\rho \right>=\bar{\rho}\end{equation}$$

In practice, $\beta$ is also unknown. The global extrema of $\rho$ are:

$$\begin{equation}\begin{cases}\rho_{gmax}=\frac{(1+\gamma_{LP}\gamma_{CP})^2}{(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)},&if
\space \beta=0,\phi=\pm\frac{\pi}{2} \\ \\
\rho_{gmin}=\frac{(1-\gamma_{LP}\gamma_{CP})^2}{(1+\gamma_{LP}^2)(1+\gamma_{CP}^2)},&if \space
\beta=0,\phi=\mp\frac{\pi}{2}\end{cases}\end{equation}$$