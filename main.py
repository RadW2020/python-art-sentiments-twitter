"""Cloud Foundry test"""
from flask import Flask, render_template, request
from form import UserNameForm
from score import ScoreTweets
import cf_deployment_tracker
import os

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)
app.secret_key = 'micumple'
# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

@app.route('/', methods=('GET', 'POST'))
def hello_world():
    form = UserNameForm()
    score = ScoreTweets()
    score.start()
    if request.method == 'POST':
        arrayValores = score.getValues(form.name.data)
        arrayValores1 = score.getValues(form.name2.data)
        arrayValores2 = score.getValues(form.name3.data)
        arrayValores3 = score.getValues(form.name4.data)
        #return str(arrayValores)
        return render_template('index.html', array=arrayValores, array2=arrayValores1, array3=arrayValores2, array4=arrayValores3)
    elif request.method == 'GET':
        return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
