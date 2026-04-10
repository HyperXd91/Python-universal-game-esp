import pymem
import numpy as np

class ESPTools:
    def __init__(self, process_name):
        try:
            self.pm = pymem.Pymem(process_name)
        except Exception as e:
            raise Exception(f"Could not connect to {process_name}: {e}")

    def read_float(self, address):
        return self.pm.read_float(address)

    def world_to_screen(self, view_matrix, world_pos, screen_width, screen_height):
        """
        Standard 4x4 Matrix transformation to convert 3D coordinates to 2D pixels.
        """
        # Matrix multiplication logic
        clip_x = world_pos[0] * view_matrix[0] + world_pos[1] * view_matrix[1] + world_pos[2] * view_matrix[2] + view_matrix[3]
        clip_y = world_pos[0] * view_matrix[4] + world_pos[1] * view_matrix[5] + world_pos[2] * view_matrix[6] + view_matrix[7]
        clip_z = world_pos[0] * view_matrix[8] + world_pos[1] * view_matrix[9] + world_pos[2] * view_matrix[10] + view_matrix[11]
        clip_w = world_pos[0] * view_matrix[12] + world_pos[1] * view_matrix[13] + world_pos[2] * view_matrix[14] + view_matrix[15]

        if clip_w < 0.1:
            return None

        # NDC Coordinates
        ndc_x = clip_x / clip_w
        ndc_y = clip_y / clip_w

        # Screen Coordinates
        screen_x = (screen_width / 2 * ndc_x) + (ndc_x + screen_width / 2)
        screen_y = -(screen_height / 2 * ndc_y) + (ndc_y + screen_height / 2)

        return int(screen_x), int(screen_y)