from flask import Flask, render_template, request
import config
import aicontent
import ryteapi
from flask_ckeditor import CKEditor
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField


def page_not_found(e):
  return render_template('404.html'), 404


main = Flask(__name__)
ckeditor = CKEditor(main)
main.config.from_object(config.config['development'])
main.register_error_handler(404, page_not_found)


@main.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@main.route('/profile', methods=["GET", "POST"])
def profile():
    return render_template('profile.html', **locals())




@main.route('/content-generator', methods=["GET", "POST"])
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
        openAIAnswer1 = openAIAnswer_unformatted[0]['text']
        if len(openAIAnswer1) > 2 :
            openAIAnswer = openAIAnswer1
            print(openAIAnswer)  
        else:
            openAIAnswer ='AI Couldnot Generate an Answer for You , Please Try Again'
            print(openAIAnswer)   
        
        prompt = 'AI Suggestions are:'
    return render_template('content-generator.html', **locals())



if __name__ == '__main__':
    main.run(host='0.0.0.0', port='5000', debug=True)


