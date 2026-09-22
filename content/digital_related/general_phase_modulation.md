Title: General Phase Modulation
Date: 2026-9-22 17:20
Category: Digital Communications
Tags: Digital, Communications, PM
Slug: general_pm
Authors: Yunchi Zhang
Summary: Describe details of general phase modulation.
Keywords: PM, PCM/PSK/PM, PCM/PM

[TOC]

## Unified PM, PCM/PM, and PCM/PSK/PM Modulation and Demodulation

### 1. Overview

This document develops a common mathematical framework for phase-modulated RF signals and uses it to describe:

- General analog phase modulation (PM)
- PCM/PM with one or more data sequences
- PCM/PSK/PM with sinusoidal or square-wave subcarriers
- PSK as a special case of phase modulation
- Pulse-shaped data sequences such as NRZ-L/M/S, BiPhase, RRC, etc.
- Residual carrier generation and carrier recovery
- Residual-carrier power and data-channel power
- Coherent demodulation
- Addition of tone-ranging signals, including major and minor ranging tones
- Practical transmitter and receiver architectures

The central idea is that all of these waveforms can be represented by a constant-envelope complex signal

$$
x(t)=\sqrt{P}\,e^{j\phi_m(t)}
$$

where the complete modulation is contained in the phase

$$
\phi_m(t)=\sum_i \theta_i s_i(t).
$$

The RF signal is then obtained by translating this complex envelope to the carrier frequency.

---

### 2. General Phase Modulation

Consider the most general PM signal

$$
S_T(t)=\sqrt{2P}
\sin\left[\omega_0t+\phi_m(t)+\phi_c(t)\right]
$$

where:

- $P$ is the average RF power,
- $\omega_0=2\pi f_0$ is the RF carrier angular frequency,
- $\phi_c(t)$ represents carrier phase/frequency errors, propagation phase, Doppler phase, etc.,
- $\phi_m(t)$ is the intentional modulation phase.

For a general PM signal,

$$
\boxed{
\phi_m(t)=\theta\,m(t)
}
$$

where $m(t)$ is a normalized modulation waveform and $\theta$ is the peak phase modulation index in radians.

More generally, with multiple phase-modulation components,

$$
\boxed{
\phi_m(t)=\sum_{i=1}^{N}\theta_i s_i(t)
}
$$

where $s_i(t)$ is normalized according to the definition of each modulation component.

The corresponding complex envelope is

$$
\boxed{
x(t)=\sqrt{P}e^{j\phi_m(t)}
}
$$

and therefore

$$
I(t)=\sqrt{P}\cos\phi_m(t),
$$

$$
Q(t)=\sqrt{P}\sin\phi_m(t).
$$

Consequently,

$$
\boxed{I^2(t)+Q^2(t)=P}.
$$

Thus ideal PM is a constant-envelope modulation.

The RF signal can be reconstructed from the complex envelope as

$$
S_T(t)=\sqrt{2}\,
\operatorname{Im}
\left\{
x(t)e^{j\omega_0t}
\right\}
$$

for the sine-carrier convention used here.

---

### 3. The Most General Unified Phase-Modulation Model

A useful model for the applications considered here is

$$
\boxed{
\phi_m(t)
=
\sum_{i=1}^{N}
\theta_i d_i(t)w_i(t)
+
\phi_R(t)
}
$$

where:

- $d_i(t)$ is a normalized data waveform,
- $w_i(t)$ is an optional subcarrier waveform,
- $\theta_i$ is the corresponding modulation index,
- $\phi_R(t)$ represents ranging or other intentional phase-modulation components.

Thus

$$
x(t)
=
\sqrt{P}
\exp\left[
j\left(
\sum_i\theta_i d_i(t)w_i(t)+\phi_R(t)
\right)
\right].
$$

This formulation is particularly useful because several apparently different modulation schemes are simply different choices of $w_i(t)$.

#### No subcarrier

$$
w_i(t)=1
$$

gives PCM/PM.

#### Sinusoidal subcarrier

$$
w_i(t)=\sin(\omega_{sci}t+\varphi_i)
$$

gives PCM/PSK/PM-type modulation.

#### Square-wave subcarrier

$$
w_i(t)=
\operatorname{sgn}
[\sin(\omega_{sci}t+\varphi_i)]
$$

gives a square-wave-subcarrier form of PCM/PSK/PM.

Here $\omega_{sci}=2\pi f_{sci}$, where $f_{sci}$ is the square-wave subcarrier's fundamental
frequency and $\varphi_i$ is its phase. The square wave alternates between $+1$ and $-1$ at
the subcarrier timing instants and contains odd harmonics of $f_{sci}$. It is therefore a
subcarrier with a frequency, not merely a sign-changing coefficient with no time scale.

Therefore PCM/PM can be viewed as a special case of the more general phase-modulation framework in which the optional subcarrier is simply

$$
\boxed{w(t)=1}.
$$

It is more precise to call this the **no-subcarrier case** rather than a subcarrier with zero frequency.

---

### 4. PCM/PM

#### 4.1 One data sequence

For one data sequence,

$$
\boxed{
\phi_m(t)=\theta d(t)
}
$$

and

$$
\boxed{
x(t)=\sqrt{P}e^{j\theta d(t)}.
}
$$

For binary data with

$$
d(t)\in\{-1,+1\},
$$

the two phase states are

$$
\phi_m=+\theta
$$

and

$$
\phi_m=-\theta.
$$

The phase separation is therefore

$$
\boxed{\Delta\phi=2\theta}.
$$

The constellation consists of two points on the unit circle.

For

$$
\theta=\frac{\pi}{2},
$$

the two states are separated by $\pi$, which is conventional BPSK.

Thus BPSK can be interpreted as a special case of binary PM.

---

### 5. PCM/PM With Multiple Data Sequences

With two data sequences,

$$
\boxed{
\phi_m(t)
=
\theta_1d_1(t)
+
\theta_2d_2(t)
}
$$

and

$$
x(t)
=
\sqrt{P}
e^{j[\theta_1d_1(t)+\theta_2d_2(t)]}.
$$

If both data sequences are binary,

$$
d_1,d_2\in\{-1,+1\},
$$

there are four possible phase states:

$$
\begin{aligned}
\phi_{++}&=+\theta_1+\theta_2,\\
\phi_{+-}&=+\theta_1-\theta_2,\\
\phi_{-+}&=-\theta_1+\theta_2,\\
\phi_{--}&=-\theta_1-\theta_2.
\end{aligned}
$$

This resembles a PSK constellation with four possible phases, but the phase states are generated as the sum of independently modulated data channels.

If

$$
\theta_1=\theta_2=\frac{\pi}{4},
$$

the four states become

$$
+\frac{\pi}{2},\quad 0,\quad 0,\quad-\frac{\pi}{2},
$$

so duplicate phase states occur. In general, the modulation indices determine whether the nominal data combinations produce distinct phase states.

---

### 6. PCM/PSK/PM

PCM/PSK/PM introduces a subcarrier into the phase modulation.

For one data channel,

$$
\boxed{
\phi_m(t)=
\theta d(t)w(t).
}
$$

The most common cases are:

#### Sinusoidal subcarrier

$$
\boxed{
\phi_m(t)=
\theta d(t)\sin(\omega_{sc}t)
}
$$

#### Square-wave subcarrier

$$
\boxed{
\phi_m(t)=
\theta d(t)c(t)
}
$$

where

$$
c(t)=\operatorname{sgn}[\sin(2\pi f_{sc}t+\varphi_{sc})]
\in\{-1,+1\}.
$$

Here $f_{sc}$ is the square-wave subcarrier's fundamental frequency and $\varphi_{sc}$ is its
phase. The receiver must be synchronized to this subcarrier timing (or estimate it) before
multiplying by $c(t)$.

The corresponding complex envelope is always

$$
x(t)=\sqrt P e^{j\phi_m(t)}.
$$

Thus the I/Q trajectory remains on a circle even though the phase may be continuously varying.

---

### 7. Relationship to PSK

PSK can be viewed as phase modulation in which the information directly selects discrete phase states.

For M-PSK,

$$
\phi_k=\phi_0+\frac{2\pi k}{M},
\qquad k=0,\ldots,M-1.
$$

The complex envelope is

$$
x_k=\sqrt P e^{j\phi_k}.
$$

Therefore:

- PM is the general continuous-phase framework.
- PSK is a discrete-phase special case.
- BPSK is binary phase modulation with phase separation $\pi$.
- QPSK is four-state phase modulation.
- PCM/PM can generate discrete phase states when $d(t)$ is discrete.
- PCM/PSK/PM additionally imposes a subcarrier waveform on the phase.

---

### 8. Data Waveform $d(t)$

The data waveform does not have to be an ideal rectangular NRZ waveform.

A general pulse-shaped sequence can be written as

$$
\boxed{
d(t)=\sum_k a_kp(t-kT_b)
}
$$

where:

- $a_k$ is the data symbol,
- $T_b$ is the symbol/bit interval,
- $p(t)$ is the pulse shape.

Possible pulse shapes include:

- NRZ-L
- NRZ-M
- NRZ-S
- BiPhase
- rectangular
- raised cosine
- root-raised cosine
- half-sine
- Gaussian
- custom FIR pulse shapes

For PM, the pulse shape is applied to the **phase argument**:

$$
\boxed{
\phi_m(t)=\theta d(t).
}
$$

This is fundamentally different from ordinary linear amplitude modulation, where the pulse-shaped waveform directly scales amplitude.

For example, with RRC pulse shaping,

$$
\phi_m(t)=
\theta
\sum_k a_kp_{\mathrm{RRC}}(t-kT_b).
$$

The resulting RF signal still has constant envelope.

---

### 9. I/Q Interpretation

After ideal carrier downconversion, the complex baseband signal is

$$
r(t)=A e^{j[\phi_c(t)+\phi_m(t)]}+n(t).
$$

If the carrier phase has been removed,

$$
r_c(t)\approx A e^{j\phi_m(t)}.
$$

Then

$$
I(t)=A\cos\phi_m(t),
$$

$$
Q(t)=A\sin\phi_m(t).
$$

Therefore

$$
I^2+Q^2=A^2.
$$

The modulation information is carried by the **angle** of the I/Q vector, not its radius.

This gives a useful distinction:

| Modulation | Radius | Phase |
|---|---|---|
| PM | Constant | Varies |
| PSK | Constant | Discrete |
| QAM | Varies | Varies |
| FM | Constant | Time integral of frequency deviation |

---

### 10. General Demodulation

The receiver problem is to recover

$$
d_i(t)
$$

from the measured phase.

The ideal conceptual sequence is

$$
\boxed{
r(t)
\rightarrow
\text{carrier recovery}
\rightarrow
\text{derotation}
\rightarrow
\text{phase extraction}
\rightarrow
\text{subcarrier separation}
\rightarrow
\text{matched filtering}
\rightarrow
\text{data decisions}
}
$$

After carrier correction,

$$
r_c(t)
=
r(t)e^{-j\hat\phi_c(t)}
\approx
A e^{j\phi_m(t)}.
$$

Then

$$
\boxed{
\hat\phi_m(t)=\arg[r_c(t)]
}
$$

with phase unwrapping as required.

For a small-noise/high-SNR conceptual model,

$$
\hat\phi_m(t)\approx\phi_m(t)+\text{phase noise}.
$$

---

### 11. Demodulation of PCM/PM

For

$$
\phi_m(t)=\theta d(t),
$$

the recovered data waveform is simply

$$
\boxed{
\hat d(t)=\frac{\hat\phi_m(t)}{\theta}.
}
$$

For pulse-shaped data,

$$
\hat d(t)
\rightarrow
\text{matched filter}
\rightarrow
\text{symbol sampler}
\rightarrow
\hat a_k.
$$

For a pulse $p(t)$, the matched filter is

$$
h(t)=p^*(-t).
$$

For an RRC transmit pulse, an RRC receive filter produces the overall raised-cosine response.

---

### 12. Demodulation of PCM/PSK/PM

For a sinusoidal subcarrier,

$$
\phi_m(t)
=
\theta d(t)\sin(\omega_{sc}t).
$$

After phase extraction,

$$
\hat\phi_m(t)
\approx
\theta d(t)\sin(\omega_{sc}t).
$$

A coherent subcarrier demodulator multiplies by the recovered subcarrier:

$$
u(t)=
\hat\phi_m(t)\sin(\omega_{sc}t).
$$

Using

$$
\sin^2x=
\frac{1-\cos2x}{2},
$$

we obtain

$$
u(t)
=
\frac{\theta d(t)}{2}
-
\frac{\theta d(t)}{2}\cos(2\omega_{sc}t).
$$

Low-pass filtering gives

$$
\boxed{
\operatorname{LPF}\{u(t)\}
=
\frac{\theta}{2}d(t).
}
$$

Therefore

$$
\boxed{
\hat d(t)
=
\frac{2}{\theta}
\operatorname{LPF}
\left\{
\hat\phi_m(t)\sin(\omega_{sc}t)
\right\}.
}
$$

The factor of two comes from the sinusoidal subcarrier power normalization.

---

### 13. Square-Wave Subcarrier Demodulation

For

$$
w(t)=c(t)=\operatorname{sgn}[\sin(2\pi f_{sc}t+\varphi_{sc})]
\in\{-1,+1\},
$$

where $f\_{sc}$ is the square-wave subcarrier frequency,

we have

$$
\phi_m(t)=\theta d(t)c(t).
$$

Since

$$
c^2(t)=1,
$$

multiplication by the synchronized subcarrier gives

$$
\phi_m(t)c(t)=\theta d(t).
$$

Therefore

$$
\boxed{
\hat d(t)
=
\frac{1}{\theta}
\hat\phi_m(t)c(t).
}
$$

A subsequent matched filter recovers the data symbols. This assumes a unit-amplitude ($\pm1$)
square wave and synchronized subcarrier timing. If the square wave is scaled by an amplitude
$A*{sc}$, the result must instead be divided by $\theta A*{sc}^2$.

Unlike the sinusoidal case, no factor of two is required when the square wave has amplitude $\pm1$.

---

### 14. Multiple Data Channels

For

$$
\phi_m(t)=
\sum_i\theta_i d_i(t)w_i(t),
$$

the receiver can separate channels using correlation.

For orthogonal sinusoidal subcarriers,

$$
\hat d_i(t)
\propto
\operatorname{LPF}
\left\{
\hat\phi_m(t)
\sin(\omega_{sci}t)
\right\}.
$$

More generally, each channel can be extracted by projection onto its known basis function.

The important requirement is that the subcarrier/basis waveforms be sufficiently orthogonal over the integration interval.

If multiple data channels are not orthogonal, residual cross-coupling remains after demodulation.

#### 14.1 How to verify orthogonality

For an integration interval of duration $T$, define the normalized inner
product of two real basis waveforms as

$$
\langle w_i,w_j\rangle*T
=
\frac{1}{T}\int_{t_0}^{t_0+T}w_i(t)w_j(t)\,dt.
$$

The waveforms are orthogonal over this interval when

$$
\boxed{
\langle w_i,w_j\rangle_T=0,
\qquad i\ne j.
}
$$

The interval $T$ is not inherently the symbol period. For data with symbol
interval $T_b$, the symbol rate is

$$
R_s=\frac{1}{T_b}.
$$

In a practical receiver, choose the coherent integration interval to cover an integer number of complete symbols,

$$
T=M T_b,
\qquad M\in\mathbb{Z}_{>0},
$$

and align its start and end with symbol boundaries. If the data symbols or
pulse shape change within the interval, the receiver normally performs this
operation per symbol or uses a matched filter rather than assuming that one
long interval has a constant data value. Thus $T$ is a receiver/design
choice, while $T_b$ is set by the data symbol rate.

In practice, form the Gram matrix

$$
G_{ij}=\langle w_i,w_j\rangle_T.
$$

The diagonal terms give the waveform energies and the off-diagonal terms
measure cross-coupling. A useful normalized measure is

$$
\boxed{
\rho_{ij}
=
\frac{\langle w_i,w_j\rangle_T}
{\sqrt{\langle w_i,w_i\rangle_T\langle w_j,w_j\rangle_T}}.
}
$$

The magnitude $|\rho_{ij}|$ should be below the allowed interference or
error budget. Exact zero is ideal; finite observation time, timing error,
frequency error, filtering, and sampling usually make the measured value
nonzero.

##### Sinusoidal subcarriers

For subcarriers $w_i(t)=\sin(2\pi f_i t+\varphi_i)$, choose the coherent
integration interval so that it contains an integer number of cycles of every
subcarrier. A sufficient condition is

$$
f_iT=N_i,
\qquad N_i\in\mathbb{Z},
$$

for every $i$, with distinct frequencies represented by distinct integer
cycle counts. Equivalently, choose a common base frequency $\Delta f=1/T$
and use $f_i=k_i\Delta f$ with distinct integers $k_i$. Under these
conditions, distinct sinusoidal basis functions are orthogonal, subject to
accurate frequency and phase synchronization.

With $T=M T_b$, this condition can also be written as

$$
f_i=\frac{k_i}{M T_b}=\frac{k_i}{M}R_s.
$$

For the simple one-symbol case $M=1$, each subcarrier has an integer
number of cycles per symbol: $f_i=k_iR_s$. Other choices of $M$ permit
fractional multiples of the symbol rate while retaining orthogonality over
the full $M$-symbol integration interval.

This is related to, but not the same as, the orthogonality used by MSK. MSK
is continuous-phase binary FSK with modulation index $h=1/2$. Its two
instantaneous frequency tones have offsets $\pm 1/(4T_b)$ from the carrier,
and its signal-space behavior depends on phase continuity and the complete
symbol waveform. Therefore MSK should not be interpreted as using
subcarriers whose frequencies are simply integer multiples of $R_s$. The
same inner-product test still applies, but it must be applied to the actual
MSK waveforms over the receiver's detection interval. GMSK additionally uses
Gaussian pulse shaping and is generally not strictly orthogonal in the same
ideal sense.

If the interval does not contain integer cycles, the cross terms generally do
not integrate to zero. Increasing $T$, aligning the integration window, or
using a longer matched filter reduces this leakage.

##### Square-wave subcarriers

For square waves, use the same Gram-matrix calculation with

$$
w_i(t)=\operatorname{sgn}[\sin(2\pi f_i t+\varphi_i)].
$$

Do not assume that distinct square-wave frequencies are automatically
orthogonal. Each square wave contains odd harmonics, and harmonics from two
channels can overlap. Choose frequencies and phases, evaluate $G_{ij}$ over
the actual symbol or integration interval, and reject a set whose normalized
cross-correlation exceeds the system budget. If a non-orthogonal set must be
used, jointly recover the channels with the Gram matrix:

$$
\mathbf{z}=\mathbf{G}\mathbf{a},
\qquad
\hat{\mathbf{a}}=\mathbf{G}^{-1}\mathbf{z},
$$

provided $\mathbf{G}$ is well-conditioned and the receiver knows the
waveforms accurately.

---

### 15. Carrier Recovery Is a Special Issue for PM

The received signal contains both carrier phase and modulation phase:

$$
r(t)=
A e^{j[\phi_c(t)+\phi_m(t)]}+n(t).
$$

The receiver directly observes only

$$
\boxed{
\phi_{\mathrm{obs}}(t)
=
\phi_c(t)+\phi_m(t).
}
$$

Therefore the carrier phase cannot, in general, be separated from the modulation phase without additional information.

Useful mechanisms include:

1. Residual carrier
2. Pilot/reference carrier
3. Known preamble
4. Data-aided carrier recovery
5. Decision-directed recovery
6. Time-scale separation between carrier dynamics and modulation

For the systems considered here, the **residual carrier** is particularly useful.

---

### 16. Residual Carrier

Define the complex envelope

$$
x(t)=\sqrt P e^{j\phi_m(t)}.
$$

The residual carrier is the spectral line at zero frequency in the complex-envelope domain.

Its normalized complex amplitude is

$$
\boxed{
C_0=
\left\langle
e^{j\phi_m(t)}
\right\rangle
}
$$

where $\langle\cdot\rangle$ denotes an appropriate time or ensemble average.

Thus

$$
x(t)
=
\sqrt P C_0
+
x_{\mathrm{AC}}(t).
$$

The residual carrier power is

$$
\boxed{
P_c=P|C_0|^2.
}
$$

The carrier-to-total-power ratio is therefore

$$
\boxed{
\frac{P_c}{P}=|C_0|^2.
}
$$

In dBc,

$$
\boxed{
C_{\mathrm{dBc}}
=
10\log_{10}\frac{P_c}{P}
=
20\log_{10}|C_0|.
}
$$

The residual carrier has complex phase

$$
\phi_{C_0}=\arg C_0.
$$

This phase can be absorbed into the receiver carrier reference.

---

### 17. Residual Carrier for Binary PCM/PM

For balanced binary data,

$$
d=\pm1
$$

with equal probability,

$$
\phi_m=\theta d.
$$

Therefore

$$
C_0
=
\frac12e^{j\theta}
+
\frac12e^{-j\theta}.
$$

Using Euler's identity,

$$
\boxed{
C_0=\cos\theta.
}
$$

Consequently,

$$
\boxed{
P_c=P\cos^2\theta
}
$$

and

$$
\boxed{
C_{\mathrm{dBc}}
=
20\log_{10}|\cos\theta|.
}
$$

This immediately shows why the residual carrier depends strongly on modulation index.

The carrier disappears when

$$
\cos\theta=0,
$$

i.e.

$$
\boxed{
\theta=\frac{\pi}{2},
\frac{3\pi}{2},
\ldots
}
$$

For the usual first quadrant,

$$
\theta=\frac{\pi}{2}.
$$

That is exactly the BPSK point.

---

### 18. Unbalanced Binary Data

If

$$
P(d=+1)=p
$$

and

$$
P(d=-1)=1-p,
$$

then

$$
C_0=
pe^{j\theta}
+
(1-p)e^{-j\theta}.
$$

Therefore

$$
C_0=
\cos\theta
+
j(2p-1)\sin\theta.
$$

Its magnitude squared is

$$
\boxed{
|C_0|^2
=
\cos^2\theta
+
(2p-1)^2\sin^2\theta.
}
$$

Thus the residual carrier can increase when the data sequence has a nonzero statistical bias.

---

### 19. Residual Carrier for Sinusoidal PCM/PSK/PM

Consider

$$
\phi_m(t)
=
\theta d(t)\sin(\omega_{sc}t).
$$

For balanced binary data and sufficiently representative averaging,

$$
C_0
=
\left\langle
e^{j\theta d\sin(\omega_{sc}t)}
\right\rangle.
$$

For either $d=+1$ or $d=-1$,

$$
\left\langle
e^{\pm j\theta\sin x}
\right\rangle
=
J_0(\theta),
$$

where $J_0$ is the zeroth-order Bessel function of the first kind.

Therefore

$$
\boxed{
C_0=J_0(\theta).
}
$$

The residual carrier power is

$$
\boxed{
P_c=P J_0^2(\theta).
}
$$

and

$$
\boxed{
C_{\mathrm{dBc}}
=
20\log_{10}|J_0(\theta)|.
}
$$

The first zero of $J_0$ occurs at approximately

$$
\boxed{
\theta=2.4048\ \mathrm{rad}.
}
$$

At this modulation index the residual carrier theoretically disappears.

---

### 20. Residual Carrier for Square-Wave PCM/PSK/PM

For

$$
w(t)=c(t)\in\{-1,+1\}
$$

and

$$
d(t)\in\{-1,+1\},
$$

the product

$$
d(t)c(t)
$$

is also $\pm1$.

Thus

$$
\phi_m=\pm\theta
$$

and for balanced states,

$$
\boxed{
C_0=\cos\theta.
}
$$

Consequently,

$$
\boxed{
P_c=P\cos^2\theta.
}
$$

This is different from the sinusoidal-subcarrier case, whose carrier coefficient is $J_0(\theta)$.

---

### 21. Multiple Phase-Modulation Components

For

$$
\phi_m(t)
=
\sum_i\theta_i s_i(t),
$$

the exact residual carrier coefficient is

$$
\boxed{
C_0=
\left\langle
\exp
\left[
j\sum_i\theta_i s_i(t)
\right]
\right\rangle.
}
$$

Equivalently,

$$
C_0=
\left\langle
\prod_i
e^{j\theta_i s_i(t)}
\right\rangle.
$$

It is tempting to write

$$
C_0=\prod_i C_{0,i},
$$

but this factorization requires suitable independence/separability assumptions.

It is not valid for arbitrary correlated data or synchronized deterministic waveforms.

When the relevant processes are statistically independent,

$$
\boxed{
C_0=
\prod_i C_{0,i}.
}
$$

Then

$$
\boxed{
P_c
=
P\prod_i|C_{0,i}|^2.
}
$$

---

### 22. Data-Channel Power

Because ideal PM is constant envelope,

$$
P_{\mathrm{total}}=P.
$$

The residual carrier consumes

$$
P_c=P|C_0|^2.
$$

Therefore the total power not contained in the residual carrier is

$$
\boxed{
P_{\mathrm{AC}}
=
P-P_c
=
P(1-|C_0|^2).
}
$$

This is the total **non-residual-carrier power**.

It is important to distinguish this from the power of a particular data channel.

For a waveform containing several data channels,

$$
P_{\mathrm{AC}}
$$

includes all non-carrier spectral components, including:

- data sidebands,
- subcarrier components,
- intermodulation/cross terms,
- harmonics generated by nonlinear phase mapping,
- ranging tones,
- interactions among phase-modulation components.

Therefore,

$$
\boxed{
P_{\mathrm{AC}}\neq
\text{power of one particular data channel}
}
$$

in general.

A particular channel's power should instead be determined by integrating the corresponding spectral components or by defining an appropriate matched-filter/correlation output.

---

### 23. Small-Modulation Approximation

For small phase modulation,

$$
|\phi_m(t)|\ll1,
$$

we can write

$$
e^{j\phi_m}
\approx
1+j\phi_m-\frac{\phi_m^2}{2}.
$$

Therefore

$$
x(t)
\approx
\sqrt P
\left[
1+j\phi_m(t)-\frac{\phi_m^2(t)}{2}
\right].
$$

The carrier term is approximately

$$
C_0
\approx
1-\frac12\langle\phi_m^2\rangle
+j\langle\phi_m\rangle.
$$

For zero-mean modulation,

$$
\boxed{
|C_0|^2
\approx
1-\langle\phi_m^2\rangle.
}
$$

Hence the non-carrier power is approximately

$$
\boxed{
P_{\mathrm{AC}}
\approx
P\langle\phi_m^2\rangle.
}
$$

This is a very useful approximation for link-budget calculations involving relatively small phase-modulation indices.

---

### 24. Tone Ranging Added to PM

A ranging signal can be added directly to the phase.

Suppose there are two ranging tones:

- major tone: frequency $f_M$, modulation index $\theta_M$
- minor tone: frequency $f_m$, modulation index $\theta_m$

Then

$$
\boxed{
\phi_R(t)
=
\theta_M\sin(\omega_Mt+\psi_M)
+
\theta_m\sin(\omega_mt+\psi_m)
}
$$

where

$$
\omega_M=2\pi f_M,
\qquad
\omega_m=2\pi f_m.
$$

The complete phase becomes

$$
\boxed{
\phi(t)
=
\phi_{\mathrm{data}}(t)
+
\theta_M\sin(\omega_Mt+\psi_M)
+
\theta_m\sin(\omega_mt+\psi_m).
}
$$

The transmitted complex envelope is

$$
\boxed{
x(t)=
\sqrt P
e^{j\phi(t)}.
}
$$

Thus tone ranging is naturally just another phase-modulation component.

---

### 25. Ranging as Phase Modulation

Consider first a single tone:

$$
x(t)
=
\sqrt P
e^{j\theta_R\sin\omega_Rt}.
$$

Using the Jacobi-Anger expansion,

$$
e^{j\theta_R\sin\omega_Rt}
=
\sum_{n=-\infty}^{\infty}
J_n(\theta_R)
e^{jn\omega_Rt}.
$$

Therefore the RF spectrum contains:

- a carrier component,
- first-order ranging sidebands,
- second-order sidebands,
- higher-order sidebands.

The complex-envelope amplitude of the $n$-th order ranging component is

$$
\boxed{
J_n(\theta_R).
}
$$

The corresponding power fraction is

$$
\boxed{
P_n/P=J_n^2(\theta_R).
}
$$

For small $\theta_R$,

$$
J_0(\theta_R)\approx1-\frac{\theta_R^2}{4},
$$

$$
J_1(\theta_R)\approx\frac{\theta_R}{2},
$$

and higher-order terms become progressively smaller.

Thus the first-order ranging sidebands contain approximately

$$
\boxed{
P_{\pm1}/P
\approx
\frac{\theta_R^2}{4}
}
$$

each.

The combined first-order sideband power is approximately

$$
\boxed{
P_{+1}+P_{-1}
\approx
\frac{\theta_R^2}{2}P.
}
$$

---

### 26. Major and Minor Ranging Tones

With two tones,

$$
\phi_R(t)
=
\theta_M\sin\omega_Mt
+
\theta_m\sin\omega_mt,
$$

the envelope is

$$
x_R(t)
=
\sqrt P
e^{j\theta_M\sin\omega_Mt}
e^{j\theta_m\sin\omega_mt}.
$$

Expanding both terms gives

$$
x_R(t)
=
\sqrt P
\sum_{k=-\infty}^{\infty}
\sum_{\ell=-\infty}^{\infty}
J_k(\theta_M)
J_\ell(\theta_m)
e^{j(k\omega_M+\ell\omega_m)t}.
$$

Therefore the ranging spectrum contains components at

$$
\boxed{
f=kf_M+\ell f_m.
}
$$

The corresponding power fraction is approximately

$$
\boxed{
P_{k,\ell}/P
=
J_k^2(\theta_M)
J_\ell^2(\theta_m)
}
$$

when the individual spectral components are resolved.

The residual carrier contribution from the two ranging tones alone is

$$
\boxed{
P_c/P
=
J_0^2(\theta_M)
J_0^2(\theta_m).
}
$$

For small modulation indices,

$$
P_c/P
\approx
1-\frac{\theta_M^2+\theta_m^2}{2}.
$$

---

### 27. Ranging Combined With Data Modulation

The complete phase may be written

$$
\boxed{
\phi_m(t)
=
\phi_D(t)+\phi_R(t)
}
$$

with

$$
\phi_D(t)
=
\sum_i\theta_i d_i(t)w_i(t)
$$

and

$$
\phi_R(t)
=
\theta_M\sin\omega_Mt
+
\theta_m\sin\omega_mt.
$$

Therefore

$$
x(t)
=
\sqrt P
e^{j\phi_D(t)}
e^{j\phi_R(t)}.
$$

This factorization is extremely useful conceptually.

The data modulation and ranging modulation are both phase modulation, but they can be separated at the receiver because their spectral/time-domain structures are different.

Under suitable independence/orthogonality assumptions, the residual carrier coefficient becomes approximately

$$
\boxed{
C_0
=
C_{0,D}
J_0(\theta_M)
J_0(\theta_m).
}
$$

Consequently,

$$
\boxed{
P_c
=
P
|C_{0,D}|^2
J_0^2(\theta_M)
J_0^2(\theta_m).
}
$$

---

### 28. Ranging Demodulation

After carrier recovery and data-component handling, a receiver can correlate the recovered phase with the known ranging tones.

For the major tone,

$$
\hat\theta_M
\propto
\left\langle
\hat\phi(t)\sin(\omega_Mt+\psi_M)
\right\rangle.
$$

Likewise,

$$
\hat\theta_m
\propto
\left\langle
\hat\phi(t)\sin(\omega_mt+\psi_m)
\right\rangle.
$$

The correlation interval should be selected so that unwanted components average toward zero.

A practical ranging receiver may therefore use:

$$
\boxed{
\text{carrier recovery}
\rightarrow
\text{phase extraction}
\rightarrow
\text{ranging correlators}
\rightarrow
\text{tone phase/amplitude estimation}
}
$$

and a parallel branch for the data channel.

---

### 29. Important Distinction: Carrier, Ranging Tones, and Data

The phase-modulated RF spectrum can contain several conceptually different components.

| Component | Origin | Receiver function |
|---|---|---|
| Residual carrier | $C_0$ | Carrier recovery |
| Major ranging tone | $\theta_M$ | Range measurement |
| Minor ranging tone | $\theta_m$ | Fine range measurement |
| Data sidebands | $d_i(t)$ | Data recovery |
| Subcarrier components | $w_i(t)$ | Data channel separation |
| Higher-order PM products | Nonlinear $e^{j\phi}$ mapping | Usually part of modulation spectrum |

The total RF power is still

$$
P.
$$

Power is redistributed among these spectral components; ideal PM does not change the envelope power.

---

### 30. Carrier Recovery Using the Residual Carrier

Suppose

$$
x(t)
=
\sqrt P
C_0e^{j\phi_c(t)}
+
x_{\mathrm{SB}}(t).
$$

If $C_0\neq0$, the carrier line provides a direct phase reference.

A narrowband PLL can lock primarily to this component:

$$
\hat\phi_c(t)
\approx
\phi_c(t)+\arg C_0.
$$

The receiver then derotates:

$$
\boxed{
r_{\mathrm{corr}}(t)
=
r(t)e^{-j\hat\phi_c(t)}.
}
$$

Ideally,

$$
r_{\mathrm{corr}}(t)
\approx
A e^{j\phi_m(t)}.
$$

The constant phase $\arg C_0$ is simply part of the carrier reference and normally does not need to be separately known.

The PLL bandwidth should be selected carefully:

- Too wide: it follows modulation and removes part of the desired phase information.
- Too narrow: it may not track Doppler or oscillator dynamics.
- Appropriate bandwidth: it tracks the residual carrier while rejecting most modulation sidebands.

---

### 31. A Unified Receiver Architecture

A practical receiver can therefore be organized as

```text
                 ┌──────────────────┐
RF input ───────►│ Downconversion   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Residual-carrier │
                 │ PLL / carrier    │
                 │ recovery         │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Carrier derotate │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ atan2 / phase    │
                 │ extraction       │
                 └────────┬─────────┘
                          │
              ┌───────────┴────────────┐
              │                        │
              ▼                        ▼
       Ranging branch             Data branch
              │                        │
       tone correlation          subcarrier
       major/minor               demodulation
              │                        │
              │                  matched filter
              │                        │
              │                  symbol decision
              ▼                        ▼
       range estimate              data bits
```

This architecture separates the fundamentally different receiver functions.

---

### 32. Phase Unwrapping and Practical Noise

The operation

$$
\hat\phi(t)=\operatorname{atan2}(Q,I)
$$

returns phase modulo $2\pi$.

If the phase excursion can cross $\pm\pi$, phase unwrapping may be required.

However, direct phase extraction is mainly a conceptual model. In a practical low-SNR receiver, an optimum receiver does not necessarily need to explicitly form

$$
\operatorname{atan2}(Q,I).
$$

Equivalent processing can be implemented with:

- complex correlation,
- matched filtering,
- Costas/PLL structures,
- maximum-likelihood phase estimation,
- decision-directed carrier recovery,
- digital phase discriminators.

The mathematical phase representation remains useful even when the implementation uses a different estimator.

---

### 33. Arbitrary Pulse-Shaped Data and Residual Carrier

For arbitrary

$$
d(t)=\sum_k a_kp(t-kT_b),
$$

the residual carrier is still

$$
\boxed{
C_0=
\left\langle
e^{j\theta d(t)}
\right\rangle.
}
$$

It is generally **not** sufficient to replace this with

$$
e^{j\theta\langle d(t)\rangle}.
$$

Because the exponential is nonlinear,

$$
\left\langle e^{j\theta d}\right\rangle
\neq
e^{j\theta\langle d\rangle}
$$

in general.

Therefore pulse shape, symbol statistics, transition regions, and deterministic data patterns can all affect the exact residual carrier.

For ideal rectangular binary NRZ with balanced symbols, the simple result

$$
C_0=\cos\theta
$$

is recovered.

---

### 34. Deterministic Sequence Versus Random Data

There are two useful interpretations of residual carrier.

#### Periodic/deterministic waveform

For a periodic sequence with period $T$,

$$
C_0=
\frac1T
\int_0^T
e^{j\phi_m(t)}dt.
$$

#### Random data

For an ergodic random process,

$$
C_0=
E\left[e^{j\phi_m(t)}\right].
$$

These definitions become equivalent when a sufficiently long observation is representative of the ensemble.

For simulation and spectrum analysis, it is therefore important to distinguish:

- finite-length FFT carrier bin,
- periodic-sequence spectral line,
- ensemble-average residual carrier,
- long-term measured carrier power.

---

### 35. Power Conservation

For ideal phase modulation,

$$
|x(t)|^2=P.
$$

Therefore

$$
\boxed{
P_{\mathrm{total}}=P.
}
$$

If all spectral components are accounted for,

$$
P=
P_c+
P_{\mathrm{data}}
+
P_{\mathrm{ranging}}
+
P_{\mathrm{other}}.
$$

The exact partition depends on how the spectral components are defined.

For a single sinusoidal PM tone,

$$
P
=
P
\sum_{n=-\infty}^{\infty}
J_n^2(\theta)
$$

because

$$
\boxed{
\sum_{n=-\infty}^{\infty}J_n^2(\theta)=1.
}
$$

Thus

$$
P_c=PJ_0^2(\theta)
$$

and the remainder is

$$
P-P_c
=
P\left[1-J_0^2(\theta)\right].
$$

This is a useful exact demonstration of power conservation in PM.

---

### 36. Practical Modulation-Index Considerations

The modulation index controls several competing quantities:

- residual carrier power,
- sideband/data-channel power,
- phase separation,
- receiver sensitivity,
- interference between phase-modulation components,
- carrier-recovery margin.

For binary PCM/PM,

$$
P_c/P=\cos^2\theta.
$$

For sinusoidal PCM/PSK/PM,

$$
P_c/P=J_0^2(\theta).
$$

Thus the same numerical modulation index does **not** produce the same residual carrier power for different subcarrier waveforms.

This is one of the most important consequences of the unified formulation.

---

### 37. Recommended Mathematical Model for Simulation

For a comprehensive digital simulator, it is useful to define the total phase as

$$
\boxed{
\phi(t)
=
\phi_{\mathrm{carrier}}(t)
+
\phi_{\mathrm{data}}(t)
+
\phi_{\mathrm{ranging}}(t)
+
\phi_{\mathrm{channel}}(t)
}
$$

where

$$
\phi_{\mathrm{data}}(t)
=
\sum_i\theta_i d_i(t)w_i(t),
$$

and

$$
\phi_{\mathrm{ranging}}(t)
=
\sum_r\theta_{R,r}
\sin(\omega_{R,r}t+\psi_{R,r}).
$$

Then

$$
\boxed{
x(t)
=
\sqrt P
e^{j\phi(t)}.
}
$$

The RF waveform is

$$
\boxed{
S_T(t)
=
\sqrt{2P}
\sin[\omega_0t+\phi(t)].
}
$$

This model provides a single implementation path for:

- PCM/PM
- PCM/PSK/PM
- multiple data channels
- ranging
- residual carrier
- Doppler
- carrier phase error
- oscillator phase noise
- channel phase distortion

---

### 38. Suggested Software Abstraction

A simulator can represent each phase-modulation component as

$$
\phi_i(t)=\theta_i s_i(t)
$$

and sum all components:

```text
phase = carrier_phase

for component in phase_components:
    phase += component.modulation_index * component.waveform(t)

x = sqrt(P) * exp(1j * phase)
```

A component can represent:

```text
DataComponent
    waveform = d(t)
    index = theta

SubcarrierDataComponent
    waveform = d(t) * w(t)
    index = theta

RangingTone
    waveform = sin(omega*t + phase)
    index = theta_R
```

This makes PCM/PM and PCM/PSK/PM naturally instances of the same software architecture.

---

### 39. Summary of Important Special Cases

| Waveform | Phase modulation |
|---|---|
| General PM | $\theta m(t)$ |
| PCM/PM | $\theta d(t)$ |
| Two-channel PCM/PM | $\theta_1d_1+\theta_2d_2$ |
| Sinusoidal PCM/PSK/PM | $\theta d(t)\sin\omega_{sc}t$ |
| Square-wave PCM/PSK/PM | $\theta d(t)\operatorname{sgn}[\sin(2\pi f_{sc}t+\varphi_{sc})]$ |
| BPSK | discrete phase states separated by $\pi$ |
| M-PSK | $\phi_k=2\pi k/M$ |
| Single ranging tone | $\theta_R\sin\omega_Rt$ |
| Two ranging tones | $\theta_M\sin\omega_Mt+\theta_m\sin\omega_mt$ |

---

### 40. Key Residual-Carrier Results

For balanced binary PCM/PM:

$$
\boxed{
C_0=\cos\theta
}
$$

$$
\boxed{
P_c=P\cos^2\theta
}
$$

For sinusoidal-subcarrier PCM/PSK/PM:

$$
\boxed{
C_0=J_0(\theta)
}
$$

$$
\boxed{
P_c=PJ_0^2(\theta)
}
$$

For square-wave-subcarrier PCM/PSK/PM:

$$
\boxed{
C_0=\cos\theta
}
$$

$$
\boxed{
P_c=P\cos^2\theta
}
$$

For arbitrary modulation:

$$
\boxed{
C_0=
\left\langle e^{j\phi_m(t)}\right\rangle
}
$$

$$
\boxed{
P_c=P|C_0|^2
}
$$

and

$$
\boxed{
P_{\mathrm{noncarrier}}
=
P(1-|C_0|^2).
}
$$

---

### 41. Final Conceptual Picture

The most useful way to think about these systems is:

$$
\boxed{
\text{Data/ranging information}
\rightarrow
\text{phase waveform}
\rightarrow
e^{j\phi(t)}
\rightarrow
\text{constant-envelope RF}
}
$$

The receiver performs the inverse operations:

$$
\boxed{
\text{RF}
\rightarrow
\text{complex baseband}
\rightarrow
\text{residual-carrier recovery}
\rightarrow
\text{phase recovery}
\rightarrow
\text{data/ranging separation}.
}
$$

The unifying principle is that PCM/PM, PCM/PSK/PM, PSK, and tone ranging are not fundamentally separate modulation mechanisms. They are different ways of constructing the phase function

$$
\boxed{
\phi_m(t).
}
$$

Once that phase function is defined, the transmitted waveform, I/Q trajectory, residual carrier, spectral distribution, and receiver architecture follow from

$$
\boxed{
x(t)=\sqrt P e^{j\phi_m(t)}.
}
$$

This is the central mathematical framework for analyzing and implementing the family of constant-envelope phase-modulated telemetry and ranging waveforms.
