import praw
import random

# 1️⃣ Configurar las credenciales de Reddit
client_id = "etMTPe_VYWlP8yQ1rx5YTg"
client_secret = "WkX36sF-D9NHOIg6yiaW00Guw-xGWw"
user_agent = "linkedin_automation/0.1 by Admirable_Put_8480"

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# 2️⃣ Lista de subreddits de interés
subreddits = ["MachineLearning", "DataScience", "ArtificialIntelligence"]

# 3️⃣ Elegir un subreddit y post aleatorio
subreddit = random.choice(subreddits)
posts = list(reddit.subreddit(subreddit).top(time_filter="week", limit=5))
selected_post = random.choice(posts)

# 4️⃣ Mostrar el resultado en consola (luego lo enviaremos por correo)
print(f"Subreddit: {subreddit}")
print(f"Título: {selected_post.title}")
print(f"Link: {selected_post.url}")
print(f"Upvotes: {selected_post.score} | Comentarios: {selected_post.num_comments}")

