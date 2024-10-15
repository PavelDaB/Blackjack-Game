# Blackjack Game 🎲🃏

A simple command-line **Blackjack** game built using Python. This game allows players to play against a dealer, following the traditional Blackjack rules. The code is structured with loops and functions to handle dealing cards, tracking hands, and checking for win/loss conditions.

## Table of Contents
- [How to Play](#how-to-play)
- [Features](#features)
- [Rules](#rules)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Gameplay](#sample-gameplay)
- [Future Improvements](#future-improvements)
- [License](#license)

## How to Play
1. The game starts by dealing **two cards** each to the player and the dealer.
2. The player can choose to:
   - **Hit** (draw another card)
   - **Stay** (end their turn)
3. The dealer will continue drawing cards until their hand total reaches 17 or more.
4. The goal is to get as close to **21** as possible without going over.
5. If either the player or dealer gets exactly 21, it's a **Blackjack**!

## Features
- **Random Card Dealing**: Cards are drawn randomly from a standard 52-card deck.
- **Ace Handling**: Aces can be counted as either 1 or 11, depending on the hand.
- **Dealer Logic**: Dealer automatically draws cards until their hand total is 17 or higher.
- **Replay Option**: After each game, players can choose to play again or exit.
- **Real-Time Score Tracking**: Both player and dealer totals are updated throughout the game.

## Rules
- Number cards (2-10) are worth their face value.
- Face cards (J, Q, K) are worth 10 points.
- Aces can be worth 11 or 1, depending on the total hand value.
- **Bust**: If a player’s hand exceeds 21, they lose.
- If both the player and dealer have the same total, it’s a **push** (a tie).

## Installation
1. Make sure Python is installed on your machine. You can download it [here](https://www.python.org/downloads/).
2. Clone this repository or download the source code:
   ```bash
   git clone https://github.com/PavelDaB/blackjack-game.git
   cd blackjack-game
