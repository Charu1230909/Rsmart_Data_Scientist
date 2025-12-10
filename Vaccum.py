# Define room states
rooms = ["Clean", "Dirty", "Clean", "Clean"]

# Start at Room1 (index 0)
position = 0

# Move through all rooms
while position < len(rooms):
    print(f"\nAgent at Room {position+1}")
    
    if rooms[position] == "Dirty":
        print("Action: Suck")
        rooms[position] = "Clean"  # Clean the room
    else:
        print("Action: Move Right")
        position += 1  # Move to next room

# Final check after loop
if all(state == "Clean" for state in rooms):
    print("\nAll rooms clean. Action: Do Nothing")

