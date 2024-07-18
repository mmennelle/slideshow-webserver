from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed
import os

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
app.config['UPLOADED_PHOTOS_ALLOW'] = IMAGES  # Explicitly allow images
configure_uploads(app, photos)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'photo' in request.files:
        file = request.files['photo']
        try:
            filename = photos.save(file)
        except UploadNotAllowed:
            return "File type not allowed", 400
        return redirect(url_for('index'))
    uploaded_photos = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    return render_template('index.html', photos=uploaded_photos)

if __name__ == '__main__':
    app.run(debug=True)
