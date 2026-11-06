import os
from PIL import Image, ImageDraw, ImageFont
import math

def render_preview():
    W, H = 840, 460
    im = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(im)

    # 1. Background Wallpaper (Deep Tahoe / Northern Lights aesthetic)
    for y in range(H):
        # Gradient from deep dark navy #0a0e17 to dark teal-slate #121c24
        ratio = y / H
        r = int(10 + ratio * 12 + 6 * math.sin(ratio * 3.14))
        g = int(15 + ratio * 24 + 18 * math.sin(ratio * 3.14))
        b = int(28 + ratio * 32 + 30 * math.sin(ratio * 3.14))
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # Ambient light orb under the widget to emphasize glass transparency
    orb = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    orb_draw = ImageDraw.Draw(orb)
    for rad in range(220, 0, -4):
        alpha = int((1 - rad / 220) * 45)
        orb_draw.ellipse([W//2 - rad*1.8, H//2 - rad + 20, W//2 + rad*1.8, H//2 + rad + 20], fill=(0, 220, 150, alpha))
    im = Image.alpha_composite(im, orb)
    draw = ImageDraw.Draw(im)

    # 2. Glass Widget Dimensions
    ww, wh = 720, 340
    wx0 = (W - ww) // 2
    wy0 = (H - wh) // 2
    wx1 = wx0 + ww
    wy1 = wy0 + wh

    # Soft ambient drop shadow
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([wx0-4, wy0+4, wx1+4, wy1+12], radius=22, fill=(0, 0, 0, 90))
    s_draw.rounded_rectangle([wx0-8, wy0+8, wx1+8, wy1+18], radius=24, fill=(0, 0, 0, 50))
    im = Image.alpha_composite(im, shadow)

    # Glass Layer
    glass = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glass)

    # Glass Body (Translucent obsidian dark-tinted frosted glass)
    g_draw.rounded_rectangle([wx0, wy0, wx1, wy1], radius=18, fill=(18, 24, 34, 185))

    # Specular 1.5px Glass Border Rim (Refractive highlight catching light)
    g_draw.rounded_rectangle([wx0, wy0, wx1, wy1], radius=18, outline=(255, 255, 255, 105), width=2)

    # Top Glass Curvature Reflection / Sheen
    sheen_h = 120
    g_draw.rounded_rectangle([wx0+2, wy0+2, wx1-2, wy0+sheen_h], radius=16, fill=(255, 255, 255, 18))

    im = Image.alpha_composite(im, glass)
    draw = ImageDraw.Draw(im)

    # Fonts
    font_mono = ImageFont.truetype("/usr/share/fonts/TTF/JetBrainsMono-Bold.ttf", 13)
    font_mono_lg = ImageFont.truetype("/usr/share/fonts/TTF/JetBrainsMono-Bold.ttf", 30)
    font_sans = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 12)
    font_sans_sm = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 11)
    font_btn = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 16)

    # 3. Liquid Glass Title Bar
    tb_y0 = wy0 + 12
    tb_y1 = tb_y0 + 30
    tb_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    tb_draw = ImageDraw.Draw(tb_layer)
    tb_draw.rounded_rectangle([wx0+12, tb_y0, wx1-12, tb_y1], radius=8, fill=(255, 255, 255, 28), outline=(0, 255, 170, 70), width=1)
    im = Image.alpha_composite(im, tb_layer)
    draw = ImageDraw.Draw(im)

    # Title Bar neon stripes & text
    draw.line([(wx0+28, tb_y0+15), (wx0+180, tb_y0+15)], fill=(0, 255, 170, 200), width=2)
    draw.line([(wx1-180, tb_y0+15), (wx1-28, tb_y0+15)], fill=(0, 255, 170, 200), width=2)
    draw.text((W//2, tb_y0+15), "RETRO AMP • LIQUID GLASS", font=font_mono, fill=(245, 250, 255, 255), anchor="mm")

    # 4. Smoked Glass LCD Screen
    lcd_x0 = wx0 + 14
    lcd_y0 = tb_y1 + 10
    lcd_x1 = wx1 - 14
    lcd_y1 = lcd_y0 + 140

    lcd_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    l_draw = ImageDraw.Draw(lcd_layer)
    # Deep smoked emerald-black translucent glass
    l_draw.rounded_rectangle([lcd_x0, lcd_y0, lcd_x1, lcd_y1], radius=10, fill=(5, 14, 8, 205), outline=(0, 255, 170, 65), width=1)
    im = Image.alpha_composite(im, lcd_layer)
    draw = ImageDraw.Draw(im)

    # LCD Top Row text
    draw.text((lcd_x0+20, lcd_y0+22), "▶ PLAY", font=font_mono, fill=(0, 255, 170, 255), anchor="lm")
    draw.text((lcd_x0+110, lcd_y0+22), "STEREO", font=font_mono, fill=(0, 240, 140, 240), anchor="lm")
    draw.text((lcd_x0+205, lcd_y0+22), "192 kbps 44 kHz", font=font_mono, fill=(0, 210, 120, 180), anchor="lm")

    # Digital Clock
    draw.text((lcd_x1-150, lcd_y0+25), "02:45", font=font_mono_lg, fill=(0, 255, 170, 255), anchor="mm")
    draw.text((lcd_x1-75, lcd_y0+25), "/ 03:50", font=font_mono, fill=(0, 210, 120, 180), anchor="lm")

    # Equalizer Bars (14 bars)
    eq_x = lcd_x0 + 20
    eq_y = lcd_y0 + 82
    heights = [18, 30, 24, 38, 28, 42, 34, 46, 38, 28, 32, 22, 16, 12]
    for i, bh in enumerate(heights):
        bx = eq_x + i * 13
        # Draw bar with glow
        bar_col = (0, 255, 170, 230) if i < 11 else (255, 215, 0, 230)
        draw.rounded_rectangle([bx, eq_y - bh, bx + 9, eq_y], radius=1.5, fill=bar_col)
        # Peak indicator dot
        draw.rectangle([bx, eq_y - bh - 3, bx + 9, eq_y - bh - 2], fill=(255, 255, 255, 220))

    # Smoked Marquee Capsule
    mq_x0 = eq_x + 195
    mq_y0 = eq_y - 36
    mq_x1 = lcd_x1 - 20
    mq_y1 = eq_y + 4
    draw.rounded_rectangle([mq_x0, mq_y0, mq_x1, mq_y1], radius=6, fill=(3, 8, 4, 160), outline=(0, 255, 170, 45), width=1)
    draw.text((mq_x0 + 16, (mq_y0 + mq_y1)//2), "Daft Punk - Around the World (Radio Edit)", font=font_mono, fill=(0, 255, 170, 255), anchor="lm")

    # 5. Frosted Glass Seekbar
    sb_y0 = lcd_y1 + 10
    sb_y1 = sb_y0 + 10
    draw.rounded_rectangle([wx0+14, sb_y0, wx1-14, sb_y1], radius=5, fill=(0, 0, 0, 110), outline=(255, 255, 255, 30), width=1)
    # Neon progress fill (70%)
    sb_fill_w = int((ww - 32) * 0.71)
    draw.rounded_rectangle([wx0+16, sb_y0+1, wx0+16+sb_fill_w, sb_y1-1], radius=4, fill=(0, 255, 170, 240))

    # 6. Info & Volume Details
    info_y = sb_y1 + 14
    draw.text((wx0+20, info_y), "ALBUM: Homework  |  VOL: 85%", font=font_sans_sm, fill=(200, 215, 230, 200), anchor="lm")
    draw.text((wx1-20, info_y), "com.spotify.music", font=font_sans_sm, fill=(140, 160, 185, 170), anchor="rm")

    # 7. Liquid Glass Transport Buttons
    btn_y0 = info_y + 14
    btn_y1 = btn_y0 + 44
    btn_w = 110
    btn_gap = 18
    btns = [
        ("|<<", False),
        ("▶", True),   # Active playing
        ("❚❚", False),
        (">>|", False),
        ("⏏", False)
    ]
    start_bx = (W - (len(btns)*btn_w + (len(btns)-1)*btn_gap)) // 2

    btn_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(btn_layer)

    for i, (sym, active) in enumerate(btns):
        bx = start_bx + i * (btn_w + btn_gap)
        if active:
            # Active button has glowing emerald aura and highlight
            b_draw.rounded_rectangle([bx, btn_y0, bx+btn_w, btn_y1], radius=11, fill=(0, 255, 170, 70), outline=(0, 255, 170, 200), width=2)
            b_draw.rounded_rectangle([bx+1, btn_y0+1, bx+btn_w-1, btn_y0+18], radius=9, fill=(255, 255, 255, 45))
        else:
            # Frosted glass key
            b_draw.rounded_rectangle([bx, btn_y0, bx+btn_w, btn_y1], radius=11, fill=(255, 255, 255, 28), outline=(255, 255, 255, 80), width=1)
            b_draw.rounded_rectangle([bx+1, btn_y0+1, bx+btn_w-1, btn_y0+16], radius=9, fill=(255, 255, 255, 20))

    im = Image.alpha_composite(im, btn_layer)
    draw = ImageDraw.Draw(im)

    for i, (sym, active) in enumerate(btns):
        bx = start_bx + i * (btn_w + btn_gap)
        sym_col = (0, 255, 170, 255) if active else (245, 250, 255, 255)
        draw.text((bx + btn_w//2, (btn_y0 + btn_y1)//2), sym, font=font_btn, fill=sym_col, anchor="mm")

    preview_path = "/root/winamp-kwgt-widget/preview.png"
    im.save(preview_path, "PNG")
    print(f"Generated preview at {preview_path} ({os.path.getsize(preview_path)} bytes)")

render_preview()
