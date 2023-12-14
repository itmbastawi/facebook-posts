import facebook
import func_helper
import os

def search_topic(topic):
    """
    search for posts by topic on facebook
    input: topic(string)
    output: list of posts(list)
    """
    access_token = os.environ.get('FACEBOOK_ACCESS_TOKEN')

    graph = facebook.GraphAPI(access_token,version="3.0")

    # Search for posts containing "karate sport"
    query = topic
    fields = ["message", "from", "created_time", "image"]  # Fields you want to collect
    parameters = {"type": "post"}  # Specify post type

    results = graph.request(f"/search?q={query}&fields={fields}&{parameters}")
    return results


if __name__ == '__main__':
    topic = 'karate'
    # get posts data
    results = search_topic(topic)
    # save data to database
    db = func_helper.connect_to_mongodb()
    collection = db['posts']
    collection.insert_many(results)
    
