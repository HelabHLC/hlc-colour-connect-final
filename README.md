# 🎨 HLC-Colour-Atlas-XL Connect

Willkommen in einer **offenen Farbwelt**.  
Dieses Projekt ist eine **freie, ICC-basierte Alternative zu Pantone Connect** – mit vollem Fokus auf **Transparenz, Modularität und Präzision im Druck-Workflow**.

---

## 🚀 Was ist das?

Ein Werkzeug zur Anzeige, Analyse und Umrechnung von Farben auf Basis des  
🌈 **HLC Colour Atlas XL (CIELAB)** – entwickelt von [**FreieFarbe e.V.**](https://freiefarbe.de), in Zusammenarbeit mit **GMG Color** und der internationalen Farb-Community.

Mit dieser App kannst du:
- 🎨 Alle HLC-Farben als Gitter durchstöbern
- 🔍 Farben per HEX, RGB, HLC oder CMYK filtern & finden
- 🖱️ Aus Bildern mit der Maus Farben extrahieren
- 🔁 Werte in CMYK/LAB eingeben und zu HLC matchen lassen
- 🧠 ICC-konform CMYK berechnen (via `.icc`-Profile deiner Wahl)
- 💾 Farben als `.json` oder `.csv` exportieren
- 🌐 Das Ganze deployen – auf Heroku, GitHub oder lokal

---

## 🧰 Features im Überblick

| Modul         | Funktion |
|---------------|----------|
| 🎨 Gitter      | Interaktive HLC-Farbdarstellung |
| 🖱️ Extrahieren | Bild-Upload + Color Picker |
| 🔍 Filter      | Suche nach HEX, RGB, CMYK, HLC |
| 💾 Export      | Exportiere deine Palette |
| 🔁 Konvertieren| CMYK / LAB → RGB → HLC |
| 📦 ICC-Profil  | Nutze dein `.icc` Profil für echte CMYK-Konvertierung |

---

---

## 🖼️ Vorschau / Screenshots

### CIELAB HLC Colour Atlas XL – by FreieFarbe e.V.

![HLC Atlas Cover](frontend/farb-atlas-cover.png)
*(Hier kannst du später Screenshots einfügen – z. B. vom Gitter oder der Extrahierfunktion)*

---

## 🛠️ Installation & Deploy

### Heroku (empfohlen)
1. `.icc`-Dateien in `/icc/` einfügen
2. In Konsole:
```bash
git init
git add .
git commit -m "Deploy HLC Colour Atlas XL Connect"
heroku create
git push heroku main
```

Oder einfach:
> `deploy-heroku.bat` ausführen (Windows)

### Lokal starten (Python 3.10+)
```bash
pip install flask pillow
python backend/app.py
```
Dann im Browser öffnen: http://localhost:5000

---

## 🙌 Credits & Quellen

- 🎨 **[FreieFarbe e.V.](https://freiefarbe.de)** – Entwickler des **HLC Colour Atlas XL (CIELAB)** Standards
- 📊 [GamutMap.org](https://gamutmap.org) – Visuelle Analyse von Farbräumen
- 🖌️ [ArtistPigments.org](https://artistpigments.org) – Farb- und Pigmentwissen
- 💻 [LittleCMS](https://littlecms.com) – ICC-Engine für Farbkonvertierung (verwendet via Pillow/ImageCms)

---

## 📄 Lizenz

Open Source – verwende, erweitere, teile frei.  
**Vorschlag:** [MIT License](https://opensource.org/licenses/MIT)

---

## ✨ Vision

**Farbe ist frei.**  
Dieses Tool will zeigen, dass Farbkommunikation nicht proprietär sein muss.  
Mit offenen Standards, echten ICC-Workflows und der Kraft der Community schaffen wir gemeinsam eine **faire, transparente Alternative** zu kommerziellen Systemen.

Made with ❤️ für Designer, Drucker, Entwickler, Kreative.
