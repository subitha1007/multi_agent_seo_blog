import os
import google.generativeai as genai

# Configure API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found!")

genai.configure(api_key=API_KEY)

# Use a supported model
MODEL_NAME = "models/gemini-1.5-pro-latest"

def generate_content(prompt):
    """Generate AI-generated content based on the provided prompt."""
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text.strip() if response else "❌ No content generated."
    except Exception as e:
        return f"❌ Error during content generation: {e}"

def save_to_file(content, filename="generated_blog_post.txt"):
    """Save generated content to a file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"✅ Blog post saved successfully as {filename}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

if __name__ == "__main__":
    print("🚀 Starting content generation...")

    # Define prompt
    prompt = "Write a detailed SEO-friendly blog post about AI in digital marketing."

    # Generate content
    blog_content = generate_content(prompt)

    # Display and save content
    if "❌" not in blog_content:
        print("✅ Generated Content:\n", blog_content)
        save_to_file(blog_content)
    else:
        print(blog_content)
