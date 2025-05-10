import praw
import random

# 1️⃣ Configura las credenciales de Reddit (iremos a configurarlas en el próximo paso)
reddit = praw.Reddit(
    client_id="TU_CLIENT_ID",
    client_secret="TU_CLIENT_SECRET",
    user_agent="linkedin_automation/0.1 by TU_USUARIO"
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
