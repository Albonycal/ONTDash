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
    #temperature {
    font-size: 18px;
    margin-top: 20px;
    text-align: center;
    color: #d9d9d9;
    text-shadow: 2px 2px #333;
}



            </style>
        </head>
        <body>
            <div id="container">
                <div id="header">
                    <h1>ONT Control Panel</h1>
                </div>
                    <div id="temperature">ONT Temperature: <span id="temp-value">--</span></div>
                    <div id="temperature">
                    <div id="temperature"><span id="power-value">--</span></div>
                    <div id="temperature">Uptime: <span id="uptime-value">--</span></div>
                    </div>
                    <br> </br>

                <div class="form-container">
                    <form method="post">
                        <button type="submit" name="button1">Turn WiFi ON</button>
                        <button type="submit" name="button2">Turn WiFi OFF</button>
                        <button type="submit" name="button3">Get a New IP</button>
                    </form>
                </div>
                <p> Made With <3 By Albony </p>
              </div>              
    <script>
        function updateTemperature() {
            fetch('/temperature')  // call the '/temperature' endpoint to get the temperature
                .then(response => response.text())  // parse the response as text
                .then(temperature => {
                    // update the temperature value in the UI
                    document.querySelector('#temp-value').textContent = temperature;
                })
                .catch(error => {
                    console.error('Failed to update temperature:', error);
                });
        }

        // update the temperature every 5 seconds
        setInterval(updateTemperature, 5000);
       function updatePower() {
           fetch('/optical') 
               .then(response => response.text()) 
               .then(optical => {
                   document.querySelector('#power-value').textContent = optical;
                })
                .catch(error => {
                     console.error('Failed to update power:', error);
                });
            }
             setInterval(updatePower, 5000);
       function updateUptime() {
           fetch('/uptime') 
               .then(response => response.text()) 
               .then(uptime => {
                   document.querySelector('#uptime-value').textContent = uptime;
                })
                .catch(error => {
                     console.error('Failed to update uptime:', error);
                });
            }
             setInterval(updateUptime, 5000);
           </script>
        </body>
        </html>
    '''
@app.route('/temperature')
def temperature():
    output = subprocess.check_output(['bash', 'scripts/get_temperature.sh'])
    lines = output.decode('utf-8').split('\n')
    temperature = lines[-2]  # get the second to last line (which should be the temperature value)
    return f"{temperature} \u2103"
@app.route('/uptime')
def uptime():
    output = subprocess.check_output(['bash' , 'scripts/get_uptime.sh'])
    lines = output.decode('utf-8').split('\n')
    uptime = lines[-2] 
    return f"{uptime}"
@app.route('/optical')
def optical():
            # get the output of optical.sh
        output = subprocess.check_output(['bash', 'scripts/optical.sh']).decode('utf-8')
        # extract the relevant information from the output
        ic_temperature = output.split('\n')[1].split(':')[1]
        bosa_temperature = output.split('\n')[2].split(':')[1]
        vcc = output.split('\n')[3].split(':')[1]
        txbias = output.split('\n')[4].split(':')[1]
        txmod = output.split('\n')[5].split(':')[1]
        txpower = output.split('\n')[6].split(':')[1].split()[1].replace('dBm', '')
        rxpower = output.split('\n')[7].split(':')[1].split()[1].replace('dBm', '')

        return f'TxPower: {txpower} dBm\nRxPower: {rxpower} dBm'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

