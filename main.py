from flask import Flask, render_template, jsonify
from database import loads_websites_from_db 

main = Flask(__name__)

@main.route("/")
#connection the data and showing it on home page
def hello_world():
    web = loads_websites_from_db()
    return render_template ('home.html', websites = web)


@main.route("/api/websites")
#creating an api and showing it in json type. It will be important to load data.
def list_websites():
  websites = loads_websites_from_db()
  return jsonify(websites) 



# @main.route("/website/<id>")
# def show_web(id):
#   website = load_web_from_db(id)

#   if not website:
#     return "Not found", 404

#   return render_template('jobpage.html', job=job)
# def show_website(id):
  


if __name__ == "__main__":
  main.run(host='0.0.0.0', debug=True)
  