"""
Optimize the images downloaded from the Wikipedia "Mascot" article.

1. Save the originals into a folder called  originals/  next to this script,
   using the names listed in IMAGES below (any extension: .jpg, .png, .webp...).
2. pip install pillow
3. python optimize_images.py

For each image it writes two files into images/:
   name.webp  (smaller file, used by modern browsers)
   name.jpg   (fallback for old browsers)
Images wider than 800px are scaled down (never up), metadata is stripped,
and both files are compressed. The real width/height are written into
the matching <img> tag in index.html.
"""
import re
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).parent
SRC = HERE / "originals"
OUT = HERE / "images"
HTML = HERE / "index.html"
MAX_WIDTH = 800

# Names match the images on https://en.wikipedia.org/wiki/Mascot, in page order.
IMAGES = [
    "rolle-the-clown",
    "san-diego-chicken",
    "sebastian-the-ibis",
    "big-boy-statue",
    "boomer-beaver",
    "rooster-mascot",
    "soohorang-bandabi",
    "royal-welsh-goat",
    "eddie",
    "vic-rattlehead",
]


def find_original(name):
    for p in SRC.glob(name + ".*"):
        return p
    return None


def main():
    OUT.mkdir(exist_ok=True)
    html = HTML.read_text(encoding="utf-8")
    for name in IMAGES:
        src = find_original(name)
        if not src:
            print(f"MISSING  originals/{name}.*  (skipped)")
            continue
        img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        if img.width > MAX_WIDTH:
            img = img.resize((MAX_WIDTH, round(img.height * MAX_WIDTH / img.width)),
                             Image.LANCZOS)
        img.save(OUT / f"{name}.webp", "WEBP", quality=80, method=6)
        img.save(OUT / f"{name}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
        w, h = img.size
        html = re.sub(
            r'(<img src="images/' + re.escape(name) + r'\.jpg"[^>]*?)width="\d+" height="\d+"',
            rf'\g<1>width="{w}" height="{h}"', html)
        before = src.stat().st_size // 1024
        jpg = (OUT / f"{name}.jpg").stat().st_size // 1024
        webp = (OUT / f"{name}.webp").stat().st_size // 1024
        print(f"OK  {name:22} {w}x{h}   original {before} KB -> jpg {jpg} KB, webp {webp} KB")
    HTML.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
