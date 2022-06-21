# IOT-Lab-5

This project is about a simple task-oriented chatbot system that uses a client-server architecture.

## Usage

To interact with the chatbot, use this [Thingsboard dashboard](https://demo.thingsboard.io/dashboard/f9abca70-f16c-11ec-a900-4f6af7758cb5?publicId=03ce7cc0-6d09-11ec-8159-03103585248e)

The server must be active before accessing the dashboard.

### Chit-chat

The chatbot can engage in multi-turn chit-chat conversations. This chatbot is based on Meta's BlenderBot, which is an open-domain chatbot, so you can chat about any topic.

### Translation

The chatbot can translate English to Genrman (using Google T5).

To do this, simply ask the chatbot to translate a sentence: `Translate this to german: Welcome to New York`

### Summarization

The chatbot can perform abstractive summarization (using Google T5).

To do this, simply ask the chatbot to summarize a long sentence or passage: `Summarize this: The quick brown fox jumps over the lazy ...`

### Grammartical Acceptability

The chatbot can check if a sentence is grammartically acceptable or not (using Google T5).

To do this, simply ask the chatbot if a sentence is grammartically acceptable: `Is this grammartically acceptable: We never go out of style`
