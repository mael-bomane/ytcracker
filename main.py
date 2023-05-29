from pytube import Playlist, YouTube
if __name__ == "__main__":
    file = open('playlist.txt', 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        playlist = Playlist(line)
        print("Downloading :\n{}".format(playlist.title))
        for video in playlist.videos:
            video.streams.filter(file_extension='mp4').first().download()
