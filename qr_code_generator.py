import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

# Data for the event (e.g., specific artworks or zones)
exhibition_items = {
    "entrance": "https://idol-nnt.com/welcome",
    "marilyn": "https://idol-nnt.com/art/marilyn-diptych",
    "soup_can": "https://idol-nnt.com/art/soup-cans"
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

# Generate a 'Hot Pink' QR code (R, G, B)
create_warhol_qr(exhibition_items["marilyn"], "marilyn", color=(255, 20, 147))