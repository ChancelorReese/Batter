import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import raylibpy
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

from game.solid_blocks import SolidBlock

def main():
    cast = {}

    cast["solid_blocks"] = []
    solid_blocks = []
    for row in range(6):
        for column in range(8):
            solid_block = SolidBlock(row,column)
            solid_blocks.append(solid_block)
    cast["solid_blocks"] = solid_blocks
    
    cast["power_ups"] = []
    cast["blocks"] = []
    cast["players"] = []


    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = []
    script["update"] = []
    script["output"] = [draw_actors_action]
    
    output_service.open_window("Playing with Fire")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()

