import os
from supabase_py import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)


# Function to Fetch All Games
def find_all_games():
    data = supabase.table("games").select("*").execute()
    # Equivalent for SQL Query "SELECT * FROM games;"
    return data['data']


games = find_all_games()


# Function to add a new game
def add_game_to_DB(title, hours) -> dict:

    game = {
        "title": title,
        "hours": hours
    }
    data = supabase.table("games").insert(game).execute()
    # Equivalent to the SQL Insert

    return data['data']
