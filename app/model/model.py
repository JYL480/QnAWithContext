import transformers
from transformers import AutoModelForQuestionAnswering,AutoTokenizer
import torch
from torch import nn
from timeit import default_timer as timer

# Create the model!!
def CreateModelandTokenizer():
    checkpoint = "distilbert/distilbert-base-uncased"
    model = AutoModelForQuestionAnswering.from_pretrained(checkpoint)
    # I dont think i have to change any of the layers or the output!!


    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    torch.manual_seed(42)
    model.load_state_dict(torch.load(f = "model\QnAModel.pth",map_location=torch.device('cpu')))

    return model,tokenizer

def Predict(question, context):
    device = "cpu"
    model,tokenizer = CreateModelandTokenizer()
    inputs = tokenizer(question, context, return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)
    model.eval()
    start_time = timer()
    with torch.inference_mode():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    start_logits = outputs.start_logits
    end_logits = outputs.end_logits
    start_index = torch.argmax(start_logits)
    end_index = torch.argmax(end_logits)
    answer = tokenizer.decode(input_ids[0][start_index:end_index+1])
    pred_time = round(timer() - start_time, 5)
    return answer, pred_time