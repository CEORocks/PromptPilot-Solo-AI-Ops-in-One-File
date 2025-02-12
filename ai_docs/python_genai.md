
# Google Gen AI SDK

[Permalink: Google Gen AI SDK](https://github.com/googleapis/python-genai#google-gen-ai-sdk)

[![PyPI version](https://camo.githubusercontent.com/af4dae966695dbde629839adb60210ed763579c6f73cf6159ed8aa64e68fd35b/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f676f6f676c652d67656e61692e737667)](https://pypi.org/project/google-genai/)

* * *

**Documentation:** [https://googleapis.github.io/python-genai/](https://googleapis.github.io/python-genai/)

* * *

Google Gen AI Python SDK provides an interface for developers to integrate Google's generative models into their Python applications. It supports the [Gemini Developer API](https://ai.google.dev/gemini-api/docs) and [Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview) APIs.

## Installation

[Permalink: Installation](https://github.com/googleapis/python-genai#installation)

```
pip install google-genai
```

## Imports

[Permalink: Imports](https://github.com/googleapis/python-genai#imports)

```
from google import genai
from google.genai import types
```

## Create a client

[Permalink: Create a client](https://github.com/googleapis/python-genai#create-a-client)

Please run one of the following code blocks to create a client for
different services ( [Gemini Developer API](https://ai.google.dev/gemini-api/docs) or [Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)).

```
# Only run this block for Gemini Developer API
client = genai.Client(api_key='GEMINI_API_KEY')
```

```
# Only run this block for Vertex AI API
client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)
```

**(Optional) Using environment variables:**

You can create a client by configuring the necessary environment variables.
Configuration setup instructions depends on whether you're using the Gemini API
on Vertex AI or the ML Dev Gemini API.

**ML Dev Gemini API:** Set `GOOGLE_API_KEY` as shown below:

```
export GOOGLE_API_KEY='your-api-key'
```

**Vertex AI API:** Set `GOOGLE_GENAI_USE_VERTEXAI`, `GOOGLE_CLOUD_PROJECT`
and `GOOGLE_CLOUD_LOCATION`, as shown below:

```
export GOOGLE_GENAI_USE_VERTEXAI=false
export GOOGLE_CLOUD_PROJECT='your-project-id'
export GOOGLE_CLOUD_LOCATION='us-central1'
```

```
client = genai.Client()
```

### API Selection

[Permalink: API Selection](https://github.com/googleapis/python-genai#api-selection)

To set the API version use `http_options`. For example, to set the API version
to `v1` for Vertex AI:

```
client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1',
    http_options={'api_version': 'v1'}
)
```

To set the API version to `v1alpha` for the Gemini API:

```
client = genai.Client(api_key='GEMINI_API_KEY',
                      http_options={'api_version': 'v1alpha'})
```

## Types

[Permalink: Types](https://github.com/googleapis/python-genai#types)

Parameter types can be specified as either dictionaries( `TypedDict`) or
[Pydantic Models](https://pydantic.readthedocs.io/en/stable/model.html).
Pydantic model types are available in the `types` module.

## Models

[Permalink: Models](https://github.com/googleapis/python-genai#models)

The `client.models` modules exposes model inferencing and model getters.

### Generate Content

[Permalink: Generate Content](https://github.com/googleapis/python-genai#generate-content)

#### with text content

[Permalink: with text content](https://github.com/googleapis/python-genai#with-text-content)

```
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='why is the sky blue?'
)
print(response.text)
```

#### with uploaded file (Gemini API only)

[Permalink: with uploaded file (Gemini API only)](https://github.com/googleapis/python-genai#with-uploaded-file-gemini-api-only)

download the file in console.

```
!wget -q https://storage.googleapis.com/generativeai-downloads/data/a11.txt
```

python code.

```
file = client.files.upload(file='a11.txt')
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=['Could you summarize this file?', file]
)
print(response.text)
```

#### How to structure `contents`

[Permalink: How to structure contents](https://github.com/googleapis/python-genai#how-to-structure-contents)

There are several ways to structure the `contents` in your request.

Provide a single string as shown in the text example above:

```
contents='Can you recommend some things to do in Boston and New York in the winter?'
```

Provide a single `Content` instance with multiple `Part` instances:

```
contents=types.Content(parts=[\
    types.Part.from_text(text='Can you recommend some things to do in Boston in the winter?'),\
    types.Part.from_text(text='Can you recommend some things to do in New York in the winter?')\
], role='user')
```

When sending more than one input type, provide a list with multiple `Content`
instances:

```
contents=[\
    'What is this a picture of?',\
    types.Part.from_uri(\
        file_uri='gs://generativeai-downloads/images/scones.jpg',\
        mime_type='image/jpeg',\
    ),\
],
```

### System Instructions and Other Configs

[Permalink: System Instructions and Other Configs](https://github.com/googleapis/python-genai#system-instructions-and-other-configs)

```
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents='high',
    config=types.GenerateContentConfig(
        system_instruction='I say high, you say low',
        temperature=0.3,
    ),
)
print(response.text)
```

### Typed Config

[Permalink: Typed Config](https://github.com/googleapis/python-genai#typed-config)

All API methods support Pydantic types for parameters as well as
dictionaries. You can get the type from `google.genai.types`.

```
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=types.Part.from_text(text='Why is the sky blue?'),
    config=types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
        candidate_count=1,
        seed=5,
        max_output_tokens=100,
        stop_sequences=['STOP!'],
        presence_penalty=0.0,
        frequency_penalty=0.0,
    ),
)

print(response.text)
```

### List Base Models

[Permalink: List Base Models](https://github.com/googleapis/python-genai#list-base-models)

To retrieve tuned models, see [list tuned models](https://github.com/googleapis/python-genai#list-tuned-models).

```
for model in client.models.list():
    print(model)
```

```
pager = client.models.list(config={'page_size': 10})
print(pager.page_size)
print(pager[0])
pager.next_page()
print(pager[0])
```

#### Async

[Permalink: Async](https://github.com/googleapis/python-genai#async)

```
async for job in await client.aio.models.list():
    print(job)
```

```
async_pager = await client.aio.models.list(config={'page_size': 10})
print(async_pager.page_size)
print(async_pager[0])
await async_pager.next_page()
print(async_pager[0])
```

### Safety Settings

[Permalink: Safety Settings](https://github.com/googleapis/python-genai#safety-settings)

```
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents='Say something bad.',
    config=types.GenerateContentConfig(
        safety_settings=[\
            types.SafetySetting(\
                category='HARM_CATEGORY_HATE_SPEECH',\
                threshold='BLOCK_ONLY_HIGH',\
            )\
        ]
    ),
)
print(response.text)
```

### Function Calling

[Permalink: Function Calling](https://github.com/googleapis/python-genai#function-calling)

#### Automatic Python function Support

[Permalink: Automatic Python function Support](https://github.com/googleapis/python-genai#automatic-python-function-support)

You can pass a Python function directly and it will be automatically
called and responded.

```
def get_current_weather(location: str) -> str:
    """Returns the current weather.

    Args:
      location: The city and state, e.g. San Francisco, CA
    """
    return 'sunny'

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents='What is the weather like in Boston?',
    config=types.GenerateContentConfig(tools=[get_current_weather]),
)

print(response.text)
```

#### Manually declare and invoke a function for function calling

[Permalink: Manually declare and invoke a function for function calling](https://github.com/googleapis/python-genai#manually-declare-and-invoke-a-function-for-function-calling)

If you don't want to use the automatic function support, you can manually
declare the function and invoke it.

The following example shows how to declare a function and pass it as a tool.
Then you will receive a function call part in the response.

```
function = types.FunctionDeclaration(
    name='get_current_weather',
    description='Get the current weather in a given location',
    parameters=types.Schema(
        type='OBJECT',
        properties={
            'location': types.Schema(
                type='STRING',
                description='The city and state, e.g. San Francisco, CA',
            ),
        },
        required=['location'],
    ),
)

tool = types.Tool(function_declarations=[function])

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents='What is the weather like in Boston?',
    config=types.GenerateContentConfig(tools=[tool]),
)

print(response.function_calls[0])
```

After you receive the function call part from the model, you can invoke the function
and get the function response. And then you can pass the function response to
the model.
The following example shows how to do it for a simple function invocation.

```
user_prompt_content = types.Content(
    role='user',
    parts=[types.Part.from_text(text='What is the weather like in Boston?')],
)
function_call_part = response.function_calls[0]
function_call_content = response.candidates[0].content

try:
    function_result = get_current_weather(
        **function_call_part.function_call.args
    )
    function_response = {'result': function_result}
except (
    Exception
) as e:  # instead of raising the exception, you can let the model handle it
    function_response = {'error': str(e)}

function_response_part = types.Part.from_function_response(
    name=function_call_part.name,
    response=function_response,
)
function_response_content = types.Content(
    role='tool', parts=[function_response_part]
)

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=[\
        user_prompt_content,\
        function_call_content,\
        function_response_content,\
    ],
    config=types.GenerateContentConfig(
        tools=[tool],
    ),
)

print(response.text)
```

#### Function calling with `ANY` tools config mode

[Permalink: Function calling with ANY tools config mode](https://github.com/googleapis/python-genai#function-calling-with-any-tools-config-mode)

If you configure function calling mode to be `ANY`, then the model will always
return function call parts. If you also pass a python function as a tool, by
default the SDK will perform automatic function calling until the remote calls exceed the
maximum remote call for automatic function calling (default to 10 times).

If you'd like to disable automatic function calling in `ANY` mode:

```
def get_current_weather(location: str) -> str:
    """Returns the current weather.

    Args:
      location: The city and state, e.g. San Francisco, CA
    """
    return "sunny"

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents="What is the weather like in Boston?",
    config=types.GenerateContentConfig(
        tools=[get_current_weather],
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        ),
        tool_config=types.ToolConfig(
            function_calling_config=types.FunctionCallingConfig(mode='ANY')
        ),
    ),
)
```

If you'd like to set `x` number of automatic function call turns, you can
configure the maximum remote calls to be `x + 1`.
Assuming you prefer `1` turn for automatic function calling.

```
def get_current_weather(location: str) -> str:
    """Returns the current weather.

    Args:
      location: The city and state, e.g. San Francisco, CA
    """
    return "sunny"

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents="What is the weather like in Boston?",
    config=types.GenerateContentConfig(
        tools=[get_current_weather],
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            maximum_remote_calls=2
        ),
        tool_config=types.ToolConfig(
            function_calling_config=types.FunctionCallingConfig(mode='ANY')
        ),
    ),
)
```

### JSON Response Schema

[Permalink: JSON Response Schema](https://github.com/googleapis/python-genai#json-response-schema)

#### Pydantic Model Schema support

[Permalink: Pydantic Model Schema support](https://github.com/googleapis/python-genai#pydantic-model-schema-support)

Schemas can be provided as Pydantic Models.

```
from pydantic import BaseModel

class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    gdp: int
    official_language: str
    total_area_sq_mi: int

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents='Give me information for the United States.',
    config=types.GenerateContentConfig(
        response_mime_type='application/json',
        response_schema=CountryInfo,
    ),
)
print(response.text)
```

```
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents='Give me information for the United States.',
    config=types.GenerateContentConfig(
        response_mime_type='application/json',
        response_schema={
            'required': [\
                'name',\
                'population',\
                'capital',\
                'continent',\
                'gdp',\
                'official_language',\
                'total_area_sq_mi',\
            ],
            'properties': {
                'name': {'type': 'STRING'},
                'population': {'type': 'INTEGER'},
                'capital': {'type': 'STRING'},
                'continent': {'type': 'STRING'},
                'gdp': {'type': 'INTEGER'},
                'official_language': {'type': 'STRING'},
                'total_area_sq_mi': {'type': 'INTEGER'},
            },
            'type': 'OBJECT',
        },
    ),
)
print(response.text)
```

### Enum Response Schema

[Permalink: Enum Response Schema](https://github.com/googleapis/python-genai#enum-response-schema)

#### Text Response

[Permalink: Text Response](https://github.com/googleapis/python-genai#text-response)

You can set response\_mime\_type to 'text/x.enum' to return one of those enum
values as the response.

```
class InstrumentEnum(Enum):
  PERCUSSION = 'Percussion'
  STRING = 'String'
  WOODWIND = 'Woodwind'
  BRASS = 'Brass'
  KEYBOARD = 'Keyboard'

response = client.models.generate_content(
      model='gemini-2.0-flash-001',
      contents='What instrument plays multiple notes at once?',
      config={
          'response_mime_type': 'text/x.enum',
          'response_schema': InstrumentEnum,
      },
  )
print(response.text)
```

#### JSON Response

[Permalink: JSON Response](https://github.com/googleapis/python-genai#json-response)

You can also set response\_mime\_type to 'application/json', the response will be identical but in quotes.

```
from enum import Enum

class InstrumentEnum(Enum):
  PERCUSSION = 'Percussion'
  STRING = 'String'
  WOODWIND = 'Woodwind'
  BRASS = 'Brass'
  KEYBOARD = 'Keyboard'

response = client.models.generate_content(
      model='gemini-2.0-flash-001',
      contents='What instrument plays multiple notes at once?',
      config={
          'response_mime_type': 'application/json',
          'response_schema': InstrumentEnum,
      },
  )
print(response.text)
```

### Streaming

[Permalink: Streaming](https://github.com/googleapis/python-genai#streaming)

#### Streaming for text content

[Permalink: Streaming for text content](https://github.com/googleapis/python-genai#streaming-for-text-content)

```
for chunk in client.models.generate_content_stream(
    model='gemini-2.0-flash-001', contents='Tell me a story in 300 words.'
):
    print(chunk.text, end='')
```

#### Streaming for image content

[Permalink: Streaming for image content](https://github.com/googleapis/python-genai#streaming-for-image-content)

If your image is stored in [Google Cloud Storage](https://cloud.google.com/storage),
you can use the `from_uri` class method to create a `Part` object.

```
for chunk in client.models.generate_content_stream(
    model='gemini-2.0-flash-001',
    contents=[\
        'What is this image about?',\
        types.Part.from_uri(\
            file_uri='gs://generativeai-downloads/images/scones.jpg',\
            mime_type='image/jpeg',\
        ),\
    ],
):
    print(chunk.text, end='')
```

If your image is stored in your local file system, you can read it in as bytes
data and use the `from_bytes` class method to create a `Part` object.

```
YOUR_IMAGE_PATH = 'your_image_path'
YOUR_IMAGE_MIME_TYPE = 'your_image_mime_type'
with open(YOUR_IMAGE_PATH, 'rb') as f:
    image_bytes = f.read()

for chunk in client.models.generate_content_stream(
    model='gemini-2.0-flash-001',
    contents=[\
        'What is this image about?',\
        types.Part.from_bytes(data=image_bytes, mime_type=YOUR_IMAGE_MIME_TYPE),\
    ],
):
    print(chunk.text, end='')
```

### Async

[Permalink: Async](https://github.com/googleapis/python-genai#async-1)

`client.aio` exposes all the analogous [`async` methods](https://docs.python.org/3/library/asyncio.html)
that are available on `client`

For example, `client.aio.models.generate_content` is the `async` version
of `client.models.generate_content`

```
response = await client.aio.models.generate_content(
    model='gemini-2.0-flash-001', contents='Tell me a story in 300 words.'
)

print(response.text)
```

### Streaming

[Permalink: Streaming](https://github.com/googleapis/python-genai#streaming-1)

```
async for chunk in await client.aio.models.generate_content_stream(
    model='gemini-2.0-flash-001', contents='Tell me a story in 300 words.'
):
    print(chunk.text, end='')
```

### Count Tokens and Compute Tokens

[Permalink: Count Tokens and Compute Tokens](https://github.com/googleapis/python-genai#count-tokens-and-compute-tokens)

```
response = client.models.count_tokens(
    model='gemini-2.0-flash-001',
    contents='why is the sky blue?',
)
print(response)
```

#### Compute Tokens

[Permalink: Compute Tokens](https://github.com/googleapis/python-genai#compute-tokens)

Compute tokens is only supported in Vertex AI.

```
response = client.models.compute_tokens(
    model='gemini-2.0-flash-001',
    contents='why is the sky blue?',
)
print(response)
```

##### Async

[Permalink: Async](https://github.com/googleapis/python-genai#async-2)

```
response = await client.aio.models.count_tokens(
    model='gemini-2.0-flash-001',
    contents='why is the sky blue?',
)
print(response)
```

### Embed Content

[Permalink: Embed Content](https://github.com/googleapis/python-genai#embed-content)

```
response = client.models.embed_content(
    model='text-embedding-004',
    contents='why is the sky blue?',
)
print(response)
```

```
# multiple contents with config
response = client.models.embed_content(
    model='text-embedding-004',
    contents=['why is the sky blue?', 'What is your age?'],
    config=types.EmbedContentConfig(output_dimensionality=10),
)

print(response)
```

### Imagen

[Permalink: Imagen](https://github.com/googleapis/python-genai#imagen)

#### Generate Images

[Permalink: Generate Images](https://github.com/googleapis/python-genai#generate-images)

Support for generate images in Gemini Developer API is behind an allowlist

```
# Generate Image
response1 = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt='An umbrella in the foreground, and a rainy night sky in the background',
    config=types.GenerateImagesConfig(
        negative_prompt='human',
        number_of_images=1,
        include_rai_reason=True,
        output_mime_type='image/jpeg',
    ),
)
response1.generated_images[0].image.show()
```

#### Upscale Image

[Permalink: Upscale Image](https://github.com/googleapis/python-genai#upscale-image)

Upscale image is only supported in Vertex AI.

```
# Upscale the generated image from above
response2 = client.models.upscale_image(
    model='imagen-3.0-generate-001',
    image=response1.generated_images[0].image,
    upscale_factor='x2',
    config=types.UpscaleImageConfig(
        include_rai_reason=True,
        output_mime_type='image/jpeg',
    ),
)
response2.generated_images[0].image.show()
```

#### Edit Image

[Permalink: Edit Image](https://github.com/googleapis/python-genai#edit-image)

Edit image uses a separate model from generate and upscale.

Edit image is only supported in Vertex AI.

```
# Edit the generated image from above
from google.genai.types import RawReferenceImage, MaskReferenceImage

raw_ref_image = RawReferenceImage(
    reference_id=1,
    reference_image=response1.generated_images[0].image,
)

# Model computes a mask of the background
mask_ref_image = MaskReferenceImage(
    reference_id=2,
    config=types.MaskReferenceConfig(
        mask_mode='MASK_MODE_BACKGROUND',
        mask_dilation=0,
    ),
)

response3 = client.models.edit_image(
    model='imagen-3.0-capability-001',
    prompt='Sunlight and clear sky',
    reference_images=[raw_ref_image, mask_ref_image],
    config=types.EditImageConfig(
        edit_mode='EDIT_MODE_INPAINT_INSERTION',
        number_of_images=1,
        negative_prompt='human',
        include_rai_reason=True,
        output_mime_type='image/jpeg',
    ),
)
response3.generated_images[0].image.show()
```

## Chats

[Permalink: Chats](https://github.com/googleapis/python-genai#chats)

Create a chat session to start a multi-turn conversations with the model.

### Send Message

[Permalink: Send Message](https://github.com/googleapis/python-genai#send-message)

```
chat = client.chats.create(model='gemini-2.0-flash-001')
response = chat.send_message('tell me a story')
print(response.text)
```

### Streaming

[Permalink: Streaming](https://github.com/googleapis/python-genai#streaming-2)

```
chat = client.chats.create(model='gemini-2.0-flash-001')
for chunk in chat.send_message_stream('tell me a story'):
    print(chunk.text)
```

### Async

[Permalink: Async](https://github.com/googleapis/python-genai#async-3)

```
chat = client.aio.chats.create(model='gemini-2.0-flash-001')
response = await chat.send_message('tell me a story')
print(response.text)
```

### Async Streaming

[Permalink: Async Streaming](https://github.com/googleapis/python-genai#async-streaming)

```
chat = client.aio.chats.create(model='gemini-2.0-flash-001')
async for chunk in await chat.send_message_stream('tell me a story'):
    print(chunk.text)
```

## Files

[Permalink: Files](https://github.com/googleapis/python-genai#files)

Files are only supported in Gemini Developer API.

```
!gsutil cp gs://cloud-samples-data/generative-ai/pdf/2312.11805v3.pdf .
!gsutil cp gs://cloud-samples-data/generative-ai/pdf/2403.05530.pdf .
```

### Upload

[Permalink: Upload](https://github.com/googleapis/python-genai#upload)

```
file1 = client.files.upload(file='2312.11805v3.pdf')
file2 = client.files.upload(file='2403.05530.pdf')

print(file1)
print(file2)
```

### Get

[Permalink: Get](https://github.com/googleapis/python-genai#get)

```
file1 = client.files.upload(file='2312.11805v3.pdf')
file_info = client.files.get(name=file1.name)
```

### Delete

[Permalink: Delete](https://github.com/googleapis/python-genai#delete)

```
file3 = client.files.upload(file='2312.11805v3.pdf')

client.files.delete(name=file3.name)
```

## Caches

[Permalink: Caches](https://github.com/googleapis/python-genai#caches)

`client.caches` contains the control plane APIs for cached content

### Create

[Permalink: Create](https://github.com/googleapis/python-genai#create)

```
if client.vertexai:
    file_uris = [\
        'gs://cloud-samples-data/generative-ai/pdf/2312.11805v3.pdf',\
        'gs://cloud-samples-data/generative-ai/pdf/2403.05530.pdf',\
    ]
else:
    file_uris = [file1.uri, file2.uri]

cached_content = client.caches.create(
    model='gemini-1.5-pro-002',
    config=types.CreateCachedContentConfig(
        contents=[\
            types.Content(\
                role='user',\
                parts=[\
                    types.Part.from_uri(\
                        file_uri=file_uris[0], mime_type='application/pdf'\
                    ),\
                    types.Part.from_uri(\
                        file_uri=file_uris[1],\
                        mime_type='application/pdf',\
                    ),\
                ],\
            )\
        ],
        system_instruction='What is the sum of the two pdfs?',
        display_name='test cache',
        ttl='3600s',
    ),
)
```

### Get

[Permalink: Get](https://github.com/googleapis/python-genai#get-1)

```
cached_content = client.caches.get(name=cached_content.name)
```

### Generate Content with Caches

[Permalink: Generate Content with Caches](https://github.com/googleapis/python-genai#generate-content-with-caches)

```
response = client.models.generate_content(
    model='gemini-1.5-pro-002',
    contents='Summarize the pdfs',
    config=types.GenerateContentConfig(
        cached_content=cached_content.name,
    ),
)
print(response.text)
```

## Tunings

[Permalink: Tunings](https://github.com/googleapis/python-genai#tunings)

`client.tunings` contains tuning job APIs and supports supervised fine
tuning through `tune`.

### Tune

[Permalink: Tune](https://github.com/googleapis/python-genai#tune)

- Vertex AI supports tuning from GCS source
- Gemini Developer API supports tuning from inline examples

```
if client.vertexai:
    model = 'gemini-1.5-pro-002'
    training_dataset = types.TuningDataset(
        gcs_uri='gs://cloud-samples-data/ai-platform/generative_ai/gemini-1_5/text/sft_train_data.jsonl',
    )
else:
    model = 'models/gemini-1.0-pro-001'
    training_dataset = types.TuningDataset(
        examples=[\
            types.TuningExample(\
                text_input=f'Input text {i}',\
                output=f'Output text {i}',\
            )\
            for i in range(5)\
        ],
    )
```

```
tuning_job = client.tunings.tune(
    base_model=model,
    training_dataset=training_dataset,
    config=types.CreateTuningJobConfig(
        epoch_count=1, tuned_model_display_name='test_dataset_examples model'
    ),
)
print(tuning_job)
```

### Get Tuning Job

[Permalink: Get Tuning Job](https://github.com/googleapis/python-genai#get-tuning-job)

```
tuning_job = client.tunings.get(name=tuning_job.name)
print(tuning_job)
```

```
import time

running_states = set(
    [\
        'JOB_STATE_PENDING',\
        'JOB_STATE_RUNNING',\
    ]
)

while tuning_job.state in running_states:
    print(tuning_job.state)
    tuning_job = client.tunings.get(name=tuning_job.name)
    time.sleep(10)
```

#### Use Tuned Model

[Permalink: Use Tuned Model](https://github.com/googleapis/python-genai#use-tuned-model)

```
response = client.models.generate_content(
    model=tuning_job.tuned_model.endpoint,
    contents='why is the sky blue?',
)

print(response.text)
```

### Get Tuned Model

[Permalink: Get Tuned Model](https://github.com/googleapis/python-genai#get-tuned-model)

```
tuned_model = client.models.get(model=tuning_job.tuned_model.model)
print(tuned_model)
```

### List Tuned Models

[Permalink: List Tuned Models](https://github.com/googleapis/python-genai#list-tuned-models)

To retrieve base models, see [list base models](https://github.com/googleapis/python-genai#list-base-models).

```
for model in client.models.list(config={'page_size': 10, 'query_base': False}):
    print(model)
```

```
pager = client.models.list(config={'page_size': 10, 'query_base': False})
print(pager.page_size)
print(pager[0])
pager.next_page()
print(pager[0])
```

#### Async

[Permalink: Async](https://github.com/googleapis/python-genai#async-4)

```
async for job in await client.aio.models.list(config={'page_size': 10, 'query_base': False}):
    print(job)
```

```
async_pager = await client.aio.models.list(config={'page_size': 10, 'query_base': False})
print(async_pager.page_size)
print(async_pager[0])
await async_pager.next_page()
print(async_pager[0])
```

### Update Tuned Model

[Permalink: Update Tuned Model](https://github.com/googleapis/python-genai#update-tuned-model)

```
model = pager[0]

model = client.models.update(
    model=model.name,
    config=types.UpdateModelConfig(
        display_name='my tuned model', description='my tuned model description'
    ),
)

print(model)
```

### List Tuning Jobs

[Permalink: List Tuning Jobs](https://github.com/googleapis/python-genai#list-tuning-jobs)

```
for job in client.tunings.list(config={'page_size': 10}):
    print(job)
```

```
pager = client.tunings.list(config={'page_size': 10})
print(pager.page_size)
print(pager[0])
pager.next_page()
print(pager[0])
```

#### Async

[Permalink: Async](https://github.com/googleapis/python-genai#async-5)

```
async for job in await client.aio.tunings.list(config={'page_size': 10}):
    print(job)
```

```
async_pager = await client.aio.tunings.list(config={'page_size': 10})
print(async_pager.page_size)
print(async_pager[0])
await async_pager.next_page()
print(async_pager[0])
```

## Batch Prediction

[Permalink: Batch Prediction](https://github.com/googleapis/python-genai#batch-prediction)

Only supported in Vertex AI.

### Create

[Permalink: Create](https://github.com/googleapis/python-genai#create-1)

```
# Specify model and source file only, destination and job display name will be auto-populated
job = client.batches.create(
    model='gemini-1.5-flash-002',
    src='bq://my-project.my-dataset.my-table',
)

job
```

```
# Get a job by name
job = client.batches.get(name=job.name)

job.state
```

```
completed_states = set(
    [\
        'JOB_STATE_SUCCEEDED',\
        'JOB_STATE_FAILED',\
        'JOB_STATE_CANCELLED',\
        'JOB_STATE_PAUSED',\
    ]
)

while job.state not in completed_states:
    print(job.state)
    job = client.batches.get(name=job.name)
    time.sleep(30)

job
```

### List

[Permalink: List](https://github.com/googleapis/python-genai#list)

```
for job in client.batches.list(config=types.ListBatchJobsConfig(page_size=10)):
    print(job)
```

```
pager = client.batches.list(config=types.ListBatchJobsConfig(page_size=10))
print(pager.page_size)
print(pager[0])
pager.next_page()
print(pager[0])
```

#### Async

[Permalink: Async](https://github.com/googleapis/python-genai#async-6)

```
async for job in await client.aio.batches.list(
    config=types.ListBatchJobsConfig(page_size=10)
):
    print(job)
```

```
async_pager = await client.aio.batches.list(
    config=types.ListBatchJobsConfig(page_size=10)
)
print(async_pager.page_size)
print(async_pager[0])
await async_pager.next_page()
print(async_pager[0])
```

### Delete

[Permalink: Delete](https://github.com/googleapis/python-genai#delete-1)

```
# Delete the job resource
delete_job = client.batches.delete(name=job.name)

delete_job
```

## About

Google Gen AI Python SDK provides an interface for developers to integrate Google's generative models into their Python applications.


[googleapis.github.io/python-genai/](https://googleapis.github.io/python-genai/ "https://googleapis.github.io/python-genai/")

### Resources

[Readme](https://github.com/googleapis/python-genai#readme-ov-file)

### License

[Apache-2.0 license](https://github.com/googleapis/python-genai#Apache-2.0-1-ov-file)

### Code of conduct

[Code of conduct](https://github.com/googleapis/python-genai#coc-ov-file)

### Security policy

[Security policy](https://github.com/googleapis/python-genai#security-ov-file)

[Activity](https://github.com/googleapis/python-genai/activity)

[Custom properties](https://github.com/googleapis/python-genai/custom-properties)

### Stars

[**927**\\
stars](https://github.com/googleapis/python-genai/stargazers)

### Watchers

[**80**\\
watching](https://github.com/googleapis/python-genai/watchers)

### Forks

[**159**\\
forks](https://github.com/googleapis/python-genai/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fgoogleapis%2Fpython-genai&report=googleapis+%28user%29)

## [Releases\  9](https://github.com/googleapis/python-genai/releases)

[v1.1.0\\
Latest\\
\\
Feb 10, 2025](https://github.com/googleapis/python-genai/releases/tag/v1.1.0)

[\+ 8 releases](https://github.com/googleapis/python-genai/releases)

## [Packages\  0](https://github.com/orgs/googleapis/packages?repo_name=python-genai)

No packages published

## [Used by 1.2k](https://github.com/googleapis/python-genai/network/dependents)

[- ![@haoyuliao](https://avatars.githubusercontent.com/u/23026269?s=64&v=4)\\
- ![@timroty](https://avatars.githubusercontent.com/u/42622148?s=64&v=4)\\
- ![@Lobooooooo14](https://avatars.githubusercontent.com/u/88998991?s=64&v=4)\\
- ![@derrismaqebe](https://avatars.githubusercontent.com/u/193747737?s=64&v=4)\\
- ![@GoUpvote](https://avatars.githubusercontent.com/u/118300643?s=64&v=4)\\
- ![@Frisyk](https://avatars.githubusercontent.com/u/112816171?s=64&v=4)\\
- ![@ParhamNajarzadeh](https://avatars.githubusercontent.com/u/116252212?s=64&v=4)\\
- ![@kuangsith](https://avatars.githubusercontent.com/u/108988177?s=64&v=4)\\
\\
\+ 1,215](https://github.com/googleapis/python-genai/network/dependents)

## [Contributors\  23](https://github.com/googleapis/python-genai/graphs/contributors)

- [![@sasha-gitg](https://avatars.githubusercontent.com/u/44654632?s=64&v=4)](https://github.com/sasha-gitg)
- [![@happy-qiao](https://avatars.githubusercontent.com/u/159568575?s=64&v=4)](https://github.com/happy-qiao)
- [![@sararob](https://avatars.githubusercontent.com/u/3814898?s=64&v=4)](https://github.com/sararob)
- [![@hkt74](https://avatars.githubusercontent.com/u/4653660?s=64&v=4)](https://github.com/hkt74)
- [![@google-genai-bot](https://avatars.githubusercontent.com/u/194307901?s=64&v=4)](https://github.com/google-genai-bot)
- [![@yyyu-google](https://avatars.githubusercontent.com/u/150068659?s=64&v=4)](https://github.com/yyyu-google)
- [![@amirh](https://avatars.githubusercontent.com/u/1024117?s=64&v=4)](https://github.com/amirh)
- [![@Ark-kun](https://avatars.githubusercontent.com/u/1829149?s=64&v=4)](https://github.com/Ark-kun)
- [![@yinghsienwu](https://avatars.githubusercontent.com/u/14824050?s=64&v=4)](https://github.com/yinghsienwu)
- [![@matthew29tang](https://avatars.githubusercontent.com/u/22719762?s=64&v=4)](https://github.com/matthew29tang)
- [![@release-please[bot]](https://avatars.githubusercontent.com/in/40688?s=64&v=4)](https://github.com/apps/release-please)
- [![@MarkDaoust](https://avatars.githubusercontent.com/u/1414837?s=64&v=4)](https://github.com/MarkDaoust)
- [![@Annhiluc](https://avatars.githubusercontent.com/u/10099501?s=64&v=4)](https://github.com/Annhiluc)

[\+ 9 contributors](https://github.com/googleapis/python-genai/graphs/contributors)

## Languages

- [Python100.0%](https://github.com/googleapis/python-genai/search?l=python)

You can’t perform that action at this time.
