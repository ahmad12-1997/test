from tkinter import E
import requests
import json

API_KEY = 'OSCULO40VBSA0BUGDS66P' # Get your API key here: https://app.rytr.me/account/api-access
API_URL = 'https://api.rytr.me/v1'

# Language list
def languageList():
  try:
    headers = {'Authentication': 'Bearer ' + API_KEY}
    r = requests.get(API_URL + '/languages', headers=headers)
    data = r.json()
    return data['data']
  except Exception as e:
    print('An exception occurred')
    print(e)
  return None

# Tone list
def toneList():
  try:
    headers = {'Authentication': 'Bearer ' + API_KEY}
    r = requests.get(API_URL + '/tones', headers=headers)
    data = r.json()
    
    return data['data']
  except:
    print('An exception occurred')
  return None

# Use case list
def useCaseList():
  try:
    headers = {'Authentication': 'Bearer ' + API_KEY}
    r = requests.get(API_URL + '/use-cases', headers=headers)
    data = r.json()
    return data['data']
  except:
    print('An exception occurred')
  return None

# Use case detail
def useCaseDetail(useCaseId):
  try:
    headers = {'Authentication': 'Bearer ' + API_KEY}
    r = requests.get(API_URL + '/use-cases/' + useCaseId, headers=headers)
    data = r.json()
    return data['data']
  except:
    print('An exception occurred')
  return None

# Generate content
def ryte(languageId, toneId, useCaseId, inputContexts):
  try:
    data = {
      'languageId': languageId,
      'toneId': toneId,
      'useCaseId': useCaseId,
      'inputContexts': inputContexts,
      'variations': 1,
      'userId': 'USER1',
      'format': 'html'
    }
    headers = {'Authentication': 'Bearer ' + API_KEY}
    r = requests.post(API_URL + '/ryte', json=data, headers=headers)
    data = r.json()
    return data['data']
  except:
    print('An exception occurred')
  return None

def main():
  # Get languages
  if True:
    languages = languageList()
    print(languages)
    dict_languages = {}
    for item in languages:
       
       language_id =item['_id']
       language_name =item['name']
       dict_languages[language_name] = language_id
      
    print(dict_languages)

  # Get tones
  if True:
    tones = toneList()
    print(tones)
    dict_tones = {}
    for item in tones:
       
       toneid =item['_id']
       tone_name =item['name']
       dict_tones[tone_name] = toneid
      
    print(dict_tones)
     

  # Get use cases
  if True:
    useCases = useCaseList()
    print(useCases)
    dict_useCases = {}
    for item in useCases:
       
       useCase_id =item['_id']
       useCase_name =item['name']
       dict_useCases[useCase_name] = useCase_id
      
    print(dict_useCases)

  # Get use case detail
  if True:
    # Example use case: Magic command
    useCaseIdMagicCommand = '60ed7113732a5b000cf99e8e'
    useCase = useCaseDetail(useCaseIdMagicCommand)
    print(useCase)
    

  # Generate content
  if False:
    # Step 1 - Identify language ID (use language list API endpoint)
    languageIdEnglish = '607adac76f8fe5000c1e636d' # English

    # Step 2 - Identify tone ID (use tone list API endpoint)
    toneIdConvincing = '60572a639bdd4272b8fe358b' # Convincing

    if True:
      # Step 3 - Identify use case ID (use use-case list API endpoint)
      useCaseIdMagicCommand = '60ed7113732a5b000cf99e8e' # Magic command

      # Step 4 - Identify use case details (use use-case detail API endpoint)
      useCaseMagicCommand = useCaseDetail(useCaseIdMagicCommand)

      key = useCaseMagicCommand['contextInputs'][0]['keyLabel']
      inputContexts = { key: 'Write an email for taking a sick leave' }

      # Step 5 - Generate content (use ryte API endpoint)
      outputs = ryte(
        languageIdEnglish,
        toneIdConvincing,
        useCaseIdMagicCommand,
        inputContexts
      )
      print(outputs)

    if False:
      # Step 3 - Identify use case ID (use use-case list API endpoint)
      useCaseIdJobDescription = '60586b31cdebbb000c21058d' # Job description

      # Step 4 - Identify use case details (use use-case detail API endpoint)
      useCaseJobDescription = useCaseDetail(useCaseIdJobDescription)

      key = useCaseJobDescription['contextInputs'][0]['keyLabel']
      inputContexts = { key: 'Product Manager' }

      # Step 5 - Generate content (use ryte API endpoint)
      outputs = ryte(
        languageIdEnglish,
        toneIdConvincing,
        useCaseIdJobDescription,
        inputContexts
      )
      print(outputs)

    if False:
      # Step 3 - Identify use case ID (use use-case list API endpoint)
      useCaseIdBlogSection = '60584cf2c2cdaa000c2a7954' # Blog section writing

      # Step 4 - Identify use case details (use use-case detail API endpoint)
      useCaseBlogSection = useCaseDetail(useCaseIdBlogSection)

      keyTopic = useCaseBlogSection['contextInputs'][0]['keyLabel']
      keyKeywords = useCaseBlogSection['contextInputs'][1]['keyLabel']
      inputContexts = { keyTopic: 'Role of AI Writers in the Future of Copywriting', keyKeywords: 'ai writer, blog generator, best writing software' }

      # Step 5 - Generate content (use ryte API endpoint)
      outputs = ryte(
        languageIdEnglish,
        toneIdConvincing,
        useCaseIdBlogSection,
        inputContexts
      )
      print(outputs)
   
   

