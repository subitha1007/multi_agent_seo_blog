import requests
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Online LanguageTool API URL
API_URL = "https://api.languagetool.org/v2/check"

def review_with_api(text):
    """Uses the LanguageTool online API to check and correct grammar/spelling."""
    data = {"text": text, "language": "en-US"}
    
    try:
        response = requests.post(API_URL, data=data)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
        result = response.json()
        
        if "matches" not in result or not result["matches"]:
            return text  # Return original text if no issues found

        # Apply corrections
        corrected_text = text
        for match in reversed(result["matches"]):  # Reverse to prevent index shifting
            start = match["offset"]
            end = start + match["length"]
            replacements = match["replacements"]
            
            if replacements:
                corrected_text = corrected_text[:start] + replacements[0]["value"] + corrected_text[end:]

        return corrected_text

    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error connecting to LanguageTool API: {e}")
        return text  # Return original text if an error occurs

if __name__ == "__main__":
    input_file = "C:/Users/Ajith/multi_agent_seo_blog/outputs/optimized_blog.txt"
    output_file = "C:/Users/Ajith/multi_agent_seo_blog/outputs/final_blog.txt"

    if not os.path.exists(input_file):
        logging.error(f"❌ Input file not found: {input_file}")
        exit(1)

    try:
        # Read content from file
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Process content using API
        reviewed_blog = review_with_api(content)

        # Save corrected content
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(reviewed_blog)

        logging.info("✅ Review Complete! Final blog saved.")
    except Exception as e:
        logging.error(f"❌ Unexpected error: {e}")
