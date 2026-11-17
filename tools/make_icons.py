"""Generate Android launcher icons from tools/icon-source.png into android/app/src/main/res."""
import os
from PIL import Image, ImageDraw
src = Image.open("tools/icon-source.png").convert("RGBA")
res = "android/app/src/main/res"
sizes = {"mdpi":48,"hdpi":72,"xhdpi":96,"xxhdpi":144,"xxxhdpi":192}
for d,s in sizes.items():
    out = os.path.join(res, "mipmap-"+d); os.makedirs(out, exist_ok=True)
    im = src.resize((s,s), Image.LANCZOS)
    im.save(os.path.join(out,"ic_launcher.png"))
    im.save(os.path.join(out,"ic_launcher_foreground.png"))
    m = Image.new("L",(s,s),0); ImageDraw.Draw(m).ellipse((0,0,s-1,s-1),fill=255)
    r = im.copy(); r.putalpha(m); r.save(os.path.join(out,"ic_launcher_round.png"))
# remove adaptive-icon xml so the PNGs above are used
import shutil
shutil.rmtree(os.path.join(res,"mipmap-anydpi-v26"), ignore_errors=True)
# splash/background colour
print("icons done")
