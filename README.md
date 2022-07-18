# Required Packages

- Beatifulsoup
    - pip install beautifulsoup4

- simplejson
    - pip install simplejson

# Communication Contract

## How To Request Data
 
 Data will be requested by utilizing a POST request. The POST request will contain a JSON string that contains the key "url" with a URL to a wikipedia page as the value. The POST request will also contain a header that contains the content-type of the request 

 An example of a call to the microservice would be utilizing a service like curl:

    curl --data "{\"url\":\"https://en.wikipedia.org/wiki/Ford_F-Series\"}" --header "Content-Type: application/json" http://localhost:8080

 ## How to Receive Data

 The data will be received through a response from the POST reqeuest that contains a JSON string. It will contain the key "url" with a URL to an external link that was obtained from the Wikipedia page's 'External Link' section as the value. 

 The receiver will be able to access the URL within the JSON string by converting it to an object and then accessing the value by using the key 'url'.


 ## UML Diagram for Microservice Communication 

 ![Alt text](uml_diagram.png?raw=true "Title")