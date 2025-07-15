import os
import praw
import openai
from dotenv import load_dotenv

load_dotenv()

# Connect to Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)

# Set your OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1: Get posts and comments
def get_user_data(username):
    redditor = reddit.redditor(username)

    posts = []
    comments = []

    for submission in redditor.submissions.new(limit=5):
        post = f"Title: {submission.title}\nText: {submission.selftext}\nURL: {submission.url}\n"
        posts.append(post)

    for comment in redditor.comments.new(limit=5):
        comments.append(f"Comment: {comment.body}")

    return posts, comments

# Step 2: Generate persona using OpenAI
def generate_user_persona(posts, comments):
    content = "\n\n".join(posts + comments)
    prompt = f"""
You are an AI researcher.

Create a detailed USER PERSONA from this Reddit user's posts and comments.
Include:
- Personality traits
- Writing style
- Interests & hobbies
- Opinions or values
- Nicknames (if any)
- Patterns of behavior
Cite exact lines or URLs from Reddit content to support each point.

Reddit Content:
{content}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content

# Step 3: Save to .txt
def save_persona(username, persona):
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"\n✅ Persona saved to {filename}")

# Step 4: Run everything
if __name__ == "__main__":
    username =  "Hungry-Move-6603"
    posts, comments = get_user_data(username)
    persona = generate_user_persona(posts, comments)
    save_persona(username, persona)


def generate_user_persona(posts, comments):
    content = "\n\n".join(posts + comments)
    prompt = f"""..."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
