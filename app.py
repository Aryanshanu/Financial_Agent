import gradio as gr
from modules.news import fetch_news, analyze_sentiment
from modules.market_data import get_financial_insights
from modules.assistant import chatbot_response

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Financial Agent")
        gr.Markdown("Ask me about the latest financial news or insights!")

        with gr.Row():
            with gr.Column():
                user_input = gr.Textbox(label="Your Question", placeholder="Type your question here...")
                submit_btn = gr.Button("Submit")
                response_output = gr.JSON(label="Response")

            submit_btn.click(chatbot_response, inputs=user_input, outputs=response_output)

        with gr.Row():
            gr.Markdown("### Latest Financial Insights")
            insights_output = gr.Dataframe(get_financial_insights())

    demo.launch()

if __name__ == "__main__":
    main()
