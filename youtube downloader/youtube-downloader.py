from pytube import YouTube

url = 'write url here'
my_video = YouTube(url)


# Print video title
print(my_video.title)

# Get tumbnail image
print(my_video.thumbnail_url)

# Download video
my_video = my_video.streams.get_highest_resolution()

my_video.download()