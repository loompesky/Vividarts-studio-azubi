from flask import Flask, render_template, request
import boto3
from werkzeug.utils import secure_filename
s3 = boto3.client('s3',
                    aws_access_key_id='',
                    aws_secret_access_key= '',
                     )
BUCKET_NAME='vivantproject'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['photo']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "
    return render_template("index.html")

if __name__ == "__main__":
    
    app.run(debug=True)