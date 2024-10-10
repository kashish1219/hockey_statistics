import json

class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = goals+assists

    def __str__(self):
        return f"{self.name:<21}{self.team:>}  {self.goals:>2} + {self.assists:>2} = {self.points:>3}"


class Storage:
    def __init__(self):
        self.players = []
    
    def load_items_from_file(self, file_name: str):
        try:
            with open(file_name) as file:
                data = file.read()
            content = json.loads(data)
            for p in content:
                if p not in self.players:
                    self.players.append(Player(p["name"], p["nationality"], p["assists"], p["goals"], p["penalties"], p["team"], p["games"]))
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{file_name}' contains invalid JSON data.")
        except KeyError as e:
            print(f"Error: Missing key {e} in data.")
        except Exception as e:
            print(f"Unexpected error while loading data: {e}")

    def find_player(self, search_player):
        found = False
        for player in self.players:
            if player.name == search_player:
                print(player)
                found = True
        if not found:
            print(f"Player '{search_player}' not found.")
    
    def sort_player_list(self, my_list):
        custom_list = sorted(set(my_list), key = lambda pl: pl.points, reverse=True)
        if custom_list:
            for player in custom_list:
                print(player)
        else:
            print("No players match the given criteria.")
    
    def player_from_team(self, team):
        match_player = filter(lambda pl: pl.team == team, self.players)
        self.sort_player_list(match_player)
    
    def player_from_country(self, nationality):
        match_player = filter(lambda pl: pl.nationality == nationality, self.players)
        self.sort_player_list(match_player)
    
    def all_teams(self):
        teams = [player.team for player in self.players]
        if teams:
            for team in sorted(list(set(teams))):
                print(team)
        else:
            print("No teams available.")

    def all_countries(self):
        countries = [player.nationality for player in self.players]
        if countries:
            for team in sorted(list(set(countries))):
                print(team)
        else:
            print("No countries available.")

    def most_points(self, how_many):
        try:
            top_scorer = sorted(self.players, key = lambda pl: (pl.points, pl.goals), reverse=True)
            desired = top_scorer[:how_many]
            for player in desired:
                print(player)
        except ValueError:
            print("Invalid number entered. Please enter a valid number.")

    def most_goals(self, how_many):
        try:
            least_games = sorted(self.players, key = lambda  pl: pl.games)
            top_scorer = sorted(least_games, key = lambda pl: pl.goals, reverse=True)
            desired = top_scorer[:how_many]
            for player in desired:
                print(player)
        except ValueError:
            print("Invalid number entered. Please enter a valid number.")
    
class Application:

    def __init__(self):
        self.store = Storage()
    
    def load_data(self):
        user = input("file name: ")            
        self.store.load_items_from_file(user)

        print(f"read the data of {len(self.store.players)} players")
    
    def search(self):
        user = input("name:")
        if not user:
            print("Error: No player name entered.")
        else:
            self.store.find_player(user)
    
    def list_teams(self):
        self.store.all_teams()

    def list_countries(self):
        self.store.all_countries()
    
    def player_in_team(self):
        user = input("team:")
        if not user:
            print("Error: No team entered.")
        else:
            self.store.player_from_team(user)

    def player_in_country(self):
        user = input("country:")
        if not user:
            print("Error: No country entered.")
        else:
            self.store.player_from_country(user)
    
    def most_points(self):
        try:
            user = int(input("how many:"))
            if user < 0:
                print("Error: Please enter a positive number.")
            else:
                self.store.most_points(user)
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
    
    def most_goals(self):
        try:
            user = int(input("how many:"))
            if user < 0:
                print("Error: Please enter a positive number.")
            else:
                self.store.most_goals(user)
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        self.load_data()
        print()
        self.help()
        while True:
            print()
            cmd = input("command: ")
            if cmd == "0":
                break
            elif cmd == "1":
                self.search()
            elif cmd == "2":
                self.list_teams()
            elif cmd == "3":
                self.list_countries()
            elif cmd == "4":
                self.player_in_team()
            elif cmd == "5":
                self.player_in_country()
            elif cmd == "6":
                self.most_points()
            elif cmd == "7":
                self.most_goals()
            else:
                self.help()

app = Application()
app.execute()
