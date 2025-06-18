from flask import Flask, request, Response, render_template, stream_with_context
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 初始化OpenAI客户端
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# 评价作文的prompt模板
EVALUATION_PROMPT = {
    'zh': """请对以下作文进行评价，评价内容包括：
1. 语言评价（用词、句法、语用等 1-5分、使用[得分/满分]格式输出得分）
2. 结构评价（段落安排、层次分明度等 1-5分）
3. 内容评价（主题、立意、内容充实度等 1-5分）
4. 总体评分（满分15分）
然后给出修改后的作文 (根据作文内容，推断出作文的难度，并根据难度给出修改后的作文)

作文内容：
{essay}

请以专业、客观的态度进行评价，并给出具体的改进建议。""",

    'en': """Please evaluate the following essay, including:
1. Content evaluation (theme, ideas, content richness, etc.)
2. Structure evaluation (paragraph arrangement, clarity of hierarchy, etc.)
3. Language evaluation (vocabulary, sentence structure, rhetoric, etc.)
4. Overall score (out of 100)
5. Improvement suggestions

Essay content:
{essay}

Please provide a professional and objective evaluation with specific improvement suggestions.""",

    'ja': """以下の中国語作文を評価してください。評価内容は以下の通りです：
1. 言語評価（語彙、文法など 1-5点、[得点/満点]のスタイルで点数を出力してください）
2. 構成評価（段落、論理的かなど 1-5点、[得点/満点]のスタイルで点数を出力してください）
3. 内容評価（分かりやすさ、、語用論的な観点など 1-5点、[得点/満点]のスタイルで点数を出力してください）
4. 総合評価（1.-3.の合計点数、[得点/満点]のスタイルで点数を出力してください）
最後に、添削後の作文を出力してください。（作文の内容からレベルを推測し、レベルに合わせて添削してください）

作文内容：
{essay}

専門的かつ厳正な態度で評価し、具体的な改善提案を提示してください。""",

    'fr': """Veuillez évaluer la dissertation suivante, en incluant :
1. Évaluation du contenu (thème, idées, richesse du contenu, etc.)
2. Évaluation de la structure (organisation des paragraphes, clarté de la hiérarchie, etc.)
3. Évaluation de la langue (vocabulaire, structure des phrases, rhétorique, etc.)
4. Note globale (sur 100)
5. Correction result (根据作文内容，推断出作文的难度，并根据难度给出修改后的作文)

Contenu de la dissertation :
{essay}

Veuillez fournir une évaluation professionnelle et objective avec des suggestions d'amélioration spécifiques.""",

    'de': """Bitte bewerten Sie den folgenden Aufsatz, einschließlich:
1. Inhaltsbewertung (Thema, Ideen, Inhaltsreichtum, etc.)
2. Strukturbewertung (Absatzanordnung, Hierarchieklarheit, etc.)
3. Sprachbewertung (Wortschatz, Satzstruktur, Rhetorik, etc.)
4. Gesamtbewertung (von 100 Punkten)
5. Verbesserungsvorschläge  (根据作文内容，推断出作文的难度，并根据难度给出修改后的作文)

Aufsatzinhalt:
{essay}

Bitte geben Sie eine professionelle und objektive Bewertung mit konkreten Verbesserungsvorschlägen.""",

    'it': """Si prega di valutare il seguente saggio, includendo:
1. Valutazione del contenuto (tema, idee, ricchezza dei contenuti, ecc.)
2. Valutazione della struttura (disposizione dei paragrafi, chiarezza gerarchica, ecc.)
3. Valutazione linguistica (vocabolario, struttura delle frasi, retorica, ecc.)
4. Punteggio complessivo (su 100)
5. Suggerimenti per il miglioramento  (根据作文内容，推断出作文的难度，并根据难度给出修改后的作文)

Contenuto del saggio:
{essay}

Si prega di fornire una valutazione professionale e obiettiva con suggerimenti specifici per il miglioramento.""",

    'ko': """다음 작문을 평가해 주세요. 평가 내용은 다음과 같습니다:
1. 내용 평가 (주제, 의도, 내용의 충실도 등)
2. 구조 평가 (단락 배치, 계층의 명확성 등)
3. 언어 평가 (용어, 문형, 수사 등)
4. 종합 평가 (100점 만점)
5. 개선 제안  (根据作文内容，推断出作文的难度，并根据难度给出修改后的作文)

작문 내용:
{essay}

전문적이고 객관적인 태도로 평가하고 구체적인 개선 제안을 제시해 주세요."""
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.get_json()
        essay = data.get('essay', '').strip()
        language = data.get('language', 'zh')  # 默认使用中文
        
        if not essay:
            return jsonify({'error': '作文内容不能为空'}), 400

        def generate():
            try:
                # 获取对应语言的prompt模板
                prompt = EVALUATION_PROMPT.get(language, EVALUATION_PROMPT['zh'])
                
                # 调用OpenAI API进行流式响应
                stream = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "你是一位专业的作文评价老师，擅长对作文进行专业、严格、客观的评价。"},
                        {"role": "user", "content": prompt.format(essay=essay)}
                    ],
                    stream=True
                )

                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content

            except Exception as e:
                yield f"\n发生错误：{str(e)}"

        return Response(stream_with_context(generate()), mimetype='text/plain')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 