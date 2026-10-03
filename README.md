# lady-car.it

Landing statica di **Lady Car** — detailing auto a domicilio a Roma. Nessun build: i file
della radice vengono pubblicati così come sono.

## Deploy
push su `main` → webhook GitHub → OVH (Hosting → Multisito, Git, branch `main`) aggiorna la cartella del sito.

## Immagini
Carica le foto in `img/` (anche direttamente da GitHub, "Add file → Upload files").
La GitHub Action `optimize-images.yml` le ridimensiona (max 2000 px), toglie i dati EXIF/GPS
e le ricomprime, poi fa un commit automatico. Nome e formato restano uguali.
In locale: `pip install pillow && python scripts/optimize_images.py`.

## Moduli e contatti
- Modulo → Formspree `mlgkbbkv` (arriva via email).
- WhatsApp / telefono: +39 380 582 6738.

## Note
- Solo cookie tecnici: l'avviso in basso è informativo, non serve consenso (Linee guida Garante 2021).
  Se si aggiungono GA4, Meta Pixel, mappe o video incorporati serve un vero banner con consenso preventivo.
- Font self-hosted in `fonts/` (Gloock, Figtree) — niente Google Fonts per il GDPR.
