# Section 10 - COOL Gradio UI
import gradio as gr

def ask_assistant(question, history):
    if not question.strip():
        return history, ""
    response = ask(question)
    history = history + [
        {"role": "user", "content": question},
        {"role": "assistant", "content": response}
    ]
    return history, ""

def clear_chat():
    return [], ""

def quick_ask(question, history):
    return ask_assistant(question, history)

css = """
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e) !important;
}
.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}
.header-text {
    text-align: center;
    padding: 20px;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.5em !important;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #a0aec0;
    font-size: 1.1em;
}
.warning-box {
    background: rgba(255, 100, 100, 0.1);
    border: 1px solid #ff6464;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    color: #ff6464;
}
.stat-box {
    background: rgba(0, 198, 255, 0.1);
    border: 1px solid #00c6ff;
    border-radius: 15px;
    padding: 15px;
    margin: 5px;
    text-align: center;
}
footer {display: none !important}
"""

with gr.Blocks(css=css, title="🏥 MediBot India") as demo:

    # Header
    gr.HTML("""
    <div style="text-align:center; padding: 30px 0 10px 0;">
        <div style="font-size:3em; margin-bottom:10px;">💊</div>
        <div style="font-size:2.2em; font-weight:900; 
                    background: linear-gradient(90deg, #00c6ff, #0072ff, #00c6ff);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;">
            MediBot India
        </div>
        <div style="color:#a0aec0; font-size:1.1em; margin-top:5px;">
            Powered by Mistral 7B • 361,052 Medical Documents • 100% Offline
        </div>
        <div style="margin-top:10px; padding:8px 20px; 
                    background:rgba(255,100,100,0.15); 
                    border:1px solid #ff6464; border-radius:20px;
                    display:inline-block; color:#ff6464; font-size:0.9em;">
            ⚠️ Educational purposes only — Always consult a real doctor!
        </div>
    </div>
    """)

    # Stats Row
    gr.HTML("""
    <div style="display:flex; justify-content:center; gap:15px; margin:20px 0;">
        <div style="background:rgba(0,198,255,0.1); border:1px solid #00c6ff; 
                    border-radius:12px; padding:12px 20px; text-align:center;">
            <div style="font-size:1.5em; font-weight:bold; color:#00c6ff;">361K+</div>
            <div style="color:#a0aec0; font-size:0.85em;">Medical Documents</div>
        </div>
        <div style="background:rgba(0,198,255,0.1); border:1px solid #00c6ff; 
                    border-radius:12px; padding:12px 20px; text-align:center;">
            <div style="font-size:1.5em; font-weight:bold; color:#00c6ff;">253K+</div>
            <div style="color:#a0aec0; font-size:0.85em;">Indian Medicines</div>
        </div>
        <div style="background:rgba(0,198,255,0.1); border:1px solid #00c6ff; 
                    border-radius:12px; padding:12px 20px; text-align:center;">
            <div style="font-size:1.5em; font-weight:bold; color:#00c6ff;">16K+</div>
            <div style="color:#a0aec0; font-size:0.85em;">Medical Q&As</div>
        </div>
        <div style="background:rgba(118,75,162,0.2); border:1px solid #764ba2; 
                    border-radius:12px; padding:12px 20px; text-align:center;">
            <div style="font-size:1.5em; font-weight:bold; color:#b794f4;">100%</div>
            <div style="color:#a0aec0; font-size:0.85em;">Offline & Private</div>
        </div>
    </div>
    """)

    with gr.Row():
        # Left - Chat
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
              height=450,
             label="Chat with your Medical Assistant",
               avatar_images=(None, "https://api.dicebear.com/7.x/bottts/svg?seed=medibot")
            )
            with gr.Row():
                question_box = gr.Textbox(
                    placeholder="💊 Ask about any medicine... e.g. 'What is Paracetamol for?'",
                    label="",
                    scale=5,
                    container=False
                )
                submit_btn = gr.Button("Ask 🚀", variant="primary", scale=1)
            clear_btn = gr.Button("🗑️ Clear Chat", size="sm")

        # Right - Info Panel
        with gr.Column(scale=1):
            gr.Markdown("### ⚡ Quick Questions")
            
            q1 = gr.Button("💊 What is Paracetamol for?", size="sm")
            q2 = gr.Button("💰 Price of Augmentin 625?", size="sm")
            q3 = gr.Button("🔬 Medicines with Amoxicillin?", size="sm")
            q4 = gr.Button("⚠️ Side effects of Azithromycin?", size="sm")
            q5 = gr.Button("🤒 Medicines for fever?", size="sm")
            q6 = gr.Button("😴 Medicines for sleep?", size="sm")

            gr.Markdown("---")
            gr.Markdown("""
### 🔧 Tech Stack
🤖 **LLM:** Mistral 7B  
🔍 **Search:** MiniLM Embeddings  
🗄️ **DB:** ChromaDB  
🦜 **Framework:** LangChain  
🖥️ **Runs:** Local GPU (RTX)
            """)

    # Button actions
    submit_btn.click(ask_assistant, inputs=[question_box, chatbot], outputs=[chatbot, question_box])
    question_box.submit(ask_assistant, inputs=[question_box, chatbot], outputs=[chatbot, question_box])
    clear_btn.click(clear_chat, outputs=[chatbot, question_box])

    # Quick question buttons
    q1.click(lambda h: ask_assistant("What is Paracetamol used for?", h), inputs=[chatbot], outputs=[chatbot, question_box])
    q2.click(lambda h: ask_assistant("Price of Augmentin 625?", h), inputs=[chatbot], outputs=[chatbot, question_box])
    q3.click(lambda h: ask_assistant("What medicines contain Amoxicillin?", h), inputs=[chatbot], outputs=[chatbot, question_box])
    q4.click(lambda h: ask_assistant("Side effects of Azithromycin?", h), inputs=[chatbot], outputs=[chatbot, question_box])
    q5.click(lambda h: ask_assistant("What medicines are used for fever in India?", h), inputs=[chatbot], outputs=[chatbot, question_box])
    q6.click(lambda h: ask_assistant("What medicines help with sleep?", h), inputs=[chatbot], outputs=[chatbot, question_box])

demo.launch()
