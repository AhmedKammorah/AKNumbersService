# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-05-11 12:38:07
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-05-11 15:40:40
from pprint import pprint
from MainService.api.ak_base_api import *
from MainService.main.ak_numbers_utils import AKNumbersUtils
from flask import jsonify

number_util = AKNumbersUtils()

@app.route('/api/number/<number_digit>', methods=['GET','POST'])
# @jwt_required()
def send_email(number_digit):
    if number_digit == None:
        return app.make_response(("number not passed correctly", 400))    
    
    number = int(number_digit)
    number_en = number_util.translate_number(number)
    out = {
        "number":number,
        "number_en":number_en
    }

    app.logger.debug("Convert number digit : {} to Number in english text: {}".format(number, number_en))
    return jsonify(out)
        


if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0')