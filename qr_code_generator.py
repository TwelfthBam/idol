import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

# Data for the event (e.g., specific artworks or zones)
exhibition_items = {
    "programme": "https://twelfthbam.github.io/idol/index.html",
    "behind-the-scenes": "https://twelfthbam.github.io/idol/making-of.html",
}

def create_warhol_qr(data, name, color=(0, 0, 0)):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=SolidFillColorMask(front_color=color, back_color=(255, 255, 255))
    )
    
    img.save(f"qr_{name}.png")
    print(f"Generated {name}")

create_warhol_qr(exhibition_items["programme"], "programme", color=(0, 0, 0))  
create_warhol_qr(exhibition_items["behind-the-scenes"], "behind_the_scenes", color=(0, 0, 0))  