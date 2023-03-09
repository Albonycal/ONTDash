from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'button1' in request.form:
            subprocess.run(['bash', 'scripts/WLAN_ON.sh'])
            return '''
        <script>alert("WiFi Turned On Successfully")</script>
        <script>window.location.replace("/");</script>
        '''
        elif 'button2' in request.form:
            subprocess.run(['bash', 'scripts/WLAN_OFF.sh'])
            return '''
               <script>alert("WiFi Turned Off Successfully")</script>
        <script>window.location.replace("/");</script>
       '''
        elif 'button3' in request.form:
            subprocess.run(['bash', 'scripts/NEW_IP.sh'])
            return '''
                <script>alert("Done")</script>
        <script>window.location.replace("/");</script> 
        '''
    else:
        return '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>WiFi Control Panel</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
    body {
        margin: 0;
        padding: 0;
        font-family: 'Arial', sans-serif;
        background-color: #1e1e1e;
        color: #d9d9d9;
    }

    #container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #292929;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    }

    #header {
        text-align: center;
        margin-bottom: 20px;
    }

    h1 {
        font-size: 32px;
        margin-top: 0;
        margin-bottom: 0;
        color: #d9d9d9;
        text-shadow: 2px 2px #333;
    }
	p {
			font-size: 15px;
			line-height: 1.5;
			margin: 25px 0;
			text-align: center;
		}

    .form-container {
        text-align: center;
    }

    button {
        background-color: #4d4d4d;
        color: #d9d9d9;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        font-size: 16px;
        margin: 10px;
        cursor: pointer;
        box-shadow: 2px 2px #333;
    }

    button:hover {
        background-color: #666666;
        color: #d9d9d9;
        box-shadow: 2px 2px #333;
    }

    button:active {
        background-color: #666666;
        color: #d9d9d9;
        box-shadow: none;
        transform: translateY(2px);
    }

            </style>
        </head>
        <body>
            <div id="container">
                <div id="header">
                    <h1>ONT Control Panel</h1>
                </div>
                <p> Made with <3 By Albony </p>
                <div class="form-container">
                    <form method="post">
                        <button type="submit" name="button1">Turn WiFi ON</button>
                        <button type="submit" name="button2">Turn WiFi OFF</button>
                        <button type="submit" name="button3">Get a New IP</button>
                    </form>
                </div>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

