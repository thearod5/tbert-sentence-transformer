import os

from dotenv import load_dotenv
from huggingface_hub import ModelCard, ModelCardData

from models import load_embedding_model

load_dotenv()

MODEL_NAME = "tbert-encoder"


def create_model_card():
    model_card_content = """
    # Model Card for tbert-embedding
    
    ## Model Description
    This repository contains the embedding model used in the siamese architecture described in the paper: "Traceability Transformed: Generating More Accurate Links with Pre-Trained BERT Models". The model was a top performer in generating traceability links between software artifacts. The original architecture utilized a relational classifier to create similarity scores between text pairs, resembling a cross-encoder. This model extracts the embedding component to enable the use of cosine similarity between embeddings, thus speeding up the process.
    
    **Note:** Evaluation is pending review.
    
    ## Intended Uses & Limitations
    This model is intended for producing embeddings of software artifacts for purposes such as clustering, Retrieval-Augmented Generation (RAG), or creating traceability links via similarity measures like cosine similarity.
    
    ## Training, Evaluation, and Results
    For detailed information on training, evaluation, and results, refer to the original [paper](https://arxiv.org/pdf/2102.04411).
    
    ## Citation
    ```
    @misc{lin2021traceability,
      title={Traceability Transformed: Generating More Accurate Links with Pre-Trained BERT Models}, 
      author={Jinfeng Lin and Yalin Liu and Qingkai Zeng and Meng Jiang and Jane Cleland-Huang},
      year={2021},
      eprint={2102.04411},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
    }
    ```
    """
    card_data = ModelCardData(
        language="en",
        license='mit',
        model_name=MODEL_NAME
    )
    card = ModelCard.from_template(card_data=card_data, template_path=None, content=model_card_content)
    return card


if __name__ == "__main__":
    model_path = os.path.expanduser(os.environ["MODEL_PATH"])

    # Load model and tokenizer
    model, tokenizer = load_embedding_model(model_path)
    model_card = create_model_card()

    # Save model and tokenizer
    repo_name = "thearod5/tbert-encoder"  # Change this to your Hugging Face model repo name

    model.push_to_hub(repo_name)
    tokenizer.push_to_hub(repo_name)
    model_card.push_to_hub(repo_name)

    # Log job finished.
    print("Model published to Hugging Face.")
