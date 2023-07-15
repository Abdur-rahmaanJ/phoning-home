from phoning_home import ph
import os

token = os.environ['TURSO_TOKEN']
ph.connect(os.environ['TURSO_URL'], token)

ph.leaderboard('scrabble-123', 'yus', 100)
ph.leaderboard('scrabble-123', 'yus', 100)
leaderboard = ph.fetch('leaderboard', 'scrabble-123')
print(leaderboard)


# Send a deluge of kv values 
ph.info({
    'version': '1.2.3',
    'os': 'linux'
})
info = ph.fetch('info')
print(info)

# Or namespace it
data = {
    'name': 'Miaw Spoogle',
    'username': 'purr678'
}
ph.namedinfo('USER_INFO', data)
namedinfo = ph.fetch('namedinfo', 'USER_INFO')
print(namedinfo)

@ph.counter('ZIP_DOWNLOAD')
def x(defwefr):
    pass

x(1)

counter = ph.fetch('counter', 'ZIP_DOWNLOAD')
print(counter)
counter = ph.fetch('counter', 'ZIP_DOWNLOADzzz')
print(counter)