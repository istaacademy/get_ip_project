import requests
from flask import jsonify
from config import Config
import logging

logger = logging.getLogger(__name__)

class IPLocationservice:
    def __init__(self):
        self.ip_api = Config.IP_API_URL
        self.ipify =  Config.IPIFY_URL    

    def get_public_ip(self):
        logger.info(f'Start to request IP {self.ipify}')
        try:
            return requests.get(self.ipify).json().get('ip')
        
        except requests.RequestException as e:
            logger.error(f'Network Error for public ip : {e}')
            return jsonify({"status":"fail","data":"faild to get public ip"})
    
    def get_location_data(self,ip_address=None):
        logger.info(f'Start to request IP {self.ip_api}/{ip_address}')
        try:
            response = requests.get(f'{self.ip_api}/{ip_address}')
        except requests.RequestException as e:
            logger.error(f'Network Error for ip  location: {e}')
        if response.json().get('status') == 'fail':
            return jsonify({"status":"faild","data":"counld not fetch location"})
        return jsonify(response.json())
