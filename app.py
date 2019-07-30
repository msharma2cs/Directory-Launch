from flask import Flask, render_template, request
from directories import getPrimaryPath, getAllSubDirectories, getAllSubDirectoriesForPath, launchDirectoryScript
app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template( './home.html', primaryPath = getPrimaryPath() )

@app.route('/directories', methods=['POST'])
def allSubDirectories():
    result = request.form['primaryPath'];
    path = result.encode('ascii', 'ignore')
    if path:
        return render_template( './directories.html', primaryPath = path, subdirs = getAllSubDirectoriesForPath(path) )
    return render_template( './directories.html', primaryPath = getPrimaryPath(), subdirs = getAllSubDirectories() )

@app.route('/launch', methods=['POST'])
def launchDirectory():
    dir = request.form['dir'].encode('ascii', 'ignore')
    path = request.form['primaryPath'].encode('ascii', 'ignore')
    launchDirectoryScript(path, dir);
    return render_template( './directories.html', primaryPath = path, subdirs = getAllSubDirectoriesForPath(path) )
