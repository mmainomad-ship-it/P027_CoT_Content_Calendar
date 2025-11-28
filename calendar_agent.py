import ollama

# Step 1: Imports & Configuration
# Define the local model name (ensure you have run 'ollama pull llama3.2')
MODEL_NAME = "llama3.1"

# Step 2: Data/Input Preparation
# Get the broad topic from the user to initiate the chain
print("--- 📅 AI Content Calendar Generator ---")
topic = input("Enter a business/topic for the content calendar: ")


# Step 3: Function Definition
# A reusable helper function to send prompts to the local LLM and return text
def get_ai_response(prompt):
    print("   -> AI is thinking...")
    response = ollama.chat(
        model=MODEL_NAME, messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


# Step 4: Core Logic - Link 1 (Chain-of-Thought Brainstorming)
# We ask the AI to identify audiences first (CoT) before listing ideas
print("\n1. Brainstorming ideas (CoT)...")
prompt_1 = f"Topic: {topic}. Let's think step-by-step. First, identify target audiences. Then, list 10 unique content ideas."
raw_ideas = get_ai_response(prompt_1)

# Step 4: Core Logic - Link 2 (Filtration/Selection)
# Pass the raw ideas back to the AI to select the top 5 based on quality
print("2. Selecting the top 5 ideas...")
prompt_2 = f"Review these ideas:\n{raw_ideas}\nSelect the 5 best ideas for high engagement. Return ONLY the list of 5 ideas."
top_5_ideas = get_ai_response(prompt_2)

# Step 4: Core Logic - Link 3 (Scheduling)
# Chain the selected ideas into a final 5-day schedule formatted as a Markdown table
print("3. Creating the content calendar...")
prompt_3 = f"Take these 5 ideas: {top_5_ideas}. Create a 5-day (Mon-Fri) content calendar in a Markdown Table."
final_schedule = get_ai_response(prompt_3)

# Step 5: Main Execution Block
# Output the final Markdown table to the console
print("\n--- 📝 Final Content Calendar ---")
print(final_schedule)

# Save the result to a Markdown file
filename = "my_content_calendar.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(final_schedule)

print(f"\n--- 💾 Successfully saved to {filename} ---")
print("--- End of Chain ---")
