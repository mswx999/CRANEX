print("hi , Welcome To CRANEX")
print("What would you like to recognize today?\n")

choice = input("Enter 'symptoms' for symptoms or 'vitals' for vital signs: ").lower()

if choice == "symptoms":
    print("how you feeling about symptoms ongoing in your body\n")
    print(" Enter Your Symptoms From Key Values Provided (type 'exit' to quit)\n ")
    print(" Headache , Anxiety , Eye Strain , Physical: fever, cough, headache, fatigue, nausea, pain, dizziness, rash, shortness of breath")
    print(" Mental: anxiety, depression, stress, insomnia, confusion, irritability")
    print(" Systemic: chills, sweating, weight loss, swelling, weakness \n")

    while True:
        symptoms = str(input("Enter Your Symptom: "))
        
        # Check if user wants to exit
        if symptoms.lower() == "exit":
            print("Thank you for using CRANEX. Goodbye!")
            break

        match symptoms:
            case "Headache":
                print('''
Stage 1: Mild pain, once a day.
•
Stage 2: Frequent pain, sensitivity to light/noise.
•
Stage 3: Severe pain, nausea, vision disturbances.
•
Causes: Stress, dehydration, eye strain, migraines.
•
Prevention: Stay hydrated, maintain good posture, manage stress.
•
Severe Care: Seek medical help for persistent or worsening pain.''')

            case "Anxiety": 
                print('''
Stage 1: Mild nervousness or worry.
•
Stage 2: Increased heart rate, restlessness.
•
Stage 3: Panic attacks, overwhelming fear.
•
Causes: Stress, trauma, genetics.
•
Prevention: Relaxation techniques, exercise, therapy.
•
Severe Care: Consult a mental health professional.''')

            case "Eye Strain":  
                print('''
Stage 1: Mild discomfort or dryness.
•
Stage 2: Blurred vision, headaches.
•
Stage 3: Severe pain, difficulty focusing.
•
Causes: Prolonged screen time, poor lighting.
•
Prevention: Take breaks, adjust screen brightness.
•
Severe Care: See an eye specialist.''')

            case "Fever":
                print('''
Stage 1: Slight temperature increase.
•
Stage 2: Moderate fever, chills.
•
Stage 3: High fever, sweating, weakness.
•
Causes: Infection, inflammation.
•
Prevention: Rest, hydration, hygiene.
•
Severe Care: Seek medical attention if above 103°F (39.4°C).''')

            case "Cough": 
                print('''
Stage 1: Occasional dry cough.
•
Stage 2: Persistent cough, throat irritation.
•
Stage 3: Severe cough, difficulty breathing.
•
Causes: Cold, allergies, infection.
•
Prevention: Avoid irritants, stay hydrated.
•
Severe Care: See a doctor if persistent or with blood.''')

            case "Fatigue": 
                print('''
Stage 1: Mild tiredness after activity.
•
Stage 2: Constant exhaustion, low energy.
•
Stage 3: Severe fatigue, inability to function.
•
Causes: Lack of sleep, stress, illness.
•
Prevention: Adequate rest, balanced diet.
•
Severe Care: Consult a doctor for underlying causes.''')

            case "Nausea": 
                print('''
Stage 1: Mild stomach discomfort.
•
Stage 2: Frequent queasiness, loss of appetite.
•
Stage 3: Severe nausea, vomiting.
•
Causes: Food poisoning, motion sickness, infection.
•
Prevention: Eat bland foods, stay hydrated.
•
Severe Care: Seek help if vomiting persists.''')

            case "Pain":  
                print('''
Stage 1: Mild, occasional discomfort.
•
Stage 2: Moderate pain, limits activity.
•
Stage 3: Severe, debilitating pain.
•
Causes: Injury, inflammation, illness.
•
Prevention: Rest, proper posture.
•
Severe Care: Medical evaluation for chronic pain.''')

            case "Dizziness":
                print('''
Stage 1: Brief lightheadedness.
•
Stage 2: Frequent unsteadiness.
•
Stage 3: Severe vertigo, inability to stand.
•
Causes: Dehydration, low blood pressure.
•
Prevention: Hydrate, avoid sudden movements.
•
Severe Care: See a doctor if persistent.''')

            case "Rash":
                print('''
Stage 1: Mild redness or itching.
•
Stage 2: Spreading rash, discomfort.
•
Stage 3: Severe rash, blisters, or swelling.
•
Causes: Allergies, infection, irritation.
•
Prevention: Avoid triggers, maintain hygiene.
•
Severe Care: Seek help if spreads or worsens.''')

            case "Shortness of Breath":
                print('''
Stage 1: Mild difficulty after exertion.
•
Stage 2: Frequent breathlessness.
•
Stage 3: Severe respiratory distress.
•
Causes: Asthma, infection, heart issues.
•
Prevention: Avoid triggers, exercise cautiously.
•
Severe Care: Emergency care if acute.''')

            case "Depression":  
                print('''
Stage 1: Occasional sadness.
•
Stage 2: Persistent low mood, withdrawal.
•
Stage 3: Severe hopelessness, suicidal thoughts.
•
Causes: Trauma, chemical imbalance.
•
Prevention: Support, therapy, exercise.
•
Severe Care: Contact a mental health expert.''')

            case "Stress":  
                print('''
Stage 1: Mild tension or worry.
•
Stage 2: Constant pressure, irritability.
•
Stage 3: Severe burnout, physical symptoms.
•
Causes: Work, life events.
•
Prevention: Relaxation, time management.
•
Severe Care: Seek professional help.''')

            case "Insomnia":
                print('''
Stage 1: Occasional trouble falling asleep.
•
Stage 2: Frequent sleeplessness.
•
Stage 3: Severe sleep deprivation.
•
Causes: Stress, caffeine, anxiety.
•
Prevention: Sleep routine, limit stimulants.
•
Severe Care: Consult a sleep specialist.''')

            case "Confusion":  
                print('''
Stage 1: Mild forgetfulness.
•
Stage 2: Difficulty concentrating.
•
Stage 3: Severe disorientation.
•
Causes: Fatigue, illness, neurological issues.
•
Prevention: Rest, mental exercises.
•
Severe Care: Medical evaluation needed.''')

            case _:
                print("Symptom not recognized. Redirecting to chatbot for assistance...")
                import google.generativeai as ai

                API_KEY = ''
                ai.configure(api_key=API_KEY)
                model = ai.GenerativeModel("gemini-1.5-pro")
                while True:
                    message = input('you : ')
                    if message.lower() == 'bye':
                        print('Chatbot: Goodbye!')
                        break
                    response = model.generate_content(message)
                    print('Chatbot:', response.text)

elif choice == "vitals":
    print("\nPlease enter your vital signs:")
    heart_rate = float(input("Enter your heart rate (beats per minute): "))
    bp_systolic = float(input("Enter your blood pressure - systolic (e.g., 120 for 120/80 mmHg): "))
    bp_diastolic = float(input("Enter your blood pressure - diastolic (e.g., 80 for 120/80 mmHg): "))
    pulse = float(input("Enter your pulse rate (beats per minute): "))
    body_temp = float(input("Enter your body temperature (in °F): "))


    if 60 <= heart_rate <= 100:
        print("\nYour heart rate is normal (60-100 bpm).")
    else:
        print("\nYour heart rate is not regular. Consult a doctor.")


    if bp_systolic < 120 and bp_diastolic < 80:
        print("\nYour blood pressure is normal (less than 120/80 mmHg).")
    elif 120 <= bp_systolic <= 129 and bp_diastolic < 80:
        print("\nYour blood pressure is elevated.")
    elif 130 <= bp_systolic <= 139 or 80 <= bp_diastolic <= 89:
        print("\nYour blood pressure indicates Stage 1 hypertension.")
    elif bp_systolic >= 140 or bp_diastolic >= 90:
        print("\nYour blood pressure indicates Stage 2 hypertension. Seek medical advice.")
    else:
        print("\nYour blood pressure reading is unusual. Please recheck or consult a doctor.")


    if 70 <= pulse <= 80:
        print("\nYour pulse is fine (70-80 bpm).")
    else:
        print("\nYour pulse is not regular. Consider medical evaluation.")

 
    if 97 <= body_temp <= 99:
        print("\nYour body temperature is normal (97-99°F).")
    elif 99 < body_temp <= 100.4:
        print("\nYou may have a low-grade fever.")
    elif body_temp > 100.4:
        print("\nYou have a fever. Seek medical attention if it persists.")
    else:
        print("\nYour body temperature is unusually low. Consult a doctor.")

else:
    print("\nInvalid choice. Please restart and enter 'symptoms' or 'vitals'.")