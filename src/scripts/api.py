#pip install -q aitextgen

import json
from aitextgen import aitextgen
from flask import Flask, request


# importa o modelo
ai = aitextgen(model="models/pytorch_model_luiz_gonzaga.bin", config="models/config_luiz_gonzaga.json")



# cria a API
app = Flask("composia")


@app.route("/estrofe", methods=["GET"])
def estrofe():
    return jsonify({'text': ai.generate_one(batch_size=100,
                        prompt=request.args['input'],
                        max_length=100,
                        temperature=1.5,
                        top_k=0,
                        top_p=1)
                      })

app.run()
