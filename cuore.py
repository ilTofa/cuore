from flask import Flask, redirect, url_for, request, render_template
from os import path
import sys
import uuid
import matplotlib
matplotlib.use("Agg")
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def cuore():
	if request.method == 'POST':
		d = path.join(path.dirname(__file__), "static")
		# Read the whole text.
		text = open(path.join(d, 'pippone.txt'), "r", encoding="utf-8").read()
		personal = (request.form["testo"] + " ") * 5
		text = personal + text + personal
		cuore_mask = np.array(Image.open(path.join(d, "cuore-mask.png")))
		stopwords =	 set(open(path.join(d, "stopwords.txt"), "r", encoding="utf-8").read().split())
		wc = WordCloud(max_words=2000, background_color = None, mode = "RGBA", colormap = request.form["colormap"], collocations=False, mask=cuore_mask, prefer_horizontal=0.7, stopwords=stopwords)
		# generate word cloud
		wc.generate(text)
		# store to file
		cuore_name = str(uuid.uuid4())
		filename = path.join(d, cuore_name) + ".png"
		wc.to_file(filename)
		return redirect("/cuore?cuore="+cuore_name)
# 		return render_template('cuore.html', cuorename=cuore_name)
	else:
		return render_template('home.html', template_dir="static")

@app.route("/cuore", methods=['GET'])
def personal_cuore():
	cuore_name = searchword = request.args.get('cuore', '')
	return render_template('cuore.html', cuorename=cuore_name)

if __name__ == "__main__":
	app.run()
	