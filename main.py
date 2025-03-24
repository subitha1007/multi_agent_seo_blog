import os
from agents.content_generator import generate_content  # Import the correct function

# Configure API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found!")

# Define a prompt for content generation
prompt = "Generate an SEO-optimized blog post about AI in digital marketing."

# Call the function to generate content
try:
    print("🚀 Starting content generation...")
    generated_content = generate_content(prompt)  # Ensure correct function name
    print("✅ Generated Content:\n", generated_content)
    
    # Save content to a file
    output_file = "generated_blog_post.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(generated_content)

    print(f"✅ Blog post saved successfully as {output_file}")

except Exception as e:
    print("❌ Error during content generation:", e)
