from setuptools import setup, find_packages

setup(
    name='hqq',
    version='0.1.1',    
    description='Half-Quadratic Quantization (HQQ)',
    url='https://github.com/mobiusml/hqq/',
    author='Dr. Hicham Badri',
    author_email='hicham@mobiuslabs.com',
    license='Apache 2',
    packages=['hqq', 'hqq/core', 'hqq/engine', 'hqq/models', 'hqq/models/hf', 'hqq/models/timm', 'hqq/models/vllm'],
    install_requires=['numpy','tqdm', 'torch', 'huggingface_hub', 'accelerate', 'timm', 'transformers', 'termcolor'], #add vllm/langchain?
)
