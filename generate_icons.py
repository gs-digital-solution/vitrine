from PIL import Image
import os

# 1. Créer le dossier s'il n'existe pas
os.makedirs('static/icons', exist_ok=True)

# 2. INDIQUE ICI LE NOM DE TON IMAGE SOURCE
# CHANGE "logo.png" par le nom de ton fichier (ex: "mon_logo.jpg")
nom_fichier_source = "logo.png"

# 3. Ouvrir l'image
img = Image.open(nom_fichier_source)

# 4. Recadrage au centre pour obtenir un carré parfait
min_side = min(img.width, img.height)
left = (img.width - min_side) // 2
top = (img.height - min_side) // 2
img_square = img.crop((left, top, left + min_side, top + min_side))

# 5. Générer les 2 tailles (192 et 512) et les sauvegarder
for size in [192, 512]:
    img_resized = img_square.resize((size, size), Image.Resampling.LANCZOS)
    img_resized.save(f'static/icons/icon-{size}.png')
    print(f'✅ Icône {size}x{size} générée avec succès !')

print("🎉 Terminé ! Les icônes sont dans le dossier 'static/icons/'")