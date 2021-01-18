from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def main():
  
    return "your bot is running SOS"
    return "your bot is running SOS."
    return "your bot is running SOS.."
    return "your bot is running SOS..."
def run():
  app.run(host="0.0.0.0", port=8080)
def keep_alive():
  server = Thread(target=run)
  server.start()

 