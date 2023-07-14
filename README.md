# phoning-home

Phoning home provides out of the box capabilities
to phone home for security, analytics, gaming and reporting
with in-built consent mechanism. 
No server setups needed, only [Turso](https://turso.tech/) atm.


# Demo

```py
from phoning_home import ph

# url, token
ph.connect('http://url.turso.io', 't0k3nfh734tr673gqi78rytg3q34786')
# or change at any time
# ph.url('...')
# ph.token('...')

# Increment counters
@ph.counter('ZIP_DWNLDS')
def download_zipfile():
    # code for downloading zip file
    # or use ph.counter('ZIP_DWNLDS').incr()
    ...
count = ph.fetch('counter', 'ZIP_DWNLDS') 

# Leaderboard
ph.leaderboard('scrabble-123', 'yus', 100)
leaderboard = ph.fetch('leaderboard', 'scrabble-123')

# Send a deluge of kv values 
ph.info({
    'version': '1.2.3',
    'os': 'linux'
})
info = ph.fetch('info')

# Or namespace it
data = {
    'name': 'Miaw Spoogle',
    'username': 'purr678'
}
ph.namedinfo('USER_INFO', data)
namedinfo = ph.fetch('namedinfo', 'USER_INFO')
```