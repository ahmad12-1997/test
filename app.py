from flask import Flask, render_template, request
import config
import aicontent
import ryteapi

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/profile', methods=["GET", "POST"])
def profile():
    return render_template('profile.html', **locals())




@app.route('/content-generator', methods=["GET", "POST"])
def contentgenerator():
      
    if request.method == 'POST':
        
        
        language_input = request.form['language']
        print(language_input)
        toneId_input = request.form['toneId']
        print(toneId_input)
        keypoints_input = request.form['contentgenerator']
        print(keypoints_input)
        
        useCaseIdMagicCommand = request.form['ContentType'] 
        print(useCaseIdMagicCommand)
        useCaseMagicCommand = ryteapi.useCaseDetail(useCaseIdMagicCommand)
        key = useCaseMagicCommand['contextInputs'][0]['keyLabel']
        inputContexts = { key: keypoints_input }
    
        
        openAIAnswer_unformatted =ryteapi.ryte(
        language_input,
        toneId_input,
        useCaseIdMagicCommand,
        inputContexts
      )  
        openAIAnswer = openAIAnswer_unformatted[0]['text']
        print(openAIAnswer)     
        
        prompt = 'AI Suggestions are:'
    return render_template('content-generator.html', **locals())



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)


