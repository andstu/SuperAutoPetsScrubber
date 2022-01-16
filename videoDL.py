from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=va3_GuhUotg&list=PLOQLqxudEz9NUjFBqyAOp9kiFlP7OoERT')

stream = yt.streams.filter(resolution='1080p')[0]
print(stream)

stream.download(output_path='videos/')

