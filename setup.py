from setuptools import setup

install_requires = []
with open("./requirements.txt", "r") as requirements_file:
    reqs = [r.strip() for r in requirements_file.readlines()]
    for r in reqs:
        install_requires.append(r)

setup(
    name='alpaca_lora_4bit',
    version='0.1.2',
    description='Alpaca LoRA 4-bit',
    package_dir={'alpaca_lora_4bit': 'src/alpaca_lora_4bit'},
    packages=['alpaca_lora_4bit', 'alpaca_lora_4bit.monkeypatch', 'alpaca_lora_4bit.server'],
    install_requires=install_requires,
    extras_require={
        'triton': 'triton',
    },
)
