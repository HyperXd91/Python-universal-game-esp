from mylib import ESPTools
import time

# Initialize for a specific game
try:
    esp = ESPTools("ac_client.exe") # Example: AssaultCube
    print("ESP Library Initialized!")
except Exception as e:
    print(e)
    exit()

# Dummy offsets (Users must find these using Cheat Engine)
VIEW_MATRIX_ADDR = 0x501AE8 
ENTITY_LIST_ADDR = 0x10F4F4

def run_esp():
    while True:
        # 1. Read View Matrix (16 floats)
        view_matrix = [esp.pm.read_float(VIEW_MATRIX_ADDR + i * 4) for i in range(16)]
        
        # 2. Get Entity Position (Example: Player 1)
        # In a real scenario, loop through an entity list
        ent_x = esp.pm.read_float(ENTITY_LIST_ADDR + 0x4)
        ent_y = esp.pm.read_float(ENTITY_LIST_ADDR + 0x8)
        ent_z = esp.pm.read_float(ENTITY_LIST_ADDR + 0xC)
        
        # 3. Convert to Screen
        coords = esp.world_to_screen(view_matrix, (ent_x, ent_y, ent_z), 1920, 1080)
        
        if coords:
            print(f"Drawing Box at: {coords}")
            # Here the user would use a library like Pygame or Overlay to draw
        
        time.sleep(0.01)

if __name__ == "__main__":
    run_esp()