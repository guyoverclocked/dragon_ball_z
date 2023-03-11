from flask import Flask, render_template, request
import mysql.connector

# establishing the connection
conn = mysql.connector.connect(
    user='nambitech', password='nambipace4', host='db4free.net', database='dragon_ball_z'
)

# Creating a cursor object using the cursor() method

cursor = conn.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    query = "SELECT COUNT(*) FROM links"
    cursor.execute(query)
    result = cursor.fetchall()
    result1 = result[0][0]
    print(result1)
    return render_template("home.html", result1 = result1)

@app.route("/player")
def player():
    episode = request.args.get("episode")
    if episode:
        episode = int(episode)
        if episode < 10:
            episode = str('0' + str(episode))
        
        cursor.execute(f"SELECT * FROM links WHERE links LIKE '%DBZ_Episode_{episode}_Dubbed_Dragonball360.me.mp4%'")
        link = cursor.fetchone()[0]
        epi_next = int(episode) + 1
        epi_prev = int(episode) - 1
        if epi_next < 10 or epi_prev < 10:
            link_next = str('0' + str(epi_next))
            link_prev = str('0' + str(epi_prev))
        else:
            link_next = str(epi_next)
            link_prev = str(epi_prev)
        # if link_prev == '00':
        #     link_prev == '01'
        query = "SELECT COUNT(*) FROM links"
        cursor.execute(query)
        result = cursor.fetchall()
        result1 = result[0][0]
        cur_epi = int(episode)
        return render_template("player.html", episode=episode, link=link, link_prev=link_prev, link_next=link_next, result1=result1, cur_epi=cur_epi)
    else:
        return render_template("player.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)
