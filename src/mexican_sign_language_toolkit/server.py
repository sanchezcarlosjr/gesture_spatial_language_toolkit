import gradio as gr
import numpy as np
from mexican_sign_language_toolkit.pipeline import pipeline,VideoPipeline
import glob 


def launch_server():
  predict = pipeline(VideoPipeline())
  demo = gr.Interface(
    predict,
    [gr.Video(source="webcam", mirror_webcam=False)],
    ["text"],
    examples=[*glob.glob('**/*.mp4', recursive=True),*glob.glob('**/*.mkv', recursive=True)],
    title="Mexican sign language recognizer demo",
    description="Mexican sign language recognizer by Ricardo Morfin, Ernesto Lozano, and Carlos Sanchez",
  )
  demo.launch(share=True)
