**HTTP VERBS**
      
 **Post**
       
1	Creates new resources

2	Creates subordinate resources , subordinate to some parent source

•	Request the origin server to accept the entity enclosed in request as subordinate resource

•	Subordinate resource is identified by the request URI in REQUEST LINE

•	Action performed by post may not result in resource which is identified by URI ;in that case it may show 200(ok) or 204(no content) as response status

•	If resource is created on origin server it SHOULD return 201(created)


**Patch**

•	Update partial resources

•	PATCH /user/jthijssen HTTP/1.1

•	<user>

•	    <firstname>Joshua</firstname>

•	</user>

•	The changes described in the PATCH document must be semantically well defined but can have a different media type than the resource being patched.

•	Either all changes specified by patch keyword are applied or none are applied

•	Patch is not idempotent

•	It may change the resource not mentioned in the URL

•	Errors using PATCH

1.	Malformed patch document

2.	Unsupported patch document

3.	Uprcessable request

4.	Resource not found

5.	Conflicting state

6.	Conflicting modification

7.	Concurrent modification


**Put**

•	The PUT method requests that the enclosed entity be stored under the supplied Request-URI

•	If the Request-URI refers to an already existing resource, the enclosed entity SHOULD be considered as a modified version of the 
one residing on the origin server.

•	Put is used to create and update

•	For a new resource:

•	PUT /questions/<new_question> HTTP/1.1

•	Host: www.example.com/

•	To overwrite an existing resource:

•	PUT /questions/<existing_question> HTTP/1.1

•	Host: www.example.com/

**Delete**

•	Delete a resource

•	On successful deletion return 200(ok) along with response body

•	Delete operations are idempotent

•	if calling DELETE say, decrements a counter (within the resource), the DELETE call is no longer idempotent.

•	Its only function is to do a destructive operation, not repeatable (once the object is deleted, there is nothing else to 
delete).

**Get**

•	Read or retrieve a representation of a resource

•	In a non-error path it returns representation in XML or JSON  format

•	In error format it returns 400(bad request) 404(not found)

•	According to the design of the HTTP specification, GET (along with HEAD) requests are used only to read data and not change it.

•	Therefore, when used this way, they are considered safe. That is, they can be called without risk of data modification or 
corruption—calling it once has the same effect as calling it 10 times, or none at all.

•	It is also idempotent-multiple request generate same effect as single request
       

**How api’s work?????**

•	Application programming interface

•	It allows one application to talk to another through simple commands , the way these commands are sent and their format

•	The interface works by laying  on the top of server side scripts ,classes, and functions that perform more detailed tasks and 
allowing external or internal applications or scripts to ask the API to tell the server to perform a specific task.

•	easy example of this is when a user logs into an application the application needs to retrieve details on the user so in terms of a REST API

•	with api’s the call back and forth are managed by something called web services XML 

•	api is a chunk of software code written in a series of XML messages
     
     

**how api’s are secured????**

•	Basic authentication w/TLS easiest to implement coz there are no addition libraries.everything in this is included in standard framework or library


•	In the above security there are no advanced options except username and password that is BASE64 encoded

•	Basic authentication should never be used without TLS encryption otherwise password is easily decoded

•	OAUTH 1.0a  is the most secure protocol. The protocol uses a cryptographic signature, (usually HMAC-SHA1) value that combines the token secret, nonce, and other request based information.  The great advantage of OAuth 1 is you never directly pass the token secret across the wire, which completely eliminates the possibility of anyone seeing a password in transit.


•	However, this level of security comes with a price: generating and validating signatures can be a complex process.  You have to use specific hashing algorithms with a strict set of steps.  

•	OAuth2 sounds like an evolution of OAuth1, but in reality it is a completely different take on authentication that attempts to reduce complexity. OAuth2’s current specification removes signatures, so you no longer need to use cryptographic algorithms to create, generate, and validate signatures.  All the encryption is now handled by TLS, which is required.  

•	OAuth2 is more challenging than OAuth1a coz of less libraries

•	Custom authentication protocols should be avoided unless you really, really know what you are doing and fully understand all the intricacies of cryptographic digital signatures.  Most organizations don’t have this expertise, so we recommend OAuth1.0a as a solid alternative.
	
 

