import sys
from visa.exception import CustomException
from visa.logger import logging
from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing CustomException.")
    
    except Exception as e:
        visa = CustomException(e, sys)
        logging.info(visa.error_message)
        logging.info("We are testing logging.")

if __name__ == "__main__":
    app.run(debug= True)