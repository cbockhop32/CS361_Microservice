# Request to the microservice

curl --data "{\"url\":\"https://en.wikipedia.org/wiki/Ford_F-Series\"}" --header "Content-Type: application/json" http://localhost:8080







# Communication Contact

## How To Request Data
 
 Data will be requested by utilizing curl through a POST request. The POST request will contain a JSON string that contains the key "url" with a URL to a wikipedia page as the value

 ## How to Receive Data

 The data will be received through a response from the POST reqeuest that contains a JSON string. It will contain the key "url" with a URL to an external link that was obtained from the Wikipedia page's 'External Link' section as the value. 


 ## UML Diagram for Microservice Communication 

 ![Alt text](uml_diagram.png?raw=true "Title")