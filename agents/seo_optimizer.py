import re

def optimize_for_seo(content, keywords):
    """Improve SEO by optimizing keyword placement and content structure."""
    # Ensure main keyword appears in the title and first paragraph
    title = content.split("\n")[0]
    if not any(keyword.lower() in title.lower() for keyword in keywords):
        content = f"{keywords[0]} - {title}\n\n" + content
    
    # Ensure headings follow a proper structure (H1, H2, H3)
    content = re.sub(r'\n\s*\*\*(.*?)\*\*\n', r'\n## \1\n', content)

    # Insert meta description (first 160 characters)
    meta_description = content[:160]
    
    optimized_content = f"<!-- Meta Description: {meta_description} -->\n\n{content}"
    
    return optimized_content

# Example usage
if __name__ == "__main__":
    sample_content = "Your generated blog content here..."
    sample_keywords = ["AI in HR", "HR automation", "AI recruitment"]
    optimized_blog = optimize_for_seo(sample_content, sample_keywords)

    with open("C:/Users/Ajith/multi_agent_seo_blog/outputs/optimized_blog.txt", "w", encoding="utf-8") as file:
        file.write(optimized_blog)
    print("✅ SEO Optimization Complete! Blog saved.")
