from ..superbase.yt import search_and_get_captions
user_query = input("Enter your Awesome query: ")+str('in English Language')
captions_result = yt.search_and_get_captions(user_query)
while "An error occurred: " in captions_result:
  captions_result = yt.search_and_get_captions(user_query)
print("\nCaptions for the video:")
print(captions_result)
