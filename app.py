import tiktoken

t = tiktoken.encoding_for_model(model_name="gpt-4")

original_text = "who is founder of pakistan"
tt = t.encode(original_text)
tt

dd = [14965, 374, 19533, 315, 87098, 198]
res = t.decode(dd)
res