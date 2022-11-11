"""
Prompts the user for the name of a file and then outputs the media type if the name ends in
(*case-insensitively) any of these suffixes: .gif .jpg .jpeg .png .pdf .txt .zip
04.22, 11.22, 0.0
"""
file = str(input('file: '))
file = file.lower().strip()

if file.endswith('.gif'):
    print('image/gif')
elif file.endswith('.png'):
    print('image/png')
elif file.endswith('.pdf'):
    print('application/pdf')
elif file.endswith('.txt'):
    print('text/plain')
elif file.endswith('.zip'):
    print('application/zip')
elif file.endswith('jpg') or file.endswith('jpeg'):
    print('image/jpeg')
else:
    print('application/octet-stream')
