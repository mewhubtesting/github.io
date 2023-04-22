from flask import Flask,jsonify,send_file,render_template,make_response
import requests
from io import BytesIO
import base64
from flask_cors import CORS


BASE_FRIENDS_URL = "https://friends.roblox.com/v1/users"    
app = Flask(__name__)
CORS(app)

@app.route("/social_stats/<userid>")
def get_social_status(userid,server=None):
    FOLLOWERS_URL = f"{BASE_FRIENDS_URL}/{userid}/followers"
    FRIENDS_URL = f"{BASE_FRIENDS_URL}//{userid}/friends"
    FOLLOWING_URL = f"{BASE_FRIENDS_URL}//{userid}/followings"
    user_follower_count = requests.get(f"{FOLLOWERS_URL}/count")
    user_friend_count = requests.get(f"{FRIENDS_URL}/count")
    user_following_count = requests.get(f"{FOLLOWING_URL}/count")
    followers_count = user_follower_count.json().get("count", 0)
    friends_count = user_friend_count.json().get("count", 0)
    followings_count = user_following_count.json().get("count", 0)
    if server:
        return {"followersC":followers_count, "followingsC":followings_count, "friendsC":friends_count}
    return jsonify({"followersC":followers_count, "followingsC":followings_count, "friendsC":friends_count})

    
@app.route("/headimage/<userid>")
def get_user_image(userid,server=None):
    HEADSHOT_URL = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false"
    response = requests.get(HEADSHOT_URL)
    response = requests.get(response.json()["data"][0]["imageUrl"])
    img = BytesIO(response.content)
    if server:
        img_content = base64.b64encode(response.content).decode('utf-8')
        return f'data:image/png;base64,{img_content}'
    return send_file(img, mimetype='image/png')

@app.route("/rapandvalue/<userid>")
def get_rap_and_value(userid,server=None):
    request = requests.get(f'https://www.rolimons.com/playerapi/player/{userid}').json()
    if request["success"] == False:
        return f"<h1>Error: {request['message']} </h1>"
    player_value = request['value']
    player_rap = request['rap']
    if server:
        return {"rap":player_rap,"value":player_value}
    return jsonify({"rap":player_rap,"value":player_value})

@app.route("/getprimry/<userid>")
def get_fav_items(userid,server=None):
    PRIMARY_URL = f"https://groups.roblox.com/v1/users/{userid}/groups/primary/role"
    req = requests.get(PRIMARY_URL).json()
    if req == None:
      return "<h1>Error</h1>"

    if req['group'] == None:
      return "<h1>Error</h1>"
    group_link = f"https://www.roblox.com/groups/{req['group']['id']}"
    if server:
        return {"group":req['group'],"link":group_link}
    return jsonify({"group":req['group'],"link":group_link})

@app.route("/getusername/<userid>")
def get_username(userid,server=None):
    USERNAME_URL = f"https://users.roblox.com/v1/users/{userid}"
    response = requests.get(USERNAME_URL)
    if response.status_code == 200:
        data = response.json()
        if server:
            return {"username":data["name"],"display":data["displayName"]}
        return jsonify({"username":data["name"],"display":data["displayName"]})
    else:
        return "<h1>Error</h1>"

@app.route("/profile/<userid>")
def profile(userid):
    social_stats = get_social_status(userid, server=True)
    image_url = get_user_image(userid, server=True)
    username_display = get_username(userid, server=True)
    if username_display == "<h1>Error</h1>":
        return "<h1>Error: Not real user</h1>"
    svg_s = render_template(
        "index.html", followers_count=social_stats["followersC"], image_url=image_url, 
        friends_count=social_stats["friendsC"], followings_count=social_stats["followingsC"], 
        username=username_display["username"], display_user=username_display["username"]
    )
    response = make_response(svg_s)
    response.headers.set('Content-Type', 'image/svg+xml')
    return response


if __name__ == "__main__":
    app.run("0.0.0.0",8080)