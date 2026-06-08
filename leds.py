# hardware controls

import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 30)

def set_mood_color(mood):
    colors = {
        "happy": (255, 182, 193),
        "sad": (135, 206, 235),
        "angry": (255, 99, 71),
        "neutral": (255, 255, 255)
    }
    pixels.fill(colors.get(mood, (255, 255, 255)))

  
 # Copyright © 2026 Osasere H. Ero. All rights reserved.
 # Proprietary and confidential. Unauthorized copying of this file, via any medium, is strictly prohibited.
