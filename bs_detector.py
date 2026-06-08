from transformers import pipeline
bs_model = pipeline("text-classification", model="microsoft/deberta-v3-base", truncation=True)

def analyze_text(text):
    result = bs_model(text)[0]
    return {
        "label": result['label'],
        "confidence": float(result['score']),
        "flagged": result['label'].lower() in ['misleading', 'false', 'toxic']
    }

# Copyright © 2026 Osasere H. Ero. All rights reserved.
# Proprietary and confidential. Unauthorized copying of this file, via any medium, is strictly prohibited.
