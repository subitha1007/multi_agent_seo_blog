class ContentPlanningAgent:
    def __init__(self):
        pass

    def generate_outline(self, topic):
        outline = {
            "title": f"{topic} - A Complete Guide",
            "sections": [
                "Introduction",
                f"What is {topic}?",
                f"Why is {topic} Important?",
                f"Key Trends in {topic}",
                f"Best Practices for {topic}",
                "Challenges and Solutions",
                "Conclusion"
            ]
        }
        return outline

if __name__ == "__main__":
    planner = ContentPlanningAgent()
    topic = "AI in the Workplace"  # Example topic
    outline = planner.generate_outline(topic)
    
    print("\nBlog Outline:")
    print(f"Title: {outline['title']}")
    for idx, section in enumerate(outline["sections"], 1):
        print(f"{idx}. {section}")
