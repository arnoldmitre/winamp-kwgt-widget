import json
import zipfile
import os
from PIL import Image, ImageDraw, ImageFont

def build_liquid_glass_kwgt():
    items = []
    
    # 1. Ambient Drop Shadow (Soft dark glow behind the glass tile)
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "Glass_Shadow",
        "shape_type": "RECT",
        "shape_width": 684.0,
        "shape_height": 324.0,
        "shape_corners": 18.0,
        "paint_color": "#33000000"
    })

    # 2. Outer Glass Specular Border (Crisp refractive edge catching light)
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "Glass_Border_Rim",
        "shape_type": "RECT",
        "shape_width": 680.0,
        "shape_height": 320.0,
        "shape_corners": 16.0,
        "paint_color": "#59FFFFFF"
    })

    # 3. Main Liquid Glass Body (Translucent obsidian dark-tinted frosted glass)
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "Glass_Body",
        "shape_type": "RECT",
        "shape_width": 676.0,
        "shape_height": 316.0,
        "shape_corners": 15.0,
        "paint_color": "#66141924"
    })

    # 4. Top Glass Sheen / Reflection Highlight (Upper curvature reflection)
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "Glass_Top_Reflection",
        "position_offset_y": -78.0,
        "shape_type": "RECT",
        "shape_width": 672.0,
        "shape_height": 154.0,
        "shape_corners": 14.0,
        "paint_color": "#12FFFFFF"
    })

    # 5. Liquid Glass Title Bar Container
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "TitleBar_Glass_Bg",
        "position_offset_y": -130.0,
        "shape_type": "RECT",
        "shape_width": 656.0,
        "shape_height": 32.0,
        "shape_corners": 8.0,
        "paint_color": "#2BFFFFFF"
    })

    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "TitleBar_Line_Left",
        "position_offset_x": -180.0,
        "position_offset_y": -130.0,
        "shape_type": "RECT",
        "shape_width": 150.0,
        "shape_height": 2.0,
        "paint_color": "#B300FFAA"
    })

    items.append({
        "internal_type": "TextModule",
        "internal_title": "TitleBar_Text",
        "position_offset_y": -130.0,
        "text_expression": "RETRO AMP • LIQUID GLASS",
        "text_size": 13.0,
        "paint_color": "#FFF8FAFC"
    })

    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "TitleBar_Line_Right",
        "position_offset_x": 180.0,
        "position_offset_y": -130.0,
        "shape_type": "RECT",
        "shape_width": 150.0,
        "shape_height": 2.0,
        "paint_color": "#B300FFAA"
    })

    # 6. Smoked Glass LCD Display Bezel & Glass Screen
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "LCD_Glass_Rim",
        "position_offset_y": -34.0,
        "shape_type": "RECT",
        "shape_width": 656.0,
        "shape_height": 136.0,
        "shape_corners": 10.0,
        "paint_color": "#3300FFAA"
    })

    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "LCD_Smoked_Screen",
        "position_offset_y": -34.0,
        "shape_type": "RECT",
        "shape_width": 652.0,
        "shape_height": 132.0,
        "shape_corners": 9.0,
        "paint_color": "#80050E07",
        "internal_events": [
            {
                "type": "SINGLE_TAP",
                "action": "MUSIC",
                "music_action": "OPEN_PLAYER"
            }
        ]
    })

    # LCD: Status
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Status",
        "position_offset_x": -250.0,
        "position_offset_y": -78.0,
        "text_expression": "$if(mi(state) = PLAYING, \"▶ PLAY\", if(mi(state) = PAUSED, \"❚❚ PAUSE\", \"■ STOP\"))$",
        "text_size": 12.0,
        "paint_color": "#FF00FFAA"
    })

    # LCD: Stereo
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Stereo",
        "position_offset_x": -160.0,
        "position_offset_y": -78.0,
        "text_expression": "$if(mi(state) = PLAYING, \"STEREO\", \"MONO\")$",
        "text_size": 12.0,
        "paint_color": "#FF00EE88"
    })

    # LCD: Bitrate & Sample rate
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Kbps",
        "position_offset_x": -70.0,
        "position_offset_y": -78.0,
        "text_expression": "192 kbps 44 kHz",
        "text_size": 11.0,
        "paint_color": "#9900FFAA"
    })

    # LCD: Digital Phosphor Clock
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Clock",
        "position_offset_x": 195.0,
        "position_offset_y": -74.0,
        "text_expression": "$tf(mi(pos), mm:ss)$",
        "text_size": 30.0,
        "paint_color": "#FF00FFAA"
    })

    # LCD: Total Duration
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Total",
        "position_offset_x": 275.0,
        "position_offset_y": -72.0,
        "text_expression": "$if(mi(len) > 0, \"/ \" + tf(mi(len), mm:ss), \"\")$",
        "text_size": 13.0,
        "paint_color": "#9900FFAA"
    })

    # LCD: 12-band Spectrum Equalizer Bars
    num_bars = 12
    start_x = -260.0
    bar_width = 8.0
    gap = 4.0
    for i in range(num_bars):
        bx = start_x + i * (bar_width + gap)
        h_formula = f"$if(mi(state) = PLAYING, 6 + (df(S) * {3 + (i%5)} + {i*7}) % 36, 4)$"
        items.append({
            "internal_type": "ShapeModule",
            "internal_title": f"LCD_SpecBar_{i+1}",
            "position_offset_x": bx,
            "position_offset_y": -32.0,
            "shape_type": "RECT",
            "shape_width": bar_width,
            "shape_height": 20.0,
            "shape_corners": 1.5,
            "internal_formulas": {
                "shape_height": h_formula
            },
            "internal_toggles": {
                "shape_height": 10
            },
            "paint_color": "#E600FFAA" if i < 9 else "#E6FFD500"
        })

    # LCD: Inner Smoked Marquee Capsule
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "LCD_Marquee_Box",
        "position_offset_x": 80.0,
        "position_offset_y": -32.0,
        "shape_type": "RECT",
        "shape_width": 380.0,
        "shape_height": 30.0,
        "shape_corners": 6.0,
        "paint_color": "#4D030804"
    })

    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Marquee_Text",
        "position_offset_x": 80.0,
        "position_offset_y": -32.0,
        "text_expression": "$if(mi(state) = PLAYING | mi(state) = PAUSED, mi(artist) + \" - \" + mi(title), \"*** NOTHING PLAYING - TAP EJECT ***\")$",
        "text_size": 13.0,
        "paint_color": "#FF00FFAA"
    })

    # 7. Frosted Glass Seekbar
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "SeekBar_Glass_Track",
        "position_offset_y": 42.0,
        "shape_type": "RECT",
        "shape_width": 650.0,
        "shape_height": 12.0,
        "shape_corners": 6.0,
        "paint_color": "#4D000000"
    })

    items.append({
        "internal_type": "ProgressModule",
        "internal_title": "SeekBar_Liquid_Progress",
        "position_offset_y": 42.0,
        "progress_mode": "MUSIC",
        "progress_width": 646.0,
        "progress_height": 8.0,
        "shape_corners": 4.0,
        "paint_color": "#E600FFAA"
    })

    # 8. Info & Volume Details
    items.append({
        "internal_type": "TextModule",
        "internal_title": "Info_Bar",
        "position_offset_x": -160.0,
        "position_offset_y": 66.0,
        "text_expression": "$if(mi(album) != \"\", \"ALBUM: \" + mi(album) + \"  |  \", \"\") + \"VOL: \" + si(vol) + \"%\"$",
        "text_size": 11.0,
        "paint_color": "#B3CBD5E1"
    })

    items.append({
        "internal_type": "TextModule",
        "internal_title": "Player_Pkg",
        "position_offset_x": 220.0,
        "position_offset_y": 66.0,
        "text_expression": "$mi(package)$",
        "text_size": 11.0,
        "paint_color": "#8094A3B8"
    })

    # 9. Liquid Glass Transport Buttons
    buttons = [
        ("Btn_Prev", -240.0, "|<<", "PREVIOUS", "#FFF8FAFC", 15.0),
        ("Btn_Play", -120.0, "▶", "PLAY_PAUSE", "$if(mi(state) = PLAYING, \"#FF00FFAA\", \"#FFF8FAFC\")$", 18.0),
        ("Btn_Pause", 0.0, "❚❚", "PLAY_PAUSE", "$if(mi(state) = PAUSED, \"#FF00FFAA\", \"#FFF8FAFC\")$", 15.0),
        ("Btn_Next", 120.0, ">>|", "NEXT", "#FFF8FAFC", 15.0),
        ("Btn_Eject", 240.0, "⏏", "OPEN_PLAYER", "#FFF8FAFC", 18.0),
    ]

    for name, ox, symbol, m_action, color_expr, font_sz in buttons:
        # Glass Capsule Outer Highlight
        items.append({
            "internal_type": "ShapeModule",
            "internal_title": f"{name}_Glass_Rim",
            "position_offset_x": ox,
            "position_offset_y": 106.0,
            "shape_type": "RECT",
            "shape_width": 96.0,
            "shape_height": 42.0,
            "shape_corners": 10.0,
            "paint_color": "#4DFFFFFF"
        })

        # Glass Capsule Face
        face_mod = {
            "internal_type": "ShapeModule",
            "internal_title": f"{name}_Glass_Face",
            "position_offset_x": ox,
            "position_offset_y": 106.0,
            "shape_type": "RECT",
            "shape_width": 94.0,
            "shape_height": 40.0,
            "shape_corners": 9.0,
            "paint_color": "#33283244",
            "internal_events": [
                {
                    "type": "SINGLE_TAP",
                    "action": "MUSIC",
                    "music_action": m_action
                }
            ]
        }
        if name == "Btn_Play":
            face_mod["internal_formulas"] = {"paint_color": "$if(mi(state) = PLAYING, \"#4D00FFAA\", \"#33283244\")$"}
            face_mod["internal_toggles"] = {"paint_color": 10}
        elif name == "Btn_Pause":
            face_mod["internal_formulas"] = {"paint_color": "$if(mi(state) = PAUSED, \"#4D00FFAA\", \"#33283244\")$"}
            face_mod["internal_toggles"] = {"paint_color": 10}
        items.append(face_mod)

        # Symbol
        text_mod = {
            "internal_type": "TextModule",
            "internal_title": f"{name}_Symbol",
            "position_offset_x": ox,
            "position_offset_y": 106.0,
            "text_expression": symbol,
            "text_size": font_sz,
            "paint_color": "#FFF8FAFC"
        }
        if "$" in color_expr:
            text_mod["internal_formulas"] = {"paint_color": color_expr}
            text_mod["internal_toggles"] = {"paint_color": 10}
        else:
            text_mod["paint_color"] = color_expr
        items.append(text_mod)

    preset_data = {
        "preset_info": {
            "version": 11,
            "title": "Retro Amp (Liquid Glass Edition)",
            "description": "Liquid Frosted Glass edition of the classic Winamp player for KWGT",
            "author": "Antigravity / Arnold Mitre",
            "email": "omalauncher@local",
            "width": 720,
            "height": 360,
            "features": "MUSIC",
            "release": 345007816,
            "locked": False,
            "pflags": 0
        },
        "preset_root": {
            "internal_type": "RootLayerModule",
            "config_scale_value": 100.0,
            "viewgroup_items": items
        }
    }

    repo_dir = "/root/winamp-kwgt-widget"
    out_json = os.path.join(repo_dir, "preset.json")
    with open(out_json, "w") as f:
        json.dump(preset_data, f, indent=2)
    print("Saved updated preset.json")

    kwgt_path = os.path.join(repo_dir, "RetroAmp_Winamp.kwgt")
    with zipfile.ZipFile(kwgt_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(out_json, arcname="preset.json")
    print(f"Created {kwgt_path}")

    # Also update /root and /sdcard
    with open("/root/preset.json", "w") as f:
        json.dump(preset_data, f, indent=2)
    with zipfile.ZipFile("/root/RetroAmp_Winamp.kwgt", "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(out_json, arcname="preset.json")
    os.system("cp /root/RetroAmp_Winamp.kwgt /sdcard/Kustom/widgets/RetroAmp_Winamp.kwgt 2>/dev/null")

build_liquid_glass_kwgt()
