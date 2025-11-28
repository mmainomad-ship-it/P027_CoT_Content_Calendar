# Step 1: Imports & Configuration
import ollama
import sys  # Import sys to handle clean exits

MODEL_NAME = "llama3.1"


# Step 2: Function Definition (Robust Version)
def get_ai_response(prompt):
    """Sends a prompt to Ollama with error handling."""
    print("   -> AI is thinking...")
    try:
        response = ollama.chat(
            model=MODEL_NAME, messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"\n❌ Error calling Ollama: {e}")
        print("Tip: Make sure Ollama is running using 'ollama serve'")
        sys.exit(1)  # Stop the script immediately if AI fails


# Step 3: Input Validation Loop
print("--- 📅 AI Content Calendar Generator (Pro) ---")
while True:
    topic = input("Enter a business/topic for the content calendar: ").strip()
    if topic:
        break  # User entered text, exit loop
    print("⚠️ Input cannot be empty. Please try again.")

# Step 4: Core Logic - The Chain

# Link 1: Brainstorming
print("\n1. Brainstorming ideas (CoT)...")
prompt_1 = f"Topic: {topic}. Let's think step-by-step. First, identify target audiences. Then, list 10 unique content ideas."
raw_ideas = get_ai_response(prompt_1)

# Link 2: Filtration
print("2. Selecting the top 5 ideas...")
prompt_2 = f"Review these ideas:\n{raw_ideas}\nSelect the 5 best ideas for high engagement. Return ONLY the list of 5 ideas."
top_5_ideas = get_ai_response(prompt_2)

# Link 3: Scheduling
print("3. Creating the content calendar...")
prompt_3 = f"Take these 5 ideas: {top_5_ideas}. Create a 5-day (Mon-Fri) content calendar in a Markdown Table."
final_schedule = get_ai_response(prompt_3)

# Step 5: Output & Save
print("\n--- 📝 Final Content Calendar ---")
print(final_schedule)

# Save the result
filename = "my_content_calendar.md"
try:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_schedule)
    print(f"\n--- 💾 Successfully saved to {filename} ---")
except IOError as e:
    print(f"\n❌ Error saving file: {e}")

print("--- End of Chain ---")
