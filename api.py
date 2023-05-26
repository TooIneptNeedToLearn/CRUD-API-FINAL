import pymysql
from app import app
from config import mysql
from flask import jsonify, request, flash

#index that shows all the column of the table i specified that is routed first
@app.route('/')
def start():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlquery = "SELECT * FROM customers"
        cursor.execute(sqlquery)
        all_row = cursor.fetchall()
        response = jsonify(all_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
#POST
@app.route('/create', methods = ['POST'])
def add_input():
    conn = None
    cursor = None
    try:
        _json = request.json
        customers_id = _json['customers_id']
        f_name = _json['f_name']
        l_name = _json['l_name']
        if customers_id and f_name and l_name and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlquery = "insert into customers(customers_id, f_name, l_name) values (%s ,%s, %s)"
            bind_var = (customers_id, f_name, l_name)
            cursor.execute(sqlquery, bind_var)
            conn.commit()
            response = jsonify("Added to table successfully")
            response.status_code = 200
            return response
        else:
            return errormess()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def errormess(error=None):
    message = {
        'Status': 404,
        'Message': "Record not found" + request.url
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True)