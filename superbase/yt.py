from youtube_transcript_api import YouTubeTranscriptApi
from youtube_search import YoutubeSearch

def search_and_get_captions(query):
    try:
        # Search for videos related to the query on YouTube
        results = YoutubeSearch(query, max_results=10).to_dict()
        print(results)

        if not results:
            return "No results found for the given query."

        # Get the video ID of the first result
        video_id = results[0]['id'] 

        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        if not transcript:
            return "No captions available for the selected video."

        # Combine the text from each entry in the transcript
        captions = '\n'.join(entry['text'] for entry in transcript)

        return captions

    except Exception as e:
        return f"An error occurred: {str(e)}"