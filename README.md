# Hockey League Statistics Application

This application allows users to examine NHL player statistics from the 2019-20 season interactively.

## Features
- Search for a player's statistics by name.
- List all NHL team abbreviations.
- List all countries represented by players.
- List players by team, ordered by points.
- List players by country, ordered by points.

## Data Files
The application works with two JSON files:
- `partial.json`: A smaller dataset for testing.
- `all.json`: Comprehensive statistics for all NHL players during the 2019-20 season.

Each player entry has the following structure:
```json
{
    "name": "Patrik Laine",
    "nationality": "FIN",
    "assists": 35,
    "goals": 28,
    "penalties": 22,
    "team": "WPG",
    "games": 68
}
```

## Usage Instructions
1. Clone the repository or download the files.
2. Ensure Python is installed.
3. Navigate to the project directory in a terminal.
4. Run the application:
   ```bash
   python hockey_statistics.py
   ```
5. Follow the interactive prompts.

## Sample Output
```
file name: partial.json
read the data of 14 players

commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals

command: 1
name: Travis Zajac

Travis Zajac         NJD   9 + 16 =  25
```

## Output Format
Each player's statistics will be formatted as follows:
```
Leon Draisaitl       EDM  43 + 67 = 110
Connor McDavid       EDM  34 + 63 =  97
Travis Zajac         NJD   9 + 16 =  25
```

## Requirements
- Python 3.x
- JSON files (`partial.json` and `all.json`) should be in the same directory as the script.

