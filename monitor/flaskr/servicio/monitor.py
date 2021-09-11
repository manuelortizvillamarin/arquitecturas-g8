import requests
import time
from ..config.logger import get_logger


def run() :
    logger = get_logger(__name__)
    last_check_health = False
    flag_microservice_down = False
    flag_microservice_degraded = False
    while True :
        try :
            r = requests.get("http://localhost:5000/health",timeout=0.05)
            if r.status_code == 200 and not last_check_health :
                logger.info(f"El microservicio Personal Clinica está saludable 200")
                last_check_health= True
                flag_microservice_down = False
                flag_microservice_degraded = False
            elif r.status_code != 200 :
                logger.error(f"Fallo {r.status_code}")
        except requests.exceptions.ConnectionError as e:
            if not flag_microservice_down :
                logger.error(f"El microservicio Personal Clinica está Caido 500")
                flag_microservice_down = True
                last_check_health = False
        except requests.exceptions.Timeout as e:
            if not flag_microservice_degraded :
                logger.error(f"El microservicio Personal Clinica está degradado 408")
                flag_microservice_degraded = True
                last_check_health = False
                time.sleep(2)
                
        time.sleep(0.5)
