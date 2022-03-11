from config.settings import *

@app.route('/blogs')
def blog():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return f"Welcome to the Blog"


app.run(host='localhost', port=5555, debug=True)
