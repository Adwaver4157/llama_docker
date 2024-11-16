# https://github.com/abetlen/llama-cpp-python

import re
from llama_cpp import Llama

EXAMPLES = [
      {"order": "\"I\'d like to have an apple.\"", "answer": "{\"apple\":1}"},
      {"order": "\"I want two peaches and coke.\"", "answer": "{\"peach\":2, \"coke\":1}"},
      {"order": "\"Orange juice and lemon and bread, please.\"", "answer": "{\"orange juice\":1, \"lemon\":1, \"bread\":1}"}
]
PROMPT = """Please make it so that when a person places an order at a restaurant, the ordered items and their quantities are output in JSON format.
{examples}

Now, please answer the following questions. PLEASE the ordered items and their quantities are output in JSON format. :
Order: {order}
Answer: 
"""



class LLM_order_extractor():
      def __init__(self, model_path, n_gpu_layers=-1, seed=None, n_ctx=1024):
            self.llm = Llama(
                  model_path=model_path,
                  n_gpu_layers=n_gpu_layers,
                  seed=seed,
                  n_ctx=n_ctx,
                  verbose=False
            )
            self.examples_prompt = self.examples_prompt_generator(EXAMPLES)
            print("Model loaded successfully.")

      def examples_prompt_generator(self, examples):
            prompt = ""
            for i, example in enumerate(examples):
                  prompt += f"Example {i}: \nOrder: {example['order']}\nAnswer: {example['answer']}\n\n"
            return prompt
      
      def text_postprocess(self, text):
            text = text.strip()
            text = text.replace("\n", "")
            text = text.replace(" ", "")
            text = text.replace("```", "")
            return text.strip()
      
      def extract_json_string(self, text):
            # print("######\n", text, "\n######")
            text = self.text_postprocess(text)
            try:
                  match = re.search(r'\{(.*?)\}', text)
                  result = match.group(1)  # {} 内の文字列を取得
                  return "{" + result + "}"
            except Exception as e:
                  raise(f"Error: {e}")
      
      def generate_text(self, order, max_tokens=32, stop=["Order:"], echo=False):
            prompt = PROMPT.format(order=order, examples=self.examples_prompt)
            output = self.llm(
                  prompt,
                  max_tokens=max_tokens,
                  stop=stop,
                  echo=echo,
            )
            answer = output["choices"][0]["text"]
            json_string = self.extract_json_string(answer)
            return json_string
      
      def generate_json(self, order, max_tokens=32, stop=["Order:"], echo=False):
            text_output = self.generate_text(order, max_tokens, stop, echo)
            try:
                  json_data = eval(text_output)
            except:
                  json_data = None

            return json_data
    

if __name__ == "__main__":
      llm_path = "./models/Llama-3.2-3B-Instruct.gguf"
      lg = LLM_order_extractor(llm_path)


      orders = ["\"I want three peaches and coke.\"", "\"Apple juice and lemon and milk, please.\"", "\"I'd like to have two plums.\""]
      for i in range(3):
            response = lg.generate_text(orders[i])
            print(f"Text Response: {response}")
      print("\n")
      for i in range(3):
            response = lg.generate_json(orders[i])
            print(f"Json Response: {response}")