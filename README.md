# 🔗 Mastering LLM Chains with LangChain

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) 
![LangChain](https://img.shields.io/badge/LangChain-0086CB?style=for-the-badge&logo=langchain) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai) ![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD61E?style=for-the-badge&logo=huggingface) ![Transformers](https://img.shields.io/badge/Transformers-FFD61E?style=for-the-badge&logo=huggingface) ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn)

Welcome to this in-depth guide on building and orchestrating **LLM Chains** with LangChain! This repository showcases how to move beyond single LLM calls and create powerful, multi-step workflows by linking models, prompts, and parsers together.

Chains are the fundamental building blocks of complex AI applications, allowing you to create sophisticated logic for tasks like question-answering, data analysis, and conditional reasoning.

---

### ✨ Core Concepts Demonstrated

This repository explores the most important and powerful chaining strategies in LangChain:

1.  **Simple Chain (`simple_chain.py`)**:
    -   The foundation of all chains. Learn how to create a basic sequence: **PromptTemplate ➔ LLM ➔ Output Parser**. This is the "Hello, World!" of LangChain and demonstrates the core concept of piping components together.

2.  **Sequential Chain (`sequential_chain.py`)**:
    -   Learn to build linear, multi-step workflows where the output of one chain becomes the input for the next. This is perfect for tasks that require a series of transformations, like generating a question and then answering it.
    -   This script demonstrates a workflow to generate a quiz question about a specific topic and then evaluate a student's answer to that question.

3.  **Parallel Chain (`parallel_chain.py`)**:
    -   Discover how to execute multiple chains simultaneously and combine their outputs. This is incredibly efficient for tasks where you need to extract multiple independent pieces of information from a single input.
    -   This script shows how to take a text about a city and extract its name, famous landmarks, and population in parallel.

4.  **Conditional Chain (`conditional_chain.py`)**:
    -   Master the art of building dynamic, intelligent workflows that can make decisions. This chain uses a classifier to route the user's query to the appropriate specialized chain (e.g., a "Math Chain" or a "History Chain").
    -   This is the key to creating AI agents that can reason about which tool or chain to use for a specific problem.

---

### 📸 Demos & Visualizations

Here are screenshots and diagrams illustrating how each chain works.


**1. Sequential Chain Workflow**
*First, the chain generates a question. Then, it evaluates an answer. The diagram below shows the flow of data.*
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/506b4fa6-fc2a-4e72-9be0-552170e14932" />
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/d0ce68cb-feae-4b1e-b366-38b1712d9d1f" />

**2. Parallel Chain Execution**
*This chain extracts multiple fields from a single text at the same time, as shown in the graph.*
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/32ac06e6-097f-4679-a283-9c65925a53cf" />
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/52da1d32-8294-42c3-b24f-f3baad44a595" />

**3. Conditional Chain Logic**
*The initial classifier decides which specialized chain to run based on the user's query.*
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/1b88ffdc-784c-4fc4-a3a8-f483f8ed5d14" />

---

### 🛠️ Tech Stack

-   **Core Framework**: LangChain
-   **LLM Provider**: OpenAI
-   **Core Libraries**: `langchain-core`, `langchain-openai`, `python-dotenv`

---

### ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jsonusuman351/langchain_chains.git](https://github.com/jsonusuman351/langchain_chains.git)
    cd langchain_chains
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # It is recommended to use Python 3.10 or higher
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    -   Create a file named `.env` in the root directory.
    -   Add your OpenAI API key to this file:
        ```env
        OPENAI_API_KEY="your-openai-api-key"
        ```

---

### 🚀 Usage Guide

Each script in this repository demonstrates a different chaining strategy.

-   **Run the Simple Chain:**
    ```bash
    python simple_chain.py
    ```
-   **Run the Sequential Chain:**
    ```bash
    python sequential_chain.py
    ```
-   **Run the Parallel Chain:**
    ```bash
    python parallel_chain.py
    ```
-   **Run the Conditional Chain:**
    ```bash
    python conditional_chain.py
    ```

---

### 🔬 A Tour of the Chains

This repository is organized by chaining technique, from the simplest to the most complex.

<details>
<summary>Click to view the code layout</summary>

```
langchain_chains/
│
├── simple_chain.py          # Basic: Prompt -> LLM -> Parser
├── sequential_chain.py      # Linear multi-step workflow
├── parallel_chain.py        # Simultaneous execution of multiple chains
├── conditional_chain.py     # Advanced: A chain that makes decisions
│
├── requirements.txt
├── .env                     # (need to create this for your API key)
└── README.md
```
</details>

---

---