
from flask import Flask ,jsonify
import requests
from utils.ip_services import IPLocationservice
from config import Config
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

app = Flask(__name__)
ip_services = IPLocationservice()


@app.route('/get-location',methods = ['GET'])
def get_location():
    try:
        return ip_services.get_location_data(ip_services.get_public_ip())

    except requests.RequestException as e:
        logger.error(f'Network Error : {e}')
        return jsonify({"status":"fail","data":"faild to fetch data"})
    except Exception as error:
        logger.error(f'Other Error : {error}')
        return jsonify({"status":"fail","data":"faild to fetch data"})

if __name__ == '__main__':
    app.run(debug=Config.DEBUG,port=Config.PORT)