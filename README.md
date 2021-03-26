# project-11
project-11 created by GitHub Classroom

Team members:

Jing Wen

Diego Kervabon

Ramon Torres

Lihong Chen

## Description of our Product Architecture:
#### Most important qualities for our software
Nonfunctional Product Characteristics such as performance are very important for commercial success. A product with performance issues could hamper users and drastically restrict the likelihood that they will play and recommend the product to potential users.

Product Lifetime is very important because we expect this game to be around on the web for many years in the future and for new features to be implemented over its lifetime. UNO has been around for almost 50 years and continues to be popular today, and, we believe, into the future.

Lastly, the Number of Users is going to start out low but could change dramatically and we need a product that can support that. Specifically, we need technology that could be flexible in the event that the product goes viral, e.g. Slashdot effect i.e., “Reddit Hug of Death” , and the product has to handle a massive number of users. 

Security and Software Reuse and Software Compatibility are of lesser importance because:
1) The data stored is just game data, no data on users is stored.
2) Building the game does not require the reuse of open source software or other products. Although the product is being built heavily with the use of open source technologies, none of these would fit the definition of being “reused”.
3) The game is being built for mainstream web browsers and does not require users to access the product and its data via a different system.

#### Technologies we will use in our product
1) Database
Should you use a relational SQL database or an unstructured NOSQL database?
A relational SQL database is sufficient for the data types that we are using for this product. Using a NOSQL database would just complicate things.

2) Platform
Should you deliver your product on a mobile app and/or a web platform?
We have known that this product is to be delivered on web platform initially to appeal to the millions of people who would normally be playing UNO on mobile device but are using the web platforms connected to their laptops and desktops instead (because of COVID).

3) Server
Should you use dedicated in-house servers or design your system to run on a public cloud? If a public cloud, should you use Amazon, Google, Microsoft, or some other option?
A public cloud would be the superior option. Purchasing in-house servers that the product could very well outgrow very quickly would be costly and insufficient. A public cloud option would cost very little upfront and could easily meet the demands of the product regardless of how far and 

#### Our Layered Architecture Diagram: 



## Our Product-Vision:
FOR people ages 5 and up with access to the internet and an internet browser WHO are looking to socialize in a way
that is socially-distanced during this pandemic, UNOpen is a card game THAT is fun and easy to learn and UNLIKE
current mobile versions of this game OUR PRODUCT is free and open source and will run in your browser.

## Gamespace Prototype(extension) #2
Here is a basic layout of our gamespace:

<img src="http://g.recordit.co/2kt2hrPttp.gif">

## Proof-of-concept prototype #1
User's can enter their desired username and can then either begin their own room, or enter a roomID to join an existing room.

<img src="gifs/prototype.gif">

## How to use:
Open a terminal window in the project folder

type "python3 -m http.server --directory templates"

go to 127.0.0.1:8000/homepage.html


## Proof-of-concept prototype #2(Our back up)
Here a quick look at our backup prototype webpage:


<img src="http://g.recordit.co/uqEcS9uNwX.gif">
