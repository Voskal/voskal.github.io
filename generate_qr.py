from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M


WEBSITE_URL = "https://yourusername.github.io/photo-website/"
OUTPUT_FILE = Path("website-qr-code.png")


def create_qr_code(url: str, output_file: Path) -> None:
    if not url.startswith(("https://", "http://")):
        raise ValueError("The URL must begin with https:// or http://")

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=12,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white",
    )

    image.save(output_file)
    print(f"QR code saved as: {output_file.resolve()}")


if __name__ == "__main__":
    create_qr_code(WEBSITE_URL, OUTPUT_FILE)