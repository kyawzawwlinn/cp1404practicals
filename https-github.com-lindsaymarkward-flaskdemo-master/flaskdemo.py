from flask import Flask, render_template, request, url_for
import wikipedia

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        try:
            page = wikipedia.page(query, auto_suggest=False)
            title = page.title
            summary = page.summary
            url = page.url
            return render_template('results.html', query=query, title=title, summary=summary, url=url)
        except wikipedia.DisambiguationError as e:
            return render_template('results.html', query=query, error="Disambiguation error", options=e.options)
        except wikipedia.PageError:
            return render_template('results.html', query=query, error="Page not found")
        except Exception as e:
            return render_template('results.html', query=query, error=str(e))
    return render_template('search.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
