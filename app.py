from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types
import os

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
STORE_ID = "fileSearchStores/zetcwx20oo6y-e6zg8karixpr"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': '質問を入力してください'}), 400
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=user_message,
            config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[STORE_ID]
                        )
                    )
                ]
            )
        )
        
        sources = []
        if response.candidates and len(response.candidates) > 0:
            candidate = response.candidates[0]
            if hasattr(candidate, 'grounding_metadata') and candidate.grounding_metadata:
                grounding = candidate.grounding_metadata
                if hasattr(grounding, 'grounding_chunks') and grounding.grounding_chunks:
                    for chunk in grounding.grounding_chunks:
                        source_info = {}
                        if hasattr(chunk, 'retrieved_context') and chunk.retrieved_context:
                            context = chunk.retrieved_context
                            if hasattr(context, 'title'):
                                source_info['title'] = context.title
                            if hasattr(context, 'uri'):
                                source_info['uri'] = context.uri
                            if hasattr(context, 'text'):
                                source_info['text'] = context.text[:200] if len(context.text) > 200 else context.text
                        if source_info:
                            sources.append(source_info)
        
        return jsonify({
            'reply': response.text,
            'sources': sources
        })
    
    except Exception as e:
        app.logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': '申し訳ございません。回答の生成中にエラーが発生しました。もう一度お試しください。'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
