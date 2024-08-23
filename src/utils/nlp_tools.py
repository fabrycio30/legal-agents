import spacy

# Carregar o modelo spaCy para NER e conseguirmosdetectar as entidades da petição
# Ainda não verifiquei se o modelo do espacy já mapeia CPF e RG, caso não, será necessário fazer esse mapeamento talvez via RE.

nlp = spacy.load("pt_core_news_sm")

# Função para mascarar dados sensíveis
def mask_sensitive_data(text):
    doc = nlp(text)
    masked_text = text
    for ent in doc.ents:
        if ent.label_ == "PER":
            masked_text = masked_text.replace(ent.text, "[nome]")
        elif ent.label_ == "ORG":
            masked_text = masked_text.replace(ent.text, "[org]")
        elif ent.label_ == "LOC":
            masked_text = masked_text.replace(ent.text, "[local]")
        elif ent.label_ == "MISC":
            masked_text = masked_text.replace(ent.text, "[misc]")
        elif ent.label_ == "CPF":
            masked_text = masked_text.replace(ent.text, "[CPF]")
        elif ent.label_ == "RG":
            masked_text = masked_text.replace(ent.text, "[RG]")
    return masked_text
