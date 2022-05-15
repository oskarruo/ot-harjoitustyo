import json
import os

DIR_NAME = os.path.dirname(__file__)

class Stagehandler:
    def __init__(self):
        with open(os.path.join(DIR_NAME, "stages", "stages.json")) as file: # pylint: disable=unspecified-encoding
            data = file.read()
        self.stages = json.loads(data)
        self.current_stage = 0

    def get_stagemap(self):
        return self.stages[self.current_stage]["stagemap"]

    def get_stage_cellsize(self):
        return self.stages[self.current_stage]["cellsize"]

    def get_stage_pickup_amount(self):
        return self.stages[self.current_stage]["pickups"]

    def get_stage_enemy_info(self):
        enemy_info = {}
        enemies = self.stages[self.current_stage]["enemies"]
        for i in range(enemies):
            enemy_info[str(i+7)] = self.stages[self.current_stage]["enemy"+str(i+7)]
        return enemy_info

    def next_stage(self):
        if self.current_stage < len(self.stages) - 1:
            self.current_stage += 1
        else:
            return True
