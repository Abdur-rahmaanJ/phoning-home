from phoning_home import ph
import os

token = os.environ['TURSO_TOKEN']
ph.connect(os.environ['TURSO_URL'], token)

ph.leaderboard('scrabble-123', 'yus', 100)
leaderboard = ph.fetch('leaderboard', 'scrabble-123')
print(leaderboard)