import json
import zipfile
import os

def create_kwgt():
    items = []
    
    # Base background (Dark metallic chassis)
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "Chassis_Shadow",
        "shape_type": "RECT",
        "shape_width": 680.0,
        "shape_height": 320.0,
        "shape_corners": 6.0,
        "paint_color": "#FF0E1014"
    })
    
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "Chassis_Bevel",
        "shape_type": "RECT",
        "shape_width": 674.0,
        "shape_height": 314.0,
        "shape_corners": 5.0,
        "paint_color": "#FF383D48"
    })

    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "Chassis_Face",
        "shape_type": "RECT",
        "shape_width": 670.0,
        "shape_height": 310.0,
        "shape_corners": 4.0,
        "paint_color": "#FF22252C"
    })

    # Title Bar
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "TitleBar_Bg",
        "position_offset_y": -132.0,
        "shape_type": "RECT",
        "shape_width": 660.0,
        "shape_height": 30.0,
        "shape_corners": 2.0,
        "paint_color": "#FF1A1C22"
    })

    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "TitleBar_Line_Left",
        "position_offset_x": -180.0,
        "position_offset_y": -132.0,
        "shape_type": "RECT",
        "shape_width": 160.0,
        "shape_height": 2.0,
        "paint_color": "#FF00FF66"
    })

    items.append({
        "internal_type": "TextModule",
        "internal_title": "TitleBar_Text",
        "position_offset_y": -132.0,
        "text_expression": "RETRO AMP • WINAMP",
        "text_size": 13.0,
        "paint_color": "#FFE5E9F0"
    })

    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "TitleBar_Line_Right",
        "position_offset_x": 180.0,
        "position_offset_y": -132.0,
        "shape_type": "RECT",
        "shape_width": 160.0,
        "shape_height": 2.0,
        "paint_color": "#FF00FF66"
    })

    # LCD Screen Frame
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "LCD_Bezel",
        "position_offset_y": -36.0,
        "shape_type": "RECT",
        "shape_width": 650.0,
        "shape_height": 134.0,
        "shape_corners": 2.0,
        "paint_color": "#FF101216"
    })

    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "LCD_Screen",
        "position_offset_y": -36.0,
        "shape_type": "RECT",
        "shape_width": 642.0,
        "shape_height": 126.0,
        "shape_corners": 2.0,
        "paint_color": "#FF081009",
        "internal_events": [
            {
                "type": "SINGLE_TAP",
                "action": "MUSIC",
                "music_action": "OPEN_PLAYER"
            }
        ]
    })

    # LCD: Play status
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Status",
        "position_offset_x": -250.0,
        "position_offset_y": -80.0,
        "text_expression": "$if(mi(state) = PLAYING, \"▶ PLAY\", if(mi(state) = PAUSED, \"❚❚ PAUSE\", \"■ STOP\"))$",
        "text_size": 12.0,
        "paint_color": "#FF00FF66"
    })

    # LCD: Stereo
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Stereo",
        "position_offset_x": -160.0,
        "position_offset_y": -80.0,
        "text_expression": "$if(mi(state) = PLAYING, \"STEREO\", \"MONO\")$",
        "text_size": 12.0,
        "paint_color": "#FF00EE55"
    })

    # LCD: Audio info
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Kbps",
        "position_offset_x": -70.0,
        "position_offset_y": -80.0,
        "text_expression": "192 kbps 44 kHz",
        "text_size": 11.0,
        "paint_color": "#FF00AA44"
    })

    # LCD: Digital Clock (Elapsed)
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Time",
        "position_offset_x": 200.0,
        "position_offset_y": -76.0,
        "text_expression": "$tf(mi(pos), mm:ss)$",
        "text_size": 30.0,
        "paint_color": "#FF00FF66"
    })

    # LCD: Total Duration
    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Total",
        "position_offset_x": 275.0,
        "position_offset_y": -74.0,
        "text_expression": "$if(mi(len) > 0, \"/ \" + tf(mi(len), mm:ss), \"\")$",
        "text_size": 13.0,
        "paint_color": "#FF00AA44"
    })

    # LCD: Simulated Spectrum Analyzer Bars
    # 12 vertical equalizer bars
    num_bars = 12
    start_x = -260.0
    bar_width = 8.0
    gap = 4.0
    for i in range(num_bars):
        bx = start_x + i * (bar_width + gap)
        # Dynamic height formula based on playback & seconds
        h_formula = f"$if(mi(state) = PLAYING, 6 + (df(S) * {3 + (i%5)} + {i*7}) % 36, 4)$"
        items.append({
            "internal_type": "ShapeModule",
            "internal_title": f"LCD_SpecBar_{i+1}",
            "position_offset_x": bx,
            "position_offset_y": -34.0,
            "shape_type": "RECT",
            "shape_width": bar_width,
            "shape_height": 20.0,
            "internal_formulas": {
                "shape_height": h_formula
            },
            "internal_toggles": {
                "shape_height": 10
            },
            "paint_color": "#FF00FF66" if i < 9 else "#FFFFCC00"
        })

    # LCD: Marquee Track Banner
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "LCD_Marquee_Box",
        "position_offset_x": 80.0,
        "position_offset_y": -34.0,
        "shape_type": "RECT",
        "shape_width": 380.0,
        "shape_height": 30.0,
        "paint_color": "#FF050C06"
    })

    items.append({
        "internal_type": "TextModule",
        "internal_title": "LCD_Marquee_Text",
        "position_offset_x": 80.0,
        "position_offset_y": -34.0,
        "text_expression": "$if(mi(state) = PLAYING | mi(state) = PAUSED, mi(artist) + \" - \" + mi(title), \"*** NOTHING PLAYING - TAP EJECT ***\")$",
        "text_size": 13.0,
        "paint_color": "#FF00FF66"
    })

    # Seek Bar (Progress Bar)
    items.append({
        "internal_type": "ShapeModule",
        "internal_title": "SeekBar_Track",
        "position_offset_y": 42.0,
        "shape_type": "RECT",
        "shape_width": 642.0,
        "shape_height": 12.0,
        "paint_color": "#FF0C0F12"
    })

    items.append({
        "internal_type": "ProgressModule",
        "internal_title": "SeekBar_Progress",
        "position_offset_y": 42.0,
        "progress_mode": "MUSIC",
        "progress_width": 638.0,
        "progress_height": 8.0,
        "paint_color": "#FF00DD55"
    })

    # Volume & Info Row
    items.append({
        "internal_type": "TextModule",
        "internal_title": "Info_Bar",
        "position_offset_x": -160.0,
        "position_offset_y": 66.0,
        "text_expression": "$if(mi(album) != \"\", \"ALBUM: \" + mi(album) + \"  |  \", \"\") + \"VOL: \" + si(vol) + \"%\"$",
        "text_size": 11.0,
        "paint_color": "#FFA0A6B2"
    })

    items.append({
        "internal_type": "TextModule",
        "internal_title": "Player_Pkg",
        "position_offset_x": 220.0,
        "position_offset_y": 66.0,
        "text_expression": "$mi(package)$",
        "text_size": 11.0,
        "paint_color": "#FF687182"
    })

    # Transport Buttons Row
    # Buttons: PREV, PLAY, PAUSE, NEXT, EJECT
    buttons = [
        ("Btn_Prev", -240.0, "|<<", "PREVIOUS", "#FFE0E0E0", 15.0),
        ("Btn_Play", -120.0, "▶", "PLAY_PAUSE", "$if(mi(state) = PLAYING, \"#FF00FF66\", \"#FFE0E0E0\")$", 18.0),
        ("Btn_Pause", 0.0, "❚❚", "PLAY_PAUSE", "$if(mi(state) = PAUSED, \"#FF00FF66\", \"#FFE0E0E0\")$", 15.0),
        ("Btn_Next", 120.0, ">>|", "NEXT", "#FFE0E0E0", 15.0),
        ("Btn_Eject", 240.0, "⏏", "OPEN_PLAYER", "#FFE0E0E0", 18.0),
    ]

    for name, ox, symbol, m_action, color_expr, font_sz in buttons:
        # Button Bevel / Frame
        items.append({
            "internal_type": "ShapeModule",
            "internal_title": f"{name}_Bevel",
            "position_offset_x": ox,
            "position_offset_y": 106.0,
            "shape_type": "RECT",
            "shape_width": 96.0,
            "shape_height": 42.0,
            "shape_corners": 3.0,
            "paint_color": "#FF3A3F4B"
        })
        items.append({
            "internal_type": "ShapeModule",
            "internal_title": f"{name}_Face",
            "position_offset_x": ox,
            "position_offset_y": 106.0,
            "shape_type": "RECT",
            "shape_width": 92.0,
            "shape_height": 38.0,
            "shape_corners": 2.0,
            "paint_color": "#FF252830",
            "internal_events": [
                {
                    "type": "SINGLE_TAP",
                    "action": "MUSIC",
                    "music_action": m_action
                }
            ]
        })
        text_mod = {
            "internal_type": "TextModule",
            "internal_title": f"{name}_Symbol",
            "position_offset_x": ox,
            "position_offset_y": 106.0,
            "text_expression": symbol,
            "text_size": font_sz,
            "paint_color": "#FFE0E0E0"
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
            "title": "Retro Amp (Winamp)",
            "description": "Late-90s Winamp music player widget for Android home screens via KWGT",
            "author": "Antigravity / Bryan Perdana",
            "email": "omalauncher@local",
            "width": 720,
            "height": 360,
            "features": "MUSIC",
            "release": 345007815,
            "locked": False,
            "pflags": 0
        },
        "preset_root": {
            "internal_type": "RootLayerModule",
            "config_scale_value": 100.0,
            "viewgroup_items": items
        }
    }

    out_json = "/root/preset.json"
    with open(out_json, "w") as f:
        json.dump(preset_data, f, indent=2)
    print("Saved preset.json successfully")

    # Zip into .kwgt
    kwgt_path = "/root/RetroAmp_Winamp.kwgt"
    with zipfile.ZipFile(kwgt_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(out_json, arcname="preset.json")
    print(f"Created {kwgt_path} ({os.path.getsize(kwgt_path)} bytes)")

create_kwgt()
