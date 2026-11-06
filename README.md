# Retro Amp (Liquid Glass Edition) – KWGT Android Widget

A **Liquid Glass (Frosted Glassmorphism)** edition of the classic late-90s Winamp-style music player widget for Android home screens (Nova, Samsung One UI, Pixel Launcher, Lawnchair, etc.) powered by **KWGT (Kustom Widget Maker)**.

It pairs modern translucent liquid glass (smooth curves, refraction rims, ambient shadows, and specular curvature sheens) with authentic Winamp retro hardware charm (phosphor green LCD readout, 12-band spectrum equalizer, digital counter, and beveled transport controls).

![Retro Amp Liquid Glass Edition Preview](preview.png)

---

## ⚡ Direct Download

* **Download Widget Preset:** [**`RetroAmp_Winamp.kwgt`**](https://github.com/arnoldmitre/winamp-kwgt-widget/releases/download/v1.1.0/RetroAmp_Winamp.kwgt)
* **Releases Page:** Check the [Releases](https://github.com/arnoldmitre/winamp-kwgt-widget/releases) tab for one-click `.kwgt` asset downloads.

---

## ✨ Features & Liquid Glass Design

* **Liquid Frosted Glass Chassis:**
  * Translucent obsidian glass body (`#66141924`) that allows your custom wallpaper to softly shine through.
  * Crisp 1.5px specular refractive highlight rim (`#59FFFFFF`) catching ambient light.
  * Top glass curvature reflection sheen (`#12FFFFFF`) providing a tactile 3D curved glass feel.
  * Smooth 16px rounded corners.
* **Liquid Glass Title Bar:**
  * Translucent frosted glass container with glowing phosphor cyan/green accent lines (`#B300FFAA`).
  * `"RETRO AMP • LIQUID GLASS"` typography in crisp frosted silver-white.
* **Smoked Glass LCD Display:**
  * Deep emerald-black smoked glass screen (`#80050E07`) with an emerald neon glass rim.
  * **Digital Phosphor Clock:** Glowing real-time track timer (`$tf(mi(pos), mm:ss)$`) and total duration.
  * **Dynamic Status Indicators:** `PLAY`, `PAUSE`, `STOP`, and `STEREO`.
  * **Bitrate & Sample Rate:** Classic `192 kbps 44 kHz` header.
  * **12-Band Equalizer / Spectrum Analyzer:** Luminous visualizer bars with white peak dots.
  * **Smoked Marquee Capsule:** Recessed smoked glass container with track title & artist.
* **Liquid Frosted Seekbar:**
  * Sunken translucent track with a vibrant liquid neon progress fill (`#E600FFAA`).
* **Liquid Glass Transport Buttons (Touch Actions):**
  * Beveled frosted glass pill capsules with refractive borders.
  * Active playing glow: the Play button illuminates with a bright emerald backlight aura when actively playing.
  * Interactive controls:
    * `|<<` (**PREV**): Skip to previous track
    * `▶` (**PLAY**): Play / Pause toggle
    * `❚❚` (**PAUSE**): Pause
    * `>>|` (**NEXT**): Skip to next track
    * `⏏` (**EJECT**): Opens active music player (Spotify, YouTube Music, Apple Music, etc.)

---

## 📲 How to Install on Android

### 1. Requirements
* [KWGT Kustom Widget Maker](https://play.google.com/store/apps/details?id=org.kustom.widget)
* **KWGT Pro Key** (required by Kustom to import external presets)

### 2. Enable Notification & Media Access
For KWGT to detect playing songs and control playback:
1. Open Android **Settings** $\rightarrow$ **Apps** $\rightarrow$ **Special app access** $\rightarrow$ **Device & app notifications**.
2. Enable access for **KWGT**.
3. In the KWGT app settings, ensure **Preferred Music Player** is set to **Auto** (or choose your preferred music app).

### 3. Import the Widget
1. Download [**`RetroAmp_Winamp.kwgt`**](https://github.com/arnoldmitre/winamp-kwgt-widget/releases/download/v1.1.0/RetroAmp_Winamp.kwgt) to your phone.
2. Move it to your phone's internal storage: `Kustom/widgets/RetroAmp_Winamp.kwgt` (or leave it in your `Downloads` folder).
3. Long-press any empty space on your home screen and select **Widgets**.
4. Choose **KWGT** and drag a **4×2** widget onto your screen.
5. Tap the blank widget to open KWGT.
6. Tap the **Library / Exported** tab (or tap the **Import / Folder** icon at the top) and select `RetroAmp_Winamp.kwgt`.
7. Tap the **Save** icon (floppy disk) in the top right corner.
8. Return to your home screen—your Liquid Glass Winamp widget is live!

---

## 🛠️ Repository Contents

* `RetroAmp_Winamp.kwgt`: Ready-to-import KWGT widget package.
* `preset.json`: Uncompressed widget structure and formula definitions.
* `generate_liquid_glass.py`: Python script used to construct and package the `.kwgt` archive.
* `render_preview.py`: Script that renders the layout preview image.
* `preview.png`: Visual layout preview.

## 📄 License

MIT License. Free to use, modify, and share!
