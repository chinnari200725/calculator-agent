# Observe -> Act Agent Loop
for iteration in range(1, 4):
    print(f"\n--- Iteration {iteration} ---")
    # 1.OBSERVE
    observation = input("observe: Enter currentn situation: ")
    # 2. DECIDE
    if "rain" in observation.lower():
        decision = "carry an umbrella"
    elif "hot" in observation.lower():
        decision = "Drink Water"
    else:
        decision = "continue normally"
        print("Decide:", decision)
        # 3. ACT
        print("Act:", decision)
        print("\aAgent loop completed after 3 iterations.")
        
        
