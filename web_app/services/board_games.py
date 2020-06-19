import os 
from flask import Blueprint, request#, jsonify, render_template
import requests, bs4 
# from dotenv import load_dotenv
# from tweepy import OAuthHandler, API

# load_dotenv()

# TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
# TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
# TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
# TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
# auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# api = API(auth)
# print("API CLIENT", api)

game_id = 13
url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, features='lxml')
print('Name: ', soup.find('name').text,'\n')
print('Min players: ', soup.find('minplayers').text, '\n')
print('Max players: ', soup.find('maxplayers').text, '\n')
print('Playing time: ', soup.find('playingtime').text, '\n')
print('Description: ', soup.find('description').text, '\n')
print('Board game mechanics:')
boardgamemechanic = soup.find_all('boardgamemechanic')
for i in boardgamemechanic: print(i.text)


# for multiple
# temp = soup.find_all('name')
# for i in temp: print(i)

print()
# breakpoint()


if __name__ == "__main__":
    # user = api.get_user("realDonaldTrump")
    # print("TWITTER USER:", type(user))

    # print(user.id)
    # print(user.screen_name)
    # print(user.name)


    # tweets = api.user_timeline("realDonaldTrump", tweet_mode = "extended")
    # print("TWEETS", type(tweets))
    # print(type(tweets[0]))


    # tweet = tweets[0]
    # print(tweet.id)
    # print(tweet.full_text)
    # breakpoint()
    print('OK')
















