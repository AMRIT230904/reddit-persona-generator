import os
import sys
import praw
import openai
from dotenv import load_dotenv

# ✅ Load API keys from .env
load_dotenv()

# ✅ Debug print to confirm .env loaded
print("🔐 Reddit Client ID:", os.getenv("REDDIT_CLIENT_ID"))
print("🔐 Reddit Client Secret:", os.getenv("REDDIT_CLIENT_SECRET"))
print("📣 User Agent:", os.getenv("USER_AGENT"))

# ✅ Connect to Reddit
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)

# ✅ Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# ✅ Step 1: Get posts and comments from Reddit
def get_user_data(username):
    print(f"\n🔄 Fetching data for: {username}")
    redditor = reddit.redditor(username)

    posts = []
    comments = []

    for submission in redditor.submissions.new(limit=5):
        post = f"Title: {submission.title}\nText: {submission.selftext}\nURL: {submission.url}\n"
        posts.append(post)

    for comment in redditor.comments.new(limit=5):
        comments.append(f"Comment: {comment.body}")

    print(f"📄 Found {len(posts)} posts and {len(comments)} comments")

    return posts, comments


# ✅ Step 2: Generate user persona using GPT
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
        model="gpt-3.5-turbo",  # 🔁 using free model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content


# ✅ Step 3: Save persona to file
def save_persona(username, persona):
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"\n✅ Persona saved to {filename}")


# ✅ Step 4: Main
if __name__ == "__main__":
    # 🟩 Take Reddit URL as input
    if len(sys.argv) < 2:
        print("❌ Please provide a Reddit profile URL")
        sys.exit(1)

    reddit_url = sys.argv[1]
    username = reddit_url.split("/")[-2]

    posts, comments = get_user_data(username)

    if not posts and not comments:
        print("⚠️ No data found for this user. Try another one.")
        sys.exit(0)

    persona = generate_user_persona(posts, comments)

    print("\n🔍 Generated Persona Preview:\n")
    print(persona)

    save_persona(username, persona)
