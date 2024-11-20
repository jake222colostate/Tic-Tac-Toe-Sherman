#Last Updated for Sprint 5
### Message Structure
- `{ "message": "some text" }`

## Running the Server
To start the server, run:
```bash
python server.py
```

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
## Project Title: Jakes Hardcore Connect Four

Team:
[Jake S]

Project Objective:
[I personally am hoping to create a functional conntect four game.]

Scope:
Inclusions:
[Connect four tiles in a row, or diagnoally to win!]
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
