from flask import Flask, render_template, request, url_for, redirect
# python has csv module
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    # pass username as name as a second parameter
    return render_template('index.html')


@app.route('/<string:page_name>')
def my_page(page_name):
    return render_template(page_name)




def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])  


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
             data = request.form.to_dict()
        
             write_to_csv(data)
             return redirect('/thankyou.html')
        except:
             return 'Not saved to DB'
    else:
        return 'Something went wrong'
