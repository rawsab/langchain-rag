from flask import Flask, request, jsonify
from main import process_pdf, query_pdf

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    pdf_file = request.files['file']
    pdf_path = "./uploads/" + pdf_file.filename
    pdf_file.save(pdf_path)
    process_pdf(pdf_path)
    return jsonify({"message": "PDF processed successfully"}), 200

@app.route('/query', methods=['GET'])
def query():
    query_text = request.args.get('query')
    results = query_pdf(query_text)
    return jsonify({"results": results}), 200

if __name__ == '__main__':
    app.run(debug=True)
