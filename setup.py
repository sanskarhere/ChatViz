from setuptools import setup,find_packages



setup(
    name='ChatViz',
    author='Sanskar Gupta',
    version='1.0.0',
    author_email='sanskargupta@gmail.com',
    description='A Streamlit application to analyze WhatsApp chat exports.',
    install_requires=['numpy', 'pandas', 'streamlit', 'matplotlib'],
    packages=find_packages(),
    python_requires=">=3.10"

)