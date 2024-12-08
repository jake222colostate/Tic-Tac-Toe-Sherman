Last Updated for Sprint 5
### Message Structure
- `{ "message": "some text" }`

## Running the Server
To start the server, run:
```bash
python server.py
```
## Write Up / Final Assesment
There is still a lot that needs to be done on my project.  For starters, I had trouble using a nonstatic IP address
for connecting seperate clients to the server, so I would work on that next.  I would also make a nice looking
functional webpage to play the game on.

-For the most part, all of my project went right.  Minus the static IP address issue, my project works smoothly and as intended.  One thing that could be improved on is placing a tile on the last moves that declares a win, opposed to just a message being sent to the client expressing that a user won. 

## Running the Client
To start the client, run:
```bash
python client.py
```
## Game Message Protocol

### Message Types
- **Join**: Sent when a player joins.
  - `{'type': 'join', 'client_id': '<unique_client_id>'}`
- **Move**: Sent when a player makes a move.
  - `{'type': 'move', 'move': <board_index>}`
- **Update**: Sent by the server to update game state.
  - `{'type': 'update', 'game_state': <game_state_dict>}`
- **Disconnect**: Notifies clients of player disconnection.
  - `{'type': 'disconnect', 'client_id': '<unique_client_id>'}`

### Game State Format
- `game_state`: Contains the board and the current player’s turn:
  ```python
  game_state = {
      'board': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      'current_turn': '<client_id>'
  }



# Statement of Work
## Project Title: Jake's TeamTryMyBest Tic-Tac-Toe.

Team:
[Jake S]

Project Objective:
[I personally am hoping to create a functional Tic-Tac-Toe game.]

Scope:
Inclusions:
[Get three Tiles in a row in a straight line or diagonally.]
Exclusions:
[N/A at the moment]
Deliverables:
[N/A at the moment]
Timeline:
Key Milestones:
Task Breakdown:
Technical Requirements:
Hardware:
Software:
Assumptions:
Roles and Responsibilities:
I, Jake Sherman will be taking on all roles and responsibilities.
