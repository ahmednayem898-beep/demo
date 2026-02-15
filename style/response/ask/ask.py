import random

def generate_response(question: str, answer: str) -> str:
    responses = [

        f"📌 **Your Question:**\n```{question}```\n\n💡 **Answer:**\n{answer}",

        f"🧠 **Question Received:**\n> {question}\n\n✨ **Here’s the Answer:**\n{answer}",

        f"❓ **You Asked:** `{question}`\n\n💬 **AI Says:**\n{answer}",

        f"📥 **Incoming Question:**\n```{question}```\n\n📤 **Outgoing Answer:**\n```{answer}```",

        f"🔎 **Question:**\n{question}\n\n📚 **Answer:**\n{answer}",

        f"🎯 **Your Question:**\n> {question}\n\n🚀 **Response:**\n{answer}",

        f"📝 **Asked:**\n```{question}```\n\n🤖 **Generated Answer:**\n{answer}",

        f"💡 **Curious About:** {question}\n\n📢 **Here’s What I Found:**\n{answer}",

        f"📌 **Question Logged**\n\n`{question}`\n\n💬 **AI Reply**\n{answer}",

        f"🔔 **New Question!**\n{question}\n\n🧠 **Smart Answer:**\n{answer}",

        f"🎤 **You Asked:**\n```{question}```\n\n🎧 **Listening... Done!**\n{answer}",

        f"🧩 **Puzzle:** {question}\n\n🧩 **Solution:**\n{answer}",

        f"🌟 **Question Spotlight:**\n> {question}\n\n🔥 **Answer Reveal:**\n{answer}",

        f"📘 **Query:**\n{question}\n\n📖 **Explanation:**\n{answer}",

        f"⚡ **Quick Question:** `{question}`\n\n⚡ **Quick Answer:**\n{answer}",

        f"🎓 **Learning Mode Activated**\n\n**Question:** {question}\n\n**Answer:**\n{answer}",

        f"📬 **Message Received:**\n```{question}```\n\n📨 **Reply Sent:**\n{answer}",

        f"🛠 **Request:** {question}\n\n🔧 **Result:**\n{answer}",

        f"🎮 **Challenge:**\n{question}\n\n🏆 **AI Response:**\n{answer}",

        f"🌈 **Your Curiosity:**\n> {question}\n\n✨ **My Response:**\n{answer}",
    ]

    return random.choice(responses)
