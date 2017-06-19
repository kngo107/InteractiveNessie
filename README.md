# InteractiveNessie
Interactive Environment which let the user to pull and manipulate bank data  through Nessie API <br>
Web app to visualize spending data and advise the user based on spending habits.

Tomek: 
- [X] Set up github in your machine and clone this repo. Then read through the code, make sure you have an idea. Then, try to run the code and play around with it.
- [X] In this [Link](http://api.reimaginebanking.com/documentation#!/Account/get_accounts_id), implement POST (Create an account) under Account.
- [ ] Understand html, css, javascript
- [ ] Setup transaction tab page: Create Merchants and create purchases

Alan:
- [X] Implement PUT and DELETE under accounts 
- [X] Implement dynamic listing for info.html
- [ ] Setup transaction page: Create Merchants and create Purchases
- [ ] Use d3 to visualize using Bubble chart, a customer's most frequent purchase from a Merchant

IMPORTANT: PLEASE MAKE SURE YOUR CODE WORKS BEFORE PUSHING IT TO GITHUB AND GIT PULL FIRST BEFORE YOU PUSH

<b>This the solution we found to fix our issue with running d3 webpages locally: </b>
1. Load a webserver "python -m SimepleHTTPServer 8888 &" <br> OR install firefox to fix "Cross origin requests..."
2. In chrome: "http://localhost:8888/d3test.html"
3. To kill: ctrl + c <br> Check if process is killed: "ps -fA", kill <enter the pid of process here>

<br />


<b>TODO:</b>
* Retrieve customer information for data analytics
* d3.js --> Visualize customers purchase data (i.e. Most visited store, most purchased category, etc.)
* Research how to make this cross platform compatible
