import pgzrun
import random

# Game state: tracks Brawler positions and health for each player
game_state = {
    "player": {"brawlers": [{"name": "Shelly", "x": 0, "y": 0, "health": 3600}, {"name": "Colt", "x": 1, "y": 1, "health": 3200}]},
    "robot": {"brawlers": [{"name": "Jessie", "x": 2, "y": 2, "health": 3400}, {"name": "Brock", "x": 3, "y": 3, "health": 2800}]}
}

current_turn = "player"

def player_move(brawler_id, new_x, new_y):
    """Handle player move by updating the game state."""
    game_state["player"]["brawlers"][brawler_id]["x"] = new_x
    game_state["player"]["brawlers"][brawler_id]["y"] = new_y
    print(f"Player moved Brawler {brawler_id} to ({new_x}, {new_y})")

    # After player move, it's robot's turn
    robot_turn()

def robot_turn():
    """Handle robot moves."""
    global current_turn
    if current_turn == "robot":
        # Robot randomly moves one of its Brawlers
        for brawler_id, brawler in enumerate(game_state["robot"]["brawlers"]):
            new_x = random.randint(0, 4)
            new_y = random.randint(0, 4)
            brawler["x"] = new_x
            brawler["y"] = new_y
            print(f"Robot moved Brawler {brawler['name']} to ({new_x}, {new_y})")
        
        # Switch back to player turn
        current_turn = "player"

def update():
    """Update the game state."""
    if current_turn == "robot":
        robot_turn()

def draw():
    """Render the game state."""
    screen.clear()
    
    # Draw player's Brawlers
    for brawler in game_state["player"]["brawlers"]:
        screen.draw.text(f"{brawler['name']} ({brawler['x']}, {brawler['y']})", (brawler['x'] * 50, brawler['y'] * 50), color="white")
    
    # Draw robot's Brawlers
    for brawler in game_state["robot"]["brawlers"]:
        screen.draw.text(f"{brawler['name']} ({brawler['x']}, {brawler['y']})", (brawler['x'] * 50, brawler['y'] * 50), color="red")

def on_mouse_down(pos):
    """Handle mouse clicks for player actions."""
    if current_turn == "player":
        # For simplicity, we assume the player is always moving Brawler 0 (Shelly)
        brawler_id = 0
        new_x = pos[0] // 50
        new_y = pos[1] // 50
        player_move(brawler_id, new_x, new_y)

# Start the game
pgzrun.go()
