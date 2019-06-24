# First of all you have to install pafy on your anaconda cmd.

#However we can use it to get correct url, and then use player such as vlc to play directly without downloading.
#First we get correct / best URL from youtube using pafy
import pafy
# Do $pip install python-vlc in anaconda cmd  
import vlc

url = "https://www.youtube.com/watch?v=fhE4bhy4pWw"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)

player.play()
#player.pause() #-- to pause video
#player.stop()  #-- to stop/end video
Message=input("Enter Your Message")
if Message=="stop":
	player.stop()
else:
	player.play()
