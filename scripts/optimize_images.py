"""Ottimizza le immagini in img/: ridimensiona oltre 2000px, rimuove EXIF (anche GPS),
ricomprime. Mantiene nome e formato, così i riferimenti nell'HTML non cambiano.
Uso: python scripts/optimize_images.py [file ...]  (senza argomenti: tutta la cartella img/)"""
import io, os, sys
from PIL import Image, ImageOps

MAX = 2000
EXT = {".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG", ".webp": "WEBP"}

def optimize(path):
    fmt = EXT.get(os.path.splitext(path)[1].lower())
    if not fmt or not os.path.isfile(path):
        return
    before = os.path.getsize(path)
    im = Image.open(path)
    had_exif = bool(im.info.get("exif"))
    im = ImageOps.exif_transpose(im)
    resized = max(im.size) > MAX
    if resized:
        im.thumbnail((MAX, MAX), Image.LANCZOS)
    buf = io.BytesIO()
    if fmt == "JPEG":
        im.convert("RGB").save(buf, "JPEG", quality=80, optimize=True, progressive=True)
    elif fmt == "WEBP":
        im.save(buf, "WEBP", quality=78, method=6)
    else:
        im.save(buf, "PNG", optimize=True)
    after = len(buf.getvalue())
    # ricomprime solo se serve davvero: ridimensionata, con EXIF, o file pesante (>300 KB)
    if resized or had_exif or (before > 300 * 1024 and after < before * 0.9):
        with open(path, "wb") as f:
            f.write(buf.getvalue())
        print(f"{path}: {before//1024} KB -> {after//1024} KB")

files = sys.argv[1:] or [os.path.join("img", f) for f in os.listdir("img")]
for f in files:
    optimize(f)
