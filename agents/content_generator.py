import os
import google.generativeai as genai

# Configure API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found!")

genai.configure(api_key=API_KEY)

# Use a supported model
MODEL_NAME = "models/gemini-1.5-pro-latest"  # You can also try "models/gemini-2.0-pro-exp"

def generate_content(prompt):
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("🚀 Content generation script started...")
    prompt = "Write a detailed SEO-friendly blog post about AI in digital marketing."
    try:
        content = generate_content(prompt)
        print("✅ Generated Content:\n", content)
    except Exception as e:
        print("❌ Error during content generation:", e)

# Define a prompt for content generation
prompt = "Generate an SEO-optimized blog post about AI in digital marketing."

# Call the function with the prompt
generated_content = generate_content(prompt)  # Pass the required argument

# Define the output file
output_file = "generated_blog_post.txt"

# Write the content to a file
with open(output_file, "w", encoding="utf-8") as file:
    file.write(generated_content)

print(f"✅ Blog post saved successfully as {output_file}")
