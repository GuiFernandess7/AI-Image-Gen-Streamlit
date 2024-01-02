from enum import Enum
import streamlit as st

class ExtendedEnum(Enum):
    @classmethod
    def names(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def get_value(cls, name):
        return cls[name].value

class Model(ExtendedEnum):
    FOOOCUS_API = "konieshadow/fooocus-api:a7e8fa2f96b01d02584de2b3029a8452b9bf0c8fa4127a6d1cfd406edfad54fb"
    STABLE_DIFFUSION = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478"
    PLAYGROUND_V2 = "playgroundai/playground-v2-1024px-aesthetic:42fe626e41cc811eaf02c94b892774839268ce1994ea778eba97103fe1ef51b8"

class Generator:

    def __init__(self, model_name: Model):
        from replicate.client import Client
        self.replicate = Client(api_token=st.secrets['KEY'])
        self.model_name = model_name

    def generate(self, prompt: str):
        output = self.replicate.run(
            self.model_name,
            input={
                "prompt": prompt
            }
        )
        return output
