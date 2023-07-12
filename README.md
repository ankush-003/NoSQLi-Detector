# NoSQLi-Detector
DistilBERT-based NoSQL Injection Payload Detection Model 
- This repo contains a fine-tuned DistilBERT model that can be used to detect NoSQL injection payloads. The model was trained on a dataset of known NoSQL injection payloads, and it can be used to classify new payloads as either malicious or benign.

- The model is implemented in Python, and it can be used with any NoSQL database. The repo also includes a Jupyter notebook that demonstrates how to use the model.

## Gradio App on 🤗Spaces
<a href = "https://huggingface.co/spaces/ankush-003/ankush-003-nosqli_identifier" >![image](https://github.com/ankush-003/NoSQLi-Detector/assets/94037471/afde1295-9c5e-4748-8a79-1cec9a3a0ade)</a>

- [🤗Spaces](https://huggingface.co/spaces/ankush-003/ankush-003-nosqli_identifier)
- [Gradio App](https://ankush-003-ankush-003-nosqli-identifier.hf.space/)

## API Documentation
Use the gradio_client Python library or the @gradio/client Javascript package to query the demo via API.
### python
```bash
pip install gradio_client
```
Named Endpoints:
api_name: ```/predict```
```python
from gradio_client import Client

client = Client("https://ankush-003-ankush-003-nosqli-identifier.hf.space/")
result = client.predict(
				"Howdy!",	# str  in 'Enter Username' Textbox component
				"Howdy!",	# str  in 'Enter Password' Textbox component
				"Malitious",	# str (Option from: ['Malitious', 'Benign']) in 'Expected' Dropdown component
				"Howdy!",	# str  in 'Enter Payload' Textbox component
				api_name="/predict"
)
print(result)
```

### Js
```bash
npm i -D @gradio/client
```
Named Endpoints:
api_name: ```/predict```
```js
import { client } from "@gradio/client";

const app = await client("https://ankush-003-ankush-003-nosqli-identifier.hf.space/");
const result = await app.predict("/predict", [		
				"Howdy!", // string  in 'Enter Username' Textbox component		
				"Howdy!", // string  in 'Enter Password' Textbox component		
				"Malitious", // string (Option from: ['Malitious', 'Benign']) in 'Expected' Dropdown component		
				"Howdy!", // string  in 'Enter Payload' Textbox component
	]);

console.log(result.data);
```

## References
- [Text Classification 🤗Docs](https://huggingface.co/docs/transformers/tasks/sequence_classification)
