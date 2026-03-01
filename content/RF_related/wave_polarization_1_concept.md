Title: Polarizations Part 1: Concept
series: Polarizations
series_index: 1
Date: 2026-2-16 15:47
Category: Antenna
Tags: Antenna, Polarization
Slug: antenna_polarization_1
Authors: Yunchi Zhang
Summary: Wave polarization concept.
Keywords: Antenna Polarization

[TOC]


Electromagnetic (EM) wave polarization describes the geometric orientation and time evolution of
the electric field vector **E** at a fixed point in space. Because the magnetic field **B** is orthogonal
to **E** and to the direction of propagation (from Maxwell’s equations), polarization is fully
characterized by the behavior of **E** in the transverse plane.

For a monochromatic plane wave propagating in the +z direction:

$$
\begin{equation}
\mathbf{E}(z,t) = \mathfrak{R}\left\{(E_x\hat{x}+E_y\hat{y})e^{j(\omega t-kz)} \right\} \label{eq:gen_wave_pol}
\end{equation}
$$

Polarization depends on the relative amplitudes and phase difference between $E_x$ and $E_y$.

A general case of tilted elliptical polarization is illustrated in the following figure.

![Tilted polarization ellipse]({static}/RF_related/images/ellip_polarization.png)

## Polarization in Cartesian Coordinate System

The time-invariant $\mathbf{E}$ field of Equation [\ref{eq:gen_wave_pol}] may also be written as

$$
\begin{equation}
\mathbf{E}=E_0\left(a\hat{x}+be^{j\phi}\hat{y}\right) \label{eq:xy_wave_pol}
\end{equation}
$$

For convenience, the distance and time phase term has been dropped. Without loss of generality,
$E_0$ and $\phi$ are chosen so that $a$ and $b$ are nonnegative real and $a^2+b^2=1$. The value of $E_0$ does
not affect the wave polarization in any way except in questions concerned with power. So $E_0$ will
be neglected.

The polarization ratio, $P$, is defined as

$$\begin{equation}P=\frac{E_y}{E_x}=\frac{b}{a}e^{j\phi}\end{equation}$$

The *modified polarization ratio*, $p$, is defined as

$$\begin{equation}p=jP=j\frac{b}{a}e^{j\phi} \end{equation}$$

Axial ratio of elliptical polarization is defined as the ratio of semi-major axis to semi-minor
axis. The axial ratio can be calculated in terms of $p$:

$$\begin{equation}AR=\left|\frac{|1+p|+|1-p|}{|1+p|-|1-p|}
\right|=\left|\frac{a^2+b^2+\sqrt{a^4+b^4+2a^2b^2\cos(2\phi)}}{2ab\sin\phi} \right| \end{equation} $$

The tilt angle, $\tau$, can be found as

$$\begin{equation}\tan 2\tau =\tan 2\alpha\cos\phi\end{equation}$$

where the angle $\alpha$ is defined as

$$\begin{equation}\tan \alpha = \frac{b}{a}\quad 0\le\alpha\le\frac{\pi}{2} \end{equation}$$

$\tau$ can also be found as

$$\begin{equation}e^{-j2\tau}=\frac{(1-p)/(1+p)}{|(1-p)/(1+p)|} \end{equation}$$

The $\mathbf{E}$ filed can also be written in terms of $AR$ and $\tau$ as:

$$\begin{equation}\mathbf{E}=\frac{E_0}{\sqrt{AR^2+1}}\left[\left(AR\cos\tau-js\sin\tau
\right)\hat{x}+\left(AR\sin\tau+js\cos\tau\right)\hat{y}\right] \end{equation}$$

where $s=\pm1$ is for rotation sense. $s=+1$ for left-handed polarization and $s=-1$ for
right-handed polarization.

It can be written in terms of inverse axial ratio $\gamma=\frac{1}{AR}$ ($0\le\gamma\le1$) as:

$$\begin{equation}\mathbf{E}=\frac{E_0}{\sqrt{\gamma^2+1}}\left[\left(\cos\tau-js\gamma\sin\tau
\right)\hat{x}+\left(\sin\tau+js\gamma\cos\tau\right)\hat{y}\right] \end{equation}$$

### Linear Polarization

- when $a=0$, the polarization is vertical polarization, and $\phi$ is irrelevant. The axial ratio is
infinite and tilt angle is 90 degree.
- When $b=0$, the polarization is horizontal polarization. The axial ratio is infinite and tilt angle
is 0 degree.
- When $\phi=0$, the polarization is a linear polarization. The axial ratio is infinite and tilt
angle is same as $\alpha$.
- When $\phi=\pi$, the polarization is a linear polarization. The axial ratio is infinite and tilt
angle is same as ${\pi}-\alpha$.

### Elliptical Polarization

For scenarios other than linear polarizations, the polarizations will be elliptical polarizations
(including circular polarizations). To determine the rotation sense, an auxiliary angle $\delta$ is
defined as

$$\begin{equation}\sin 2\delta=\sin 2\alpha\sin\phi \end{equation}$$

The axial ratio can be calculated as

$$\begin{equation}AR=\left|\frac{1}{\tan\delta}\right| \end{equation}$$

The rotation sense can be determined as

$$\begin{equation} \begin{cases}\sin 2\delta<0, & right-hand \\ \\ \sin 2\delta>0, &
left-hand\end{cases}\end{equation}$$

Therefore, the sign of $\sin\phi$ defines the rotation sense since $\sin 2\alpha>0$.

$$\begin{equation}\begin{cases}\pi<\phi<2\pi,& right-hand \\ \\ 0<\phi<\pi,&left-hand\end{cases} \end{equation}$$

Also, $Re(p)=-\frac{b}{a}\sin\phi$, thus

$$\begin{equation}\begin{cases}Re(p)>0,& right-hand \\ \\ Re(p)<0,&left-hand\end{cases} \end{equation}$$

When $\phi=\frac{\pi}{2}$ and $a\ne b$, the tilt angle will be 0 degree if $a>b$ or 90 degree if $a<b$, which
means the x and y axes are aligned with semi-major and semi-minor axes of the polarization ellipse.
The axial ratio $AR = max\{\frac{a}{b},\frac{b}{a}\}$. The rotation sense will be left-hand since
$\sin 2\delta>0$.

When $\phi=-\frac{\pi}{2}$ and $a\ne b$, the tilt angle and axial ratio are sames as $\phi=\frac{\pi}{2}$ case.
The rotation sense will be right-hand since $\sin 2\delta<0$.

When $a=b$ and $\phi \ne \pm \frac{\pi}{2}$, the tile angle will be always 45 degree if $\cos
\phi>0$ and always 135 degree if $\cos \phi < 0$.

### Circular Polarization

Circular polarization is a special case of elliptical polarization. It occurs when $a=b$ and
$\phi=\pm\frac{\pi}{2}$. It is left-hand when $\phi=\frac{\pi}{2}$ and right-hand when
$\phi=-\frac{\pi}{2}$. Tilt angle is irrelevant and axial ratio is 1.

## Circular Wave Components

Consider the complex vectors:

$$\begin{equation}\begin{cases}\mathbf{\omega_L}=\frac{1}{\sqrt{2}}\left(\hat{x}+j\hat{y} \right)
\\ \\ \mathbf{\omega_R}=\frac{1}{\sqrt{2}}\left(\hat{x}-j\hat{y} \right)\end{cases}\end{equation}$$

It is clear that $\mathbf{\omega_L}$ is a left circular wave ($a=b$, $\phi=\frac{\pi}{2}$), and
$\mathbf{\omega_R}$ is a right circular wave. The field $\mathbf{E}$ can be expanded in terms of
$\mathbf{\omega_L}$ and $\mathbf{\omega_R}$, giving

$$\begin{equation}\mathbf{E}=E_0\left(a\hat{x}+be^{j\phi}\hat{y}
\right)=E_0\left(L\mathbf{\omega_L}+Re^{j\theta}\mathbf{\omega_R}
\right)=E_L\mathbf{\omega_L}+E_R\mathbf{\omega_R} \end{equation}$$

Solving for $L$ and $Re^{j\theta}$ gives,

$$\begin{equation}\begin{cases}L=\frac{1}{\sqrt{2}}\left(a-jbe^{j\phi} \right)\\ \\
R=\frac{1}{\sqrt{2}}\left(a+jbe^{j\phi} \right) \end{cases} \end{equation}$$

Circular polarization ratio, $q$, is defined as

$$\begin{equation}q=\frac{E_L}{E_R}=\frac{L}{R}e^{-j\theta}=\frac{a-jbe^{j\phi}}{a+jbe^{j\phi}}=\frac{1-p}{1+p}
\end{equation}$$

The modified polarization ratio can be obtained as

$$\begin{equation}p = \frac{1-q}{1+q} \end{equation}$$

The axial ratio can be given in terms of $q$ as

$$\begin{equation}AR=\left|\frac{1+|q|}{1-|q|} \right| \end{equation}$$

The tilt angle is given by

$$\begin{equation}\begin{cases}\tau=\frac{\theta}{2}, & if\space\theta\ge0 \\
\\\pi+\frac{\theta}{2}, &if \space\theta\le0 \end{cases} \end{equation}$$

The magnitude of $q$ defines rotation sense as

$$\begin{equation}\begin{cases}|q|<1,& right-hand \\ \\ |q|>1,&left-hand\end{cases}
\end{equation}$$

$|q|<1$ corresponds to $|L|<|R|$, which results in a right-hand rotation.
