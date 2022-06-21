# IOT-Lab-5

This project is about a simple task-oriented chatbot system that uses a client-server architecture.

## Usage

To interact with the chatbot, use this [Thingsboard dashboard](https://demo.thingsboard.io/dashboard/f9abca70-f16c-11ec-a900-4f6af7758cb5?publicId=03ce7cc0-6d09-11ec-8159-03103585248e)

The server must be active before accessing the dashboard.

### Open-domain conversation

The chatbot can engage in multi-turn chit-chat conversations. This chatbot is based on Meta's BlenderBot, which is an open-domain chatbot, so you can chat about any topic.

<img width="1187" alt="Screen Shot 2022-06-22 at 06 19 39" src="https://user-images.githubusercontent.com/62071233/174912392-bde6b301-a840-4b06-ac77-7378b76c7b08.png">


### Translation

The chatbot can translate English to Genrman (using Google T5).

To do this, simply ask the chatbot to translate a sentence: `Translate this to german: Welcome to New York`

<img width="1188" alt="Screen Shot 2022-06-22 at 06 23 43" src="https://user-images.githubusercontent.com/62071233/174912602-df2de67d-c423-4dd5-9cb9-a72bd805ec0f.png">


### Summarization

The chatbot can perform abstractive summarization (using Google T5).

To do this, simply ask the chatbot to summarize a long sentence or passage: `Summarize this: The quick brown fox jumps over the lazy ...`

<img width="1177" alt="Screen Shot 2022-06-22 at 06 26 04" src="https://user-images.githubusercontent.com/62071233/174912864-e87b1e56-7071-4b86-86a4-0aa19c369a84.png">


### Grammartical Acceptability

The chatbot can check if a sentence is grammartically acceptable or not (using Google T5).

To do this, simply ask the chatbot if a sentence is grammartically acceptable: `Is this grammartically acceptable: We never go out of style`

<img width="1174" alt="Screen Shot 2022-06-22 at 06 28 49" src="https://user-images.githubusercontent.com/62071233/174913054-b834483f-22bc-4396-af3c-adb564c93041.png">

