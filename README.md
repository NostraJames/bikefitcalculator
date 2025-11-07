# Bike Fit Calculator

**Project Type:** Medium doesn’t mean Medium anymore.  
**Role:** Engineer, Product Manager  
**Skills:** Python, AWS, JSON, API  

---

## Bike geometry is changing: Mediums don’t fit like they used to.

### Problem Statement
Bike geometry is changing as we get more advanced about building bikes. Like shoes, a size 9 with one company isn’t the same as a size 9 in another. So you have to wear the shoe to know if it fits. Same thing is happening to the mountain bike industry. And if you lived in say, Texas, where mountain biking is not a major recreation, demoing bikes is hard to come by.

**Key Industry Standards:**
- All bike manufacturers list geometry charts on their website for all sizes and all bikes.
- A mountain bike coach developed the *Rider Area Distance (RAD)* measurement on a bike and a person.
- A rider has a RAD measurement.
- A bike has a RAD measurement.
- Those two measurements should equal: **RAD(R) = RAD(B)**

![RAD Diagram](Bike_Fit_RAD.png)

---

### Vision
Build a bike fit calculator with a database. People would be able to type in their RAD number in a user interface and a database would retrieve all the bikes and their sizes and setups (handlebar widths, stem lengths, etc.) that would fit that rider.

This could be used by bike shops and individuals alike to find the right bike for the rider.

---

### Key Challenge
RAD was intellectual property of the mountain bike coach, and I needed to get approval and work with him to achieve this vision.

I was new to Python, but this was a great inspirational project to learn.

---

### Process

**MVP:** Design a Python script that contained all the formulas and had input values for bike geometry to give you a RAD number.  
**Phase 2:** Script was broken down into several functions.  
**Phase 3:** Converted the script into a serverless Lambda function in AWS.  

Additional steps:
- Built a database so users could also contribute to the collection of data.  
- Created a front-end that fed from a GitHub repo and sent API calls to Lambda code.  
- Built an automation script to pull several bike geo-charts and plug them into the front end to contribute to the database build.

---

### Impact
A friend and I used this to purchase our next bikes with size-fit success.

---

### Roadblock
The owner of RAD did not want to partner up as he had a calculator for purchase with his coaching service.  
I do not believe we shared the same end vision.

---

