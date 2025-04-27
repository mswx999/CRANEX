   
CRANEX – Symptoms & Vitals Recognition And DHR  
  
  
  
  
Software Requirements Specification  
  
    
Table of Contents  
   
 1. INTRODUCTION	1  
1.1 PURPOSE	1 
1.2 SCOPE	1 
1.3 DEFINITIONS, ACRONYMS, AND ABBREVIATIONS	1 
1.4 REFERENCES ........................................................................................................................................................1 	
1.5 OVERVIEW  	1  
 2. GENERAL DESCRIPTION	2  
2.1 PRODUCT PERSPECTIVE	2 
2.2 PRODUCT FUNCTIONS	2 
2.3 USER CHARACTERISTICS .....................................................................................................................................2 	
2.4 GENERAL CONSTRAINTS	2 

2.5 ASSUMPTIONS AND DEPENDENCIES .....................................................................................................................2  
  
 3. SPECIFIC REQUIREMENTS ...............................................................................................................................2 3.1 
EXTERNAL INTERFACE REQUIREMENTS ...............................................................................................................3  
3.1.1 User Interfaces ............................................................................................................................................3  
3.1.2 Hardware Interfaces ...................................................................................................................................3  
3.1.3 Software Interfaces......................................................................................................................................3  
3.1.4 Communications Interfaces.........................................................................................................................3 
3.2 FUNCTIONAL REQUIREMENTS ..............................................................................................................................3  
3.2.1 <Functional Requirement or Feature #1> .................................................................................................3 
3.2.2 <Functional Requirement or Feature #2> .................................................................................................3  
3.3 NON-FUNCTIONAL REQUIREMENTS .....................................................................................................................4  
3.3.1 Performance ................................................................................................................................................4  
3.3.2 Reliability ....................................................................................................................................................4  
3.3.3 Availability ..................................................................................................................................................4  
3.3.4 Security .......................................................................................................................................................4  
3.3.5 Maintainability ............................................................................................................................................4  
Page    
3.3.6 Portability ...................................................................................................................................................4  
3.4 DESIGN CONSTRAINTS .........................................................................................................................................4  
  
iii     
 1. Introduction  
The Software Requirements Specification (SRS) for the CRANEX healthcare system provides a detailed overview of the software product that is to be developed. This document contains all the necessary requirements to guide in the design and implementation of the CRANEX system. It outlines the purpose, scope, functions, and system constraints, ensuring all stakeholders have a unified understanding of the software’s expectations and behavior.   
  
1.1 Purpose  
The purpose of this SRS is to define the functional and non-functional requirements for the CRANEX system. This document will serve as a blueprint for the implementation of a proactive healthcare monitoring.  

 1.2 Scope  
The software product is named CRANEX - FOR LIFE. CRANEX is designed to track vital signs such as heart rate, blood pressure, oxygen levels, and neural signals, along with recognizing physical symptoms like eye strain, fatigue, and stress. It provides real-time monitoring, predictive analysis, and stores encrypted digital health records. The system will:  
  
•	Monitor and analyze user-provided health data and sensor inputs.  
  
•	Alert users and healthcare providers about potential health risks.  
  
•	Offer health insights and educational recommendations.  
  
CRANEX benefits include:  
  
•	Early detection of health anomalies using pattern recognition.  
  
•	Education and awareness on health management.  
  
1.3 Definitions, Acronyms, and Abbreviations  
•	CRANEX: Cranial Nerve X-inspired Proactive healthcare system  
  
•	DHR: Digital Health Record  
  
•	IoT: Internet of Things  
  
•	API: Application Programming Interface  
  
•	S&V: Symptoms And Vitals Recognition      
  
1.4 References  
•	MySQL database ref. (https://www.w3resource.com/projects/sql/sql-projects-on-hospital-patient-database.php)

•	AI Integration (https://hyqoo.com/artificial-intelligence/how-to-integrate-ai-into-your-project)

•	API Based Chat Support (https://aistudio.google.com/app/apikey)

•	Relevant Articles (https://mcpress.mayoclinic.org/healthy-aging/ai-in-healthcare-the-future-of-patient-care-and-health-management/

•	https://indiaai.gov.in/article/ai-in-indian-healthcare-emerging-trends-and-opportunities-in-2025
  
•	Facts & Stat : NIH And WHO , MOH gov. India .  
  
 1.5 Overview  
This document is structured to provide a complete and clear understanding of the CRANEX system requirements. It is organized as follows:
•	General Description:
Describes the overall product perspective, key functions, user characteristics, system constraints, and dependencies. This section provides the context in which the CRANEX system operates.
•	Specific Requirements:
Details the external interface requirements (user, hardware, software, and communication interfaces), along with the functional and non-functional requirements necessary for system performance, security, reliability, and usability.
•	References and Appendices:
Includes external resources, technical references, and supporting documents that influenced or guided the development of the CRANEX system.

2. General Description  
  
2.1 Product Perspective  
CRANEX is a standalone healthcare application but can also be integrated with wearable health devices and hospital systems for advanced functionalities. It acts as a personal digital health assistant that keeps track of the user’s health status through real-time data input and analysis. CRANEX mainly uses mobile technology, cloud storage, and artificial intelligence to give accurate health suggestions and store medical records securely. This product is designed to work as an all-in-one platform combining multiple existing healthcare functions like symptom checking, vitals tracking, and secure digital health record storage. While other apps may offer similar features separately, CRANEX brings them all together in a single, smart, and user-friendly system.  
  
CRANEX also differs from traditional hospital systems in that it allows users to selfmonitor and manage their health from home, without needing to visit a doctor for basic concerns. It uses AI-based prediction to detect early signs of health problems and offers useful suggestions before the issue becomes serious. The platform supports secure data sharing with healthcare professionals in case of emergencies or regular check-ups. In short, CRANEX is not just a mobile app—it is part of a broader digital healthcare environment. It connects the user, the data, and the doctor, making healthcare smarter, faster, and more accessible.  
  
2.2 Product Functions  
The CRANEX system will perform the following tasks:  
  
•	Collect health data such as heart rate, blood pressure, and oxygen levels.  
  
•	Analyze the data using AI to detect warning signs.  
  
•	Store health records safely on the cloud.  
  
•	Notify users and doctors about risks.  
  
•	Provide helpful suggestions and health awareness content.  
  
2.3 User Characteristics  
The CRANEX system is designed for all types of users. It includes regular people who want to track their health, patients who need continuous monitoring, and doctors who need quick access to records. The app will have a simple, clean, and user-friendly design to help everyone use it easily.  
  
2.4 General Constraints  
Some limitations of the system include:  
  
•	The software must follow healthcare rules and data privacy laws  
.  
•	It can only work with supported devices and cloud services.  
  
•	It must ensure data is safe and not shared without permission  
  
2.5 Assumptions and Dependencies  
•	It is assumed that users have smart wearable devices that can send data.  
  
•	It depends on cloud platforms like AWS or Google Cloud.  
  
•	The software needs accurate input from users or devices to work correctly.  
  
•	Feedback from healthcare experts is needed to improve AI accuracy.  
  
 3. Specific Requirements  
3.1 External Interface Requirements  
  
3.1.1 User Interfaces  
•  Mobile and web applications with input forms, visual charts, alerts, and educational material.  
  
3.1.2 Hardware Interfaces  
•	Bluetooth-enabled smart wearables (smartwatches, fitness trackers)  
•	Data Base Storage   
  
3.1.3 Software Interfaces  
The system will use tools like Gemini API model for backend data processing , and MySQL for database storage ,  and Frontend UI with Java .  
  
3.1.4 Communications Interfaces : Chatbot APIs for data exchange, secure HTTPS protocols .  
   
3.2 Functional Requirements  
  
3.2.1 Real-Time Vitals Monitoring  
  
3.2.1.1 Introduction: Monitors heart rate, BP, oxygen, neural activity   
  
3.2.1.2 Inputs: Sensor data from connected devices   
  
3.2.1.3 Processing: AI analysis and data interpretation   
  
3.2.1.4 Outputs: Alerts, predictions   
  
3.2.1.5 Error Handling: Invalid data alerts, retry mechanisms  
  
3.2.2 Digital Health Record Management   
  
3.2.2.1 Introduction: Maintain secure health records  
  
3.2.2.2 Inputs: User submissions, device inputs   
  
3.2.2.3 Processing: Data storage, indexing   
  
3.2.2.4 Outputs: Retrieved data reports, medical summaries  
  
 3.2.2.5 Error Handling: Authentication errors, failed sync  
  
3.3 Non-Functional Requirements  
  
3.3.1 Performance  
CRANEX should respond quickly to user actions. Most of the tasks like symptom checking, viewing vitals, or updating health records should be completed within minute. Even when many users are using the app at the same time, the system should not slow down. The backend should be able to handle large amounts of health data without delay.  
  
3.3.2 Reliability  
The system should be reliable, meaning it should work correctly most of the time. Users should be able to trust the app to show accurate health results. CRANEX should not crash or give wrong outputs. If a device is disconnected, the system should handle it smoothly and reconnect without losing data.  
  
3.3.3 Availability  
CRANEX is available to use 24/7. Users must be able to check their symptoms or vitals anytime, especially in emergency situations. if updates or maintenance are needed, the system should give a warning and come back online quickly. Planned downtime should not exceed 30 minutes per month.  
  
3.3.4 Security  
Security is very important in CRANEX because it deals with personal health information. The system use protected my SQL database for digital health records. Only admin and authorized users (patients or doctors) be able to access data.  
  
3.3.5 Maintainability  
The CRANEX system is easy to maintain. If there are bugs or problems, developers are able to fix them without changing the entire system. The code is clean, well commented, and modular so that future improvements or changes can be done easily.  
  
3.3.6 Portability  
CRANEX  work on different types of devices like Android phones, tablets, and desktops. It will also support future platforms if needed. The software will be able to run on multiple operating systems with minimal changes, and user data should remain safe and accessible even when switching devices.  
  
