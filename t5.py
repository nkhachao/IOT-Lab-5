from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")


def reply(task_prefix, sentence):
    inputs = tokenizer([task_prefix + sentence], return_tensors="pt", padding=True)

    output_sequences = model.generate(input_ids=inputs["input_ids"], attention_mask=inputs["attention_mask"],
    do_sample=False)

    return tokenizer.batch_decode(output_sequences, skip_special_tokens=True)[0]


print(reply("translate English to German: ", "I like to work in NYC."))