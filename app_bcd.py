import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'ID': "",   
                            'Diagnosis': "",   
                            'Mean Radius': Col3,   
                            'Mean Texture': Col4,   
                            'Mean Perimeter': Col5,   
                            'Mean Area': Col6,   
                            'Mean Smoothness': Col7,   
                            'Mean Compactness': Col8,   
                            'Mean Concavity': Col9,   
                            'Mean Concave Points': Col10,   
                            'Mean Symetry': Col11,   
                            'Mean Fractal Dimension': Col12,   
                            'Radius Standard Error': Col13,   
                            'Texture Standard Error': Col14,   
                            'Perimeter Standard Error': Col15,   
                            'Area Standard Error': Col16,   
                            'Smoothness Standard Error': Col17,   
                            'Compactness Standard Error': Col18,   
                            'Concavity Standard Error': Col19,   
                            'Concave Points Standard Error': Col20,   
                            'Symetry Standard Error': Col21,   
                            'Fractal Dimension Standard Error': Col22,   
                            'Worst Radius': Col23,   
                            'Worst Texture': Col24,   
                            'Worst Perimeter': Col25,   
                            'Worst Area': Col26,   
                            'Worst Smoothness': Col27,   
                            'Worst Compactness': Col28,   
                            'Worst Concavity': Col29,   
                            'Worst Concave Points': Col30,   
                            'Worst Symetry': Col31,   
                            'Worst Fractal Dimension': Col32,   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/b3cefb7f8c3049be84caa7f8984756e0/services/e24d918a989f4a6b9b4f0f160aab2f9a/execute?api-version=2.0&format=swagger'
api_key = '26irrxk5CilbPInZaR8lTvq6CNmImmwL2hOpXKTeu3OYZpvAxQZB4JNbdckONbcecyr4ArO3CsB5pLgHCNnQhg=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))