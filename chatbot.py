from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration


class BlenderBot:
    def __init__(self):
        super().__init__()
        self.chat_history = []
        self.tokenizer = BlenderbotTokenizer.from_pretrained('facebook/blenderbot-400M-distill')
        self.model = BlenderbotForConditionalGeneration.from_pretrained('facebook/blenderbot-400M-distill')
        self.turn_sep_token = '    '

    def reply(self, message):
        previous_response = self.chat_history[-1] if self.chat_history else ''
        self.chat_history.append(message)

        # Transformer-based language generation models tend to repeat the same thing. This is a known issue.
        # https://github.com/microsoft/DialoGPT/issues/45
        # https://arxiv.org/pdf/1911.00536.pdf - 5.2 Addressing Cross-turn Repetitions
        # Generate a new response until we get one that doesn't repeat the last response
        # Generate a new response until we get one that doesn't repeat the user's message

        response, score = self.generate_candidate_response()

        # If the context is becoming too much for the bot to handle, reset conversation history
        while score > -0.1:
            self.forget_oldest_response()
            response, score = self.generate_candidate_response()
            print('Model overwhelmed by large context. Cleared 1 conversation turn. '
                  'Current conversation length: ', len(self.chat_history))

        while response.lower() == previous_response.lower() or response.lower() == message.lower():
            response, score = self.generate_candidate_response()

        print('Sequence score:', score)
        self.chat_history.append(response)

        return response

    def generate_candidate_response(self):
        # Model adds its response tokens to chat history ids. Conversation length is limited to 1000 tokens

        # Beam search tries to choose the most probable answer possible
        # But human likes to be surprised by the responses, so some randomness is needed
        # Using beam search with 2 beams and sampling

        outputs = self.model.generate(self.message_to_ids(self.chat_history), max_length=1000,
                                      pad_token_id=self.tokenizer.eos_token_id,
                                      num_beams=2, do_sample=True,
                                      return_dict_in_generate=True, output_scores=True)

        reply_ids = outputs['sequences']
        score = outputs['sequences_scores'][0].item()

        return self.tokenizer.decode(reply_ids[0], skip_special_tokens=True), score

    def message_to_ids(self, chat_history):
        input_string = self.turn_sep_token.join(chat_history)
        return self.tokenizer.encode(input_string, return_tensors='pt')

    def forget_oldest_response(self):
        self.chat_history = self.chat_history[2:]

    def reset(self):  # Reinitialize this class is really slow. So we need a reset method instead
        self.chat_history = []

