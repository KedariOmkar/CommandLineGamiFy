import os
import sys
from datetime import date

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")

from flask import Flask, render_template, request, jsonify, redirect, url_for
from supabase import create_client, Client

url = "https://nkfwwmxxuxxnpgrqpjxg.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5rZnd3bXh4dXh4bnBncnFwanhnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyODM3OTc3MiwiZXhwIjoyMDQzOTU1NzcyfQ.019wNYjA51jRneaLQjA1CsDt9bF6deMHKeW0X-6bLOE"
supabase: Client = create_client(url, key)

app = Flask(__name__)

@app.route("/")
def index():
    response = supabase.storage.list_buckets()
    print(response)
    # for x in response:
    #     print("Data: ",x)
    #     for system in x:
    #         print(system['name'])

    return "nothing"

@app.route('/folder')
def bucket_folder():
    response = supabase.storage.from_("avatars").list()
    file_list = []
    for file_name in response:
        file_list.append(file_name['name'])
    return file_list

@app.route('/system')
def systemCheck():
    response = supabase.storage.from_("avatars").list("tomcruise")
    file_name_list = []
    for image in response:
        print(image['name'])
        file_name_list.append(image['name'])

    file_url_list = []
    for x in file_name_list:
        file_url_list.append(supabase.storage.from_("avatars").get_public_url(f"tomcruise/{x}"))

    return render_template("pics.html",data=file_url_list)

# @app.route('/db')
# def db():
#     # Define the table name
#     table_name = "user_enemies"
#
#     # Retrieve all rows
#     response = supabase.schema("dev_db").from_('user_enemies').select('*').eq('enemy_id', '1')
#     print(response)
#     # Print the rows
#     result = []
#     for row in rows.execute():
#         print(row)
#         for x in row:
#             print(x)
#             result.append(x)
#
#     return render_template('db.html',data=result)

@app.route("/locations")
def locations():

    response = supabase.schema("dev_db").from_("locations_db").select("*").execute()
    data = response.data
    result_list = []
    for x in data:
        print(x)
        result_list.append(x)

    return render_template("locations.html",data=result_list)


@app.route('/lavish')
def skills():

    responce = supabase.schema("dev_db").from_("user_lavish").select("*").execute()
    data = responce.data
    result_list = []
    for x in data:
        print(x)
        result_list.append(x)

    return render_template("porn.html",data=result_list)

@app.route("/agents")
def agents():
    response = supabase.schema("dev_db").from_("user_enemies").select("*").execute()
    data = response.data
    result_list = []
    for x in data:
        print(x)
        result_list.append(x)

    return render_template("agents.html",agents=result_list)

@app.route('/attack_agent', methods=['POST'])
def attack_agent():
    data = request.get_json()
    agent_id = data.get('agent_id')

    print("killed:",agent_id)
    # Fetch the current kill count for the agent
    response = supabase.schema("dev_db").table('user_enemies').select('agent_kill').eq('agent_id', agent_id).single().execute()
    if response.data:
        current_kill_count = response.data['agent_kill']
        new_kill_count = current_kill_count + 1

        # Update the agent_kill count in the database
        update_response = supabase.schema("dev_db").table('user_enemies').update({'agent_kill': new_kill_count}).eq('agent_id',
                                                                                             agent_id).execute()

        if update_response:
            return jsonify({'success': True, 'new_kill_count': new_kill_count})

    return jsonify({'success': False}), 400


@app.route('/lifestyle', methods=['GET'])
def lifestyle():
    return render_template('lifestyle.html', muscle_stats=muscle_stats, current_date=date.today())

# This would normally be fetched from your database
muscle_stats = {
    'chest': 50,
    'back': 40,
    'bicep': 30,
    'tricep': 35,
    'abs': 45,
    'leg': 60,
    'forearm': 25
}
@app.route('/update_muscle', methods=['POST'])
def update_muscle():
    muscle = request.json['muscle']
    if muscle in muscle_stats:
        muscle_stats[muscle] += 12
        return jsonify(success=True, new_value=muscle_stats[muscle])
    return jsonify(success=False), 400
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
