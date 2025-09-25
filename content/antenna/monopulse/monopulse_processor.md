Title: Monopulse Processor
Date: 2025-04-29 18:40
Status: hidden
Slug: monopulse-processor
Save_as: pages/antenna/monopulse/monopulse_processor.html
Url: pages/antenna/monopulse/monopulse_processor.html
Comments: False
Template: simple_page
Authors: Yunchi Zhang

[TOC]

Two-coordinate monopulse normally requires three receiver channels. However, systems that require
only two channels or a single channel are also reported in the technical literature.

# Single-Channel Processor

One approach to minimizing receiver complexity and lack of accurate gain and phase tracking among
the three receiver channels is to combine the sum and difference signals, either at RF or after
conversion to IF. Therefore, a single-channel receiver system is sufficient.

## Digital Monoscan using Periodic Phase Shifter

![Digital monoscan with phase shifter]({static}/antenna/monopulse/images/monoscan_with_phase_shifter.png)

*Digital monoscan using periodic phase shifter*

### Sum and Difference Signal

The sum signal of feed source is:

$$\Sigma=\Re\left\{V_0e^{j\left[\omega_ct+\phi_m(t)
\right]}\right\}=V_0\cos\left[\omega_ct+\phi_m(t)\right] $$

The difference signal of feed source is:

$$\Delta=\Re\left\{\mu V_0\left(\Delta_{EL}+j\Delta_{AZ} \right)e^{-j\psi}e^{\left[\omega_ct+\phi_m(t)+\varphi
\right]}\right\}=\mu V_0\Delta_{EL}\cos\left[\omega_ct+\phi_m(t)+\varphi-\psi\right]-\mu V_0\Delta_{AZ}\sin\left[\omega_ct+\phi_m(t)+\varphi-\psi\right] $$

where $\omega_c$ is the carrier frequency, $\varphi_m(t)$ is phase modulated telemetry signal,
$\mu$ is the difference slope, $Δ_{EL}$ is the elevation error, $Δ_{AZ}$ is the azimuth error,
$\varphi$ is the phase difference between sum and difference signal paths, $\psi$ is the
polarization angle with respect to horizon axis (0 for circular polarizations).

### Periodic Phase Shifter

The periodic phase shift function is $e^{j\theta(t)}$, where $\theta(t)$ follows a periodic
sequence.

**For 90-degree periodic phase shifter**:

$$\theta(t)=\begin{cases} 0, &0 \le t <T_s \\ \\ \frac{\pi}{2}, & T_s \le t <2T_s \\ \\ \pi, & 2T_s \le t
<3T_s \\ \\ \frac{3\pi}{2}, & 3T_s\le t < 4T_s\end{cases}$$

and

$$e^{\theta(t)}=\begin{cases} 1, &0 \le t <T_s \\ \\ j, & T_s \le t <2T_s \\ \\ -1, & 2T_s \le t
<3T_s \\ \\ -j, & 3T_s\le t < 4T_s\end{cases}$$

where $T_s=2\pi/\omega_s$, $\omega_s=2\pi f_s$, $f_s$ is the scan frequency. Since this pattern
repeats every $T_p=4T_s$, then $e^{jθ(t)}$ can be expanded as Fourier series.

$$e^{j\theta(t)}=\sum_{n=-\infty}^{\infty}C_ne^{jn\omega_pt} $$

where $\omega_p=\frac{2\pi}{T_p}=\frac{\pi}{2T_s}=\frac{\pi}{2}f_s$,
$f_p=\frac{1}{T_p}=\frac{f_s}{4}$, and

$$C_n=\frac{1}{T_p}\int_0^{T_p}e^{j\theta(t)}e^{-jn\omega_pt}dt=\begin{cases}\frac{2\sqrt{2}e^{-j\frac{\pi}{4}}}{n\pi},
&n=4k+1 \\ \\ 0, & n=others\end{cases} $$

Thus,

$$e^{j\theta(t)}=\sum_{k=-\infty}^{\infty}\frac{2\sqrt{2}e^{-j\frac{\pi}{4}}}{(4k+1)\pi}e^{j(4k+1)\omega_p
t} $$

The periodic 90-degree phase shifter results in discrete spectral components at $(4k+1)f_p=\frac{4k+1}{4}f_s$.

**For 180-degree periodic phase shifter**:

$$\theta(t)=\begin{cases}0, & 0\le t<T_s \\ \\ \pi, & T_s\le t<2T_s\end{cases}$$

and

$$e^{j\theta(t)}=\begin{cases}1, & 0 \le t<T_s \\ \\ -1, & T_s\le t<2T_s\end{cases}=\sum_{k=-\infty}^{\infty}\frac{2j}{(2k+1)\pi}e^{j(2k+1)\omega_pt} $$

where $\omega_p=\frac{\pi}{T_s}=\pi f_s$  for 180-degree periodic phase shifter. The periodic 180-degree phase
shifter results in discrete spectral components at $(2k+1)f_p=\frac{2k+1}{2} f_s$.

### Sum and Difference Signal Combination (Using 90-deg Periodic Phase Shifter)

After phase shifter, the difference signal is:

$$\begin{split}\Delta&=\Re\left\{\mu V_0\left(\Delta_{EL}+j\Delta_{AZ}
\right)e^{-j\psi}e^{j\left[\omega_c t+\phi_m(t)+\varphi\right]}e^{j\theta(t)} \right\} \\ \\
&=\sum_{k=-\infty}^{\infty}\frac{2\sqrt{2}\mu
V_0\Delta_{EL}}{(4k+1)\pi}\cos\left[\omega_ct+\phi_mt+\varphi-\psi-\frac{\pi}{4}+(4k+1)\omega_pt\right]
\\ \\ & -\sum_{k=-\infty}^{\infty}\frac{2\sqrt{2}\mu
V_0\Delta_{AZ}}{(4k+1)\pi}\sin\left[\omega_ct+\phi_mt+\varphi-\psi-\frac{\pi}{4}+(4k+1)\omega_pt\right] \end{split}$$

After summation of sum and difference channel, an amplitude and phase modulated composite signal is
created. Thus, we have

$$\begin{split}v(t)&=\sqrt{C}V_0\cos\left[\omega_ct+\phi_m(t)\right] \\ \\
&+\sum_{k=-\infty}^{\infty}\frac{2\sqrt{2}\mu
V_0\Delta_{EL}}{(4k+1)\pi}\cos\left[\omega_ct+\phi_mt+\varphi-\psi-\frac{\pi}{4}+(4k+1)\omega_pt\right]
\\ \\ & -\sum_{k=-\infty}^{\infty}\frac{2\sqrt{2}\mu
V_0\Delta_{AZ}}{(4k+1)\pi}\sin\left[\omega_ct+\phi_mt+\varphi-\psi-\frac{\pi}{4}+(4k+1)\omega_pt\right]
\end{split}$$

where $C$ is coupling value of the coupler. After down converter and AGC, this signal can be showed
in the following form.

$$\begin{split}v(t)&=\cos\left[\omega_{if}t+\phi_m(t)\right] \\ \\
&+\sum_{k=-\infty}^{\infty}\frac{2\sqrt{2}\mu
\Delta_{EL}}{(4k+1)\pi\sqrt{C}}\cos\left[\omega_{if}t+\phi_mt+\varphi-\psi-\frac{\pi}{4}+(4k+1)\omega_pt\right]
\\ \\ & -\sum_{k=-\infty}^{\infty}\frac{2\sqrt{2}\mu
\Delta_{AZ}}{(4k+1)\pi\sqrt{C}}\sin\left[\omega_{if}t+\phi_mt+\varphi-\psi-\frac{\pi}{4}+(4k+1)\omega_pt\right]
\end{split}$$

where $\omega_{if}$ is the intermediate frequency.

### Demodulation of Signal

#### Bandpass Filtering (Pre-Detection Filter)

To prevent telemetry from interfering with tracking extraction, a narrow band bandpass filter is
applied. This ensures that tracking error extraction is not disturbed by data transitions. Higher
order discrete components due to phase shifter will be filtered out as well.

To simplify the derivation, we assume only the $\omega_p$ harmonic is kept since higher order harmonics
can be filtered out after demodulation. Therefore, we have

$$\begin{split}v(t)&=\cos\left[\omega_{if}t+\phi_m(t)\right] \\ \\
&+\frac{2\sqrt{2}\mu
\Delta_{EL}}{\pi\sqrt{C}}\cos\left[\omega_{if}t+\phi_mt+\varphi-\psi-\frac{\pi}{4}+\omega_pt\right]
\\ \\ & -\frac{2\sqrt{2}\mu
\Delta_{AZ}}{\pi\sqrt{C}}\sin\left[\omega_{if}t+\phi_mt+\varphi-\psi-\frac{\pi}{4}+\omega_pt\right]
\end{split}$$

#### Tracking Error Extraction

To extract AM tracking errors, we can use square law to do the envelop detection. Thus we have the
following expression by filtering out the DC and high frequency items:

$$\begin{split}V(t)=v^2(t)
&=\frac{2\sqrt{2}\mu
\Delta_{EL}}{\pi\sqrt{C}}\cos\left[\omega_{if}t+\phi_m(t)\right]\cos\left[\omega_{if}t+\phi_mt+\varphi-\psi-\frac{\pi}{4}+\omega_pt\right]
\\ \\ & -\frac{2\sqrt{2}\mu
\Delta_{AZ}}{\pi\sqrt{C}}\cos\left[\omega_{if}t+\phi_m(t)\right]\sin\left[\omega_{if}t+\phi_mt+\varphi-\psi-\frac{\pi}{4}+\omega_pt\right]
\\ \\ &=\frac{2\sqrt{2}\mu
\Delta_{EL}}{\pi\sqrt{C}}\cos\left[\varphi-\psi-\frac{\pi}{4}+\omega_pt\right]-\frac{2\sqrt{2}\mu
\Delta_{AZ}}{\pi\sqrt{C}}\sin\left[\varphi-\psi-\frac{\pi}{4}+\omega_pt\right]
\end{split}$$

We can make $\varphi−\psi−\frac{\pi}{4}=0$ by calibration ($\psi$ can be obtained from polarizer for linear polarization
case), thus the tracking error signal is:

$$V(t)=\frac{2\sqrt{2}\mu
\Delta_{EL}}{\pi\sqrt{C}}\cos\left(\omega_pt\right)-\frac{2\sqrt{2}\mu
\Delta_{AZ}}{\pi\sqrt{C}}\sin\left(\omega_pt\right) $$

#### Synchronous Demodulation of Az/El Errors

The extracted tracking error signals can be coherently demodulated using the scan frequency:

- Multiplying with $\cos⁡(\omega_p t)$  to extract $\frac{2\sqrt{2}\mu\Delta_{EL}}{\pi\sqrt{C}}$  (Elevation error)
- Multiplying with $\sin⁡(\omega_p t)$to extract $\frac{2\sqrt{2}\mu\Delta_{AZ}}{\pi\sqrt{C}}$ (Azimuth error).
- Low-pass filtering removes residual high-frequency components.

## Monoscan

![Monoscan]({static}/antenna/monopulse/images/monoscan.png)

### Sum and Difference Signal Combination

The sum signal of feed source is:

$$\Sigma=V_0\cos\left[\omega_c t+\phi_m(t) \right] $$

The difference signal of feed source is:

$$\Delta=\mu V_0\Delta_{EL}\cos\left[\omega_ct+\phi_m(t)+\varphi-\psi \right]\cos(\omega_st)+\mu V_0\Delta_{AZ}\cos\left[\omega_ct+\phi_m(t)+\varphi-\psi \right]\sin(\omega_st) $$

where $\omega_c$ is carrier frequency, $\phi_m (t)$ is phase modulated telemetry signal, $\mu$ is the difference
slope, $\Delta_{EL}$ is the elevation error, $\Delta_{AZ}$ is the azimuth error, $\varphi$ is the phase difference between
sum and difference signal paths, $\psi$ is the polarization angle with respect to horizon axis (0 for
circular polarizations), $\omega_s$ is the scan frequency.

After monoscan and summation of sum and difference channel, an amplitude and phase modulated
composite signal is  created. Thus, we have:

$$v(t)=\sqrt{C}V_0\cos\left[\omega_ct+\phi_m(t) \right]+ \mu V_0\Delta_{EL}\cos\left[\omega_ct+\phi_m(t)+\varphi-\psi \right]\cos(\omega_st)+\mu V_0\Delta_{AZ}\cos\left[\omega_ct+\phi_m(t)+\varphi-\psi \right]\sin(\omega_st) $$

where $C$ is coupling value of the coupler. After down converter and AGC, this signal can be showed
in the following form:

$$v(t)=\cos\left[\omega_{if}t+\phi_m(t) \right]+ \frac{\mu}{\sqrt{C}}\Delta_{EL}\cos\left[\omega_{if}t+\phi_m(t)+\varphi-\psi \right]\cos(\omega_st)+\frac{\mu}{\sqrt{C}}\Delta_{AZ}\cos\left[\omega_{if}t+\phi_m(t)+\varphi-\psi \right]\sin(\omega_st) $$

where $ω_{if}$ is the intermediate frequency.

### Demodulation of Signal

#### Bandpass Filtering (Pre-Detection Filter)

To prevent telemetry from interfering with tracking extraction, a narrow band bandpass filter is
applied. This ensures that tracking error extraction is not disturbed by data transitions.

#### Tracking Error Extraction

To extract AM tracking errors, the square law envelope detection can be employed and we can have:

$$V(t)=\frac{\mu}{\sqrt{C}}\Delta_{EL}\cos\left[\varphi-\psi-\eta \right]\cos(\omega_st)+\frac{\mu}{\sqrt{C}}\Delta_{AZ}\cos\left[\varphi-\psi-\eta \right]\sin(\omega_st) $$

We can make $\phi−\psi−\eta=0$ by calibrating, thus the tracking errors are:

$$V(t)=\frac{\mu}{\sqrt{C}}\Delta_{EL}\cos(\omega_st)+\frac{\mu}{\sqrt{C}}\Delta_{AZ}\sin(\omega_st) $$

#### Synchronous Demodulation of Az/El Errors

The extracted tracking error signal can be coherently demodulated using the scan frequency:

- Multiplying with $\cos(\omega_s t)$ extracts $\frac{\mu}{\sqrt{C}}\Delta_{EL}$ (Elevation error).
- Multiplying with $\sin(\omega_s t)$  extracts $\frac{\mu}{\sqrt{C}}\Delta_{AZ}$ (Azimuth error).
- Low-pass filtering removes residual high-frequency components.

## Time Multiplexing

![Time multiplexing]({static}/antenna/monopulse/images/time_multiplexing.png)

## Frequency Multiplexing

Under Development

## SCAMP

![SCAMP]({static}/antenna/monopulse/images/scamp_monopulse.png)

# Two-Channel Processor

## Using $s \pm d$

![Two Channel Processor]({static}/antenna/monopulse/images/two_channel_processor.png)

# Three-Channel Processor

In the diagram of the various processors in this section only a single angle channel will be shown.
It is to be understood that if monopulse is used in both angular coordinates, a corresponding
processor must be added for the other coordinate.

## Using Phases and Linear Amplitudes of s and d

![Three s&d Channel Processor]({static}/antenna/monopulse/images/three_channel_s_d_processor.png)

## Using I and Q

![Three I&Q Channel Processor]({static}/antenna/monopulse/images/three_channel_I_Q_processor.png)

## Using Phases and Logarithmic Amplitudes

![Three P&logM Channel Processor]({static}/antenna/monopulse/images/three_channel_phase_logm_processor.png)

## Using Dot-Product Detector With AGC

![Three Channel dot-product Processor]({static}/antenna/monopulse/images/three_channel_dot_product_processor.png)

## Noncoherent Processor Using Sum and Difference

![Three Channel noncoherent s&d Processor]({static}/antenna/monopulse/images/three_channel_noncoho_s_d_processor.png)

## Using $ s \pm jd$

![Three Channel complex s&d Processor]({static}/antenna/monopulse/images/three_channel_complex_s_d_processor.png)
