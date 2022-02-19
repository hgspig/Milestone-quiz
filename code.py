
from adafruit_magtag.magtag import MagTag
import terminalio

magtag = MagTag()

magtag.add_text(
    text_font="/fonts/Arial-12.bdf",        # text_font="/fonts/epilogue18.bdf",
    text_position=(
        (magtag.graphics.display.width // 2) - 1,
        10,
    ),
    text_scale=1,
    # text_wrap=25,
    text_anchor_point=(0.5, 0.5),
    is_data=False,
)
magtag.set_text("Guess Hannah's recent achievement!", auto_refresh=False, index=0)
LINE_HEIGHT=23
LINE_X_SHIFT=37

texts = [
    "A. Published a short story",
    "B. Bought her first car",
    "C. Was accepted to BYU Provo",
    "D. Was recruited to a star youth ultimate frisbee team"
]

for i in range(4):
    magtag.add_text(
        text_font = terminalio.FONT, 
        text_position=(
            10,
            LINE_HEIGHT*i+LINE_X_SHIFT+4,
        ),
        line_spacing=0.9,
        text_scale=1,
        text_wrap=30,
        text_anchor_point=(0, 0.5),
        is_data=False,
    )
    magtag.set_text(texts[i], auto_refresh=False, index=i+1)

# Create the QR code
url = "https://github.com/hgspig/Milestone-quiz#answer-c"
magtag.graphics.qrcode(url, qr_size=3, x=(magtag.graphics.display.width-93), y=34)

magtag.refresh()
magtag.exit_and_deep_sleep(24*60*60)
