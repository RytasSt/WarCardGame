# WarCardGame
## Functionality
### Game Setup
- You play against an AI opponent upon starting.

### Gameplay
- At the start standard deck of cards is shuffled and split evenly between both players
- Every round players reveal the top card from their deck.
- The player with the higher card wins and collects both cards.
- When a player wins a round and collects cards, those cards should be added to the player's deck. Subsequently, the player's deck should be shuffled to ensure randomness in card distribution for future rounds.
- In case of a tie, a "war" occurs:
  - Each player reveals three additional cards face-down and then one card face-up.
  - The player with the higher face-up card wins the war and collects all cards in play.
- The game continues until one player collects all the cards.

### User interface
- Upon starting the game, players are presented with title and instructions on how to play the game
- The game interface displays the current round number, the cards played by the player and the AI opponent, and the outcome of each round.
- Once the game is over the winner is declared

### Controls
- Player presses Enter to reveal cards during gameplay.
